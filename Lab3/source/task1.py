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

def predict_pollution(hour, pollution, x):
    model = linear_model.LinearRegression()
    hour = np.reshape(hour, (len(hour), 1))
    pollution = np.reshape(pollution, (len(pollution), 1))
    model.fit(hour, pollution)
    pollution_predict = model.predict(hour)

    plt.scatter(hour, pollution, color='black')
    plt.plot(hour, pollution_predict, color='yellow', linewidth=2)
    plt.show()
    result = model.predict(x)
    return result[0][0]



get_data('PRSA_data_2010.1.1-2014.12.31.csv')
prediction = predict_pollution(hour,pollution,12.5)
print("predicted PM2.5 at 12:30 is:%f"%prediction)

