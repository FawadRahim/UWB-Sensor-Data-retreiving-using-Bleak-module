# -*- coding: utf-8 -*-

import sys
import numpy
import math
#import scipy
from threading import Timer
from time import time,sleep

anchor0x40a1 = []
anchor0x5633 = []
anchor0xc24 = []
anchor0x5da9 = []
run = True
milisecond = 0.210
x=0
tag_id = 5
size=1000
file = "C:/Users/fawad/Downloads/myhardrive/scripts/Newfolder/sampledata.txt"
#file = "/home/pi/Desktop/DWM1001_DWM1001-DEV_MDEK1001_Sources_and_Docs_v8/DWM1001/Source_Code/DWM1001_host_api/dwm1001_host_api/examples/ex1_TWR_2Hosts/tag/newdata.txt"
anchor_loc_dict={}

#anchor_loc_dict["0xc24"] =(700,730,2400)
#anchor_loc_dict["0x40a1"]=(6580, 730, 2400)
#anchor_loc_dict["0x5633"]=(6580,6450,2400)
#anchor_loc_dict["0x5da9"]=(700, 6450,2400)

#tag_position by api dwm_loc_get is x=3844, y=4284 and z =2329 qf=100

anchor_loc_dict["0xc24"] =(5560,0,0)
anchor_loc_dict["0x40a1"]=(5970, 5828, 0)
anchor_loc_dict["0x5633"]=(361,5911,0)
anchor_loc_dict["0x5da9"]=(0, 0,0)




def getdata():
    global anchorx1,anchory1,anchorz1,anchordist1,anchorx2,anchory2,anchorz2,anchordist2,anchorx3,anchory3,anchorz3,anchordist3
    dic_dist = [{}]



    anchor_0 =[]
    anchor_1 = []
    anchor_2 = []
    anchor_3 = []
    date_time = []





    read_data = readfile(file)
    #print(read_data)

    anchor_tuple = (anchor_0,anchor_1,anchor_2,anchor_3)

   # for temp in read_data:
    #    templist = temp.split(",")
     #   print(templist)
      #  if(templist[1]=="0x5da9"):
       #     print("hello")
        #elif(templist[1] == "0x40a1"):
         #   anchorx1 = templist[2]
          #  anchory1 = templist[3]
           # anchorz1 = templist[4]
            #anchordist1 = templist[5]
        #elif(templist[1] == "0xc24"):
         #   anchorx2 = templist[2]
          #  anchory2 = templist[3]
           # anchorz2 = templist[4]
            #anchordist2 = templist[5]
        #elif(templist[1] == "0x5633"):
         #   anchorx3 = templist[2]
          #  anchory3 = templist[3]
           # anchorz3 = templist[4]
            #anchordist3 = templist[5]
        #else:
         #   print("nothing")

#        Trilateration(anchorx1,anchory1,anchorz1,anchordist1,anchorx2,anchory2,anchorz2,anchordist2,anchorx3,anchory3,anchorz3,anchordist3)





def Trilateration3d(anchor0x5da9,anchor0x40a1,anchor0xc24,anchor0x5633):

    print(anchor0x5da9)
    anchor1list = list(numpy.float_(anchor0x40a1[2:]))
    P1 = numpy.array(anchor1list[:-1])
    
    anchor2list = list(numpy.float_(anchor0xc24[2:]))
    P2 = numpy.array(anchor2list[:-1])
    
    anchor3list = list(numpy.float_(anchor0x5633[2:]))
    P3 = numpy.array(anchor3list[:-1])
    
    anchor4list = list(numpy.float_(anchor0x5da9[2:]))
    P4 = numpy.array(anchor4list[:-1])
    
    print(P1)
    print(P2)
    print(P3)
    print(P4)
    
    anchor1_d1 = float(anchor0x40a1[5]) #anchor1list[3] #3264 #milimeter
    print(anchor1_d1)

    anchor2_d2 = float(anchor0xc24[5]) #anchor2list[3] #4056
    print(anchor2_d2)
    
    anchor3_d3 = float(anchor0x5633[5]) #anchor3[3] # 5344
    print(anchor3_d3)
    
    anchor4_d4 = float(anchor0x5da9[5])
    print(anchor4_d4)
    
    
    
    
	
    r1 = anchor1_d1
    r2 = anchor2_d2
    r3 = anchor3_d3
    r4 = anchor4_d4
	
    e_x = (P2 - P1) / numpy.linalg.norm(P2 - P1)
    print(e_x)
	
    i = numpy.dot(e_x, (P3 - P1))
    print(i)
	
    e_y = (P3 - P1 - (i * e_x)) / (numpy.linalg.norm(P3 - P1 - (i * e_x)))
    print(e_y)
	
    e_z = numpy.cross(e_x,e_y)
    print(e_z)
	
    d = numpy.linalg.norm(P2 - P1)
    print(d)
	
    j = numpy.dot(e_y, (P3 - P1))
    print(j)
	
    x = ((r1 ** 2) - (r2 ** 2) + (d ** 2)) / (2 * d)
    print(x)
	
    y = (((r1 ** 2) - (r3 ** 2) + (i ** 2) + (j ** 2)) / (2 * j)) - ((i / j) * x)
    print(y)
	
    z1 = numpy.sqrt(r1 ** 2 - x ** 2 - y ** 2)
    print(z1)
	
    z2 = numpy.sqrt(r1 ** 2 - x ** 2 - y ** 2) * (-1)
    print(z2)
	
    ans1 = P1 + (x * e_x) + (y * e_y) + (z1 * e_z)
    print(ans1)
	
    ans2 = P1 + (x * e_x) + (y * e_y) + (z2 * e_z)
    print(ans2)
	
    dist1 = numpy.linalg.norm(P4 - ans1)
    print(dist1)
	
    dist2 = numpy.linalg.norm(P4 - ans2)
    print(dist2)
	
    if numpy.abs(r4 - dist1) < numpy.abs(r4 - dist2):
        return ans1
    else:
        return ans2






def Trilateration(anchor0x5da9,anchor0x40a1,anchor0xc24,anchor0x5633):
    #lets introduce variables first
    #print("anchor 1 = ")
    #print(anchor0x40a1)
    #print("anchor 2 =")
    #print(anchor0xc24)
    #print("anchor 3 =")
    #print(anchor0x5633)
    anchors = 3
    tag_location_x = 0
    tag_location_y = 0
    pi = 3.14  #constant value
    anchor1_x = int(anchor0x40a1[2])#5831 #anchor1list[0]   #anchor1 0x40al
    anchor1_y = int(anchor0x40a1[3]) #anchor1list[1] #5779
    anchor1_d1 = int(anchor0x40a1[5]) #anchor1list[3] #3264 #milimeter

    anchor2_x = int(anchor0x5633[2]) #anchor2list[0] #345  #anchor2 0x5633
    anchor2_y = int(anchor0x5633[3]) #anchor2list[1] #5810
    anchor2_d2 = int(anchor0x5633[5]) #anchor2list[3] #4056

    anchor3_x = int(anchor0xc24[2]) #anchor3list[0]  #5519  #anchor3 0xc24
    anchor3_y = int(anchor0xc24[3]) #anchor3[1]  #0
    anchor3_d3 =  int(anchor0xc24[5]) #anchor3[3] # 5344

    #print(type(anchor1_x))
    #print(anchor1_y)
    print(anchor1_d1)
    #print(anchor2_x)
    #print(anchor2_y)
    print(anchor2_d2)
    #print(anchor3_x)
    #print(anchor3_y)
    print(anchor3_d3)




    #anchor1_d1 = (anchor1_x - tag_location_x) **2 + (anchor1_y - tag_location_y) **2 #standard equation of circle for first anchor
    #anchor2_d2 = (anchor2_x - tag_location_x) **2 + (anchor2_y - tag_location_y) **2 #standard equation of circle for Second anchor
    #anchor3_d3 = (anchor3_x - tag_location_x) **2 + (anchor3_y - tag_location_y) **2 #standard equation of circle for third anchor

    #print(anchor1_d1)
    #print(anchor2_d2)
    #print(anchor3_d3)
    #anchor1_d1_ = math.sqrt(anchor1_d1)
    #anchor2_d2_  = math.sqrt(anchor2_d2)
    #anchor3_d3_  = math.sqrt(anchor3_d3)
    #print(anchor1_d1_)
    #print(anchor2_d2_)
    #print(anchor3_d3_)

    P1 = numpy.array([anchor1_x, anchor1_y, anchor1_d1])
    P2 = numpy.array([anchor2_x, anchor2_y, anchor2_d2])
    P3 = numpy.array([anchor3_x, anchor3_y, anchor3_d3])

    #print(P1)
    #print(P2)
    #print(P3)

    # from wikipedia using the formula for ex and ey and ez
    # transform to get circle 1 at origin
    # transform to get circle 2 on x axis
    ex = (P2 - P1) / (numpy.linalg.norm(P2 - P1))
    #print(ex)
    i = numpy.dot(ex, P3 - P1)
    #print("i = " + str(i))
    ey = (P3 - P1 - i * ex) / (numpy.linalg.norm(P3 - P1 - i * ex))
    #print(ey)
    ez = numpy.cross(ex, ey)
    #print(ez)
    d = numpy.linalg.norm(P2 - P1)
    #print("d = " + str(d))
    j = numpy.dot(ey, P3 - P1)
    #print("j = " + str(j))

    # from wikipedia using the formula for x and y to get the values
    # plug and chug using above values
    x = (pow(anchor1_d1, 2) - pow(anchor2_d2, 2) + pow(d, 2)) / (2 * d)
    y = ((pow(anchor1_d1, 2) - pow(anchor3_d3, 2) + pow(i, 2) + pow(j, 2)) / (2 * j)) - ((i / j) * x)

    #print("x =" + str(x))
    #print("y = " + str(y))

    z = numpy.sqrt(pow(anchor1_d1, 2) - pow(x, 2) - pow(y, 2))
    #print("z = " + str(z))

    # TagLocation is an array with x,y,z of trilateration point (intersection point of three circles (anchors))
    TagLocation = P1 + x * ex + y * ey + z * ez

    print("Tag Location point is = " + str(TagLocation))

    #lets draw circles first
    #a2 = (x−0)**2 + (y−0)**2

def readfile(file):
    data = []
    i=0
    global x
    global anchor0x40a1
    global anchor0x5633
    global anchor0xc24
    global anchor0x5da9
    with open(file) as myfile:

        while True:
            myline = myfile.readline()
            myline2 = myfile.readline()
            myline3 = myfile.readline()
            myline4 = myfile.readline()
            #print(x)
            #print(myline)
            #print(myline2)
            #print(myline3)
            #print(myline4)
            if not myline:
                break
            anchor0x5da9 = myline.rstrip().split(",")
            anchor0x40a1 = myline2.rstrip().split(",")
            anchor0xc24 = myline3.rstrip().split(",")
            anchor0x5633 = myline4.rstrip().split(",")
            print(anchor0x5da9)
            print(anchor0x40a1)
            print(anchor0xc24)
            print(anchor0x5633)
            #Trilateration(anchor0x5da9,anchor0x40a1,anchor0xc24,anchor0x5633)
            location = Trilateration3d(anchor0x5da9,anchor0x40a1,anchor0xc24,anchor0x5633)
            print(location)
            #sleep(milisecond)
            #if(myline != ""):
             #   #processfiledata(linelist)
              #  if (linelist[1] == "0x40a1"):
               #     anchor0x40a1 = linelist[2:]
                #    # print(anchor0x40a1)
                 #   # print(type(anchor0x40a1))
                #elif (linelist[1] == "0xc24"):
                 #   anchor0xc24 = linelist[2:]
                  #  # print(anchor0xc24)
                #elif (linelist[1] == "0x5633"):
                 #   anchor0x5633 = linelist[2:]
                  #  # print(anchor0x5633)
                #elif (linelist[1] == "0x5da9"):
                 #   anchor0x5da9 = linelist[2:]
                #else:
                 #   print("nothing")
                #x = x + 1

                #if (x >= 3):
                 #   #print("anchor 1 = ")
                  #  #print(anchor0x40a1)
                   # print("anchor 2 =")
                    #print(anchor0x5633)
                    #print("anchor 3 =")
                    #print(anchor0xc24)
                    #print("anchor 4 =")
                    #print(anchor0x5da9)
                    #Trilateration(anchor0xc24,anchor0x5633,anchor0x40a1)
                #else:
                 #   print("loops is not reached to 3 anchor data yet")
            #lines_alldata = alldata.split("\n")
            #data.extend(lines_alldata)
    return data


def processfiledata(linelist):
    global anchor0x40a1
    global anchor0x5633
    global anchor0xc24
    global anchor0x5da9
    global x

    #print(linelist)
    if(linelist[1] == "0x40a1"):
        anchor0x40a1 = linelist[2:]
        #print(anchor0x40a1)
        #print(type(anchor0x40a1))
    elif(linelist[1] == "0xc24"):
        anchor0xc24 = linelist[2:]
        #print(anchor0xc24)
    elif(linelist[1] == "0x5633"):
        anchor0x5633 = linelist[2:]
        #print(anchor0x5633)
    elif(linelist[1] == "0x5da9"):
        anchor0x5da9 = linelist[2:]
    else:
        print("nothing")

    x = x+1

    if(x == 3):
        print("anchor 1 = ")
        print(anchor0xc24)
        print("anchor 2 =")
        print(anchor0x5633)
        print("anchor 3 =")
        print(anchor0x40a1)
        print("anchor 4 =")
        print(anchor0x5da9)
        # Trilateration(anchor0xc24,anchor0x5633,anchor0x40a1)
    else:
        print("loops is not reached to 3 anchor data yet")

    #print(anchorx1)
    #print(anchorz1)
    #print(anchordist1)


def Test():
    global run
    print("something!")
    if run:
        Timer(1, Test).start()
        #sleep(5 - time() % 1)



if __name__ == "__main__":
    getdata()
    #Test()
    #Trilateration()
