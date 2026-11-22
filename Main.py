import numpy as np
import pygame
from Sphere import *
import RenderUtils
import player
from random import randint
from ScreenType import *
keyPressed =[]
time_elasped =0
speed =0
yawSpeed =0
pitchSpeed =0
rollSpeed =0
while True :
    shooting =False
    clicking =False
    for event in pygame .event .get ():
            if event .type ==pygame .QUIT :
                pygame .quit ()
            elif event .type ==pygame .MOUSEBUTTONUP :
                clicking =True
            elif player .screenType ==ScreenType .GAME and (event .type in (pygame .KEYDOWN ,pygame .KEYUP )):
                key_name =pygame .key .name (event .key )
                key_name =key_name .upper ()
                if event .type ==pygame .KEYDOWN :
                    keyPressed .append (key_name )
                    if key_name =="SPACE":
                        SOUND_SHOT .play ()
                        shooting =True
                elif event .type ==pygame .KEYUP :
                    if (key_name in keyPressed ):
                        keyPressed .remove (key_name )
                    SOUND_ROCKET .stop ()
    if (player .screenType ==ScreenType .INTRO ):
        changeTitleColor =False
        CLOCK =pygame .time .Clock ()
        if (pygame .time .get_ticks ()%2000 ==0 ):
            changeTitleColor =True
        RenderUtils .drawIntro (clicking ,changeTitleColor )
        keyPressed =[]
        yawSpeed =0
        pitchSpeed =0
        rollSpeed =0
        speed =0
    elif (player .screenType ==ScreenType .GAME ):
        player .z +=speed
        transformAll (yawSpeed ,"Y")
        transformAll (pitchSpeed ,"X")
        transformAll (rollSpeed ,"Z")
        sortSpheres ()
        for key in keyPressed :
            if key =="F"or key =="UP":
                speed +=0.0001
                SOUND_ROCKET .play (-1 )
            elif key =="G"or key =="DOWN":
                speed -=0.0001
                SOUND_ROCKET .play (-1 )
            elif key =="W":
                pitchSpeed +=0.00004
            elif key =="S":
                pitchSpeed -=0.00004
            elif key =="A":
                yawSpeed +=0.00004
            elif key =="D":
                yawSpeed -=0.00004
            elif key =="Q":
                rollSpeed +=0.00004
            elif key =="E":
                rollSpeed -=0.00004
            elif key =="[+]":
                player .fromScreenD +=0.005
            elif key =="[-]":
                if (player .fromScreenD >0.01 ):
                    player .fromScreenD -=0.005
        dt =CLOCK .tick ()
        time_elasped +=dt
        if time_elasped >2000 :
            Sphere ([randint (-MAX ,MAX ),randint (-MAX ,MAX ),randint (-MAX ,MAX )])
            time_elasped =0
        RenderUtils .drawGame (shooting ,dt )
    elif (player .screenType ==ScreenType .GAMEOVER ):
        RenderUtils .drawGameOver (clicking )
        SOUND_ROCKET .stop ()
        keyPressed =[]
    elif (player .screenType ==ScreenType .RULES ):
        RenderUtils .drawRules (clicking )
        keyPressed =[]
    pygame .display .flip ()
pygame .mixer .quit ()
pygame .quit ()