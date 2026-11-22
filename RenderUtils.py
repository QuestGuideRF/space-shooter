import pygame
import numpy as np
from math import *
from CONSTANTS import *
import player
import Sphere
from ScreenType import *
from random import randint
def initGame ():
    player .score =0
    player .x =0
    player .y =0
    player .z =0
    player .yaw =0
    player .pitch =0
    player .roll =0
    player .fromScreenD =3.5
    if (player .mode =="timed"):
        player .timePassed =0
    Sphere .spheres =[]
    for i in range (0 ,INITIAL_SPHERES ):
        Sphere .Sphere ([randint (-MAX ,MAX ),randint (-MAX ,MAX ),randint (-MAX ,MAX )])
class Button ():
    def __init__ (self ,color ,x ,y ,width ,height ,text =''):
        self .color =color
        self .buColor =color
        self .x =x
        self .y =y
        self .width =width
        self .height =height
        self .text =text
    def draw (self ,screen ,clicking ):
        pygame .draw .rect (screen ,self .color ,(self .x ,self .y ,self .width ,self .height ),0 )
        if self .text !='':
            text =FONT .render (self .text ,1 ,BLACK )
            screen .blit (text ,(self .x +(self .width /2 -text .get_width ()/2 ),self .y +(self .height /2 -text .get_height ()/2 )))
        if (self .isMouseOver ()and clicking ):
            SOUND_BUTTON .play ()
            if (player .screenType ==ScreenType .INTRO ):
                if (self .text =="Режим времени"):
                    player .mode ="timed"
                    initGame ()
                    player .screenType =ScreenType .GAME
                elif (self .text =="Хардкор режим"):
                    player .mode ="hardcore"
                    initGame ()
                    player .screenType =ScreenType .GAME
                elif (self .text =="Правила"):
                    player .screenType =ScreenType .RULES
                elif (self .text =="Выход"):
                    pygame .quit ()
                    exit ()
            elif (player .screenType ==ScreenType .GAMEOVER or player .screenType ==ScreenType .RULES ):
                if (self .text =="Назад"):
                    player .screenType =ScreenType .INTRO
    def isMouseOver (self ):
        pos =pygame .mouse .get_pos ()
        if pos [0 ]>self .x and pos [0 ]<self .x +self .width :
            if pos [1 ]>self .y and pos [1 ]<self .y +self .height :
                self .color =(100 ,100 ,100 )
                return True
        self .color =self .buColor
        return False
def randomColor ():
    return (randint (0 ,255 ),randint (0 ,255 ),randint (0 ,255 ))
pygame .init ()
screen =pygame .display .set_mode (SIZE )
crosshair =pygame .image .load ("images/crosshair.png")
tcrosshair =pygame .image .load ("images/crosshair-target.png")
gameover =pygame .image .load ("images/gameover.jpg")
rulesBG =pygame .image .load ("images/rulesBG.png")
startY =200
Button_Timed_Mode =Button (randomColor (),SIZE [0 ]/2 -150 ,startY ,300 ,100 ,text ="Режим времени")
Button_Hardcore_Mode =Button (randomColor (),SIZE [0 ]/2 -150 ,startY +130 ,300 ,100 ,text ="Хардкор режим")
Button_Rules =Button (WHITE ,SIZE [0 ]/2 -150 ,startY +260 ,300 ,100 ,text ="Правила")
Button_Quit =Button (RED ,SIZE [0 ]/2 -150 ,startY +390 ,300 ,100 ,text ="Выход")
Button_Back =Button (randomColor (),SIZE [0 ]/2 -150 ,startY +390 ,300 ,100 ,text ="Назад")
def drawIntro (clicking ,changeTitleColor ):
    global titleColor
    screen .fill (COLOR_BG )
    if (changeTitleColor ):
        titleColor =randomColor ()
    try :
        screen .blit (FONT_BIGGEST .render ('3D',False ,titleColor ),(260 ,20 ))
        screen .blit (FONT_BIG .render ('КОСМИЧЕСКИЙ СТРЕЛОК',False ,titleColor ),(80 ,120 ))
    except NameError :
        titleColor =randomColor ()
    Button_Timed_Mode .draw (screen ,clicking )
    Button_Hardcore_Mode .draw (screen ,clicking )
    Button_Rules .draw (screen ,clicking )
    Button_Quit .draw (screen ,clicking )
def drawGameOver (clicking ):
    screen .fill (COLOR_BG )
    screen .blit (gameover ,(SIZE [0 ]/2 -315 ,SIZE [0 ]/2 -340 ))
    screen .blit (FONT_BIG .render ('Ваш счёт: '+str (player .score ),False ,COLOR_TEXT ),(150 ,50 ))
    Button_Back .draw (screen ,clicking )
def drawRules (clicking ):
    screen .fill (COLOR_BG )
    scaled_rulesBG =pygame .transform .scale (rulesBG ,SIZE )
    screen .blit (scaled_rulesBG ,(0 ,0 ))
    Button_Back .draw (screen ,clicking )
def drawGame (shooting ,dt ):
    screen .fill (COLOR_BG )
    Sphere .drawAll ()
    drawCrossHair (shooting )
    screen .blit (FONT .render ('Счёт: '+str (player .score )+" (Рекорд: "+str (player .highScore )+")",False ,COLOR_TEXT ),(10 ,0 ))
    if (player .mode =="timed"):
        player .timePassed +=dt
        screen .blit (FONT .render ('Время: '+str (TIME_LIMIT -player .timePassed //1000 )+"с",False ,COLOR_TEXT ),(10 ,50 ))
        if (TIME_LIMIT -player .timePassed //1000 <0 ):
            player .screenType =ScreenType .GAMEOVER
            SOUND_GAMEOVER .play ()
    elif (player .mode =="hardcore"):
        screen .blit (FONT .render ('Сферы: '+str (len (Sphere .getSpheres ()))+" (Макс: 35)",False ,COLOR_TEXT ),(10 ,50 ))
        if (len (Sphere .getSpheres ())>SPHERES_LIMIT ):
            player .screenType =ScreenType .GAMEOVER
            SOUND_GAMEOVER .play ()
def drawPoint (coords ,s ,color ):
    if (inScreen (coords ,s )):
        pygame .draw .circle (screen ,color ,[int (coords [0 ]),int (coords [1 ])],int (s ))
def drawCrossHair (shooting ):
    center_x =SIZE [0 ]/2
    center_y =SIZE [0 ]/2
    image =crosshair
    insideData =Sphere .isInAnySphere (center_x ,center_y )
    color =GREEN
    if (insideData [0 ]):
        image =tcrosshair
        color =RED
        if (shooting ):
            insideData [1 ].delete ()
            player .score +=1
            SOUND_POINT .play ()
            if (player .highScore <player .score ):
                player .highScore =player .score
                player .saveHighScore ()
    pygame .draw .line (screen ,color ,[center_x -30 ,center_y -3 ],[center_x +30 ,center_y -3 ],3 )
    pygame .draw .line (screen ,color ,[center_x -3 ,center_y -30 ],[center_x -3 ,center_y +30 ],3 )
    screen .blit (image ,(SIZE [0 ]/2 -160 ,SIZE [0 ]/2 -120 ))
def inScreen (point ,rad ):
    if len (point )!=2 :
        return False
    elif point [0 ]<=SIZE [0 ]+rad and point [1 ]<=SIZE [1 ]+rad and point [0 ]>=0 -rad and point [1 ]>=0 -rad :
        return True
    else :
        return False