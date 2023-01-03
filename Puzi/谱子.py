import pygame,time,sys,json
from pygame.locals import*
pygame.init()
a=[]
b=[]
c=0
clock=pygame.time.Clock()
screen=pygame.display.set_mode((300,200),0,32)
pygame.mixer.init()
pygame.mixer.music.load(".\\assets\\start\\start_game\\game\\arknight.wav")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(0)
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
        print(a)
    if event.type==KEYDOWN and event.key==K_f:
        b.append(d)
        print(b)
    if event.type ==KEYDOWN and event.key == K_RETURN:
        print("一线谱子为",a)
        print("二线谱子为",b)
        with open(".\\Puzi\\arknighta.json","w") as a2:
            json.dump(a,a2)
        with open(".\\Puzi\\arknightb.json","w") as b2:
            json.dump(b,b2)
    pygame.display.update()
    clock.tick(60)

