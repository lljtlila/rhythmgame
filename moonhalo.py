import pygame
pygame.init()
screen=pygame.display.set_mode((1280,720),0,32)

clock=pygame.time.Clock()
def button(x,y,x1,y1):#起始x，起始y，终点x，终点y
     x2=(x1-x)//4
     for i in range(x2):
        bg=pygame.image.load(".\\assets\\mod.jpg")
        bgpos=bg.get_rect()
        screen.blit(bg,bgpos,(x,y))
        pygame.display.flip()
while True:
    button(4,4,4,4)
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:            
            run=False
            pygame.quit()
            quit()
      
    pygame.display.update()
    clock.tick(60)
