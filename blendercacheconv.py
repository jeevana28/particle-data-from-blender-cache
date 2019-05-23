import struct
import math
vel=[]
def dump_one_file(fname):
    global vel
    f = open(fname, "rb")

    magic = f.read(8)
    if magic != b'BPHYSICS':
        raise Exception("not a blender physics cache")

    flavor = f.read(12)
    (flavor,count,something) = struct.unpack("iii", flavor)

    #print( "%d\t%d\t%d"%(flavor,count,something))

    if flavor==1: # point cache

        while True:
            vel
            rec_len = 4
            chunk = f.read(rec_len)

            if chunk is None or len(chunk)==0:
                break
            if len(chunk) != rec_len:
                raise Exception("short read (%d<%d)"%(len(chunk), rec_len))
            all = struct.unpack("i ", chunk)
            #print("%d\t"%all)


            rec_len=12
            chunk = f.read(rec_len)
            if chunk is None or len(chunk)==0:
                break
            if len(chunk) != rec_len:
                raise Exception("short read (%d<%d)"%(len(chunk), rec_len))
            all=struct.unpack("fff ", chunk)
            #print("<%f,%f,%f>\t"%all)


            rec_len=12
            chunk = f.read(rec_len)

            if chunk is None or len(chunk)==0:
                break
            if len(chunk) != rec_len:
                raise Exception("short read (%d<%d)"%(len(chunk), rec_len))
            (vel_x, vel_y, vel_z) = struct.unpack("fff ", chunk)
            #print("<%f,%f,%f>"%(vel_x,vel_y, vel_z))
            vel.append(math.sqrt(vel_x*vel_x+vel_y*vel_y+vel_z*vel_z))
        

dump_one_file("C:/Users/lenovo/Desktop/blenderfolder/bpy/43756265_000081_00.bphys")
#print(*vel,  sep=",")
#print("\n")
M_vel=max(vel)
m_vel=min(vel)
print(max(vel))
print(min(vel))
l=len(vel)
print(l)
num=[]
velocity=[]
v=0.5
while v<=M_vel:
    i=0
    n=0
    velocity.append(v)
    while(i<l):
        if(vel[i]<v and vel[i]>=v-0.5):
            n=n+1
        i=i+1
    num.append(n)
    v=v+0.5
print(*velocity,sep=",")
print(*num, sep=",")
import matplotlib.pyplot as plt 
x=velocity
y=num
plt.plot(x,y)
plt.show()



'''import numpy as np 
   
a = np.array(vel) 
np.histogram(a,bins = [0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0,10.5,11.0,11.5,12.0]) 
hist,bins = np.histogram(a,bins = [0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0,10.5,11.0,11.5,12.0]) 
print(hist) 
print (bins) 
from matplotlib import pyplot as plt 
import numpy as np  
   
a = np.array(vel) 
b=a/l
plt.hist(b, bins = [0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0,10.5,11.0,11.5,12.0]) 
plt.title("histogram") 
plt.show()'''


'''i=2
import csv

myData = [velocity,num]  
myFile = open("C:/Users/lenovo/Desktop/blenderdata.csv", "a")  
with myFile:  
   writer = csv.writer(myFile)
   writer.writerows(myData)
   myFile.close()'''
