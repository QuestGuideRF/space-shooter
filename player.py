from ScreenType import *
x ,y ,z =0 ,0 ,0
yaw ,pitch ,roll =0 ,0 ,0
fromScreenD =3.5
score =0
highScoreFile =open ("highScore.txt","r")
highScore =int (highScoreFile .read ())
highScoreFile .close ()
screenType =ScreenType .INTRO
mode ="timed"
timePassed =0
def getPos ():
    return [x ,y ,z ]
def setPos (pos ):
    global x ,y ,z
    x ,y ,z =pos
def getCam ():
    return [yaw ,pitch ,roll ]
def setCam (cam ):
    global yaw ,pitch ,roll
    yaw ,pitch ,roll =cam
def getHighScore ():
    return highScore
def saveHighScore ():
    highScoreFile =open ("highScore.txt","w")
    highScoreFile .write (str (highScore ))
    highScoreFile .close ()