import pygame
pygame .font .init ()
ARIAL =pygame .font .SysFont ("arial",10 )
FONT =pygame .font .Font ('font.ttf',23 )
FONT_BIG =pygame .font .Font ('font.ttf',40 )
FONT_BIGGEST =pygame .font .Font ('font.ttf',100 )
pygame .mixer .init ()
pygame .mixer .music .load ("audio/music.mp3")
pygame .mixer .music .play (True )
SOUND_SHOT =pygame .mixer .Sound (file ="audio/shot.ogg")
SOUND_ROCKET =pygame .mixer .Sound (file ="audio/rocket.ogg")
SOUND_POINT =pygame .mixer .Sound (file ="audio/point.ogg")
SOUND_GAMEOVER =pygame .mixer .Sound (file ="audio/gameover.ogg")
SOUND_BUTTON =pygame .mixer .Sound (file ="audio/button.ogg")
CLOCK =pygame .time .Clock ()
SCALEUP =50
BLACK =(0 ,0 ,0 )
WHITE =(255 ,255 ,255 )
BLUE =(0 ,0 ,255 )
GREEN =(0 ,255 ,0 )
RED =(255 ,0 ,0 )
COLOR_BG =BLACK
COLOR_TEXT =WHITE
INITIAL_SPHERES =30
TIME_LIMIT =120
SPHERES_LIMIT =100
MAX =30
SIZE =[720 ,720 ]
ORIGIN =[SIZE [0 ]/2 ,SIZE [1 ]/2 ]