
import csv 
import time
import matplotlib.pyplot as plt
from drawnow import *

plt.ion()
filename = "C:/Users/lenovo/Desktop/blenderdata.csv"
fields = [] 
rows = [] 

with open(filename, 'r') as csvfile: 
    csvreader = csv.reader(csvfile)  
    for row in csvreader: 
        rows.append(row) 
#print(*rows[1], sep = ",")


def makegraph():
    i=0
    while i<48:
        plt.plot(rows[i], rows[i+1])
        time.sleep(200)
        i=i+2
        plt.show()
drawnow(makegraph)
