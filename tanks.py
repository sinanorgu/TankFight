import numpy as np
import pygame
import math

import constants
import time

import wall


def in_triangle(triangle, p):

    def icinde_mi(a, b, c, p):

        def alan(a, b, c):

            return abs((a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1])) / 2.0)

        ABC = alan(a, b, c)
        ABP = alan(a, b, p)
        ACP = alan(a, c, p)
        BCP = alan(b, c, p)

        return ABC > (ABP + ACP + BCP)

    return icinde_mi(triangle[0],triangle[1],triangle[2], p)



class tank():

    tanks = []
    __id_count = 0

    @classmethod
    def draw_(cls,pencere):
        for i in cls.tanks:
            i.draw(pencere)
    def __del__(self):
        print("silindim sanırım")

    def __init__(self,color = (255,0,0),position = np.array([200,200])):
        self.__is_alive= True
        self.__color_changed = False
        self.__color=color
        self.__position= position
        self.__rotation_angle=25
        self.__size=20
        self.__health=100
        self.__bullet=10
        self.__boy = 44
        self.__en = 33
        self.__k_acisi = math.degrees(math.atan(self.__en / self.__boy))
        self.__kosegen = ((self.__en**2+self.__boy**2)**0.5 ) / 2
        self.__speed = 3
        self.__shot_time = 0
        self.__shot_delay = 0.2
        self.tanks.append(self)
        self.__id = tank.__id_count
        tank.__id_count+=1
        print(tank.__id_count)
        self.__points = np.array([0,0,0,0])

    def get_id(self):
        return self.__id


    def rotate(self,yon = constants.SAG):
        if self.__is_alive:
            if yon == constants.SAG:
                rotation_angle = self.__rotation_angle + 5
            elif yon == constants.SOL:
                rotation_angle = self.__rotation_angle - 5
            else:
                return 0
            p1 = self.__position + self.__kosegen * np.array(
                [math.cos(math.radians(rotation_angle + self.__k_acisi)),
                 math.sin(math.radians(rotation_angle + self.__k_acisi))])
            p2 = self.__position + self.__kosegen * np.array(
                [math.cos(math.radians(180 + rotation_angle - self.__k_acisi)),
                 math.sin(math.radians(180 + rotation_angle - self.__k_acisi))])
            p3 = self.__position + self.__kosegen * np.array(
                [math.cos(math.radians(180 + rotation_angle + self.__k_acisi)),
                 math.sin(math.radians(180 + rotation_angle + self.__k_acisi))])
            p4 = self.__position + self.__kosegen * np.array(
                [math.cos(math.radians(rotation_angle - self.__k_acisi)),
                 math.sin(math.radians(rotation_angle - self.__k_acisi))])

            inside_wall = False
            for w in wall.wall.get_walls():
                for i in [p1, p2, p3, p4]:
                    if w.get_direction() == constants.VERTICAL:
                        if w.get_pos()[0] < i[0] < w.get_pos()[0] + w.get_width():
                            if w.get_pos()[1] < i[1] < w.get_pos()[1] + w.get_length():
                                inside_wall = True
                                break
                    if w.get_direction() == constants.HORIZONTAL:
                        if w.get_pos()[0] < i[0] < w.get_pos()[0] + w.get_length():
                            if w.get_pos()[1] < i[1] < w.get_pos()[1] + w.get_width():
                                inside_wall = True
                                break




                if inside_wall:
                    break

                wall_points = []
                wall_points.append(w.get_pos())

                if w.get_direction() == constants.VERTICAL:
                    wall_points.append([w.get_pos()[0] + w.get_width(), w.get_pos()[1]])
                    wall_points.append([w.get_pos()[0] + w.get_width(), w.get_pos()[1] + w.get_length()])
                    wall_points.append([w.get_pos()[0], w.get_pos()[1] + w.get_length()])

                elif w.get_direction() == constants.HORIZONTAL:
                    wall_points.append([w.get_pos()[0] + w.get_length(), w.get_pos()[1] + w.get_width()])
                    wall_points.append([w.get_pos()[0], w.get_pos()[1] + w.get_width()])
                    wall_points.append([w.get_pos()[0] + w.get_length(), w.get_pos()[1]])

                for i in wall_points:
                    if in_triangle([p1, p2, p3], i) or in_triangle([p1, p3, p4], i):
                        inside_wall = True
                        break

            if inside_wall == False:
                self.__rotation_angle = rotation_angle

    def draw(self,pencere:pygame.surface.Surface):
        if self.__is_alive:
            p1 = self.__position + self.__kosegen * np.array([math.cos(math.radians(self.__rotation_angle+self.__k_acisi)), math.sin(math.radians(self.__rotation_angle+self.__k_acisi))])
            p2 = self.__position + self.__kosegen * np.array([math.cos(math.radians(180+self.__rotation_angle-self.__k_acisi)), math.sin(math.radians(180+self.__rotation_angle-self.__k_acisi))])
            p3= self.__position + self.__kosegen * np.array([math.cos(math.radians(180+self.__rotation_angle+self.__k_acisi)), math.sin(math.radians(180+self.__rotation_angle+self.__k_acisi))])
            p4 = self.__position + self.__kosegen * np.array([math.cos(math.radians(self.__rotation_angle-self.__k_acisi)), math.sin(math.radians(self.__rotation_angle-self.__k_acisi))])
            #pygame.draw.rect(self.__pencere,(255,255,0),(self.__position[0],self.__position[1],self.__boy,self.__en))

            self.__points=np.array([p1,p2,p3,p4])
            p5 = self.__position + self.__en*np.array([math.cos(math.radians(self.__rotation_angle)),math.sin(math.radians(self.__rotation_angle))])
            pygame.draw.polygon(pencere,self.__color,[p1,p2,p3,p4])
            pygame.draw.circle(pencere,(0,0,0),self.__position,self.__kosegen//4)

            pygame.draw.aaline(pencere , (0,0,0),self.__position,p5,0)



    def move(self,yon = constants.ILERI):
        if self.__is_alive:
            mesafe = self.__speed * np.array([math.cos(math.radians(self.__rotation_angle)), math.sin(math.radians(self.__rotation_angle))])

            if yon == constants.ILERI:
                position = self.__position + mesafe
            elif yon == constants.GERI:
                position = self.__position - mesafe
            else:
                return 0

            p1 = position + self.__kosegen * np.array(
                [math.cos(math.radians(self.__rotation_angle + self.__k_acisi)),
                 math.sin(math.radians(self.__rotation_angle + self.__k_acisi))])
            p2 = position + self.__kosegen * np.array(
                [math.cos(math.radians(180 + self.__rotation_angle - self.__k_acisi)),
                 math.sin(math.radians(180 + self.__rotation_angle - self.__k_acisi))])
            p3 = position + self.__kosegen * np.array(
                [math.cos(math.radians(180 + self.__rotation_angle + self.__k_acisi)),
                 math.sin(math.radians(180 + self.__rotation_angle + self.__k_acisi))])
            p4 = position + self.__kosegen * np.array(
                [math.cos(math.radians(self.__rotation_angle - self.__k_acisi)),
                 math.sin(math.radians(self.__rotation_angle - self.__k_acisi))])

            inside_wall = False
            for w in wall.wall.get_walls():
                for i in [p1, p2, p3, p4]:

                    #for ile tankın köşe noktalarını geziyoruz ve eğer dikdörtgenin içine girerse in_walll = True yapıyoruz.
                    if w.get_direction() == constants.VERTICAL:
                        if w.get_pos()[0] < i[0] < w.get_pos()[0] + w.get_width():
                            if w.get_pos()[1] < i[1] < w.get_pos()[1] + w.get_length():
                                inside_wall = True
                                break

                    if w.get_direction() == constants.HORIZONTAL:
                        if w.get_pos()[0] < i[0] < w.get_pos()[0] + w.get_length():
                            if w.get_pos()[1] < i[1] < w.get_pos()[1] + w.get_width():
                                inside_wall = True
                                break

                wall_points = []
                wall_points.append(w.get_pos())

                if w.get_direction() == constants.VERTICAL:
                    wall_points.append([w.get_pos()[0] + w.get_width(), w.get_pos()[1]])
                    wall_points.append([w.get_pos()[0] + w.get_width(), w.get_pos()[1]+w.get_length()])
                    wall_points.append([w.get_pos()[0] , w.get_pos()[1]+w.get_length()])

                elif w.get_direction() == constants.HORIZONTAL:
                    wall_points.append([w.get_pos()[0] + w.get_length(), w.get_pos()[1] + w.get_width()])
                    wall_points.append([w.get_pos()[0] , w.get_pos()[1] + w.get_width()])
                    wall_points.append([w.get_pos()[0] + w.get_length(), w.get_pos()[1] ])


                for i in wall_points:
                    if in_triangle([p1,p2,p3],i) or in_triangle([p1,p3,p4],i):
                        inside_wall = True
                        break



                if inside_wall:
                    break

            if inside_wall == False:
                self.__position = position

    def get_rotation(self):
        if self.__is_alive:
            return self.__rotation_angle

    def get_pos(self):
        if self.__is_alive:
            return self.__position.copy()

    def shot(self):
        if self.__is_alive:
            if time.time()-self.__shot_time>self.__shot_delay:
                blt_list = bullet.get_bullets()

                blt_count = 0
                for i in blt_list:
                    if i.get_sahip() == self:
                        blt_count += 1

                #print("count:" ,blt_count)
                if blt_count < 5:
                    bullet(self)
                    self.__shot_time = time.time()




    def dead(self):
        self.__is_alive = False

    def get_points(self):
        return self.__points.copy()

    def change_color(self,color):
        if self.__color_changed == False:
            self.__color = color





class bullet():


    __bullets = []
    __life_time = 10

    @classmethod
    def get_bullets(cls):
        new_list = []
        for i in cls.__bullets:
            new_list.append(bullet(i,copy = True))
        return new_list



    @classmethod
    def draw_(cls,pencere):
        i:bullet
        for i in cls.__bullets:
            durum = i.draw(pencere)
            if time.time() - i.get_start_time()> cls.__life_time or durum:
                cls.__bullets.remove(i)



    def __init__(self,sahip,copy = False):
        self.__sahip = sahip

        self.__speed = 6
        self.__rotation_angle = sahip.get_rotation()
        self.__position = sahip.get_pos()
        self.__tank_id = sahip.get_id()

        self.__radius = 3

        if copy == False:
            sahip:tank
            self.__start_time = time.time()
            self.__bullets.append(self)
        else:
            sahip:bullet
            self.__start_time = sahip.get_start_time()

    def get_sahip(self):
        return self.__sahip

    def get_id(self):
        return self.__tank_id

    def get_start_time(self):
        return self.__start_time

    def get_pos(self):
        return self.__position
    def get_rotation(self):
        return self.__rotation_angle


    def draw(self,pencere:pygame.surface.Surface):
        self.__position = self.__position + self.__speed * np.array([math.cos(math.radians(self.__rotation_angle)), math.sin(math.radians(self.__rotation_angle))])
        pygame.draw.circle(pencere,(0,0,0), self.__position ,self.__radius)
        t:tank

        for t in tank.tanks:
            #print(t.get_id())
            if t.get_id() != self.__tank_id:
                #print("yesss")
                if in_triangle(t.get_points()[:3],self.__position) or in_triangle([t.get_points()[0],t.get_points()[2],t.get_points()[3]],self.__position):

                    tank.tanks.remove(t)
                    t.dead()
                    return True

        w:wall.wall
        for w in wall.wall.get_walls():
            direction = w.get_direction()
            pos = w.get_pos()
            width = w.get_width()
            length = w.get_length()

            if direction == constants.VERTICAL:
                if math.cos(math.radians(self.__rotation_angle))>0:
                    if self.__position[0]+self.__radius >pos[0] and self.__position[0]+self.__radius<pos[0]+width:
                        if pos[1]<self.__position[1]<pos[1]+length:
                            self.__rotation_angle = 180 - self.__rotation_angle

                if math.cos(math.radians(self.__rotation_angle)) < 0:
                    if self.__position[0] - self.__radius > pos[0] and self.__position[0] - self.__radius < pos[0] + width:
                        if pos[1] < self.__position[1] < pos[1] + length:
                            self.__rotation_angle = 180 - self.__rotation_angle

            if direction == constants.HORIZONTAL:
                if math.sin(math.radians(self.__rotation_angle)) > 0:
                    if self.__position[1] + self.__radius > pos[1] and self.__position[1] + self.__radius < pos[1] + width:
                        if pos[0] < self.__position[0] < pos[0] + length:
                            self.__rotation_angle *= -1

                if math.sin(math.radians(self.__rotation_angle)) < 0:
                    if self.__position[1] - self.__radius > pos[1] and self.__position[1] - self.__radius < pos[1] + width:
                        if pos[0] < self.__position[0] < pos[0] + length:
                            self.__rotation_angle *= -1

    def __del__(self):
        #print("siilindim")
        pass