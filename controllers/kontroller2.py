import pygame
import constants
import tanks
import wall
import time
import random

class kontroller():
    def __init__(self,tank:tanks.tank):
        self.tank = tank
        self.a = 0




    def kontrol(self):

        """ x = random.randint(0, 100)
        if 0<x<10 :
            self.tank.move(constants.ILERI)
        if 10<x<15:
            self.tank.move(constants.GERI)
        if 15<x<30:
            self.tank.rotate(constants.SOL)
        if  30<x<45:
            self.tank.rotate(constants.SAG)
        if x>90:
            self.tank.shot()"""

        keys = pygame.key.get_pressed()
        #print(self.a)
        #time.sleep(0.1)

        if keys[pygame.K_e]:
            #print(4/0)
            pass
            #print(wall.wall.get_walls()[0].get_pos())
            #w = wall.wall.get_walls()[0]
            #w.color = (255, 255, 0)
            #self.a = tanks.bullet.get_bullets()[0]


        if keys[pygame.K_d]:
            self.tank.rotate(constants.SAG)


        if keys[pygame.K_a]:
            self.tank.rotate(constants.SOL)

        if keys[pygame.K_w]:
            self.tank.move(constants.ILERI)

        if keys[pygame.K_s]:
            self.tank.move(constants.GERI)

        if keys[pygame.K_q]:
            self.tank.shot()




