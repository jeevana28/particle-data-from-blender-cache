import csv 
import math
import matplotlib.pyplot as plt
import numpy as np
import time
from drawnow import *
filename = "C:/Users/lenovo/Desktop/blenderdata.csv"
fields = [] 
rows = [] 

with open(filename, 'r') as csvfile: 
    csvreader = csv.reader(csvfile)  
    for row in csvreader: 
        rows.append(row) 
#print(*rows[1], sep = ",")
#print(*rows[8], sep=',')
l=len(rows[8])
#print(l)
i=0
while i<48:
        rows[i]=list(filter(None, rows[i]))
        i=i+1
'''k=0
while k<48:
        rows[k]=rows[k][slice(0,21,1)]
        k=k+1'''
def plotg():
        plt.plot(x,y)
        plt.show()
j=0
plt.ion()
while j<47:
        xraw=np.array(rows[j])
        x=xraw.astype(np.float)
        yraw=np.array(rows[j+1])
        y=yraw.astype(np.float)
        time.sleep(0.5)
        j=j+2
        drawnow(plotg)