#import pygame and initialize the pygame engine.
# Made by Dylan Ashraf, American High School, 10th Grade, On August 2nd, 2024
import pygame
from pygame.locals import *
import numpy as np
import random
import time

#initialize pygame
pygame.init()

#creates a blank window of width 640 pixels and height 480 pixels.
#Window :top left corner is (0, 0), right bottom corner is (640,480).
screen = pygame.display.set_mode((880,880))
#To set the name of our window to “Shapes”
pygame.display.set_caption("Shapes!!")

#variables and intialization
# Circle = 30
# Lines = 20
# Barrier = 50
# (16 x 30) + (20 x 15) + (50 x 2) = 880
n1=0
neuronreach=0
screenfillnum=0
data = np.load("data_video.npz")
yellow = (235,225,0)
pure_red = (255, 0, 0)
pure_blue = (0, 0, 255)
pure_green = (0, 255, 0)
pink = (175, 0, 175)
orange = (240, 100, 0)
white = (255, 255, 255)
bgcolor = (57, 12, 180)
nodeindex=20
startloopnum=0
nodelist0=[]
nodelist1=[]
for i in range(0, 16, 1):
    for n in range(0, 16, 1):
        nodelist0.append(int(data["out_samps1"] [0, i, n]))
        nodelist1.append(int(data["out_samps1"] [1, i, n]))
nodecoordinates=[]
neuroncoordinates=[]
for i in range(0, 16, 1):
    for n in range(0, 16, 1):
        neuroncoordinates.append([(65+(n*50)), (65+(i*50))])
        nodecoordinates.append(((65+(n*50)), (65+(i*50))))
topleftcorner=[16, 17, 1]
toprightcorner=[-1, 15, 16]
bottomleftcorner=[-16, -15, 1]
bottomrightcorner=[-1, -17, -16]
top=[-1, 15, 16, 17, 1]
left=[-16, -15, 1, 16, 17]
right=[-17, -16, -1, 15, 16]
bottom=[-1, -17, -16, -15, 1]
middle=[-17, -16, -15, -1, 1, 15, 16, 17]

bneuron=pygame.image.load("blueneuron.png")
bneuron=pygame.transform.scale(bneuron, (16, 16))
oneuron=pygame.image.load("orangeneuron.png")
oneuron=pygame.transform.scale(oneuron, (16, 16))
yneuron=pygame.image.load("yellowneuron.png")
yneuron=pygame.transform.scale(yneuron, (16, 16))
pneuron=pygame.image.load("purpleneuron.png")
pneuron=pygame.transform.scale(pneuron, (16, 16))
bluenodeoff=pygame.image.load("bluenodeoff.png")
bluenodeoff=pygame.transform.scale(bluenodeoff, (30, 30))
bluenodeon=pygame.image.load("bluenodeon.png")
bluenodeon=pygame.transform.scale(bluenodeon, (30, 30))
neurons=[bneuron, oneuron, yneuron, pneuron]


#The Game Loop”
while True:
    #Most of our game logic goes here
    for event in pygame.event.get():
        if screenfillnum==0:
            screen.fill(bgcolor)
            screenfillnum=1000
        if event.type == QUIT:
            pygame.quit()
            exit()
    for i in range(0, 16, 1):
        pygame.draw.line(screen, white, (nodecoordinates[i]), (nodecoordinates[i][0], (nodecoordinates[i][1]+750)), 2)
    for i in range(0, 16, 1):
        pygame.draw.line(screen, white, (nodecoordinates[i*16]), ((nodecoordinates[i*16][0]+750), nodecoordinates[i*16][1]), 2)
    for n in range(0, 15, 1):
        for i in range((n*16), 15+(n*16), 1):
            pygame.draw.line(screen, white, (nodecoordinates[i]), (nodecoordinates[i+17]), 2)
            pygame.draw.line(screen, white, (nodecoordinates[i+1]), (nodecoordinates[i+16]), 2)
    for i in range(0, 256, 1):
        if nodelist0[i]==1:
            screen.blit(bluenodeon, ((nodecoordinates[i][0])-15, (nodecoordinates[i][1])-15))
        if nodelist0[i]==0:
            screen.blit(bluenodeoff, ((nodecoordinates[i][0])-15, (nodecoordinates[i][1])-15))
    if startloopnum>0:
        for p in range(0, 256, 1):
            nodeindex=p
            neuronreach=0
            n1=0
            if nodeindex==0:
                while neuronreach==0:
                    screen.fill(bgcolor)
                    for i in range(0, 16, 1):
                        pygame.draw.line(screen, white, (nodecoordinates[i]), (nodecoordinates[i][0], (nodecoordinates[i][1]+750)), 2)
                    for i in range(0, 16, 1):
                        pygame.draw.line(screen, white, (nodecoordinates[i*16]), ((nodecoordinates[i*16][0]+750), nodecoordinates[i*16][1]), 2)
                    for n in range(0, 15, 1):
                        for i in range((n*16), 15+(n*16), 1):
                            pygame.draw.line(screen, white, (nodecoordinates[i]), (nodecoordinates[i+17]), 2)
                            pygame.draw.line(screen, white, (nodecoordinates[i+1]), (nodecoordinates[i+16]), 2)
                    for i in range(0, 256, 1):
                        if nodelist0[i]==1:
                            screen.blit(bluenodeon, ((nodecoordinates[i][0])-15, (nodecoordinates[i][1])-15))
                        if nodelist0[i]==0:
                            screen.blit(bluenodeoff, ((nodecoordinates[i][0])-15, (nodecoordinates[i][1])-15))
                    for i in topleftcorner:
                        if n1==0:
                            neuroncoordinates1=[]
                            for i in range(0, 16, 1):
                                for n in range(0, 16, 1):
                                    neuroncoordinates1.append([(65+(n*50)), (65+(i*50))])
                            neuronuse=neurons[random.randint(0, 3)]
                            n1=1
                            print((neuroncoordinates1[nodeindex+i][0]-8, neuroncoordinates1[nodeindex][1]-8))
                        screen.blit(neuronuse, tuple((neuroncoordinates1[nodeindex+i][0]-8, neuroncoordinates1[nodeindex+i][1]-8)))
                        if tuple(neuroncoordinates1[nodeindex+i])==nodecoordinates[nodeindex]:
                            print("hi")
                            neuronreach=1
                            if nodelist0[p]==nodelist1[p]:
                                pass
                            elif nodelist0[p]!=nodelist1[p]:
                                nodelist0[p]=nodelist1[p]
                            neuroncoordinates1=neuroncoordinates
                    neuroncoordinates1[nodeindex+16][1]=neuroncoordinates1[nodeindex+16][1]-0.5
                    neuroncoordinates1[nodeindex+1][0]=neuroncoordinates1[nodeindex+1][0]-0.5
                    neuroncoordinates1[nodeindex+17][1]=neuroncoordinates1[nodeindex+17][1]-0.5
                    neuroncoordinates1[nodeindex+17][0]=neuroncoordinates1[nodeindex+17][0]-0.5
                    pygame.display.update()
            elif nodeindex==15:
                while neuronreach==0:
                    screen.fill(bgcolor)
                    for i in range(0, 16, 1):
                        pygame.draw.line(screen, white, (nodecoordinates[i]), (nodecoordinates[i][0], (nodecoordinates[i][1]+750)), 2)
                    for i in range(0, 16, 1):
                        pygame.draw.line(screen, white, (nodecoordinates[i*16]), ((nodecoordinates[i*16][0]+750), nodecoordinates[i*16][1]), 2)
                    for n in range(0, 15, 1):
                        for i in range((n*16), 15+(n*16), 1):
                            pygame.draw.line(screen, white, (nodecoordinates[i]), (nodecoordinates[i+17]), 2)
                            pygame.draw.line(screen, white, (nodecoordinates[i+1]), (nodecoordinates[i+16]), 2)
                    for i in range(0, 256, 1):
                        if nodelist0[i]==1:
                            screen.blit(bluenodeon, ((nodecoordinates[i][0])-15, (nodecoordinates[i][1])-15))
                        if nodelist0[i]==0:
                            screen.blit(bluenodeoff, ((nodecoordinates[i][0])-15, (nodecoordinates[i][1])-15))
                    for i in toprightcorner:
                        if n1==0:
                            neuroncoordinates1=[]
                            for i in range(0, 16, 1):
                                for n in range(0, 16, 1):
                                    neuroncoordinates1.append([(65+(n*50)), (65+(i*50))])
                            neuronuse=neurons[random.randint(0, 3)]
                            n1=1
                        screen.blit(neuronuse, tuple((neuroncoordinates1[nodeindex+i][0]-8, neuroncoordinates1[nodeindex+i][1]-8)))
                        if tuple(neuroncoordinates1[nodeindex+i])==nodecoordinates[nodeindex]:
                            neuronreach=1
                            if nodelist0[p]==nodelist1[p]:
                                pass
                            elif nodelist0[p]!=nodelist1[p]:
                                nodelist0[p]=nodelist1[p]
                            neuroncoordinates1=neuroncoordinates
                    neuroncoordinates1[nodeindex-1][0]=neuroncoordinates1[nodeindex-1][0]+0.5
                    neuroncoordinates1[nodeindex+15][0]=neuroncoordinates1[nodeindex+15][0]+0.5
                    neuroncoordinates1[nodeindex+15][1]=neuroncoordinates1[nodeindex+15][1]-0.5
                    neuroncoordinates1[nodeindex+16][1]=neuroncoordinates1[nodeindex+17][1]-0.5
                    pygame.display.update()
            elif nodeindex==240:
                while neuronreach==0:
                    screen.fill(bgcolor)
                    for i in range(0, 16, 1):
                        pygame.draw.line(screen, white, (nodecoordinates[i]), (nodecoordinates[i][0], (nodecoordinates[i][1]+750)), 2)
                    for i in range(0, 16, 1):
                        pygame.draw.line(screen, white, (nodecoordinates[i*16]), ((nodecoordinates[i*16][0]+750), nodecoordinates[i*16][1]), 2)
                    for n in range(0, 15, 1):
                        for i in range((n*16), 15+(n*16), 1):
                            pygame.draw.line(screen, white, (nodecoordinates[i]), (nodecoordinates[i+17]), 2)
                            pygame.draw.line(screen, white, (nodecoordinates[i+1]), (nodecoordinates[i+16]), 2)
                    for i in range(0, 256, 1):
                        if nodelist0[i]==1:
                            screen.blit(bluenodeon, ((nodecoordinates[i][0])-15, (nodecoordinates[i][1])-15))
                        if nodelist0[i]==0:
                            screen.blit(bluenodeoff, ((nodecoordinates[i][0])-15, (nodecoordinates[i][1])-15))
                    for i in bottomleftcorner:
                        if n1==0:
                            neuroncoordinates1=[]
                            for i in range(0, 16, 1):
                                for n in range(0, 16, 1):
                                    neuroncoordinates1.append([(65+(n*50)), (65+(i*50))])
                            neuronuse=neurons[random.randint(0, 3)]
                            n1=1
                        screen.blit(neuronuse, tuple((neuroncoordinates1[nodeindex+i][0]-8, neuroncoordinates1[nodeindex+i][1]-8)))
                        if tuple(neuroncoordinates1[nodeindex+i])==nodecoordinates[nodeindex]:
                            neuronreach=1
                            if nodelist0[p]==nodelist1[p]:
                                pass
                            elif nodelist0[p]!=nodelist1[p]:
                                nodelist0[p]=nodelist1[p]
                            neuroncoordinates1=neuroncoordinates
                    neuroncoordinates1[nodeindex-16][1]=neuroncoordinates1[nodeindex-16][1]+0.5
                    neuroncoordinates1[nodeindex-15][0]=neuroncoordinates1[nodeindex-15][0]-0.5
                    neuroncoordinates1[nodeindex-15][1]=neuroncoordinates1[nodeindex-15][1]+0.5
                    neuroncoordinates1[nodeindex+1][0]=neuroncoordinates1[nodeindex+1][0]-0.5
                    pygame.display.update()
            elif nodeindex==255:
                while neuronreach==0:
                    screen.fill(bgcolor)
                    for i in range(0, 16, 1):
                        pygame.draw.line(screen, white, (nodecoordinates[i]), (nodecoordinates[i][0], (nodecoordinates[i][1]+750)), 2)
                    for i in range(0, 16, 1):
                        pygame.draw.line(screen, white, (nodecoordinates[i*16]), ((nodecoordinates[i*16][0]+750), nodecoordinates[i*16][1]), 2)
                    for n in range(0, 15, 1):
                        for i in range((n*16), 15+(n*16), 1):
                            pygame.draw.line(screen, white, (nodecoordinates[i]), (nodecoordinates[i+17]), 2)
                            pygame.draw.line(screen, white, (nodecoordinates[i+1]), (nodecoordinates[i+16]), 2)
                    for i in range(0, 256, 1):
                        if nodelist0[i]==1:
                            screen.blit(bluenodeon, ((nodecoordinates[i][0])-15, (nodecoordinates[i][1])-15))
                        if nodelist0[i]==0:
                            screen.blit(bluenodeoff, ((nodecoordinates[i][0])-15, (nodecoordinates[i][1])-15))
                    for i in bottomrightcorner:
                        if n1==0:
                            neuroncoordinates1=[]
                            for i in range(0, 16, 1):
                                for n in range(0, 16, 1):
                                    neuroncoordinates1.append([(65+(n*50)), (65+(i*50))])
                            neuronuse=neurons[random.randint(0, 3)]
                            n1=1
                        screen.blit(neuronuse, tuple((neuroncoordinates1[nodeindex+i][0]-8, neuroncoordinates1[nodeindex+i][1]-8)))
                        if tuple(neuroncoordinates1[nodeindex+i])==nodecoordinates[nodeindex]:
                            neuronreach=1
                            if nodelist0[p]==nodelist1[p]:
                                pass
                            elif nodelist0[p]!=nodelist1[p]:
                                nodelist0[p]=nodelist1[p]
                            neuroncoordinates1=neuroncoordinates
                    neuroncoordinates1[nodeindex-1][0]=neuroncoordinates1[nodeindex-1][0]+0.5
                    neuroncoordinates1[nodeindex-17][0]=neuroncoordinates1[nodeindex-17][0]+0.5
                    neuroncoordinates1[nodeindex-17][1]=neuroncoordinates1[nodeindex-17][1]+0.5
                    neuroncoordinates1[nodeindex-16][1]=neuroncoordinates1[nodeindex-16][1]+0.5
                    pygame.display.update()
            elif nodeindex>0 and nodeindex<15:
                while neuronreach==0:
                    screen.fill(bgcolor)
                    for i in range(0, 16, 1):
                        pygame.draw.line(screen, white, (nodecoordinates[i]), (nodecoordinates[i][0], (nodecoordinates[i][1]+750)), 2)
                    for i in range(0, 16, 1):
                        pygame.draw.line(screen, white, (nodecoordinates[i*16]), ((nodecoordinates[i*16][0]+750), nodecoordinates[i*16][1]), 2)
                    for n in range(0, 15, 1):
                        for i in range((n*16), 15+(n*16), 1):
                            pygame.draw.line(screen, white, (nodecoordinates[i]), (nodecoordinates[i+17]), 2)
                            pygame.draw.line(screen, white, (nodecoordinates[i+1]), (nodecoordinates[i+16]), 2)
                    for i in range(0, 256, 1):
                        if nodelist0[i]==1:
                            screen.blit(bluenodeon, ((nodecoordinates[i][0])-15, (nodecoordinates[i][1])-15))
                        if nodelist0[i]==0:
                            screen.blit(bluenodeoff, ((nodecoordinates[i][0])-15, (nodecoordinates[i][1])-15))
                    for i in top:
                        if n1==0:
                            neuroncoordinates1=[]
                            for i in range(0, 16, 1):
                                for n in range(0, 16, 1):
                                    neuroncoordinates1.append([(65+(n*50)), (65+(i*50))])
                            neuronuse=neurons[random.randint(0, 3)]
                            n1=1
                        # screen.blit(neuronuse, (neuroncoordinates1[nodeindex+i][0]-8, neuroncoordinates1[nodeindex][1]-8))
                        screen.blit(neuronuse, tuple((neuroncoordinates1[nodeindex+i][0]-8, neuroncoordinates1[nodeindex+i][1]-8)))
                        if tuple(neuroncoordinates1[nodeindex+i])==nodecoordinates[nodeindex]:
                            neuronreach=1
                            if nodelist0[p]==nodelist1[p]:
                                pass
                            elif nodelist0[p]!=nodelist1[p]:
                                nodelist0[p]=nodelist1[p]
                            neuroncoordinates1=neuroncoordinates
                    neuroncoordinates1[nodeindex-1][0]=neuroncoordinates1[nodeindex-1][0]+0.5
                    neuroncoordinates1[nodeindex+15][0]=neuroncoordinates1[nodeindex+15][0]+0.5
                    neuroncoordinates1[nodeindex+15][1]=neuroncoordinates1[nodeindex+15][1]-0.5
                    neuroncoordinates1[nodeindex+16][1]=neuroncoordinates1[nodeindex+16][1]-0.5
                    neuroncoordinates1[nodeindex+17][0]=neuroncoordinates1[nodeindex+17][0]-0.5
                    neuroncoordinates1[nodeindex+17][1]=neuroncoordinates1[nodeindex+17][1]-0.5
                    neuroncoordinates1[nodeindex+1][0]=neuroncoordinates1[nodeindex+1][0]-0.5
                    pygame.display.update()
            elif nodeindex!=240 and nodeindex!=0 and nodeindex%16==0:
                while neuronreach==0:
                    screen.fill(bgcolor)
                    for i in range(0, 16, 1):
                        pygame.draw.line(screen, white, (nodecoordinates[i]), (nodecoordinates[i][0], (nodecoordinates[i][1]+750)), 2)
                    for i in range(0, 16, 1):
                        pygame.draw.line(screen, white, (nodecoordinates[i*16]), ((nodecoordinates[i*16][0]+750), nodecoordinates[i*16][1]), 2)
                    for n in range(0, 15, 1):
                        for i in range((n*16), 15+(n*16), 1):
                            pygame.draw.line(screen, white, (nodecoordinates[i]), (nodecoordinates[i+17]), 2)
                            pygame.draw.line(screen, white, (nodecoordinates[i+1]), (nodecoordinates[i+16]), 2)
                    for i in range(0, 256, 1):
                        if nodelist0[i]==1:
                            screen.blit(bluenodeon, ((nodecoordinates[i][0])-15, (nodecoordinates[i][1])-15))
                        if nodelist0[i]==0:
                            screen.blit(bluenodeoff, ((nodecoordinates[i][0])-15, (nodecoordinates[i][1])-15))
                    for i in left:
                        if n1==0:
                            neuroncoordinates1=[]
                            for i in range(0, 16, 1):
                                for n in range(0, 16, 1):
                                    neuroncoordinates1.append([(65+(n*50)), (65+(i*50))])
                            neuronuse=neurons[random.randint(0, 3)]
                            n1=1
                        screen.blit(neuronuse, tuple((neuroncoordinates1[nodeindex+i][0]-8, neuroncoordinates1[nodeindex+i][1]-8)))
                        if tuple(neuroncoordinates1[nodeindex+i])==nodecoordinates[nodeindex]:
                            neuronreach=1
                            if nodelist0[p]==nodelist1[p]:
                                pass
                            elif nodelist0[p]!=nodelist1[p]:
                                nodelist0[p]=nodelist1[p]
                            neuroncoordinates1=neuroncoordinates
                    neuroncoordinates1[nodeindex-16][1]=neuroncoordinates1[nodeindex-16][1]+0.5
                    neuroncoordinates1[nodeindex-15][0]=neuroncoordinates1[nodeindex-15][0]-0.5
                    neuroncoordinates1[nodeindex-15][1]=neuroncoordinates1[nodeindex-15][1]+0.5
                    neuroncoordinates1[nodeindex+1][0]=neuroncoordinates1[nodeindex+1][0]-0.5
                    neuroncoordinates1[nodeindex+16][1]=neuroncoordinates1[nodeindex+16][1]-0.5
                    neuroncoordinates1[nodeindex+17][1]=neuroncoordinates1[nodeindex+17][1]-0.5
                    neuroncoordinates1[nodeindex+17][0]=neuroncoordinates1[nodeindex+17][0]-0.5
                    pygame.display.update()
            elif nodeindex!=15 and nodeindex!=255 and nodeindex%16==15:
                while neuronreach==0:
                    screen.fill(bgcolor)
                    for i in range(0, 16, 1):
                        pygame.draw.line(screen, white, (nodecoordinates[i]), (nodecoordinates[i][0], (nodecoordinates[i][1]+750)), 2)
                    for i in range(0, 16, 1):
                        pygame.draw.line(screen, white, (nodecoordinates[i*16]), ((nodecoordinates[i*16][0]+750), nodecoordinates[i*16][1]), 2)
                    for n in range(0, 15, 1):
                        for i in range((n*16), 15+(n*16), 1):
                            pygame.draw.line(screen, white, (nodecoordinates[i]), (nodecoordinates[i+17]), 2)
                            pygame.draw.line(screen, white, (nodecoordinates[i+1]), (nodecoordinates[i+16]), 2)
                    for i in range(0, 256, 1):
                        if nodelist0[i]==1:
                            screen.blit(bluenodeon, ((nodecoordinates[i][0])-15, (nodecoordinates[i][1])-15))
                        if nodelist0[i]==0:
                            screen.blit(bluenodeoff, ((nodecoordinates[i][0])-15, (nodecoordinates[i][1])-15))
                    for i in right:
                        if n1==0:
                            neuroncoordinates1=[]
                            for i in range(0, 16, 1):
                                for n in range(0, 16, 1):
                                    neuroncoordinates1.append([(65+(n*50)), (65+(i*50))])
                            neuronuse=neurons[random.randint(0, 3)]
                            n1=1
                        screen.blit(neuronuse, tuple((neuroncoordinates1[nodeindex+i][0]-8, neuroncoordinates1[nodeindex+i][1]-8)))
                        if tuple(neuroncoordinates1[nodeindex+i])==nodecoordinates[nodeindex]:
                            neuronreach=1
                            if nodelist0[p]==nodelist1[p]:
                                pass
                            elif nodelist0[p]!=nodelist1[p]:
                                nodelist0[p]=nodelist1[p]
                            neuroncoordinates1=neuroncoordinates
                    neuroncoordinates1[nodeindex-17][0]=neuroncoordinates1[nodeindex-17][0]+0.5
                    neuroncoordinates1[nodeindex-17][1]=neuroncoordinates1[nodeindex-17][1]+0.5
                    neuroncoordinates1[nodeindex-16][1]=neuroncoordinates1[nodeindex-16][1]+0.5
                    neuroncoordinates1[nodeindex-1][0]=neuroncoordinates1[nodeindex-1][0]+0.5
                    neuroncoordinates1[nodeindex+15][0]=neuroncoordinates1[nodeindex+15][0]+0.5
                    neuroncoordinates1[nodeindex+15][1]=neuroncoordinates1[nodeindex+15][1]-0.5
                    neuroncoordinates1[nodeindex+16][1]=neuroncoordinates1[nodeindex+16][1]-0.5
                    pygame.display.update()
            elif nodeindex>240 and nodeindex<255:
                while neuronreach==0:
                    screen.fill(bgcolor)
                    for i in range(0, 16, 1):
                        pygame.draw.line(screen, white, (nodecoordinates[i]), (nodecoordinates[i][0], (nodecoordinates[i][1]+750)), 2)
                    for i in range(0, 16, 1):
                        pygame.draw.line(screen, white, (nodecoordinates[i*16]), ((nodecoordinates[i*16][0]+750), nodecoordinates[i*16][1]), 2)
                    for n in range(0, 15, 1):
                        for i in range((n*16), 15+(n*16), 1):
                            pygame.draw.line(screen, white, (nodecoordinates[i]), (nodecoordinates[i+17]), 2)
                            pygame.draw.line(screen, white, (nodecoordinates[i+1]), (nodecoordinates[i+16]), 2)
                    for i in range(0, 256, 1):
                        if nodelist0[i]==1:
                            screen.blit(bluenodeon, ((nodecoordinates[i][0])-15, (nodecoordinates[i][1])-15))
                        if nodelist0[i]==0:
                            screen.blit(bluenodeoff, ((nodecoordinates[i][0])-15, (nodecoordinates[i][1])-15))
                    for i in bottom:
                        if n1==0:
                            neuroncoordinates1=[]
                            for i in range(0, 16, 1):
                                for n in range(0, 16, 1):
                                    neuroncoordinates1.append([(65+(n*50)), (65+(i*50))])
                            neuronuse=neurons[random.randint(0, 3)]
                            n1=1
                        screen.blit(neuronuse, tuple((neuroncoordinates1[nodeindex+i][0]-8, neuroncoordinates1[nodeindex+i][1]-8)))
                        if tuple(neuroncoordinates1[nodeindex+i])==nodecoordinates[nodeindex]:
                            neuronreach=1
                            if nodelist0[p]==nodelist1[p]:
                                pass
                            elif nodelist0[p]!=nodelist1[p]:
                                nodelist0[p]=nodelist1[p]
                            neuroncoordinates1=neuroncoordinates
                    neuroncoordinates1[nodeindex-1][0]=neuroncoordinates1[nodeindex-1][0]+0.5
                    neuroncoordinates1[nodeindex-17][0]=neuroncoordinates1[nodeindex-17][0]+0.5
                    neuroncoordinates1[nodeindex-17][1]=neuroncoordinates1[nodeindex-17][1]+0.5
                    neuroncoordinates1[nodeindex-16][1]=neuroncoordinates1[nodeindex-16][1]+0.5
                    neuroncoordinates1[nodeindex-15][0]=neuroncoordinates1[nodeindex-15][0]+0.5
                    neuroncoordinates1[nodeindex-15][1]=neuroncoordinates1[nodeindex-15][1]-0.5
                    neuroncoordinates1[nodeindex+1][0]=neuroncoordinates1[nodeindex+1][0]-0.5
                    pygame.display.update()
            elif nodeindex>16 and nodeindex<239 and nodeindex%16!=0 and nodeindex%16!=15:
                while neuronreach==0:
                    screen.fill(bgcolor)
                    for i in range(0, 16, 1):
                        pygame.draw.line(screen, white, (nodecoordinates[i]), (nodecoordinates[i][0], (nodecoordinates[i][1]+750)), 2)
                    for i in range(0, 16, 1):
                        pygame.draw.line(screen, white, (nodecoordinates[i*16]), ((nodecoordinates[i*16][0]+750), nodecoordinates[i*16][1]), 2)
                    for n in range(0, 15, 1):
                        for i in range((n*16), 15+(n*16), 1):
                            pygame.draw.line(screen, white, (nodecoordinates[i]), (nodecoordinates[i+17]), 2)
                            pygame.draw.line(screen, white, (nodecoordinates[i+1]), (nodecoordinates[i+16]), 2)
                    for i in range(0, 256, 1):
                        if nodelist0[i]==1:
                            screen.blit(bluenodeon, ((nodecoordinates[i][0])-15, (nodecoordinates[i][1])-15))
                        if nodelist0[i]==0:
                            screen.blit(bluenodeoff, ((nodecoordinates[i][0])-15, (nodecoordinates[i][1])-15))
                    for i in middle:
                        if n1==0:
                            neuroncoordinates1=[]
                            for i in range(0, 16, 1):
                                for n in range(0, 16, 1):
                                    neuroncoordinates1.append([(65+(n*50)), (65+(i*50))])
                            neuronuse=neurons[random.randint(0, 3)]
                            n1=1
                        screen.blit(neuronuse, tuple((neuroncoordinates1[nodeindex+i][0]-8, neuroncoordinates1[nodeindex+i][1]-8)))
                        if tuple(neuroncoordinates1[nodeindex+i])==nodecoordinates[nodeindex]:
                            neuronreach=1
                            if nodelist0[p]==nodelist1[p]:
                                pass
                            elif nodelist0[p]!=nodelist1[p]:
                                nodelist0[p]=nodelist1[p]
                            neuroncoordinates1=neuroncoordinates
                    neuroncoordinates1[nodeindex-1][0]=neuroncoordinates1[nodeindex-1][0]+0.5
                    neuroncoordinates1[nodeindex-17][0]=neuroncoordinates1[nodeindex-17][0]+0.5
                    neuroncoordinates1[nodeindex-17][1]=neuroncoordinates1[nodeindex-17][1]+0.5
                    neuroncoordinates1[nodeindex-16][1]=neuroncoordinates1[nodeindex-16][1]+0.5
                    neuroncoordinates1[nodeindex-15][0]=neuroncoordinates1[nodeindex-15][0]-0.5
                    neuroncoordinates1[nodeindex-15][1]=neuroncoordinates1[nodeindex-15][1]+0.5
                    neuroncoordinates1[nodeindex+1][0]=neuroncoordinates1[nodeindex+1][0]-0.5
                    neuroncoordinates1[nodeindex+15][0]=neuroncoordinates1[nodeindex+15][0]+0.5
                    neuroncoordinates1[nodeindex+15][1]=neuroncoordinates1[nodeindex+15][1]-0.5
                    neuroncoordinates1[nodeindex+16][1]=neuroncoordinates1[nodeindex+16][1]-0.5
                    neuroncoordinates1[nodeindex+17][1]=neuroncoordinates1[nodeindex+17][1]-0.5
                    neuroncoordinates1[nodeindex+17][0]=neuroncoordinates1[nodeindex+17][0]-0.5
                    pygame.display.update()
    startloopnum=startloopnum+1
    #Continuously update the screen
    pygame.display.update()
