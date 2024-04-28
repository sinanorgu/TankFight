import pygame

class text():
    size=30
    yazi_tipi='Veranda'
    @classmethod
    def print_text(cls,yazi,yazi_rengi=(255,255,255),arka_plan_rengi=None,size=None):
        if size==None:
            size=cls.size
        font = pygame.font.SysFont(cls.yazi_tipi, size)
        return font.render(yazi, True,yazi_rengi , arka_plan_rengi)

