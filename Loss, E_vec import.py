# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 14:49:01 2022

@author: Sung Ik
"""
# import numpy as np
# import scipy.io
# mat = scipy.io.loadmat('C:\\Users\\Sung Ik\\AEL Dropbox\\Projects\\hyperthermia_cylindrical\\matlab\\multiLayer\\Loss.csv')
# Lossa= list(mat.items())
# Lossa=np.Lossay(Lossa)
# Lossa2=list(mat.values())


# import pandas as pd
# data = pd.read_csv('C:\\Users\\Sung Ik\\AEL Dropbox\\Projects\\hyperthermia_cylindrical\\matlab\\multiLayer\\Loss.csv')
# data2=list(data)

import numpy as np
import csv
Loss=np.zeros((8,8))
E_foc_square=np.zeros((8,8))

f = open('C:\\Users\\Sung Ik\\AEL Dropbox\\Projects\\hyperthermia_cylindrical\\matlab\\multiLayer\\Loss.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
idx=0;
for line in rdr:
    Loss[idx]=line
    idx=idx+1
f.close() 


f = open('C:\\Users\\Sung Ik\\AEL Dropbox\\Projects\\hyperthermia_cylindrical\\matlab\\multiLayer\\E_foc_square.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
idx=0;
for line in rdr:
    E_foc_square[idx]=line
    idx=idx+1
f.close() 