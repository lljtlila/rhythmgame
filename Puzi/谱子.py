import pygame,time,sys
from pygame.locals import*
pygame.init()
a=[]
b=[]
c=0
clock=pygame.time.Clock()
screen=pygame.display.set_mode((1280,720),0,32)

while True:
    
    time.sleep(0.1)   
    c=c+0.1
    d=round(c,2)
    event=pygame.event.poll()       
    if event.type==QUIT:
        pygame.quit()
        sys.exit()
            

    if event.type == KEYDOWN and event.key==K_j:
        a.append(d)
    if event.type==KEYDOWN and event.key==K_f:
        b.append(d)
    if event.type ==KEYDOWN and event.key == K_RETURN:
        print("一线谱子为",a)
        print("二线谱子为",b)
      
    pygame.display.update()
    clock.tick(60)

