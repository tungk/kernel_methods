#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:30:43 2017

@author: fubao
"""

#implementation of kernel ridge regression
import numpy as np



def KRRS(trainData, testData, i):     
    '''
    kernel ridge regression from scratch
    k(x1,x2) = (1+x1 * x2) ^i
    '''

    trainX = trainData[0]
    trainY = trainData[1]
    
    print ("trainX shape[0]: ", trainX.shape[0])
    kArr = np.empty((trainX.shape[0], trainX.shape[0]), dtype=np.float)

    print ("kArr shape: ", kArr.shape)

    #kArr = np.empty(1)
    for i in range(0, trainX.shape[0]):
        for j in range(0, trainX.shape[0]):
            xi = trainX[i]
            xj = trainX[j]
            kij = (1 + np.dot(xi, xj))
            
            #print ("kij: ", kij)
            #kArr = np.vstack((kArr, np.array(kij)))
            #print ("trainX kij: ", kArr)
            kArr = np.append(kArr, kij)
            #print ("kij: ", kArr)
    
    print ("kArr shape: ", kArr[0][0], kArr[2][0], kArr[199][199], type(kArr), kArr.shape)
    print ("kij: ", kArr)
    
    '''        
    a=np.array([[1,2,3],[3,4,5], [7,8,9], [1,2,5]])
    b=np.array([[1,2,3],[1,2,3]])
    c = np.array([1,2,3])
    d = np.array([1,2,3])
    res = np.dot(c,d)
    '''
    