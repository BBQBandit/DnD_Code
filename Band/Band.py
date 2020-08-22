# -*- coding: utf-8 -*-

import pygame
import random
import time
import playsound

random.seed(time.time())

pygame.init()

width = 1000
height = 1000
run = True

win = pygame.display.set_mode((width, height))

array = []

while run:
    win.fill((0,0,0))    
    
    for event in pygame.event.get():
        if pygame.key.get_mods() & pygame.KMOD_ALT and pygame.key.get_pressed()[pygame.K_F4]:
            pygame.quit()
            continue
        """
        Replace this with serial button readins
        """
        if pygame.key.get_pressed()[pygame.K_q]:
                playsound.playsound("20134__gezortenplotz__magic-gong.mp3", False)
                print("q")
        if pygame.key.get_pressed()[pygame.K_w]:
            state = 1
            print("w")
        if pygame.key.get_pressed()[pygame.K_e]:
            state = 2
            print("e")
        if pygame.key.get_pressed()[pygame.K_r]:
            state = 3
            print("r")

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            runner = 0
            
    pygame.display.flip()
    
    