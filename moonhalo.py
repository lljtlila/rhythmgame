import pygame
import button
class bocciready():
    start1=pygame.image.load("底.moonhalo.png")
    start2=pygame.image.load("简介.moonhalo.png")
    start3=pygame.image.load("开始.moonhalo.png")
    start4=pygame.image.load("歌手.moonhalo.png")
    start5=pygame.image.load("歌名.moonhalo.png")
    screen=pygame.display.set_mode((1280,720),0,32)
    gequ1=button.Button(336,80,start1,1)   
    gequ2=button.Button(459,260,start2,1) 
    gequ3=button.Button(500,470,start3,1) 
    gequ4=button.Button(336,600,start4,1)
    gequ5=button.Button(336,600,start5,1)
    gequ1.draw(screen)
    gequ2.draw(screen)
    gequ3.draw(screen)
    gequ4.draw(screen)
    gequ5.draw(screen)