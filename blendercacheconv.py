import struct
import math
vel=[]
pos=[]
p_x=[]
p_y=[]
p_z=[]
def dump_one_file(fname):
    global vel
    global pos
    global p_x
    global p_y
    global p_z
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
            (pos_x,pos_y,pos_z) = struct.unpack("fff ", chunk)
            p_x.append(pos_x)
            p_y.append(pos_y)
            p_z.append(pos_z)
            pos.append(math.sqrt(pos_x*pos_x+pos_y*pos_y+pos_z*pos_z))
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
#print(*pos, sep=',')

l=len(pos)
print(l)
print(max(pos))
maxpos=pos.index(max(pos))
print('x=', p_x[maxpos])
print('y=', p_y[maxpos])
print('z=', p_z[maxpos])
print('max(x)=', max(p_x))
#max_x=pos.index(max(p_x))
#print('y(max_x)=',p_y[max_x])
#print('z(max_x)=',p_z[max_x])
print('max(y)=', max(p_y))
print('max(z)=', max(p_z))
print('min(x)=', min(p_x))
print('min(y)=', min(p_y))
print('min(z)=', min(p_z))
k=[]
i=0
j=0
while i<l:
    if pos[i]>8.18:
        k.append(pos.index(pos[i]))
        j=j+1
    i=i+1
print(j)
i=0
while i<j:
    print(i+1,'=', '(',p_x[k[i]], ',', p_y[k[i]], ',', p_z[k[i]], ')')
    i=i+1
i=0
while i<l:
    p_x[i]=p_x[i]+5.782
    p_y[i]=p_y[i]+5.782
    p_z[i]=p_z[i]-0.047
    i=i+1

# assigning index number to each particle
num=[0]*40
i=0
print(p_x[1])
print(p_y[1])
while i<l:
    j=0
    while j<4:
        k=0
        if p_y[i] >= (2.891*(j))  and  p_y[i] < (2.891*(j+1)):
                
            while k<10:
                if p_x[i]>= 1.1564*(k) and p_x[i]< 1.1564*(k+1):
                    num[10*j+k]=num[10*j+k]+1
                k=k+1
        j=j+1
    i=i+1
print(i)
print(*num, sep=',')
# assigning index numbers to all the small cubes formed
i=1
c_y=0
rows,cols=(4,10)
sub_cubes=[[0]*cols]*rows
q=0


while q<4:
    c_x=0
    p=0
    sub_cubes.append([])

    while p<10:
        sub_cubes[q][p]={"indexno": i, "c_x": c_x, "c_y": c_y}
        c_x=c_x+0.5782
        p=p+1
        i=i+1
    c_y=c_y+5.782/4
    q=q+1 


# defining class for each particle
class Particle:
    def __init__(posx,posy,posz,velocity,index):
        self.posx=posx
        self.posy=posy
        self.posz=posz
        self.velocity=velocity
        self.index=index


'''M_vel=max(vel)
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
plt.show()'''



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
