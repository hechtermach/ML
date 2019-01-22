# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 01:27:35 2019

@author: mach0
"""
import itertools
list_step=['R','L','U','D']
list_all=[]
for item in itertools.product(list_step,repeat=3):
    print (item)