import pygame,sys,button

pygame.init()
bg=pygame.image.load("背景.jpg")
bg1=pygame.image.load("背景1.jpg")
bgpos=bg.get_rect()
bgpos1=bg1.get_rect()
logo=pygame.image.load("对话背景.png")
pygame.display.set_icon(logo)
screen=pygame.display.set_mode((1280,720),0,32)
clock=pygame.time.Clock()
pygame.display.set_caption("Rhythm")
screen.blit(bg,bgpos)


            
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()   
    key=pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        screen.blit(bg1,bgpos1)
    pygame.display.update()
    clock.tick(60)









