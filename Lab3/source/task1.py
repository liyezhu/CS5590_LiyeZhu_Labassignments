import csv
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

hour = []
pollution = []

def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            hour.append(int(row[4]))
            pollution.append(int(row[5]))
    return


def show_plot(hour, pollution):
    linear_mod = linear_model.LinearRegression()
    hour = np.reshape(hour, (len(hour), 1))
    pollution = np.reshape(pollution, (len(pollution), 1))
    linear_mod.fit(hour, pollution)
    plt.scatter(hour, pollution, color='black')
    plt.plot(hour, linear_mod.predict(hour), color='yellow', linewidth=2)
    plt.show()
    return


def predict_pollution(hour, pollution, x):
    linear_mod = linear_model.LinearRegression()
    hour = np.reshape(hour, (len(hour), 1))
    pollution = np.reshape(pollution, (len(pollution), 1))
    linear_mod.fit(hour, pollution)
    predicted_pollution = linear_mod.predict(x)
    return predicted_pollution[0][0]



get_data('PRSA_data_2010.1.1-2014.12.31.csv')
show_plot(hour, pollution)
print("predicted PM2.5 at 12:30 is:%f"%predict_pollution(hour, pollution, 12.5))

