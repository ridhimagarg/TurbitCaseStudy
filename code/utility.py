from random import shuffle
import pandas as pd
import numpy as np
import json


def train_test_split_(data):


    train_data = data[:int(data.shape[0] * 0.9)]
    val_data = data[int(data.shape[0] * 0.9):int(data.shape[0] * 0.95)]
    test_data = data[int(data.shape[0] * 0.95):]

    return train_data, val_data, test_data

# convert an array of values into a dataset matrix
## setting timestep by defualt=1
def dataset_creation(data, time_step=1, ismultivariate=False):

    if ismultivariate:

        dataX, dataY = [], []
        for i in range(len(data)-time_step-1):
            a = data[i:(i+time_step), :]   ###i=0, 0,1,2,3-----99   100
            dataX.append(a)
            dataY.append(data[i + time_step, 0])
        return np.array(dataX), np.array(dataY)

    else:
        dataX, dataY = [], []
        for i in range(len(data)-time_step-1):
            a = data[i:(i+time_step), 0]   ###i=0, 0,1,2,3-----99   100
            dataX.append(a)
            dataY.append(data[i + time_step, 0])
        return np.array(dataX), np.array(dataY)
