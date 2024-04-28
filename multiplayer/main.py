import pygame,sys
import os
import kullanici_olustur
if os.path.isdir("data") == False:
    os.mkdir("data")

if os.path.isfile("data/info.info") ==False:
    dosya = open("data/info.info","w")
    dosya.close()

dosya = open("data/info.info","r")
yeni_kullanici = False
if dosya.readlines() == []:
    yeni_kullanici = True
dosya.close()



pygame.init()
pencere=pygame.display.set_mode((1600,800))
FPS = 60



clock=pygame.time.Clock()
while True:
    clock.tick(FPS)
    pencere.fill((0,125,0))
    for i in pygame.event.get():
        if i.type==pygame.QUIT:sys.exit()

    if yeni_kullanici:
        kullanici_olustur.kullanici_olustur(pencere)
        yeni_kullanici = False




    pygame.display.update()
