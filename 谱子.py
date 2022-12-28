import pygame,time,sys
a=[]
b=0
clock=pygame.time.Clock()
screen=pygame.display.set_mode((1280,720),0,32)
while True:
    time.sleep(0.1)   
    b=b+0.1
    key=pygame.key.get_pressed() 
    if key[pygame.K_f]:
        a.append(b)
    print(a)
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            
            run=False
            pygame.quit()
            quit()
      
    pygame.display.update()
    clock.tick(60)
