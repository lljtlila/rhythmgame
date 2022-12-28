import pygame,sys,button
import time,math
import moonhalo

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load(".\\assets\\start\\start_bg\\背景音乐.wav")
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
start1=font.render(' ',True,color)
start2=font.render(" ",True,color)
start3=font.render(" ",True,color)                 
start4=font.render(" ",True,color)

gequ1=button.Button(336,80,start1,1)   
gequ2=button.Button(459,260,start2,1) 
gequ3=button.Button(500,470,start3,1) 
gequ4=button.Button(336,600,start4,1) 

score=0

Yinfu3=True

run=True  
game_start=False

moonhalo=False 
moonhalo_start=True 
moonhalo_start2=False
moonhalo_start3=False

wuqi=False
wuqi_start=False
wuqi_start2=False

#boqi=False 
boqi=True
boqi_start=False
boqi_start2=False
boqi_start3=False
boqi_start4=False

button_appear=False


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

            
  

set_time=0

        



    

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
            boqi=False

        if moonhalo==True:
            for i in range(15):
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
            moonhalo_start3=True
        if moonhalo_start3==True:
            boqi=False
            wuqi=False
            game_bg=pygame.image.load(".\\assets\\start\\start_game\\game\\game.png").convert_alpha()
            bgpos3=(1280,720)
            
            
            image=pygame.transform.scale(game_bg,bgpos3)
            bg_rect=image.get_rect()
            bg_width=image.get_width()
            moonhalo_start=False
            screen.blit(image,(0,0))
            tiles=math.ceil(1280/bg_width)+1

            for i in range(0,tiles):
                screen.blit(image,(i*bg_width+score,0))
                bg_rect.x=i*bg_width+score
            if abs(score)>bg_width:
                score=0

            score-=3
        if moonhalo_start3==True:
            YinFu.draw_Yinfu(screen)
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
            boqi_start2=True
        if boqi_start == True:
            for i in range(29):
                a=str(i+1)              
                bg2=pygame.image.load(".\\assets\\bg\\Bocci\\bocci"+a+"jpg")
                bgpos3=(1280,720)
                image=pygame.transform.scale(bg2,bgpos3)
                screen.blit(image,(0,0))
                
                pygame.display.flip()
                time.sleep(0.033)
            boqi_start=False
            boqi=False           
            moonhalo_start=False
    if boqi_start2==True:
            if key[pygame.K_RETURN]:
                boqi_start3=True

    if boqi_start3==True:
                boqi=False
                wuqi=False
                moonhalo_start=False
                moonhalo_start2=False
                moonhalo_start3=False
                game_bg=pygame.image.load(".\\assets\\start\\start_game\\game\\game.png").convert_alpha()
                bgpos3=(1280,720)
                boqi_start4=True
            
                image=pygame.transform.scale(game_bg,bgpos3)
                bg_rect=image.get_rect()
                bg_width=image.get_width()
                screen.blit(image,(0,0))
                tiles=math.ceil(1280/bg_width)+1

                for i in range(0,tiles):
                    screen.blit(image,(i*bg_width+score,0))
                    bg_rect.x=i*bg_width+score
                if abs(score)>bg_width:
                    score=0
                score-=3
                
    if boqi_start4==True:
        YinFu.draw_Yinfu(screen)


            


    if game_start==False:
        screen.blit(bg,bgpos1)
    
        
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            
            run=False
            pygame.quit()
            quit()
      
    pygame.display.update()
    clock.tick(60)









