import pygame,time,sys
from pygame.locals import*
pygame.init()
a=[]
b=[]
c=0
clock=pygame.time.Clock()
screen=pygame.display.set_mode((1280,720),0,32)

class YinFu():
    def __init__(self) :
        self.x=720
        self.y=320
        self.speed=2

    def draw_Yinfu(self):
        
        image=pygame.image.load(".\\assets\\start\\start_game\\YinFu_short.png").convert_alpha()
        bgpos=(50,50)
        Yinfu=pygame.transform.scale(image,bgpos)
        bgsize=50
        yinfu_x=1280
        yinfu_x=yinfu_x-100
        if yinfu_x==200:       
            yinfu_x=-1280
        Yinfu_rect=pygame.Rect(yinfu_x,200,bgsize,bgsize)  
  
        screen.blit(Yinfu,Yinfu_rect)
        pygame.display.flip()

while True:

    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            
            run=False
            pygame.quit()
            quit()
      
        pygame.display.update()
        clock.tick(60)
