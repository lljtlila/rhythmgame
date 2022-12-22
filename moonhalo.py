import pygame
pygame.init()
screen=pygame.display.set_mode((1280,720),0,32)
def button(x,y,x1,y1):#起始x，起始y，终点x，终点y
     x2=(x1-x)//4
     for i in range(x2):
         screen.blit("..\\assets\\mod.jpg",(x,y))
         pygame.display.flip()
button(4,4,4,4)
