import pygame,sys,button
import time

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("背景音乐.wav")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)


bg=pygame.image.load(".\\assets\\start\\start_bg\\背景.jpg")
bg1=pygame.image.load(".\\assets\\start\\start_bg\\背景1.jpg")

bgpos=bg.get_rect()
bgpos1=bg1.get_rect()



logo=pygame.image.load(".\\assets\\logo\\logo.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("Rhythm")

screen=pygame.display.set_mode((1280,720),0,32)
screen.blit(bg,bgpos)
key=pygame.key.get_pressed()

color=(255,255,255)

clock=pygame.time.Clock()


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
moonhalo_start2=False

wuqi=False
wuqi_start=False
wuqi_start2=False

boqi=False 
button_appear=False



    

while run:
    key=pygame.key.get_pressed() 
    if key[pygame.K_SPACE] :
        game_start=True
        if game_start==True:
            
            button_appear=True 
        
            screen.blit(bg1,bgpos1)
          

    if moonhalo_start==True:
        if gequ1.draw(screen):
            button_appear=False
            moonhalo_start=True
            moonhalo=True
            moonhalo_start2=True

        if moonhalo==True:
            for i in range(29):
                a=str(i+1)              
                bg2=pygame.image.load(".\\assets\\bg\\MoonHalo\\moonhalo"+a+".jpg")
                bgpos3=bg2.get_rect()
                
                screen.blit(bg2,bgpos3)
                pygame.display.flip()
                time.sleep(0.033)
            moonhalo=False
            moonhalo_start=False
    if moonhalo_start2==True:
        if key[pygame.K_RETURN]:
            boqi=False
            wuqi=False
            moonhalo_start=False
            screen.blit(bg1,bgpos1)
            wuqi=True


    if wuqi==True:
        if gequ2.draw(screen):
            button_appear=False
            wuqi_start=True
            wuqi_start2=True
        if wuqi_start==True:
            for i in range(29):
                a=str(i+1)              
                bg2=pygame.image.load(".\\assets\\bg\\IceCream\\"+a+".jpg")
                bgpos3=(1280,720)
                image=pygame.transform.scale(bg2,bgpos3)
                screen.blit(image,(0,0))
                pygame.display.flip()
                time.sleep(0.033)
                
            wuqi=False
            wuqi_start=False
            
            
        if wuqi_start2==True:
            if key[pygame.K_RETURN]:
                boqi=False
                wuqi=False
                moonhalo_start=False

                screen.blit(bg1,bgpos1)
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









