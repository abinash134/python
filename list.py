#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 10:00:17 2019

@author: abinash
"""

funs=[]
valss=[]
lis_t={}
result=[]
def record(result):
    n=result.copy()
    valss.append(n)
    print(valss)
N = int(input())
for i in range(N):
    fun,*vals=input().split()
    vals = list(map(int, vals))
    lis_t[fun]=vals
    #funs.append(fun)
    j=fun
    if j== "insert":
       result.insert(lis_t[j][0],lis_t[j][1])
       print(result)
    if j=="print":
        record(result)
    if j=="remove":
        result.remove(lis_t[j][0]) 
        print(result)
    if j=="append":
        result.append(lis_t[j][0])
        print(result)
    if j=="sort":
        result.sort()
        print(result)
    if j=="pop":
        result.pop()
        print(result)
    if j =="reverse":
        result.reverse()
        print(result)
       
