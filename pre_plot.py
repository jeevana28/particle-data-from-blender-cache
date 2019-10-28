import struct
import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


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

# counting number of particles in each cube
num=[0]*40
i=0
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
print(*num, sep=',')
##num_sorted=num
#num_sorted.sort()
#print(*num_sorted, sep=',')
print(num[0], num[1], num[2],num[3])

#creating class of cubes formed
class Cube:
    def __init__(self,c_x,c_y,c_z,par_num,colour):                       #x,y,z coordinates are one of the corners of cuboids
        self.c_x=c_x
        self.c_y=c_y
        self.c_z=c_z
        self.par_num=par_num 
        self.colour=colour



#plotting 3D graph to find pressure in different regions
#preparing coordinates
x,y,z = np.indices((10,4,1))

j=0
red_x=[]
red_y=[]
# setting coordinates of cuboids
while j<4:
    i=0
    while i<10:
        if(num[10*j+i]>25000):
            red_x.append(i)
            red_y.append(j)
        i=i+1
    j=j+1
          
cube0=(x>0)&(x<1)&(y>0)&(y<1)&(z<1)        
print(*red_x, sep=',')
print(*red_y, sep=',')
k=0
cube=[]

while(k<len(red_x)):
    cube.append((x>i)&(x<i+1)&(y>j)&(y<j+1)&(z<1))
    k=k+1
voxels = cube[0] | cube[1] | cube[2] | cube[3] | cube0


#cube1=(x<3)&(y<2)&(z<1)
#cube2=(x>7)&(y>=3)&(z<1)

#combine objects into single array            

#set the colours of each object
colors = np.empty(voxels.shape, dtype=object)
colors[cube0]='green'
while(k<4):
    colors[cube[k]]='red'
    k=k+1
#colors[cube2]='orange'
#colors[cube3]='green'

#plotting the graph
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.voxels(voxels, facecolors=colors, edgecolor='k')

plt.show()

i=8
print(i)


# defining class for each particle
class Particle:
    def __init__(self,posx,posy,posz,velocity,index):
        self.posx=posx
        self.posy=posy
        self.posz=posz
        self.velocity=velocity
        self.index=index

