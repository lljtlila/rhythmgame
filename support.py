from os import walk
import pygame

def import_floder(path):
    surface_list=[]
    for _,__,img_files in walk(path):
        for image in img_files:
            full_path =path + "/"+image_surf
            image_surf = pygame.image.load(full_path)
            surface_list.append(image_surf)
    return surface_list