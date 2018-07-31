# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 23:56:19 2018

@author: gauravkgupta
"""

import pandas as pd

df = pd.DataFrame({'X': [7, 2, 0, 3, 4, 2, 5, 0, 3, 4]})
s = []
count = 0
for x in range(0, len(df)):
    if(df.iloc[x]['X']!=0):
        s.append(count+1)
        count = count+ 1
    else:
        s.append(0)
        count = 0
       
       
df['y'] = s
        