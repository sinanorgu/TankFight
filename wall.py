import numpy as np
import pygame

import constants


class wall():

    __walls = []

    @classmethod
    def get_walls(cls):
        new_list = []
        i:wall
        for i in cls.__walls:
            new_list.append(wall(i.get_pos(),i.get_direction(),True))
        return new_list




    @classmethod
    def draw_(cls,pencere):
        for i in cls.__walls:
            i.draw(pencere)

    def __init__(self,location=[10,10],direction = constants.VERTICAL,copy =False):
        self.__location = np.array(location)
        self.__length = 100
        self.__width = 10
        self.__direction = direction
        self.color = (0,0,0)

        if copy==False:
            self.__walls.append(self)


    def draw(self,pencere):

        if self.__direction == constants.HORIZONTAL:
            pygame.draw.rect(pencere, self.color, (self.__location[0], self.__location[1], self.__length, self.__width))

        if self.__direction == constants.VERTICAL:
            pygame.draw.rect(pencere, self.color, (self.__location[0], self.__location[1], self.__width, self.__length))

    def get_direction(self):
        return self.__direction

    def get_pos(self):
        return self.__location.copy()

    def get_width(self):
        return self.__width

    def get_length(self):
        return self.__length
