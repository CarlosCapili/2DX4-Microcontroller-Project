import serial
import numpy as np

#Python 3.6.8 was used
#Carlos Capili - 400184894

s = serial.Serial("COM3",115200)#configure port for data transmission

print("Opening: " + s.name)

s.write(b'1')           #This program will send a '1' or 0x31

g=0
x = 0 #x coordinate is 0
distances=[] #used to store the distance measurements

while g!=20: #controls how many x displacements taken by user. In my case there are 20 displacement points each of 0.2m
    i=0
    degree=0
    
    while i<512: #512 will be taken
        
        i+=1
        b = s.readline()    # read one byte
        c = b.decode()      # convert byte type to str
        d = float(c)        #convert into a decimal value
        print(d)
        distances.append(d) #save distance in array
        
    g+=1 
    
f=open("coord.xyz","w")  #create xyz file

for k in range(g*512):#The total number of points is how 512 times how many x displacements taken
    if(k%512==0):#1 rotation consists of 512 points then increment to new x displacement
        x+=200 #new displacement 200mm
        deg=0 #reset
        
    y = int(distances[k])*(np.sin(deg*(np.pi/180))) #vertical axis
    z = int(distances[k])*(np.cos(deg*(np.pi/180))) #horiztonal axis
    f.write(str(x-200)+" " ) #minus 200 so the x starts at 0
    f.write(str(y)+" ")
    f.write(str(z)+"\n")
    deg+=1 #measurement taken every 1 degree
            
f.close()

    
print("Closing: " + s.name)
s.close();

