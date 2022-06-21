#Created 06/19/22 7:01pm
#Author: Kahin Akram Hassan
#This little helper is for fetching the data from the source, 
# loading it, and splitting it into train and test sets
#Some of the code is inspired by the steps in ch2. 

#====================================Dependencies==================================================

from . import data_constants as c

import os
import pandas as pd
import numpy as np
import requests
import hashlib
from sklearn.model_selection import StratifiedShuffleSplit


#Load the csv file into a pandas dataframe
def load_housing_data():

    req = requests.get(c.DOWNLOAD_URL + c.FILE_NAME)
    local_file_name = c.HOUSING_PATH + c.FILE_NAME
    
    if os.path.exists(local_file_name):
        print('The file "{0}" already exists under "{1}".'\
            .format(c.FILE_NAME,c.HOUSING_PATH))
    else:
        open(local_file_name,'wb').write(req.content)
        print('Done downloading! Check "{0}" for the file.'\
            .format(c.HOUSING_PATH))

#Read the data into dataframe 
def read_csv_file():
    df = pd.read_csv(c.HOUSING_PATH + c.FILE_NAME)
    df.reset_index() # add "index" column 
    #To be sure that we use unique identifiers when splitting the data and that 
    # adding new data will not break the split, we can create a new id column
    df["id"] = df["longitude"]*1000 + df["latitude"] 
    
    return df

#Functions to split the datasets into train and test in a robust way 
# (combination with hashing and unique id creation)
def test_set_check(identifier,test_ratio,hash):
    # Compute a hash of each instance’s identifier and keep only the last byte of the hash.
    # Then put the instance in the test set if this value is lower or equal to 51 (~20% of 256).
    return hash(np.int64(identifier)).digest()[-1] < 256*test_ratio

def split_train_test_id(data, test_ratio, id_col, hash=hashlib.md5):
    ids = data[id_col]
    in_test_set = ids.apply(lambda id_: test_set_check(id_,test_ratio,hash))
    
    return data.loc[~in_test_set], data.loc[in_test_set] # Return the data values for train and test.

def stratisfied_split_train_test(data, test_ratio, category):
    # Let's ensure our split follows the stratified sampling approach 
    # Splitting the population into homogeneous subgroups. 
    data[category] = np.ceil(data["median_income"] / 1.5)
    data[category].where(data[category] < 5, 5.0, inplace=True)

    split = StratifiedShuffleSplit(n_splits=1,test_size=test_ratio, random_state=42)
    for train_index, test_index in split.split(data, data[category]):
        strat_train_set = data.loc[train_index]
        strat_test_set = data.loc[test_index]
        
    for set in (strat_train_set,strat_test_set):
        set.drop([category], axis=1, inplace=True)
    
    return strat_train_set, strat_test_set
