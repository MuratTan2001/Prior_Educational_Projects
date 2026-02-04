# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 19:20:37 2023

@author: Ranger
"""
from scipy.misc import electrocardiogram
import matplotlib.pyplot as plt
import numpy as np

#get ready to use ECG signal
ecg = electrocardiogram()
#sampling frequency 360Hz
fs = 360
#lower and upper index for investigation
lower=0
upper=20000

x1=ecg[lower:upper]

# generating time axis values
time = np.arange(x1.size) / fs
plt.figure()
plt.title("ECG mV/s")
plt.plot(time, x1)
plt.xlabel("time in s")
plt.ylabel("ECG in mV")
# zooming specific area
plt.show()


def smoothing_mov_av(array=x1,width=5,iteration=5):
     arr=array
     smoothend=np.array([])
     f=round(((width-1)/2))
     t=np.zeros([f])
     for n in range(0,iteration,1):
         sum_of=0
         smoothend=np.array([])
         arr= np.append(t,arr)
         arr= np.append(arr,t)
         for i in range(f,arr.size-f):
            for h in range(-f,f,1):
                 sum_of=arr[h+i]+sum_of
            sum_of= sum_of/width
            smoothend= np.append(smoothend, [sum_of])
         arr=smoothend
     return smoothend
 
 
x=smoothing_mov_av(array=x1,width=5,iteration=30)
plt.figure()
plt.title("Smoothed")
plt.plot(time, x)
plt.xlabel("time in s")
plt.ylabel("ECG in mV")
plt.show()


# find peaks
from scipy.signal import find_peaks
# get specific range of ecg signal

p_allR, p_allRproperties = find_peaks(x, distance=150)
plt.figure()
plt.title("ALL R points")
plt.plot(x)
plt.plot(p_allR, x[p_allR], "xr")
plt.show()

p_allPRT, p_allPRTproperties = find_peaks(x, prominence=[0.05],distance=30)
plt.figure()
plt.title("All PRT points")
plt.plot(x)
plt.plot(p_allPRT, x[p_allPRT], 'xr')
plt.show()

p_allQS, p_allQSproperties = find_peaks(x*(-1), prominence=[0.05],distance=30)
plt.figure()
plt.title("ALL QS points")
plt.plot(x)
plt.plot(p_allQS, x[p_allQS], 'xk')
plt.show()

p_allPQRST = np.concatenate((p_allPRT,p_allQS))
p_allPQRST.sort(kind='mergesort')
plt.figure()
plt.title("All PQRST points")
plt.plot(x)
plt.plot(p_allQS, x[p_allQS], 'xk')
plt.plot(p_allPRT, x[p_allPRT], 'xr')
plt.show()

p_abnormalR, p_abnormalRproperties = find_peaks(x, prominence=1, width=20)
p_abnormalRproperties["prominences"]
p_abnormalRproperties["widths"]
plt.figure()
plt.title("Abnormal R")
plt.plot(x)
plt.plot(p_abnormalR, x[p_abnormalR], "x")
plt.vlines(x=p_abnormalR, ymin=x[p_abnormalR] - p_abnormalRproperties["prominences"],
           ymax = x[p_abnormalR], color = "C1")
plt.hlines(y=p_abnormalRproperties["width_heights"], xmin=p_abnormalRproperties["left_ips"],
           xmax=p_abnormalRproperties["right_ips"], color = "C1")
plt.show()

p_abnormalS, p_abnormalSproperties = find_peaks(x*(-1), prominence=[2],width=100)
p_abnormalSproperties["prominences"]
p_abnormalSproperties["widths"]
plt.figure()
plt.title("Abnormal S")
plt.plot(x)
plt.plot(p_abnormalS, x[p_abnormalS], "x")
plt.show()

p_normalPRT=p_allPRT
for i_abnormal in p_abnormalR:
    print(i_abnormal)
    p_normalPRT=np.delete(p_normalPRT, np.where(p_normalPRT==i_abnormal))
    
p_normalQS=p_allQS
for i_abnormal in p_abnormalS:
    print(i_abnormal)
    p_normalQS=np.delete(p_normalQS, np.where(p_normalQS==i_abnormal))
    
p_normalR=p_allR
for i_abnormal in p_abnormalR:
    p_normalR=np.delete(p_normalR, np.where(p_normalR==i_abnormal))

p_normalPT=p_normalPRT
for i_abnormal in p_allR:
    p_normalPT=np.delete(p_normalPT, np.where(p_normalPT==i_abnormal))


p_normalT=np.array([])
for i_separateR in p_normalR:
    for i_separatePT in p_normalPT:
        if round(i_separateR*1000)<round(i_separatePT*1000):
            p_normalT=np.append(p_normalT,round(i_separatePT))
            break
p_normalT=p_normalT.astype(int)

p_normalP=p_normalPT
for i_abnormal in p_normalT:
    p_normalP=np.delete(p_normalP, np.where(p_normalP==i_abnormal))

p_normalS=np.array([])
for i_separateR in p_normalR:
    for i_separateQS in p_allQS:
        if round(i_separateR*1000)<round(i_separateQS*1000):
            p_normalS=np.append(p_normalS,i_separateQS)
            break
p_normalS=p_normalS.astype(int)

p_allQ=p_allQS
for i_abnormal in p_normalS:
    p_allQ=np.delete(p_allQ, np.where(p_allQ==i_abnormal))
    
p_normalQ=np.array([])
for i_separateP in p_normalP:
    for i_separateQ in p_allQ:
        if round(i_separateP*1000)<round(i_separateQ*1000):
            p_normalQ=np.append(p_normalQ,round(i_separateQ))
            break
p_normalQ=p_normalQ.astype(int)

p_fault=p_allQS
for i_abnormal in p_normalQ:
    p_fault=np.delete(p_fault, np.where(p_fault==i_abnormal))

p_PQRST = np.concatenate((p_normalR,p_normalT,p_normalP,p_normalS,p_normalQ))
p_PQRST.sort(kind='mergesort')
plt.figure()
plt.title("Normal PQRST")
plt.plot(x)
plt.plot(p_normalR, x[p_normalR], 'sb')
plt.plot(p_normalT, x[p_normalT], 'xg')
plt.plot(p_normalP, x[p_normalP], 'xr')
plt.plot(p_normalS, x[p_normalS], 'oc')
plt.plot(p_normalQ, x[p_normalQ], 'om')
#plt.plot(p_fault, x[p_fault], '*k')
plt.show()

def sequence_diffrence(array0):
    result_array=np.array([])
    for i in range(1,array0.size-1,1):
        result_array=np.append(result_array,(array0[i+1]-array0[i]))
    return result_array

def sequence_diffrence_2(array1,array2):
    array3 = np.concatenate((array1,array2))
    array3.sort(kind='mergesort')
    result_array=np.array([])
    for i in range(1,array3.size-1,1):
        result_array=np.append(result_array,(array3[i+1]-array3[i]))
    return result_array

#In sequential blocks: PP, QQ, TP
#In the same block: PQ, QR, RS, ST, PT
Dict=[
sequence_diffrence(p_normalP),
sequence_diffrence(p_normalQ),
sequence_diffrence_2(p_normalT,p_normalP),
sequence_diffrence_2(p_normalP,p_normalQ),
sequence_diffrence_2(p_normalQ,p_normalR),
sequence_diffrence_2(p_normalR,p_normalS),
sequence_diffrence_2(p_normalS,p_normalT),
sequence_diffrence_2(p_normalP,p_normalT)
      ]