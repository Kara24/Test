#!/usr/bin/env python
import rospy
import numpy as nmp
from array import *

from std_msgs.msg import String
from sensor_msgs.msg import LaserScan

class koordinaten:
    x=0
    y=0

    def __init__(self, inx, iny):
        self.x=inx
        self.y=iny


if __name__ == '__main__':
    p1=koordinaten(100,500)
    p2=koordinaten(5,6)
    p3=koordinaten(7,8)
    p4=koordinaten(9,1) 
    
    myList=[p1,p2,p3,p4]
    p5=koordinaten(11,12)
    myList.append(p5)



    for iKoordinate in myList:
        print(iKoordinate.x)
        print(iKoordinate.y)

    print("---------------")

    