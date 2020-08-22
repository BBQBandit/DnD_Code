# -*- coding: utf-8 -*-

import pygame
import random
import time

random.seed(time.time())

pygame.init()

width = 1000
height = 1000
run = True
state = 0
runner = 0
r = 0
s = 0

Heal = pygame.image.load('heal_50.png')
recti = Heal.get_rect()
Rage = pygame.image.load('rage_50.png')
Fire = pygame.image.load('fire_50.png')
Clean = pygame.image.load('clean_50.png')

pics = [Clean, Heal, Rage, Fire]

array = [[0] * int(width / recti.width) for i in range(int(height / recti.height))] 

win = pygame.display.set_mode((width, height))

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
            state = 0
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
        """
        """
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            runner = 0
            while runner < random.randint(5, 10):           # This should be the corresponding analog value
                w = random.randint(0, int(width / recti.width) - 1)
                h = random.randint(0, int(height / recti.height) - 1)
                print(w,h)
                array [w] [h] = state
                runner += 1
    
    r = 0
    s = 0             
    for row in array:
        for ele in row:        
            win.blit(pics[ele], [r * recti.width,s * recti.height])
            s += 1
        s = 0
        r += 1

    for i in range(0, int(width / recti.width)):
        pygame.draw.line(win, (255,255,255), (i * recti.width, 0), (i * recti.width, height), 3)
    for i in range(0, int(height / recti.height)):
        pygame.draw.line(win, (255,255,255), (0, i * recti.height), (width, i * recti.height), 3)
            
    pygame.display.flip()