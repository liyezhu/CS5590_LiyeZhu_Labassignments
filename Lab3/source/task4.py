from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.tokenize import RegexpTokenizer


file = open("input.txt")

list=[]
dict={}

input = file.read()

tokenizer = RegexpTokenizer(r'\w+')
[list.append(tokenizer.tokenize(line)) for line in sent_tokenize(input)]
#print(list)

lemmatizer = WordNetLemmatizer()
for l in list:
   temp = pos_tag([lemmatizer.lemmatize(word) for word in l])
   for t in temp:
       # remove verbs
       if 'VB' in t[1]:
           continue
       else:
           #Calculate the word frequency
           if t[0] in dict:
               dict[t[0]] += 1
           else:
               dict[t[0]] = 1
#sort
dict= sorted(dict.iteritems(), key=lambda d:d[1], reverse = True)
#print dict
index=0
top=[]

#get the top five words
for key in dict:
    top.append(key[0])
    index+=1
    if index==5:
        break

#extract sentences
result={}
for word in top:
    for line in sent_tokenize(input):
        if word in line:
            try:
                result[word].append(line)
            except:
                result[word] = [line]
print("here's the top five words that has been repeated most:")
for key in result:
    print key
    print result[key]