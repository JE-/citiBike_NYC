# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 11:44:34 2015

@author: Jonathan
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.chdir('/Users/Jonathan/citiBike_NYC')
data = pd.read_csv('201511-citibike-tripdata.csv')
print data.head()