# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 11:13:01 2019

@author: mach0
"""
list_all=[]
list_un=[('R', 'R', 'R'), ('R', 'R', 'L'), ('R', 'R', 'U'), ('R', 'R', 'D'), ('R', 'L', 'R'), ('R', 'L', 'L'), ('R', 'L', 'U'), ('R', 'L', 'D'), ('R', 'U', 'R'), ('R', 'U', 'L'), ('R', 'U', 'U'), ('R', 'U', 'D'), ('R', 'D', 'R'), ('R', 'D', 'L'), ('R', 'D', 'U'), ('R', 'D', 'D'), ('L', 'R', 'R'), ('L', 'R', 'L'), ('L', 'R', 'U'), ('L', 'R', 'D'), ('L', 'L', 'R'), ('L', 'L', 'L'), ('L', 'L', 'U'), ('L', 'L', 'D'), ('L', 'U', 'R'), ('L', 'U', 'L'), ('L', 'U', 'U'), ('L', 'U', 'D'), ('L', 'D', 'R'), ('L', 'D', 'L'), ('L', 'D', 'U'), ('L', 'D', 'D'), ('U', 'R', 'R'), ('U', 'R', 'L'), ('U', 'R', 'U'), ('U', 'R', 'D'), ('U', 'L', 'R'), ('U', 'L', 'L'), ('U', 'L', 'U'), ('U', 'L', 'D'), ('U', 'U', 'R'), ('U', 'U', 'L'), ('U', 'U', 'U'), ('U', 'U', 'D'), ('U', 'D', 'R'), ('U', 'D', 'L'), ('U', 'D', 'U'), ('U', 'D', 'D'), ('D', 'R', 'R'), ('D', 'R', 'L'), ('D', 'R', 'U'), ('D', 'R', 'D'), ('D', 'L', 'R'), ('D', 'L', 'L'), ('D', 'L', 'U'), ('D', 'L', 'D'), ('D', 'U', 'R'), ('D', 'U', 'L'), ('D', 'U', 'U'), ('D', 'U', 'D'), ('D', 'D', 'R'), ('D', 'D', 'L'), ('D', 'D', 'U'), ('D', 'D', 'D')]
for combo in list_un:
    ss='URL???DDDDU'      
    for i in combo:
        ss=ss.replace('?',i,1)     
        list_all.append(ss)


print (list_all)  