import pygame,sys,time
pygame.init()
screen=pygame.display.set_mode((1280,720),0,32)
class moonhalogif():
    def load():
        for i in range(30):
            a = str(i+1)
            image = pygame.image.load(".\\assets\\knifes\\moonhalo"+a+".jpg")
            screen.blit(image,(0,0))
            pygame.display.flip()
            time.sleep(0.033)
        moonhalo = False
