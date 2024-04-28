import random
import sys
from tanks import *
import screen
import numpy as np
import _thread
import os
#import controllers
import importlib

pygame.init()
FPS = 60
size=np.array(pygame.display.get_desktop_sizes()[0])*0.8
pencere=pygame.display.set_mode(size,pygame.RESIZABLE)

screen.screen_init(pencere)
clock=pygame.time.Clock()


new_surface = pygame.surface.Surface((1200,800))


#pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)






controller_list = []

for i in os.listdir("controllers"):
    if i != "__init__.py" and i!= "__pycache__":
        try:
            module_name = "controllers." + i[:-3]
            module = importlib.import_module(module_name)

            controller_list.append(module.kontroller(tank(color=(0, 255, 0), position=[random.randint(0,500),random.randint(0,500)])))
        except:
            print("controllers klasöründe bir sorun oluştu galiba :)")




wall1 = wall.wall([0,0],constants.VERTICAL)
wall2 = wall.wall([100,100],constants.HORIZONTAL)
wall3 = wall.wall([500,0],constants.VERTICAL)




def call_back(kontroller):
    while True:
        try:
            time.sleep(1/FPS)
            kontroller.kontrol()
        except:
            print("Thread içinde hata oldu")


for i in controller_list:
    _thread.start_new_thread(call_back,(i,))


while True:
    clock.tick(FPS)
    new_surface.fill((200,200,200))
    pencere.fill((100,100,100))
    for i in pygame.event.get():
        if i.type==pygame.QUIT:sys.exit()


    tank.draw_(new_surface)


    wall.wall.draw_(new_surface)
    #my_kontroller.kontrol()
    #diger_kpntoller.kontrol()

    bullet.draw_(new_surface)

    pencere.blit(new_surface,(100,50))


    pygame.display.update()

