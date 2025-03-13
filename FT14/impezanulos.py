import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
import pylab as plt

#read the data
df_train = pd.read_csv('https://www.rootsystems.pt/train.csv')

print(df_train.head())
print(df_train.tail())

#view the data types of each column
print(df_train.dtypes)

#type 'object' is a string for pandas, which poses problems with the machine learning algorithms
#if we wannt to use these as features, we'll need to convert these to a numerical representation
#get some basic information on the dataframe
print(df_train.info())