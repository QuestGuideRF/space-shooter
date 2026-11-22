from numpy import array
import player
import numpy as np
from math import *
from CONSTANTS import *
import RenderUtils
RADIUS =5
spheres =[]
class Sphere ():
    def __init__ (self ,coords =[0 ,0 ,0 ]):
        self .x =coords [0 ]
        self .y =coords [1 ]
        self .z =coords [2 ]
        self .color =RenderUtils .randomColor ()
        global spheres
        spheres .append (self )
    def getCoords (self ):
        return [self .x ,self .y ,self .z ]
    def setCoords (self ,coords ):
        self .x =coords [0 ]
        self .y =coords [1 ]
        self .z =coords [2 ]
    def getDistance (self ):
        playerPos =player .getPos ()
        return ((self .x -playerPos [0 ])**2 +(self .y -playerPos [1 ])**2 +(self .z -playerPos [2 ])**2 )**0.5
    def getRealRadius (self ):
        return RADIUS /max (0.0000000000001 ,self .getDistance ())*player .fromScreenD *SCALEUP
    def get2D (self ):
        tC =np .copy (self .getCoords ())
        x =tC [0 ]
        y =tC [1 ]
        z =tC [2 ]
        if ((z -player .z )*100 >player .fromScreenD ):
            if (player .z -z ==0 ):
                z +=0.00000001
            fx =(player .x -x )*(player .fromScreenD /(player .z -z ))*SCALEUP
            fy =(player .y +y )*(player .fromScreenD /(player .z -z ))*SCALEUP
            return np .array ([ORIGIN [0 ]+fx ,ORIGIN [1 ]-fy ])
        else :
            return []
    def transformPoints (self ,degree ,fixedAxis ):
        tC =np .array (np .copy (self .getCoords ()),dtype =float )
        transformation =[]
        if fixedAxis .upper ()=="X":
            transformation =[[1 ,0 ,0 ],[0 ,cos (degree ),sin (degree )],[0 ,-sin (degree ),cos (degree )]]
        elif fixedAxis .upper ()=="Y":
            transformation =[[cos (degree ),0 ,sin (degree )],[0 ,1 ,0 ],[-sin (degree ),0 ,cos (degree )]]
        elif fixedAxis .upper ()=="Z":
            transformation =[[cos (degree ),sin (degree ),0 ],[-sin (degree ),cos (degree ),0 ],[0 ,0 ,1 ]]
        tC [0 ]-=player .x
        tC [1 ]-=player .y
        tC [2 ]-=player .z
        tC =np .dot (transformation ,tC )
        tC [0 ]+=player .x
        tC [1 ]+=player .y
        tC [2 ]+=player .z
        self .setCoords (tC )
    def drawSphere (self ):
        RenderUtils .drawPoint (self .get2D (),self .getRealRadius (),self .color )
    def isInSphere (self ,x ,y ):
        if (len (self .get2D ())!=2 ):
            return False
        center_x =self .get2D ()[0 ]
        center_y =self .get2D ()[1 ]
        rad =self .getRealRadius ()
        if ((x -center_x )**2 +(y -center_y )**2 <rad **2 ):
            return True
        else :
            return False
    def delete (self ):
        spheres .remove (self )
def getSpheres ():
    return spheres
def transformAll (degree ,fixedAxis ):
    for i in getSpheres ():
        i .transformPoints (degree ,fixedAxis )
def drawAll ():
    for i in getSpheres ():
        i .drawSphere ()
def sortSpheres ():
    numSpheres =len (spheres )
    for i in range (numSpheres ):
        for j in range (0 ,numSpheres -i -1 ):
            if spheres [i -1 ].getDistance ()<spheres [i ].getDistance ():
                spheres [i -1 ],spheres [i ]=spheres [i ],spheres [i -1 ]
def isInAnySphere (x ,y ):
    for i in getSpheres ():
        if (i .isInSphere (x ,y )):
            return [True ,i ]
    return [False ]