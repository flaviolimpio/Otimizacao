# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 11:15:34 2016

@author: pulabio
"""

import csv
import numpy as np

filename = "AR6.csv"
#input_file = csv.DictReader(open(filename))

with open(filename, mode='r') as infile:
    reader = csv.reader(infile)
    mydict = {float(rows[0]):float(rows[1]) for rows in reader}
    
#    infile.seek(0)
#    keys = tuple(float(rows[0]) for rows in reader)
#    infile.seek(0)
#    values = tuple(float(rows[1]) for rows in reader)
    
#    values = tuple(mydict[key] for key in keys)
    #values = [mydict[key] for key in keys]

def lookup(dic, valor):
    
    keys = list(dic.keys())
    keys.sort()
    
    values = tuple(dic[key] for key in keys)

    return np.interp(valor,keys,values)

#060948417728961105, 0.053978189647269664
#0.07122799210988566, 0.04659946563823142
#0.15312952107967537, 0.016519382671171673