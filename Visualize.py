import numpy as np
import open3d as o3d

#Python 3.6.8 was used
#Carlos Capili - 400184894

if __name__ == "__main__":

 
    print("TESTING IO FOR POINT CLOUD...")  #taking 
    pcd=o3d.io.read_point_cloud("coord.xyz", format='xyz') #load a point cloud from data

    print(pcd)
    print(np.asarray(pcd.points))

    lines=[] #used to hold connected lines
    po=0 #plane offset

    for x in range(20): #divided by 512 since 20 displacement measurements are taken
        for y in range(0,512,1): #connect all 512 points in the same plane together
            if (y==511):
                lines.append([y+po,po]) #connect points in same plane together
            else:
                lines.append([y+po,y+1+po])
        po+=512; #offset of 512 since we have 512 points

    po=0 #reset variables
    do=512 #offset between planes

    for x in range(19):
        for y in range(0,512,1):
            lines.append([y+po,y+do+po])#connect planes together
        po+=512;
            

    #use LineSet command to weave together all lines in line array
    line_set=o3d.geometry.LineSet(points=o3d.utility.Vector3dVector(np.asarray(pcd.points)), lines=o3d.utility.Vector2iVector(lines))

    o3d.visualization.draw_geometries([line_set]) #visualize data
   
        
