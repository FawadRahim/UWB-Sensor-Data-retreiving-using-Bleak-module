import datetime
import logging
import math
import statistics
import time
import asyncio
import logging
import bitstruct
import bleak
import asyncio
from bleak import BleakScanner, BleakError
from bleak import BleakClient


currenclustertime = []
currentcluster = []
pendinglocation = []
interestspaces = []
positiondata = []
tempx = []
tempy = []
posx = []
posy = []
timestamp = []
d=380 #in centimeter
t=3  # seconds

#testposx = [743,722,724,718,729]
#testposy = [8567,8501,8531,8570,8581]
#testtimestamp = ['2:35:40:815681','2:35:40:893718','2:35:41:3078','2:35:41:143642','2:35:41:190480']

firsttime = True




#positiondata = list(map(list, zip(testposx, testposy, testtimestamp)))
#print(type(positiondata))
#print(positiondata)










def meanpositiondistance(currentcluster):
    for item in currentcluster:
        sum = item[0] + item[1]
        averagevalue = sum / len(currentcluster)
        print(averagevalue)

    return averagevalue



def finddistance(previouspositionx,previouspositiony, currentpositionx,currentpositiony):
    #previousposition can be a tuple so need to extract x and y from it
    print(previouspositionx) #currentcluster[-1][0], currentcluster[-1][1]
    print(previouspositiony)
    print(type(previouspositionx))
    print(currentpositionx)
    print(currentpositiony)

    #made some changes here
    meanx = statistics.mean(previouspositionx)
    meany = statistics.mean(previouspositiony)
    print("mean of current cluster X="+str(meanx))
    print("mean of current cluster Y ="+str(meany))
    previouspositionx = int (meanx)
    previouspositiony = int(meany)
    currentpositionx = int(currentpositionx)
    currentpositiony = int(currentpositiony)
    print("new posiiton X="+str(currentpositionx))
    print("new position Y="+str(currentpositiony))


    #eDistance = math.dist([previouspositionx, previouspositiony], [currentpositionx, currentpositiony])
    #print(eDistance)

    eDistance = math.dist([previouspositionx, previouspositiony], [currentpositionx, currentpositiony])
    print(eDistance)


    return eDistance

    pass




def findtime(clusterstarttime,clusterendtime):
    print("clusterstartime = "+str(clusterstarttime))
    print(type(clusterstarttime))
    print("clusterendtime = " + str(clusterendtime))
    print(type(clusterendtime))
    startime = str(clusterstarttime)
    endtime = str(clusterendtime)

    clusterstarttime = datetime.datetime.strptime(startime,'%H:%M:%S')
    clusterendtime = datetime.datetime.strptime(endtime,'%H:%M:%S')
    currentclusterduration = clusterendtime.second - clusterstarttime.second

    print("duration =" + str(currentclusterduration))

    return currentclusterduration










def ApplyAlgorithm():
    global positiondata
    global pendinglocation
    global interestspaces
    global firsttime
    global tempx
    global tempy

    print("inside apply algorithm")
    print(positiondata)
    for data in positiondata:

        #step 1
        if len(currentcluster)==0 and firsttime == True:
            #step 2 # program starts from here because cluster is zero so the sensor is just started taking positions of a user.
            currentcluster.append(positiondata[0])
            print("first time current cluster "+str(currentcluster))
            print("first time pending location"+ str(pendinglocation))

            # making a list just for the mean position purpose
            tempx.append(int (positiondata[0][0]))
            tempy.append(int (positiondata[0][1]))
            
            print("tempx = "+ str(tempx))
            print("tempy ="+str(tempy))

            firsttime = False



        else:
            # step 3
            #meanposition =meanpositiondistance(currentcluster)
            if finddistance(tempx, tempy, data[0], data[1]) < d:
                currentcluster.append(data)


                #making changes here
                tempx.append(int(data[0]))
                tempy.append(int(data[1]))



                print(currentcluster)
                print("cluster continue")
                pendinglocation.clear()  # we make the pending location empty or Null
                print("pending location" + str(pendinglocation))
            else:
                print("cluster break")
                print(pendinglocation)
                print(currentcluster)
                if len(pendinglocation) != 0: #it means its not null or not empty
                    #pendinglocation.insert(0,[data[0],data[1],data[2]])
                    print(pendinglocation)
                    temptime = findtime(currentcluster[0][-1],currentcluster[-1][-1])
                    print("timeduration"+str(temptime))
                    if  temptime > t:
                        print("time to add current cluster to places"+ str(currentcluster))

                        interestspaces.extend(currentcluster)
                        currenclustertime.append(temptime)
                        print("interest spaces" + str(interestspaces))
                        print("current cluster time duration is =" + str(currenclustertime))
                        for item in currentcluster:
                            
                            with open("C:/Users/fawad/Downloads/experiment3/testingposx.txt",'a') as filee:
                                filee.write(str(item[0]))
                                filee.write("\n")
                            with open("C:/Users/fawad/Downloads/experiment3/testingposy.txt",'a') as filee:
                                filee.write(str(item[1]))
                                filee.write("\n")
                            with open("C:/Users/fawad/Downloads/experiment3/testingtimestamp.txt",'a') as filee:
                                filee.write(str(item[2]))
                                filee.write("\n")
                        
                        
                    currentcluster.clear()
                    #made some changes here
                    tempx.clear()
                    tempy.clear()
                    
                    currentcluster.append(pendinglocation[0])

                    #made some changes here
                    tempx.append( int (pendinglocation[0][0]))
                    tempy.append(int (pendinglocation[0][1]))
                    
                    print("current cluster after adding pending location "+ str(currentcluster))
                    if finddistance(tempx, tempy, data[0], data[1]) < d:
                        currentcluster.append(data)
                        #made some changes here
                        tempx.append(int (data[0]) )
                        tempy.append(int (data[1]) )

                        pendinglocation.clear()  # we make the pending location empty or Null
                    else:
                        #pendinglocation.clear()
                        pendinglocation.insert(0,[data[0],data[1],data[2]])

                else:
                    print("pending locaiton ="+str(pendinglocation))
                    #pendinglocation.clear()
                    pendinglocation.insert(0, [data[0], data[1], data[2]])
                    print("pending locaiton =" + str(pendinglocation))







    print("current cluster = "+str(currentcluster))
    print("time for every cluster in a list"+ str(currenclustertime))
    print("interestspaces =" + str(interestspaces))
    print("spaces count = "+ str(len(currenclustertime)))
    print("pending location = "+str(pendinglocation))


    for item in interestspaces:
        print(item)
        with open("C:/Users/fawad/Downloads/Wxperiment/test.txt",'a')as ff:
            ff.write(item[0][0])
            ff.write("/n")






def readfile():
    global posx
    global posy
    posz = []
    posqf = []
    global timestamp
    global positiondata
    # start reading from files e.g posx, posy, qf, timestamp
    with open('C:/Users/fawad/Downloads/experiment3/posx.txt', 'r') as fileX:
        for line in fileX:
            posx.append(line.rstrip())
    with open('C:/Users/fawad/Downloads/experiment3/posy.txt', 'r') as fileY:
        for line in fileY:
            posy.append(line.rstrip())
    #with open('C:/Users/fawad/Downloads/posz.txt', 'r') as fileZ:
    #    for line in fileZ:
    #        posz.append(line.rstrip())
    #with open('C:/Users/fawad/Downloads/qf.txt', 'r') as fileqf:
    #    for line in fileqf:
    #        posqf.append(line.rstrip())
    with open('C:/Users/fawad/Downloads/experiment3/timestamp.txt', 'r') as filetimestamp:
        for line in filetimestamp:
            timestamp.append(line.rstrip())

    positiondata = list(map(list, zip(posx, posy, timestamp)))
    print(type(positiondata))
    print(positiondata)
    # print(positiondata)
    # print(type(posx))
    # print(posx)
    # print(posy)
    # print(posz)
    # print(posqf)
    # print(timestamp)












if __name__ == "__main__":
    readfile()
    ApplyAlgorithm()


