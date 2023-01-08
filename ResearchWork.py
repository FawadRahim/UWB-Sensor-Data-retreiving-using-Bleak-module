import csv
import datetime
import logging
import math
import statistics
import pandas as pd
import numpy as np
import time
import asyncio
import logging
import bitstruct
import bleak
import asyncio
from bleak import BleakScanner, BleakError
from bleak import BleakClient
onlyonetimerun = True
clusterARtMeanPts = []
number  = 0
clusterassignednumber = []
resultx =[]
resulty = []
arthematicmeanclusterx = 0
clusterperiodlist =[]
arthematicmeanclustery = 0
currenclustertime = []
currentcluster = []
pendinglocation = []
eventsdata = []
a= []
interestspaces = []
positiondata = []
centroidX = []
centroidY = []
tempx = []
tempy = []
firsteventclass = []
lasteventclass = []
neweventsdata = []


d = 200
t = 2
firsttime = True




class1XStartrange = 1890 #checking books
class1XEndrange = 3780   #checking books

class1YStartrange = 8930  #checking books
class1YEndrange = 9770    #checking books

class2XStartrange = 3780  #checking refrigerator
class2XEndrange = 4710    #checking refrigerator

class2YStartrange = 8780   #checking refrigerator
class2YEndrange = 9770     #checking refrigerator


class3XStartrange = 90  #working at desk
class3XEndrange = 3079   #working at desk

class3YStartrange = 6190 #working at desk
class3YEndrange = 8610   #working at desk

class4XStartrange = 750  #working at desk
class4XEndrange = 3190   #working at desk

class4YStartrange = 3160   #working at desk
class4YEndrange = 5600   #working at desk

class5XStartrange = 440  #working at desk
class5XEndrange = 3640   #working at desk

class5YStartrange = 550   #working at desk
class5YEndrange = 2680   #working at desk

class6XStartrange = 4100  #drinking space
class6XEndrange = 5010  #drinking space

class6YStartrange = 240  #drinking space
class6YEndrange = 1770   #drinking space

class7XStartrange = 4373  #heating food using oven
class7XEndrange = 5010   #heating food using oven


class7YStartrange = 1770  #heating food using oven
class7YEndrange = 2350    #heating food using oven

class8XStartrange = 3800   #throwing gomi in dustbin
class8XEndrange = 5010     #throwing gomi in dustbin

class8YStartrange = 3290   #throwing gomi in dustbin
class8YEndrange = 4510      #throwing gomi in dustbin

class9XStartrange = -830   #working at desk
class9XEndrange = 140      #working at desk

class9YStartrange = 4250    #working at desk
class9YEndrange = 3280     #working at desk

class10XStartrange = -830   #printing pages on printer device
class10XEndrange = 350      #printing pages on printer device

class10YStartrange = 4550    #printing pages on printer device
class10YEndrange = 5130      #printing pages on printer device

class11XStartrange = -830  #checking lab accessories
class11XEndrange = 225     #checking lab accessories

class11YStartrange = 5210  #checking lab accessories
class11YEndrange = 6137    #checking lab accessories

class12XStartrange = 1050  #checking books
class12XEndrange = 3890   #checking books

class12YStartrange = -670   #checking books
class12YEndrange = 50    #checking books




def readfile():
    posx = []
    posy = []
    posz = []
    posqf = []
    timestamp = []
    global positiondata
    # start reading from files e.g posx, posy, qf, timestamp

    fileX = pd.read_csv(r"C:/Users/fawad/Downloads/rwork/tag5/sensordata.txt", sep=',')
    firstCol = np.asarray(fileX.X)
    print(firstCol)
    print(firstCol.size)

    fileY = pd.read_csv(r"C:/Users/fawad/Downloads/rwork/tag5/sensordata.txt", sep=',')
    secondcol = np.asarray(fileY.Y)
    print(secondcol)
    print(secondcol.size)

    filetimestamp = pd.read_csv(r"C:/Users/fawad/Downloads/rwork/tag5/sensordata.txt", sep=',')
    thirdcol = np.asarray(filetimestamp.Timestamp)
    print(thirdcol)

    #print(type(filetimestamp))






    #fileQF = pd.read_csv(r"C:/Users/fawad/Downloads/rwork/researchwork/sensordata.txt", sep=',')
    #fourthcol = np.asarray(fileQF.QF)
    #print(fourthcol)
    #print(fourthcol.size)


    positiondata = list(map(list, zip(firstCol, secondcol, thirdcol)))
    print(type(positiondata))
    print(positiondata)


def isWithIn(currentpositionX,currentpositionY):
    currentpositionX = float (currentpositionX)
    currentpositionY = float (currentpositionY)

    #check for metalwall
    if currentpositionX > 5000:
        return True
    elif currentpositionY > 10000:
        return True
    else:
        print("this point is not noisy!")






def meanpositiondistance(currentcluster):
    for item in currentcluster:
        sum = item[0] + item[1]
        averagevalue = sum / len(currentcluster)
        print(averagevalue)
    return averagevalue


def finddistance(previouspositionx,previouspositiony, currentpositionx,currentpositiony):
    # previousposition can be a tuple so need to extract x and y from it
    print(previouspositionx)  # currentcluster[-1][0], currentcluster[-1][1]
    print(previouspositiony)
    print(type(previouspositionx))
    print(currentpositionx)
    print(currentpositiony)

    # made some changes here
    meanx = statistics.mean(previouspositionx)
    meany = statistics.mean(previouspositiony)
    print("mean of current cluster X=" + str(meanx))
    print("mean of current cluster Y =" + str(meany))
    previouspositionx = float(meanx)
    previouspositiony = float(meany)
    currentpositionx = float(currentpositionx)
    currentpositiony = float(currentpositiony)
    print("new posiiton X=" + str(currentpositionx))
    print("new position Y=" + str(currentpositiony))


    eDistance = math.dist([previouspositionx, previouspositiony], [currentpositionx, currentpositiony])
    print(eDistance)

    return eDistance

    pass




def findtime(clusterstarttime,clusterendtime):


    print("clusterstartime = " + str(clusterstarttime))
    print(type(clusterstarttime))
    print("clusterendtime = " + str(clusterendtime))
    print(type(clusterendtime))
    startime = str(clusterstarttime)
    endtime = str(clusterendtime)

    #clusterstarttime = datetime.datetime.strptime(startime, '%H:%M:%S')
    #clusterendtime = datetime.datetime.strptime(endtime, '%H:%M:%S')

    clusterstarttime = datetime.datetime.strptime(startime, '%Y-%m-%d %H:%M:%S.%f')
    clusterendtime = datetime.datetime.strptime(endtime, '%Y-%m-%d %H:%M:%S.%f')

    print("cl start time = "+ str(clusterstarttime))
    print("cl end time = " + str(clusterendtime))


   #currentclusterduration = clusterendtime.second - clusterstarttime.second    # 10:45:02 10:46:10

    #hourdifference = clusterendtime.hour - clusterstarttime.hour
    #mindifference = clusterendtime.min - clusterstarttime.min
    #secdifference = clusterendtime.second - clusterstarttime.second

    if (clusterendtime > clusterstarttime):
        currentclusterduration = clusterendtime - clusterstarttime
    else:
        currentclusterduration = clusterstarttime - clusterendtime
    #currentclusterduration = int(round(timed.total_seconds() / 60))



    print("duration =" + str(currentclusterduration))

    return currentclusterduration






def ApplyAlgorithm():
    global positiondata
    global arthematicmeanclusterx
    global clusterARtMeanPts
    global arthematicmeanclustery
    global centroidX
    global pendinglocation
    global clusterassignednumber
    global interestspaces
    global firsttime
    global tempx
    global number
    global clusterperiodlist
    global tempy
    global resultx
    global resulty

    print("inside apply algorithm")
    #print(positiondata)


    for data in positiondata:

        #step 1
        if len(currentcluster)==0 and firsttime == True:
            # step 2 # program starts from here because cluster is zero so the sensor is just started taking positions of a user.
            currentcluster.append(positiondata[0])
            print("first time current cluster " + str(currentcluster))
            print("first time pending location" + str(pendinglocation))

            # making a list just for the mean position purpose
            tempx.append(float(positiondata[0][0]))
            tempy.append(float(positiondata[0][1]))

            #print("tempx = " + str(tempx))
            #print("tempy =" + str(tempy))

            firsttime = False




        else:
            # step 3
            #check for the noisy points near metal wall
            result = isWithIn(data[0],data[1])
            #resultagain = isWithInagain(data[0], data[1])




            if result == True:
                continue
           # if resultagain == True:
            #    continue
            if finddistance(tempx, tempy, data[0], data[1]) < d:
                currentcluster.append(data)   # add this position to current cluster
                #centroidX.append(data[0])
                #centroidY.append(data[1])
                #print(currentcluster)
                #print("cluster continue")

                # making changes here
                tempx.append(float(data[0]))
                tempy.append(float(data[1]))

                #print(currentcluster)
                #print("cluster continue")
                pendinglocation.clear()  # we make the pending location empty or Null
                print("pending location" + str(pendinglocation))
            else:
                print("cluster break")
                print(pendinglocation)
                print(currentcluster)
                if len(pendinglocation) != 0: #it means its not null or not empty
                    # pendinglocation.insert(0,[data[0],data[1],data[2]])
                    print(pendinglocation)
                    clusterstarttime = currentcluster[0][-1]
                    clusterendtime = currentcluster[-1][-1]
                    print("clstarttime = " + str(clusterstarttime))
                    print("clendtime = " + str(clusterendtime))

                    temptime = findtime(clusterstarttime, clusterendtime)
                    print("timeduration" + str(temptime))
                    if temptime.seconds >= t:
                        print("time to add current cluster to places" + str(currentcluster))

                        interestspaces.extend(currentcluster)



                        #to check class and make event log
                        categorize_classes(currentcluster,clusterstarttime,clusterendtime)


                        number += 1
                        clusterassignednumber.append(number)
                        currenclustertime.append(temptime)
                        tuplevar = clusterstarttime, clusterendtime

                        clusterperiodlist.append(tuplevar)
                        #print("cluster period list = " + str(clusterperiodlist))
                        #print("interest spaces" + str(interestspaces))
                        #print("current cluster time duration is =" + str(currenclustertime))


                        #resultx.append(arthematicmeanclusterx / len(currentcluster))
                        #resulty.append(arthematicmeanclustery / len(currentcluster))

                        #arthematicmeanclusterx = 0
                        #arthematicmeanclustery = 0

                        #clusterARtMeanPts.append(list(zip(resultx,resulty)))
                        #print("aRTMeanCLuster = "+str(clusterARtMeanPts))

                        print("interest spaces with cluster number = " + str(list(zip(interestspaces,clusterassignednumber,currenclustertime,clusterperiodlist))))

                    currentcluster.clear()
                    # made some changes here
                    tempx.clear()
                    tempy.clear()

                    currentcluster.append(pendinglocation[0])

                    # made some changes here
                    tempx.append(float(pendinglocation[0][0]))
                    tempy.append(float(pendinglocation[0][1]))

                    print("current cluster after adding pending location " + str(currentcluster))
                    if finddistance(tempx, tempy, data[0], data[1]) < d:
                        currentcluster.append(data)
                        # made some changes here
                        tempx.append(float(data[0]))
                        tempy.append(float(data[1]))

                        pendinglocation.clear()  # we make the pending location empty or Null
                    else:
                        # pendinglocation.clear()
                        pendinglocation.insert(0, [data[0], data[1], data[2]])

                else:
                    print("pending locaiton =" + str(pendinglocation))
                    # pendinglocation.clear()
                    pendinglocation.insert(0, [data[0], data[1], data[2]])
                    print("pending locaiton =" + str(pendinglocation))







    print("current cluster = "+str(currentcluster))
    print("time for every cluster in a list"+ str(currenclustertime))
    print("interestspaces =" + str(interestspaces))
    print("spaces count = "+ str(len(interestspaces)))
    print("pending location = "+str(pendinglocation))

def ApplyingMovingAverageFilter(inputx,inputy, windowsize):
    global movingaveragedata
    result = []

    #print(inputx)
    #print(inputy)
    resultx = []
    resulty = []
    movingsumx = sum(inputx[:windowsize])
    movingsumy = sum(inputy[:windowsize])
    #print(movingsumx)
    #print(movingsumy)
    resultx.append(movingsumx / windowsize)
    resulty.append(movingsumy / windowsize)
    #print(resultx)
    #print(resulty)
    for i in range(len(inputx) - windowsize):
        movingsumx += (inputx[i + windowsize] - inputx[i])
        movingsumy += (inputy[i + windowsize] - inputy[i])
        resultx.append(movingsumx / windowsize)
        resulty.append(movingsumy / windowsize)
    #print(resultx)
    #print(resulty)


    for item in resultx:
        with open('C:/Users/fawad/Downloads/rwork/tag5/movingaverageposxWinsize10.txt', 'a') as file:
            file.write(str(item))
            file.write("\n")

    for item in resulty:
        with open('C:/Users/fawad/Downloads/rwork/tag5/movingaverageposyWinsize10.txt', 'a') as file:
            file.write(str(item))
            file.write("\n")


    return resultx,resulty


    #movingaveragedata = list(map(list, zip(resultx, resulty)))
    #print("movingaveragecluster = "+str(movingaveragedata))

def categorize_classes(currentcluster,clusterstarttime,clusterendtime):


    '''
    countlie1 = 0
    countlie2 = 0
    countlie3 = 0
    countlie4 = 0
    countlie5 = 0
    countlie6 = 0
    countlie7 = 0
    countlie8 = 0
    countlie9 = 0
    countlie10 = 0
    countlie11 = 0
    countlie12 = 0
    print("current clus = " + str(currentcluster))
    '''
    columns = zip(*currentcluster)

    for item in currentcluster:

        #with open("C:/Users/fawad/Downloads/rwork/tag5/posx.txt", 'a') as filee:
        #    filee.write(str(item[0]))
        #    #arthematicmeanclusterx += float(item[0])
        #    filee.write("\n")
        #with open("C:/Users/fawad/Downloads/rwork/tag5/posy.txt", 'a') as fileee:
        #    fileee.write(str(item[1]))
        #    #arthematicmeanclustery += float(item[1])
        #    fileee.write("\n")
        #with open("C:/Users/fawad/Downloads/rwork/tag5/timestamp.txt", 'a') as fileeee:
        #    fileeee.write(str(item[2]))
        #    fileeee.write("\n")



        x = item[0]
        y = item[1]




        x = float(x)
        y = float(y)

        x = round(x)
        y = round(y)

        centroidX.append(x)
        centroidY.append(y)

        #convert into meter
        #x = x / 1000
        #y = y / 1000

        print(x)
        print(y)

        # lets find centroid of cluster first

        #print("current cl =" + str(currentcluster))
        #print(centroidX)
        #print(centroidY)



        '''
        if x in range(class3XStartrange,class3XEndrange) and y in range(class3YStartrange,class3YEndrange):
            print("working at desk! class 3")
            countlie3 += 1
        else:
            print("could not recognize activity!")
        if x in range(class4XStartrange,class4XEndrange) and y in range(class4YStartrange,class4YEndrange):
            print("working at desk! class 4")
            countlie4 += 1
        else:
            print("could not recognize activity!")

        if x in range(class5XStartrange,class5XEndrange) and y in range(class5YStartrange,class5YEndrange):
            print("working at desk! class 5")
            countlie5 += 1
        else:
            print("could not recognize activity!")

        if x in range(class6XStartrange,class6XEndrange) and y in range(class6YStartrange,class6YEndrange):
            print("drinking coffee! class 6")
            countlie6 += 1
        else:
            print("could not recognize activity!")

        if x in range(class10XStartrange,class10XEndrange) and y in range(class10YStartrange,class10YEndrange):
            print("printing pages at printer! class 10")
            countlie10 += 1
        else:
            print("could not recognize activity!")

        if x in range(class1XStartrange,class1XEndrange) and y in range(class1YStartrange,class1YEndrange):
            print("checking books or some tech accessories class 1")
            countlie1 += 1
        else:
            print("could not recognize activity!")

        if x in range(class12XStartrange,class12XEndrange) and y in range(class12YStartrange,class12YEndrange):
            print("checking books or some tech accessories class 12")
            countlie12 += 1
        else:
            print("could not recognize activity!")

        if x in range(class2XStartrange,class2XEndrange) and y in range(class2YStartrange,class2YEndrange):
            print("taking food from refrigerator or heating food")
            countlie2 += 1
        else:
            print("could not recognize activity!")

        if x in range(class7XStartrange,class7XEndrange) and y in range(class7YStartrange,class7YEndrange):
            print("heating food Using Oven")
            countlie7 += 1
        else:
            print("could not recognize activity!")

        if x in range(class8XStartrange,class8XEndrange) and y in range(class8YStartrange,class8YEndrange):
            print("Throwing Trash")
            countlie8 += 1
        else:
            print("could not recognize activity!")

        if x in range(class9XStartrange,class9XEndrange) and y in range(class9YStartrange,class9YEndrange):
            print("Working at desk")
            countlie9 += 1
        else:
            print("could not recognize activity!")

        if x in range(class11XStartrange,class11XEndrange) and y in range(class11YStartrange,class11YEndrange):
            print("Checking tech accessories")
            countlie11 += 1
        else:
            print("could not recognize activity!")

        '''


    '''
    if countlie3 > 50:
        print("activity determined from current cluster!")
        with open("C:/Users/fawad/Downloads/researchwork/d.csv", 'a',newline='')as filee:
            filee = csv.writer(filee)

            #write the headers

            data = [clusterstarttime, clusterendtime ,1 , 'working at desk No 3', 'user1', 27 , 'M2']
            #write the row
            filee.writerow(data)

    if countlie2 > 50:
        print("activity determined from current cluster!")
        with open("C:/Users/fawad/Downloads/researchwork/d.csv", 'a',newline='')as filee:
            filee = csv.writer(filee)

            #write the headers

            data = [clusterstarttime,clusterendtime , 1 , 'working at desk No 2', 'user1', 27 , 'M2']
            #write the row
            filee.writerow(data)

    if countlie6 > 50:
        print("activity determined from current cluster!")
        with open("C:/Users/fawad/Downloads/researchwork/d.csv", 'a',newline='')as filee:
            filee = csv.writer(filee)

            #write the headers

            data = [clusterstarttime,clusterendtime , 1 , 'Coffee Making Activity', 'user1', 27 , 'M2']
            #write the row
            filee.writerow(data)

    if countlie4 > 50:
        print("activity determined from current cluster!")
        with open("C:/Users/fawad/Downloads/researchwork/d.csv", 'a',newline='')as filee:
            filee = csv.writer(filee)

            #write the headers

            data = [clusterstarttime,clusterendtime , 1, 'Desk Activity', 'user1', 27, 'M2']
            #write the row
            filee.writerow(data)

    if countlie5 > 15:
        print("activity determined from current cluster!")
        with open("C:/Users/fawad/Downloads/researchwork/d.csv",
                  'a', newline='') as filee:
            filee = csv.writer(filee)

            # write the headers

            data = [clusterstarttime,clusterendtime, 1, 'Desk Activity', 'user1', 27, 'M2']
            # write the row
            filee.writerow(data)

    if countlie1 > 50:
        print("activity determined from current cluster!")
        with open("C:/Users/fawad/Downloads/researchwork/d.csv",
                  'a', newline='') as filee:
            filee = csv.writer(filee)

            # write the headers

            data = [clusterstarttime,clusterendtime, 1, 'Checking books or tech accessories', 'user1', 27, 'M2']
            # write the row
            filee.writerow(data)

    if countlie12 > 50:
        print("activity determined from current cluster!")
        with open("C:/Users/fawad/Downloads/researchwork/d.csv",
                  'a', newline='') as filee:
            filee = csv.writer(filee)

            # write the headers

            data = [clusterstarttime,clusterendtime, 1, 'Checking books or tech accessories', 'user1', 27, 'M2']
            # write the row
            filee.writerow(data)

    if countlie2 > 50:
        print("activity determined from current cluster!")
        with open("C:/Users/fawad/Downloads/researchwork/d.csv",
                  'a', newline='') as filee:
            filee = csv.writer(filee)

            # write the headers

            data = [clusterstarttime,clusterendtime, 1, 'Checking Food In Refrigerator', 'user1', 27, 'M2']
            # write the row
            filee.writerow(data)

    if countlie7 > 50:
        print("activity determined from current cluster!")
        with open("C:/Users/fawad/Downloads/researchwork/d.csv",
                  'a', newline='') as filee:
            filee = csv.writer(filee)

            # write the headers

            data = [clusterstarttime,clusterendtime, 1, 'heating food Using Oven', 'user1', 27, 'M2']
            # write the row
            filee.writerow(data)

    if countlie8 > 50:
        print("activity determined from current cluster!")
        with open("C:/Users/fawad/Downloads/researchwork/d.csv",
                  'a', newline='') as filee:
            filee = csv.writer(filee)

            # write the headers

            data = [clusterstarttime,clusterendtime, 1, 'Throwing Trash', 'user1', 27, 'M2']
            # write the row
            filee.writerow(data)

    if countlie9 > 50:
        print("activity determined from current cluster!")
        with open("C:/Users/fawad/Downloads/researchwork/d.csv",
                  'a', newline='') as filee:
            filee = csv.writer(filee)

            # write the headers

            data = [clusterstarttime,clusterendtime, 1, 'Desk Activity', 'user1', 27, 'M2']
            # write the row
            filee.writerow(data)

    if countlie11 > 50:
        print("activity determined from current cluster!")
        with open("C:/Users/fawad/Downloads/researchwork/d.csv",
                  'a', newline='') as filee:
            filee = csv.writer(filee)

            # write the headers

            data = [clusterstarttime,clusterendtime, 1, 'checking tech accessories', 'user1', 27, 'M2']
            # write the row
            filee.writerow(data)

    if countlie10 > 20:
        print("activity determined from current cluster!")
        with open("C:/Users/fawad/Downloads/researchwork/d.csv",
                  'a', newline='') as filee:
            filee = csv.writer(filee)

            # write the headers

            data = [clusterstarttime,clusterendtime, 1, 'Using Printer Device', 'user1', 27, 'M2']
            # write the row
            filee.writerow(data)
    '''
    arthX = statistics.mean(centroidX)
    arthY = statistics.mean(centroidY)
    #print(currentcluster)
    #ApplyingMovingAverageFilter(centroidX,centroidY,5)

    #updatedarthX = statistics.mean(updatedCentroidX)
    #updatedarthY = statistics.mean(updatedCentroidY)


    centroidX.clear()
    centroidY.clear()

    arthX = round(arthX)
    arthY = round(arthY)

    #updatedarthX = round(updatedarthX)
    #updatedarthY =round(updatedarthY)

    print("mean or centroid of clusterX =" + str(arthX))
    print("mean or centroid of clusterY =" + str(arthY))

    if arthX in range(class3XStartrange, class3XEndrange) and arthY in range(class3YStartrange, class3YEndrange):
        print("working at desk! class 3")
        clusterstarttime = datetime.datetime.strptime(clusterstarttime, '%Y-%m-%d %H:%M:%S.%f')
        caseid = clusterstarttime.strftime("%A")
        data = [clusterstarttime, clusterendtime, caseid, 'working at desk No 3', 'user1', 27, 'M2']

        eventsdata.append(data)
        #countlie3 += 1
    #else:
    #    print("could not recognize activity!")
    elif arthX in range(class4XStartrange, class4XEndrange) and arthY in range(class4YStartrange, class4YEndrange):
        print("working at desk! class 4")
        clusterstarttime = datetime.datetime.strptime(clusterstarttime, '%Y-%m-%d %H:%M:%S.%f')
        caseid = clusterstarttime.strftime("%A")

        data = [clusterstarttime, clusterendtime, caseid, 'working at desk! class 4', 'user1', 27,
                'M2']

        eventsdata.append(data)

        #countlie4 += 1
    #else:
    #    print("could not recognize activity!")

    elif arthX in range(class5XStartrange, class5XEndrange) and arthY in range(class5YStartrange, class5YEndrange):
        print("working at desk! class 5")
        clusterstarttime = datetime.datetime.strptime(clusterstarttime, '%Y-%m-%d %H:%M:%S.%f')
        caseid = clusterstarttime.strftime("%A")
        data = [clusterstarttime, clusterendtime, caseid, 'working at desk! class 5', 'user1', 27,
                'M2']

        eventsdata.append(data)

        #countlie5 += 1
    #else:
    #    print("could not recognize activity!")

    elif arthX in range(class6XStartrange, class6XEndrange) and arthY in range(class6YStartrange, class6YEndrange):
        print("drinking coffee! class 6")
        clusterstarttime = datetime.datetime.strptime(clusterstarttime, '%Y-%m-%d %H:%M:%S.%f')
        caseid = clusterstarttime.strftime("%A")

        data = [clusterstarttime, clusterendtime, caseid, 'drinking coffee! class 6', 'user1', 27,
                'M2']

        eventsdata.append(data)

        #countlie6 += 1
    #else:
    #    print("could not recognize activity!")

    elif arthX in range(class10XStartrange, class10XEndrange) and arthY in range(class10YStartrange, class10YEndrange):
        print("printing pages at printer! class 10")
        clusterstarttime = datetime.datetime.strptime(clusterstarttime, '%Y-%m-%d %H:%M:%S.%f')
        caseid = clusterstarttime.strftime("%A")
        data = [clusterstarttime, clusterendtime, caseid, 'printing pages at printer! class 10', 'user1', 27,
                'M2']

        eventsdata.append(data)
        #countlie10 += 1
    #else:
    #    print("could not recognize activity!")

    elif arthX in range(class1XStartrange, class1XEndrange) and arthY in range(class1YStartrange, class1YEndrange):
        print("checking books or some tech accessories class 1")
        clusterstarttime = datetime.datetime.strptime(clusterstarttime, '%Y-%m-%d %H:%M:%S.%f')
        caseid = clusterstarttime.strftime("%A")
        data = [clusterstarttime, clusterendtime, caseid, 'checking books or some tech accessories class 12', 'user1', 27,
                'M2']

        eventsdata.append(data)
        #countlie1 += 1
    #else:
    #    print("could not recognize activity!")

    elif arthX in range(class12XStartrange, class12XEndrange) and arthY in range(class12YStartrange, class12YEndrange):
        print("checking books or some tech accessories class 12")
        clusterstarttime = datetime.datetime.strptime(clusterstarttime, '%Y-%m-%d %H:%M:%S.%f')
        caseid = clusterstarttime.strftime("%A")
        data = [clusterstarttime, clusterendtime, caseid, 'checking books or some tech accessories class 12', 'user1', 27, 'M2']

        eventsdata.append(data)
        #countlie12 += 1
    #else:
    #    print("could not recognize activity!")

    elif arthX in range(class2XStartrange, class2XEndrange) and arthY in range(class2YStartrange, class2YEndrange):
        print("taking food from refrigerator")
        clusterstarttime = datetime.datetime.strptime(clusterstarttime, '%Y-%m-%d %H:%M:%S.%f')
        caseid = clusterstarttime.strftime("%A")

        data = [clusterstarttime, clusterendtime, caseid, 'taking food from refrigerator', 'user1', 27, 'M2']

        eventsdata.append(data)
        #countlie2 += 1
    #else:
    #    print("could not recognize activity!")

    elif arthX in range(class7XStartrange, class7XEndrange) and arthY in range(class7YStartrange, class7YEndrange):
        print("heating food Using Oven")
        clusterstarttime = datetime.datetime.strptime(clusterstarttime, '%Y-%m-%d %H:%M:%S.%f')
        caseid = clusterstarttime.strftime("%A")
        data = [clusterstarttime, clusterendtime, caseid, 'heating food Using Oven', 'user1', 27, 'M2']

        eventsdata.append(data)
        #countlie7 += 1
    #else:
    #    print("could not recognize activity!")

    elif arthX in range(class8XStartrange, class8XEndrange) and arthY in range(class8YStartrange, class8YEndrange):
        print("Throwing Trash")
        clusterstarttime = datetime.datetime.strptime(clusterstarttime, '%Y-%m-%d %H:%M:%S.%f')
        caseid = clusterstarttime.strftime("%A")
        data = [clusterstarttime, clusterendtime, caseid, 'Throwing Trash', 'user1', 27, 'M2']

        eventsdata.append(data)
        #countlie8 += 1
    #else:
    #    print("could not recognize activity!")

    elif arthX in range(class9XStartrange, class9XEndrange) and arthY in range(class9YStartrange, class9YEndrange):
        print("Working at desk")
        clusterstarttime = datetime.datetime.strptime(clusterstarttime, '%Y-%m-%d %H:%M:%S.%f')
        caseid = clusterstarttime.strftime("%A")
        data = [clusterstarttime, clusterendtime, caseid, 'Working at desk', 'user1', 27, 'M2']

        eventsdata.append(data)
        #countlie9 += 1
    #else:
    #    print("could not recognize activity!")

    elif arthX in range(class11XStartrange, class11XEndrange) and arthY in range(class11YStartrange, class11YEndrange):
        print("Checking tech accessories")
        clusterstarttime = datetime.datetime.strptime(clusterstarttime, '%Y-%m-%d %H:%M:%S.%f')
        caseid = clusterstarttime.strftime("%A")

        data = [clusterstarttime, clusterendtime, caseid, 'Checking tech accessories', 'user1', 27, 'M2']

        eventsdata.append(data)
        #countlie11 += 1
    else:
        print("could not recognize activity!")


def writecsv():
    #global onlyonetimerun
    #global a
    header = ['start time','End time','Caseid','Activity','Agent','Age','Year']
    #global firsteventclass
    #global lasteventclass
    #global neweventsdata

    print(eventsdata)




    with open("C:/Users/fawad/Downloads/rwork/tag5/new.csv",
              'wt', newline='') as filee:





        filee = csv.writer(filee, delimiter=',')
        filee.writerow(i for i in header)
        for j in eventsdata:

            #storing row in csv
            filee.writerow(j)





def processcsvfile():
    global a
    # lets process our events list to join the events from the same class and seperate breaks as well
    # in events list we have follwing structure for data: Starting time, Ending time, caseid, activity, Resource, Age, Year

    for event in eventsdata:
        if (onlyonetimerun == True):
            a.append(event)
            firsteventclass.append(event)
        else:
            if (a[0][3] == event[3]):
                print("joining event")

                a.clear()

                a.append(event)


            else:
                print("different activity started so needs to close the checking for the previous activity!")




if __name__ == "__main__":
    readfile()
    ApplyAlgorithm()
    writecsv()
    #processcsvfile()