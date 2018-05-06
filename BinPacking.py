from Main import toporeader
from random import randint
import random
import time
startTime = time.time()
print " The begin of Filling the Buffer"


class Bin():
    def __init__(self,id,ram):
        self.id = id
        self.Maxcapacity = ram #buf proc
        self.Acapacity = self.Maxcapacity



nodes = toporeader()
bins ={}
for k in nodes.keys():
    bins[nodes[k].nodeID] = Bin(nodes[k].CHF,int(nodes[k].ram))



#raw_input("Wait")
low = 0.1
high =4.0
size = 300
ran_floats = [float("{0:.1f}".format(random.uniform(low,high))) for _ in xrange(size)]
print ran_floats
#T = [0.3,0.2,2.3,0.2,0.1,0.1,0.1,0.9,1.0,1.1,1.5,0.3,0.2,2.3,0.2,0.1,0.1,0.1,0.9,1.0,1.1,1.5,0.1,0.9,1.0,1.1,1.5] # defined in terms of Composition Score // Chanege it later
T =ran_floats
#T = [0.3,0.2,2.3,0.2,0.1,0.1,0.1,0.9,1.0,1.1,1.5,0.3,0.2,2.3,0.2,0.1,0.1,0.1,0.9,1.0,1.1,1.5,0.1,0.9,1.0,1.1,1.5]
x={}
print "Total Available Bins ",len(bins)
print "Total Packets", len(T)
TotalDroped = 0
TotalAccepted = 0
for k in bins.keys():
    x[k] =[]
for h,i in enumerate(T):
     k =0
     fflag =False
     while (k < len(bins) and fflag == False):
        if str(i) <= str(bins[k].id):
            rr = randint(1,5)
            if (int(bins[k].Acapacity) - rr > 0) and (int(bins[k].Acapacity) >= rr):
                bins[k].Acapacity = bins[k].Acapacity - rr
                print ("Inside 2nd if","scheduling the packet",i, "to the bin",k," capacity is after allocating ",bins[k].Acapacity)
                #print ("Inside 2nd if","embedding the Subtask",i, "to the bin",k," capacity is after allocating ",bins[k].Acapacity)
                x[k].append(i)
                TotalAccepted = TotalAccepted+1

                    #raw_input("wait")
                fflag = True
            elif k == (len(bins)-1) and fflag !=True:
                print "Packet",i," could not be schedulded, index at", h
                TotalDroped = TotalDroped+1
        k =k+1
     count =1
     #count = count + 1





count =0
utilization=0
TotalCapacity =0
for k in bins.keys():
    print k, bins[k].Maxcapacity, bins[k].Acapacity
    if int(bins[k].Acapacity) < 30:
        count = count +1
        utilization = utilization+ bins[k].Acapacity
        TotalCapacity = TotalCapacity + bins[k].Maxcapacity



for k in x.keys():
    print "Packet ",x[k]," to Buffered in Queue",k


print "DropRatio=", TotalDroped
print "Incoming Packets  =", TotalAccepted
#print "Dropped ",(len(T)-TotalAccepted)#/float(len(T))
#print "CHF = ",sum(T)/float(len(T))
print "Congestion Handling Percentage = ",(TotalCapacity-utilization)*100/float(TotalCapacity)
print "TotalTimeTaken = ", time.time()-startTime

print "count/Total Bins = ", count/float(len(bins))
#print "Total Tasks schedulded = ", TotalAccepted
