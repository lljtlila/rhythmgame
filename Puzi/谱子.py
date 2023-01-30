import pygame,time,sys
from pygame.locals import*
pygame.init()
a=[]
c=0
clock=pygame.time.Clock()
screen=pygame.display.set_mode((1280,720),0,32)

pygame.mixer.init()
pygame.mixer.music.load(".\\Puzi\\吉他与孤独与蓝色星球.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

while True:
    
    time.sleep(0.1)   
    c=c+0.1
    d=round(c,2)
    event=pygame.event.poll()       
    if event.type==QUIT:
        pygame.quit()
        sys.exit()
            

    if event.type == KEYDOWN and event.key==K_f:
        a.append(d)
    if event.type ==KEYDOWN and event.key == K_RETURN:
        print("一线谱子为",a)
      
    pygame.display.update()
    clock.tick(60)

