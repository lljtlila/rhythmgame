import pygame,sys,button


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
button_appear=False
moonhalo=False  
while run:
    if key[pygame.K_SPACE] :
        if game_start==False:
            screen.blit(bg1,bgpos1)
            game_start=True
            button_appear=True 
            pygame.mixer.init()
            pygame.mixer.music.load("背景音乐.wav")
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play(-1)
            if button_appear==True :           
                gequ1.draw(screen)
                gequ2.draw(screen)
                gequ3.draw(screen)
                gequ4.draw(screen)
    if gequ1.draw(screen):
        button_appear=False
        moonhalo=True
    if button_appear==False:               
        #pygame.mixer.music.load("伴奏1.mp3")
        #pygame.mixer.music.set_volume(0.1)
        #pygame.mixer.music.play(-1)
        bg2=pygame.image.load("moonhalo.jpg")
        bgpos3=bg2.get_rect()
        screen.blit(bg2,bgpos3)
        #gequ1=button.Button(336,80,start1,0)
        #gequ1.draw(screen)
    #if gequ2.draw(screen):
        #bianse2=True
    #if bianse2==True:
        #bgpos3=(512,512)
       # bg1=pygame.image.load("对话背景.png")
        #screen.blit(bg1,bgpos3)
    if game_start==False:
        screen.blit(bg,bgpos1)
    
        
  
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            pygame.quit()
            quit()   
    pygame.display.update()
    clock.tick(60)









