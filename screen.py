import pygame,sys
from tanks import *
win_size=0
margin_horizontal = 0
margin_vertical = 0

def screen_init(pencere):
    pass
    global win_size,margin_vertical,margin_horizontal

"""
def draw(pencere,object:tank) :
    win_size = pygame.display.get_window_size()
    margin_horizontal = win_size[0] // 30
    margin_vertical = win_size[1] // 30

    pygame.draw.rect(pencere,(0,255,0), (margin_horizontal,margin_vertical,win_size[0]-2*margin_horizontal,win_size[1]-2*margin_vertical),1)

    if type(object)==tank:
        merkez=object.position
        baslangic=[merkez[0]-object.size/2+margin_horizontal,merkez[1]-object.size/2+margin_vertical]

        pygame.draw.rect(pencere,object.color,(object.position[0],object.position[1],object.size,object.size))

"""



