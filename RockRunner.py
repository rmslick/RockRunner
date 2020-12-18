import pygame
from random import randint
pygame.init()
screen=pygame.display.set_mode((1000,600))
pygame.display.set_caption("Rock Runner")
clear=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
runnerX=640
runnerY=585
runnerHeight=15
runnerWidth=40
runnerVel=0.8
# object current co-ordinates  
x = 500
y = 0
speed = 0.5
while True:
    # completely fill the surface object   
    # with black colour
       
    screen.fill((0, 0, 0))
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if runnerX>=0:
            pygame.draw.rect(screen,(clear),(runnerX,runnerY,runnerWidth,runnerHeight))
            runnerX-=runnerVel
    if keys[pygame.K_RIGHT]:
        if runnerX<=960:
            pygame.draw.rect(screen,(clear),(runnerX,runnerY,runnerWidth,runnerHeight))
            runnerX+=runnerVel
    pygame.draw.rect(screen,(red),(runnerX,runnerY,runnerWidth,runnerHeight))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    pygame.draw.rect(screen, (255, 255, 0), (x, y, 20, 40)) 
    pygame.display.update()
    y = y + speed
    if y > 590:
        y = 0
        x = randint(10,990)