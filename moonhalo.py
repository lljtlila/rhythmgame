import pygame,sys,button
import time,math
clock = pygame.time.Clock()
clock.tick(60)
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(".\\assets\\start\\start_game\\game\\moonhalo.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-50)
screen=pygame.display.set_mode((1280,720),0,32)
run = True
score=0
def update():
    pygame.display.update()
while run:
    game_bg=pygame.image.load(".\\assets\\start\\start_game\\game\\game.png")
    bgpos3=(1280,720)
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
    update()
    for event in pygame.event.get():
       if event.type==pygame.QUIT:
           run=False
           pygame.quit()
           quit()
    update()
    clock.tick(60)
    pygame.font.init
    font=pygame.font.SysFont(".\\assets\\得意黑.ttf",40)
    start1=font.render("Hey,这里是新手教程",True,"pink")
    screen.blit(start1,(200,100))
    update()
    
    