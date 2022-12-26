import pygame,sys,button
import time,math
clock = pygame.time.Clock()
clock.tick(60)
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(".\\assets\\start\\start_game\\game\\arknight.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-50)
screen=pygame.display.set_mode((1280,720),0,32)
run = True
text = True
score=0
def update():
    pygame.display.update()
def bg():
   game_bg=pygame.image.load(".\\assets\\start\\start_game\\game\\game.png")
   bgpos3=(1280,720)
   image=pygame.transform.scale(game_bg,bgpos3)
   bg_rect=image.get_rect()
   bg_width=image.get_width()
   screen.blit(image,(0,0))
while run:
    bg()
    while text:
      for i in range(7):
         a=str(i+1)
         image = pygame.image.load(".\\assets\\text\\"+a+".png")
         dx = 200
         dy = 200
         screen.blit(image,(dx,dy))
         update()
         pygame.time.wait(3500)
         bg()
         update()
         text = False
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
    update()
    def mod():
      mod=pygame.image.load(".\\assets\\start\\mod.jpg")
      bgpos3=(1280,720)
      image=pygame.transform.scale(mod,bgpos3)
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
      
    