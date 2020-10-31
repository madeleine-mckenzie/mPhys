import pandas as pd
import numpy as np

def get_arrays_ts4(data_array, index):

    gal = data_array[index][0]
    gas = data_array[index][1]
    new = data_array[index][2]
    old = data_array[index][3]

    return gal, gas, new, old


def to_pandas_ts4(data_array):
    col_header = ['x', 'y', 'z', 'vx', 'vy', 'vz', 'iwas', 'id', 'mass']

    gal = pd.DataFrame(data_array[0], columns=col_header)
    gas = pd.DataFrame(data_array[1], columns=col_header)
    new = pd.DataFrame(data_array[2], columns=col_header)
    old = pd.DataFrame(data_array[3], columns=col_header)

    return gal, gas, new, old