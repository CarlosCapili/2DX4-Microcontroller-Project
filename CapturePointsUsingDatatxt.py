import serial
import numpy as np

a=open("data.txt","r")
deg=0
x=0

distances=[] #used to store the distance measurements
for s in range(10240): #number of points captured for 20 x displacment 
    distances.append(a.readline())
    
a.close()

f=open("coord.xyz","w")  #create xyz file
for k in range(10240):
    if(k%512==0):#1 rotation consists of 512 points then increment to new x displacement
        x+=200 #new displacement 200mm
        deg=0 #reset
        
    y = int(distances[k])*(np.sin(deg*(np.pi/180))) #vertical axis
    z = int(distances[k])*(np.cos(deg*(np.pi/180))) #horiztonal axis
    f.write(str(x-200)+" " ) #minus 200 so the x starts at 0
    f.write(str(y)+" ")
    f.write(str(z)+"\n")
    deg+=1 #taken every 1 degree
    
f.close()
