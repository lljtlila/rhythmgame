import pygame
for i in range(30):
    x = str(i+1)
    image=pygame.image.load(".\\assets\\icecream\\"+x+".jpg") 
    screen.blit(bg2,bgpos3)
    pygame.display.flip()
    time.sleep(0.033)