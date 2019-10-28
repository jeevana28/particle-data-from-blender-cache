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



j=0
red_x=[]
red_y=[]
# setting coordinates of cuboids
while j<4:
    i=0
    while i<10:
        if(num[10*j+i]>20000):
            red_x.append(i)
            red_y.append(j)
        i=i+1
    j=j+1
i=0

def explode(data):
    size = np.array(data.shape)*2
    data_e = np.zeros(size - 1, dtype=data.dtype)
    data_e[::2, ::2, ::2] = data
    return data_e

n_voxels = np.zeros((10,4,1), dtype = bool)
while(i<len(red_x)):
    n_voxels[red_x[i], red_y[i], :] = True
    i=i+1
    print(i)


facecolors = np.where(n_voxels, '#FFc78a29', '#1f77b430')
edgecolors = np.where(n_voxels, '#BFAB6E', '#7D84A6')
filled = np.ones(n_voxels.shape)

filled_2 = explode(filled)
fcolors_2 = explode(facecolors)
ecolors_2 = explode(edgecolors)


x, y, z = np.indices(np.array(filled_2.shape) + 1).astype(float) // 2
x[0::2, :, :] += 0.05
y[:, 0::2, :] += 0.05
z[:, :, 0::2] += 0.05
x[1::2, :, :] += 0.95
y[:, 1::2, :] += 0.95
z[:, :, 1::2] += 0.95


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.voxels(x, y, z, filled_2, facecolors=fcolors_2, edgecolors=ecolors_2)

plt.show()