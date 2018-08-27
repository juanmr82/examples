'''
Created on Aug 10, 2018

@author: juanr
'''

import pandas as pd
import numpy as np


#Read from Google. C.a. 17000 rows and 8 columns
df = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")

#Get Column names and print them
column_names = list(df)

mean_values = {}
max_values = {}
min_values = {}

#Print Important values
(nr_rows,nr_columns) =df.shape

print('Nr Rows: %d' % nr_rows)
print('Nr Columns: %d' % nr_columns)
print('Column names: %s' % column_names)



#Store Main Values
for i in column_names:
    print("Series Name: %s, mean valueprint(column_names): %f, min value: %f, max value:%f" % (i,df[i].mean(),df[i].min(),df[i].max()))
    

print("Series operations. Create a new series based on data from other series")

#Create a new series indicating either tru/false if population is greater than 1500
df['enough_population'] = df['median_house_value'].apply(lambda x: x>1500)

print("")
column_names = list(df)
(nr_rows,nr_columns) =df.shape
print ('New Shape of the Data Frame')
print('Nr Rows: %d' % nr_rows)
print('Nr Columns: %d' % nr_columns)
print('Column names: %s' % column_names)

print("")
print("Shuffling data")


#Shuffle Dataframe based on ndex of total rooms new DF is radomized
df = df.reindex(np.random.permutation(df['total_rooms'].index))

print(df.head)
                         
                          
