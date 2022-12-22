import pygame,sys,button
from moonhalogif import *
from support import *

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("背景音乐.wav")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)


bg=pygame.image.load("背景.jpg")
bg1=pygame.image.load("背景1.jpg")
bgpos=bg.get_rect()
bgpos1=bg1.get_rect()



logo=pygame.image.load("logo.png")
pygame.display.set_icon(logo)
screen=pygame.display.set_mode((1280,720),0,32)
clock=pygame.time.Clock()
pygame.display.set_caption("Rhythm")
screen.blit(bg,bgpos)
key=pygame.key.get_pressed()
color=(255,255,255)


font=pygame.font.SysFont("微软雅黑",40)
start1=font.render(" ",True,color)
start2=font.render(" ",True,color)
start3=font.render(" ",True,color)
start4=font.render(" ",True,color)

gequ1=button.Button(336,80,start1,1)   
gequ2=button.Button(459,260,start2,1) 
gequ3=button.Button(500,470,start3,1) 
gequ4=button.Button(336,600,start4,1) 
run=True  
game_start=False
moonhalo=False 
moonhalo_start=True 
wuqi=False
boqi=False 
button_appear=False

def import_assets(self):
    self.animations={"波奇":[],"刀子":[],"物凄":[],"小圆":[]}

    for animation in self.animations.keys():
        full_path="../资源"+animation
        self.animations[animation]=import_floder(full_path)
    print(self.animations)

while run:
    key=pygame.key.get_pressed() 
    if key[pygame.K_SPACE] :
        game_start=True
        if game_start==True:
            pygame.mixer.music.load("背景音乐.wav")
            
            button_appear=True 
            pygame.mixer.init()
        
            screen.blit(bg1,bgpos1)
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)
          
            #gequ1.draw(screen)
            #gequ2.draw(screen)
            #gequ3.draw(screen)
            #gequ4.draw(screen)
    if moonhalo_start==True:
        if gequ1.draw(screen):
            button_appear=False
            moonhalo_start=True
            moonhalo=True
        if moonhalo==True:              
            moonhalogif.load()
        if key[pygame.K_RETURN]:
            boqi=False
            wuqi=False
            moonhalo_start=False
            screen.blit(bg,bgpos1)
        #gequ1=button.Button(336,80,start1,0)
        #gequ1.draw(screen)
    if wuqi==True:
        if gequ2.draw(screen):
            button_appear=False
            wuqi_start=True
        if wuqi_start==True:
            wuqi4=pygame.image.load("wuqi4.jpeg")
            bgpos4=wuqi4.get_rect()
            screen.blit(wuqi4,bgpos4)

            if key[pygame.K_0]:
                boqi=False
                wuqi=False
                moonhalo_start=False

                screen.blit(bg,bgpos1)
    if boqi==True:
        if gequ3.draw(screen):
            button_appear=False
            boqi_start=True
        if boqi == True:
            boqi1=pygame.image.load("底.png")
            bgpos5=boqi1.get_rect()
            screen.blit(boqi1,bgpos5)
            if key[pygame.K_0]:
                boqi=False
                screen.fill(color)
                screen.blit(bg,bgpos1)
                boqi=False
                wuqi=False
                moonhalo_start=False
    if game_start==False:
        screen.blit(bg,bgpos1)
    
        
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            
            run=False
            pygame.quit()
            quit()
      
    pygame.display.update()
    clock.tick(60)









