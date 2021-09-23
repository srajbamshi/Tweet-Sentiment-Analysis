dataset_url = 'https://www.kaggle.com/gpreda/covid19-tweets'


import opendatasets as od
od.download(dataset_url)

import pandas as pd
import numpy as np


# Change this
data_dir = './covid19-tweets'


import os
os.listdir(data_dir)

data_set=pd.read_csv('./covid19-tweets/covid19_tweets.csv')


# In[ ]:




