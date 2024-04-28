import pygame,sys
import entry
import text
import button

def save(kullanici_entry:entry.entry):
    dosya = open("data/info.info","w")
    dosya.write(kullanici_entry.string+"\n")
    dosya.close()



def kullanici_olustur(pencere = pygame.display.set_mode((1600, 800)) ):

    FPS = 60

    length = 300
    width = 50
    win_size = pencere.get_size()
    kullanici_adi = entry.entry(win_size[0]//2-length//2,win_size[1]//3-width//2,length,width)
    kullanici_adi.place_holder = "isim giriniz.."

    ok_butonu = button.button("TAMAM",kullanici_adi.x,kullanici_adi.y+100)

    clock = pygame.time.Clock()
    devam = True
    while devam:
        clock.tick(FPS)
        pencere.fill((0, 0, 0))
        for i in pygame.event.get():
            if i.type == pygame.QUIT: sys.exit()
            kullanici_adi.update(i)


        kullanici_adi.draw(pencere)
        ok_butonu.draw(pencere)

        if ok_butonu.is_click():
            save(kullanici_adi)
            devam = False




        pygame.display.update()
