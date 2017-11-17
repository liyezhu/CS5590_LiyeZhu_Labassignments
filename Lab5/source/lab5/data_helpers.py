import numpy as np
import re
import itertools
from collections import Counter


def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()


def load_data_and_labels(rate_1_file, rate_2_file,rate_3_file,rate_4_file,rate_5_file):
    """
    Loads MR polarity data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """
    # Load data from files
    examples_1 = list(open(rate_1_file, "r",encoding='utf-8').readlines())
    examples_1 = [s.strip() for s in examples_1]
    examples_2 = list(open(rate_2_file,"r",encoding='utf-8').readlines())
    examples_2 = [s.strip() for s in examples_2]
    examples_3 = list(open(rate_3_file,"r",encoding='utf-8').readlines())
    examples_3 = [s.strip() for s in examples_3]
    examples_4 = list(open(rate_4_file,"r",encoding='utf-8').readlines())
    examples_4 = [s.strip() for s in examples_4]
    examples_5 = list(open(rate_5_file,"r",encoding='utf-8').readlines())
    examples_5 = [s.strip() for s in examples_5]

    # Split by words
    x_text = examples_1 + examples_2 + examples_3 + examples_4 + examples_5
    x_text = [clean_str(sent) for sent in x_text]

    # Generate labels
    labels_1 = [[0, 1, 1, 1, 1] for _ in examples_1]
    labels_2 = [[1, 0, 1, 1, 1] for _ in examples_2]
    labels_3 = [[1, 1, 0, 1, 1] for _ in examples_3]
    labels_4 = [[1, 1, 1, 0, 1] for _ in examples_4]
    labels_5 = [[1, 1, 1, 1, 0] for _ in examples_5]

    y = np.concatenate([labels_1, labels_2,labels_3,labels_4,labels_5], 0)
    return [x_text, y]


def batch_iter(data, batch_size, num_epochs, shuffle=True):
    """
    Generates a batch iterator for a dataset.
    """
    data = np.array(data)
    data_size = len(data)
    num_batches_per_epoch = int((len(data)-1)/batch_size) + 1
    for epoch in range(num_epochs):
        # Shuffle the data at each epoch
        if shuffle:
            shuffle_indices = np.random.permutation(np.arange(data_size))
            shuffled_data = data[shuffle_indices]
        else:
            shuffled_data = data
        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)
            yield shuffled_data[start_index:end_index]
