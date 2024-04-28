import random

import pygame

import constants
import tanks


class kontroller():
    def __init__(self,tank:tanks.tank):
        self.tank = tank

    def kontrol(self):
        keys = pygame.key.get_pressed()


        #rakip = tanks.tank.tanks[1]
        x = random.randint(0, 100)
        if 0 < x < 10:
            self.tank.move(constants.ILERI)
        if 10 < x < 15:
            self.tank.move(constants.GERI)
        if 15 < x < 30:
            self.tank.rotate(constants.SOL)
        if 30 < x < 45:
            self.tank.rotate(constants.SAG)
        if x > 90:
            self.tank.shot()


        """
        if keys[pygame.K_RIGHT]:
            self.tank.rotate(constants.SAG)

        if keys[pygame.K_LEFT]:
            self.tank.rotate(constants.SOL)

        if keys[pygame.K_UP]:
            self.tank.move(constants.ILERI)

        if keys[pygame.K_DOWN]:
            self.tank.move(constants.GERI)

        if keys[pygame.K_SPACE]:
            self.tank.shot()

        """


