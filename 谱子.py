import pygame,time,sys,json
a=[]
b=[]
c=0
pygame.init()
pygame.key.set_repeat(100, 150)
clock=pygame.time.Clock()
screen=pygame.display.set_mode((300,300),0,32)
pygame.mixer.init()
pygame.mixer.music.load(".\\assets\\start\\start_game\\game\\arknight.wav")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(0)
while True:
    time.sleep(0.1)
    c=c+0.1
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                c=round(c,2)
                a.append(c)
                print(a)
    for event1 in pygame.event.get():
        if event1.type == pygame.KEYDOWN:
            if event1.key == pygame.K_j:
                c=round(c,2)
                b.append(c)
                print(b)
    for event2 in pygame.event.get():
        if event2.type==pygame.QUIT:
            run=False
            pygame.quit()
            quit()
    pygame.display.update()
    clock.tick(60)
