import pygame,time,sys,json
a=[]
b=[]
c=0
e=0
pygame.init()
pygame.key.set_repeat(100, 150)
clock=pygame.time.Clock()
screen=pygame.display.set_mode((100,100),0,32)
pygame.mixer.init()
pygame.mixer.music.load(".\\assets\\start\\start_game\\game\\arknight.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(0)
while True:
    time.sleep(0.1)
    c+0.1
    c = round(c)
    key=pygame.key.get_pressed()
    if key[pygame.K_f]:
        a.append(c)
        print(c)
    if key[pygame.K_j]:
        b.append(c)
        print(b)
    for event in pygame.event.get():#傻逼罗智麒，我选择摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂摆烂
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
            quit()
    pygame.display.update()
    clock.tick(60)
