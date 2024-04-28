import pygame
from text import *
class entry():
    def __init__(self,x=0,y=0,len_x=150,len_y=50):
        self.rect=pygame.Rect(x,y,len_x,len_y)
        self.x=x
        self.y=y
        self.len_x=len_x
        self.len_y=len_y

        self.active=False
        self.string=""
        self.place_holder=""
        self.active_color=(0,255,0)
        self.inactive_color=(255,255,255)
        self.color=self.inactive_color
    def update(self,event):
        if self.active == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.string = self.string[:-1]
                elif event.key == pygame.K_RETURN:
                    pass

                else:
                    self.string += event.unicode

    def draw(self,pencere):
        if pygame.mouse.get_pressed()[0]:
            x,y=pygame.mouse.get_pos()
            if self.x<x<self.x+self.len_x and self.y<y<self.y+self.len_y :
                self.active=True
                self.color=self.active_color
            else:
                self.active=False
                self.color=self.inactive_color



        pygame.draw.rect(pencere,self.color,(self.x,self.y,self.len_x,self.len_y),1)
        if len(self.string)==0:
            pencere.blit(text.print_text(self.place_holder), (self.x + 10, self.y + 15))

        pencere.blit(text.print_text(self.string),(self.x+10,self.y+15))



