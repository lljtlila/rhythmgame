import pygame
pygame.init()
class jieshao():
    def __init__(self,x,y,image,scale):
        index=1
        wuqi=pygame.image.load(wuqi(index).jpg)
        wuqipos=wuqi(index).get_ret
        self.image=(wuqi,wuqipos)      
        self.rect.topleft=(x,y)
    def draw(self,surface):
        surface.blit(self.image(self.rect.x,self.rect.y))
