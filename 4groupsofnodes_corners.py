#import pygame and initialize the pygame engine.
# Made by Dylan Ashraf, American High School, 10th Grade, On August 2nd, 2024
import pygame
from pygame.locals import *
import numpy as np
import random
import sys

#initialize pygame
pygame.init()

#creates a blank window of width 640 pixels and height 480 pixels.
#Window :top left corner is (0, 0), right bottom corner is (640,480).
screen = pygame.display.set_mode((880, 880))
#To set the name of our window to “Shapes”
pygame.display.set_caption("Shapes!!")

#variables and intialization
xindex=0
n10=0
n20=0
n30=0
n40=0
n50=0
n6=0
yellow = (235,225,0)
pure_red = (255, 0, 0)
pure_blue = (0, 0, 255)
pure_green = (0, 255, 0)
pink = (175, 0, 175)
orange = (240, 100, 0)
startloopnum=0
data = np.load("data_video.npz")
nodelist0=[]
nodelist1=[]
for i in range(0, 16, 1):
    for n in range(0, 16, 1):
        nodelist0.append(int(data["out_samps1"] [0, i, n]))
        nodelist1.append(int(data["out_samps1"] [1, i, n]))
nodecoordinates=[]
neuroncoordinates=[]
neuroncoordinatesall=[]
neuroncoordinates1=[]
for i in range(16):
    for n in range(16):
        nodecoordinates.append((65+(n*50), 65+(i*50)))
        neuroncoordinates.append((65+(n*50), 65+(i*50)))
topleftcorner1=[16, 17, 1]
toprightcorner1=[-1, 15, 16]
bottomleftcorner1=[-16, -15, 1]
bottomrightcorner1=[-1, -17, -16]
top1=[-1, 15, 16, 17, 1]
left1=[-16, -15, 1, 16, 17]
right1=[-17, -16, -1, 15, 16]
bottom1=[-1, -17, -16, -15, 1]
middle1=[-17, -16, -15, -1, 1, 15, 16, 17]
bgcolor = (57, 12, 180)
white = (255, 255, 255)
rednodegroup=[]
bluenodegroup=[]
greennodegroup=[]
purplenodegroup=[]
rednodedifflist=[]
bluenodedifflist=[]
purplenodedifflist=[]
greennodedifflist=[]

for i in range(0, 16, 1):
    for n in range(0, 16, 1):
        if (65+(i*50))<416 and (65+(n*50))<416:
            bluenodegroup.append((n+(i*16)))
        elif (65+(i*50))>416 and (65+(n*50))<416:
            greennodegroup.append((n+(i*16)))
        elif (65+(i*50))<416 and (65+(n*50))>416:
            rednodegroup.append((n+(i*16)))
        elif (65+(i*50))>416 and (65+(n*50))>416:
            purplenodegroup.append((n+(i*16)))


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
greennodeoff=pygame.image.load("greennodeoff.png")
greennodeoff=pygame.transform.scale(greennodeoff, (30, 30))
greennodeon=pygame.image.load("greennodeon.png")
greennodeon=pygame.transform.scale(greennodeon, (30, 30))
purplenodeoff=pygame.image.load("purplenodeoff.png")
purplenodeoff=pygame.transform.scale(purplenodeoff, (30, 30))
purplenodeon=pygame.image.load("purplenodeon.png")
purplenodeon=pygame.transform.scale(purplenodeon, (30, 30))
rednodeoff=pygame.image.load("rednodeoff.png")
rednodeoff=pygame.transform.scale(rednodeoff, (30, 30))
rednodeon=pygame.image.load("rednodeon.png")
rednodeon=pygame.transform.scale(rednodeon, (30, 30))
neurons=[bneuron, oneuron, yneuron, pneuron]
nodeons=[bluenodeon, greennodeon, purplenodeon, rednodeon]
nodeoffs=[bluenodeoff, greennodeoff, purplenodeoff, rednodeoff]

def changenodes(bluenodedifflist):
    global nodedifflist
    global n2
    global n5
    global topleftcorner1
    global toprightcorner1
    global bottomleftcorner1
    global bottomrightcorner1
    global top1
    global left1
    global right1
    global bottom1
    global middle1
    global nodecoordinates
    global nodelist0
    global nodelist1
    global neuroncoordinatesall
    global neuroncoordinates1
    global neuroncoordinates
    global neuronreach
    if n2==0:
        neuroncoordinatesall=[]
        neuroncoordinates1=[]
        for g in range(600):
            neuroncoordinates1=[]
            for i in range(0, 16, 1):
                for n in range(0, 16, 1):
                    neuroncoordinates1.append([(65+(n*50)), (65+(i*50))])
            neuroncoordinatesall.append(neuroncoordinates1)
        n2=1
    for j in range(0, len(bluenodedifflist), 1):
        xindex=bluenodedifflist[j]
        if xindex==0:
            for i in topleftcorner1:
                screen.blit(bneuron, (neuroncoordinatesall[j][xindex+i][0]-8, neuroncoordinatesall[j][xindex+i][1]-8))
                if n5>50:
                    neuronreach=1
                    if nodelist0[xindex]==1:
                        nodelist0[xindex]=0
                    elif nodelist0[xindex]==0:
                        nodelist0[xindex]=1
            neuroncoordinatesall[j][xindex+16][1]=neuroncoordinatesall[j][xindex+16][1]-1
            neuroncoordinatesall[j][xindex+1][0]=neuroncoordinatesall[j][xindex+1][0]-1
            neuroncoordinatesall[j][xindex+17][1]=neuroncoordinatesall[j][xindex+17][1]-1
            neuroncoordinatesall[j][xindex+17][0]=neuroncoordinatesall[j][xindex+17][0]-1
            continue
        elif xindex==15:
            for i in toprightcorner1:
                screen.blit(bneuron, (neuroncoordinatesall[j][xindex+i][0]-8, neuroncoordinatesall[j][xindex+i][1]-8))
                if n5>50:
                    neuronreach=1
                    if nodelist0[xindex]==1:
                        nodelist0[xindex]=0
                    elif nodelist0[xindex]==0:
                        nodelist0[xindex]=1
            neuroncoordinatesall[j][xindex-1][0]=neuroncoordinatesall[j][xindex-1][0]+1
            neuroncoordinatesall[j][xindex+15][0]=neuroncoordinatesall[j][xindex+15][0]+1
            neuroncoordinatesall[j][xindex+15][1]=neuroncoordinatesall[j][xindex+15][1]-1
            neuroncoordinatesall[j][xindex+16][1]=neuroncoordinatesall[j][xindex+17][1]-1
            continue
        elif xindex==240:
            for i in bottomleftcorner1:
                screen.blit(bneuron, (neuroncoordinatesall[j][xindex+i][0]-8, neuroncoordinatesall[j][xindex+i][1]-8))
                if n5>50:
                    neuronreach=1
                    if nodelist0[xindex]==1:
                        nodelist0[xindex]=0
                    elif nodelist0[xindex]==0:
                        nodelist0[xindex]=1
            neuroncoordinatesall[j][xindex-16][1]=neuroncoordinatesall[j][xindex-16][1]+1
            neuroncoordinatesall[j][xindex-15][0]=neuroncoordinatesall[j][xindex-15][0]-1
            neuroncoordinatesall[j][xindex-15][1]=neuroncoordinatesall[j][xindex-15][1]+1
            neuroncoordinatesall[j][xindex+1][0]=neuroncoordinatesall[j][xindex+1][0]-1
            continue
        elif xindex==255:
            for i in bottomrightcorner1:
                screen.blit(bneuron, (neuroncoordinatesall[j][xindex+i][0]-8, neuroncoordinatesall[j][xindex+i][1]-8))
                if n5>50:
                    neuronreach=1
                    if nodelist0[xindex]==1:
                        nodelist0[xindex]=0
                    elif nodelist0[xindex]==0:
                        nodelist0[xindex]=1
            neuroncoordinatesall[j][xindex-1][0]=neuroncoordinatesall[j][xindex-1][0]+1
            neuroncoordinatesall[j][xindex-17][0]=neuroncoordinatesall[j][xindex-17][0]+1
            neuroncoordinatesall[j][xindex-17][1]=neuroncoordinatesall[j][xindex-17][1]+1
            neuroncoordinatesall[j][xindex-16][1]=neuroncoordinatesall[j][xindex-16][1]+1
            continue
        elif xindex>0 and xindex<15:
            for i in top1:
                screen.blit(bneuron, (neuroncoordinatesall[j][xindex+i][0]-8, neuroncoordinatesall[j][xindex+i][1]-8))
                if n5>50:
                    neuronreach=1
                    if nodelist0[xindex]==1:
                        nodelist0[xindex]=0
                    elif nodelist0[xindex]==0:
                        nodelist0[xindex]=1
            neuroncoordinatesall[j][xindex-1][0]=neuroncoordinatesall[j][xindex-1][0]+1
            neuroncoordinatesall[j][xindex+15][0]=neuroncoordinatesall[j][xindex+15][0]+1
            neuroncoordinatesall[j][xindex+15][1]=neuroncoordinatesall[j][xindex+15][1]-1
            neuroncoordinatesall[j][xindex+16][1]=neuroncoordinatesall[j][xindex+16][1]-1
            neuroncoordinatesall[j][xindex+17][0]=neuroncoordinatesall[j][xindex+17][0]-1
            neuroncoordinatesall[j][xindex+17][1]=neuroncoordinatesall[j][xindex+17][1]-1
            neuroncoordinatesall[j][xindex+1][0]=neuroncoordinatesall[j][xindex+1][0]-1
            continue
        elif xindex%16==0 and xindex!=0 and xindex!=240:
            for i in left1:
                screen.blit(bneuron, (neuroncoordinatesall[j][xindex+i][0]-8, neuroncoordinatesall[j][xindex+i][1]-8))
                if n5>50:
                    neuronreach=1
                    if nodelist0[xindex]==1:
                        nodelist0[xindex]=0
                    elif nodelist0[xindex]==0:
                        nodelist0[xindex]=1
            neuroncoordinatesall[j][xindex-16][1]=neuroncoordinatesall[j][xindex-16][1]+1
            neuroncoordinatesall[j][xindex-15][0]=neuroncoordinatesall[j][xindex-15][0]-1
            neuroncoordinatesall[j][xindex-15][1]=neuroncoordinatesall[j][xindex-15][1]+1
            neuroncoordinatesall[j][xindex+1][0]=neuroncoordinatesall[j][xindex+1][0]-1
            neuroncoordinatesall[j][xindex+16][1]=neuroncoordinatesall[j][xindex+16][1]-1
            neuroncoordinatesall[j][xindex+17][1]=neuroncoordinatesall[j][xindex+17][1]-1
            neuroncoordinatesall[j][xindex+17][0]=neuroncoordinatesall[j][xindex+17][0]-1
            continue
        elif xindex%16==15 and xindex!=15 and xindex!=255:
            for i in right1:
                screen.blit(bneuron, (neuroncoordinatesall[j][xindex+i][0]-8, neuroncoordinatesall[j][xindex+i][1]-8))
                if n5>50:
                    neuronreach=1
                    if nodelist0[xindex]==1:
                        nodelist0[xindex]=0
                    elif nodelist0[xindex]==0:
                        nodelist0[xindex]=1
            neuroncoordinatesall[j][xindex-17][0]=neuroncoordinatesall[j][xindex-17][0]+1
            neuroncoordinatesall[j][xindex-17][1]=neuroncoordinatesall[j][xindex-17][1]+1
            neuroncoordinatesall[j][xindex-16][1]=neuroncoordinatesall[j][xindex-16][1]+1
            neuroncoordinatesall[j][xindex-1][0]=neuroncoordinatesall[j][xindex-1][0]+1
            neuroncoordinatesall[j][xindex+15][0]=neuroncoordinatesall[j][xindex+15][0]+1
            neuroncoordinatesall[j][xindex+15][1]=neuroncoordinatesall[j][xindex+15][1]-1
            neuroncoordinatesall[j][xindex+16][1]=neuroncoordinatesall[j][xindex+16][1]-1
            continue
        elif xindex>240 and xindex<255:
            for i in bottom1:
                screen.blit(bneuron, (neuroncoordinatesall[j][xindex+i][0]-8, neuroncoordinatesall[j][xindex+i][1]-8))
                if n5>50:
                    neuronreach=1
                    if nodelist0[xindex]==1:
                        nodelist0[xindex]=0
                    elif nodelist0[xindex]==0:
                        nodelist0[xindex]=1
            neuroncoordinatesall[j][xindex-1][0]=neuroncoordinatesall[j][xindex-1][0]+1
            neuroncoordinatesall[j][xindex-17][0]=neuroncoordinatesall[j][xindex-17][0]+1
            neuroncoordinatesall[j][xindex-17][1]=neuroncoordinatesall[j][xindex-17][1]+1
            neuroncoordinatesall[j][xindex-16][1]=neuroncoordinatesall[j][xindex-16][1]+1
            neuroncoordinatesall[j][xindex-15][0]=neuroncoordinatesall[j][xindex-15][0]-1
            neuroncoordinatesall[j][xindex-15][1]=neuroncoordinatesall[j][xindex-15][1]+1
            neuroncoordinatesall[j][xindex+1][0]=neuroncoordinatesall[j][xindex+1][0]-1
            continue
        elif xindex>16 and xindex<239 and xindex%16!=0 and xindex%16!=15:
            for i in middle1:
                screen.blit(bneuron, (neuroncoordinatesall[j][xindex+i][0]-8, neuroncoordinatesall[j][xindex+i][1]-8))
                if n5>50:
                    neuronreach=1
                    if nodelist0[xindex]==1:
                        nodelist0[xindex]=0
                    elif nodelist0[xindex]==0:
                        nodelist0[xindex]=1
            neuroncoordinatesall[j][xindex-1][0]=neuroncoordinatesall[j][xindex-1][0]+1
            neuroncoordinatesall[j][xindex-17][0]=neuroncoordinatesall[j][xindex-17][0]+1
            neuroncoordinatesall[j][xindex-17][1]=neuroncoordinatesall[j][xindex-17][1]+1
            neuroncoordinatesall[j][xindex-16][1]=neuroncoordinatesall[j][xindex-16][1]+1
            neuroncoordinatesall[j][xindex-15][0]=neuroncoordinatesall[j][xindex-15][0]-1
            neuroncoordinatesall[j][xindex-15][1]=neuroncoordinatesall[j][xindex-15][1]+1
            neuroncoordinatesall[j][xindex+1][0]=neuroncoordinatesall[j][xindex+1][0]-1
            neuroncoordinatesall[j][xindex+15][0]=neuroncoordinatesall[j][xindex+15][0]+1
            neuroncoordinatesall[j][xindex+15][1]=neuroncoordinatesall[j][xindex+15][1]-1
            neuroncoordinatesall[j][xindex+16][1]=neuroncoordinatesall[j][xindex+16][1]-1
            neuroncoordinatesall[j][xindex+17][1]=neuroncoordinatesall[j][xindex+17][1]-1
            neuroncoordinatesall[j][xindex+17][0]=neuroncoordinatesall[j][xindex+17][0]-1
            continue
    n5=n5+1
    pygame.display.update()



#The Game Loop”
while True:
    #Most of our game logic goes here
    for event in pygame.event.get():
        if startloopnum==0:
            screen.fill(bgcolor)
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
        if i%32>-1 and i%32<16:
            if i%2==0:
                if nodelist0[i]==1:
                    screen.blit(bluenodeon, (nodecoordinates[i][0]-15, nodecoordinates[i][1]-15))
                elif nodelist0[i]==0:
                    screen.blit(bluenodeoff, (nodecoordinates[i][0]-15, nodecoordinates[i][1]-15))
            elif i%2==1:
                if nodelist0[i]==1:
                    screen.blit(greennodeon, (nodecoordinates[i][0]-15, nodecoordinates[i][1]-15))
                elif nodelist0[i]==0:
                    screen.blit(greennodeoff, (nodecoordinates[i][0]-15, nodecoordinates[i][1]-15))
        if i%32>15:
            if i%2==0:
                if nodelist0[i]==1:
                    screen.blit(rednodeon, (nodecoordinates[i][0]-15, nodecoordinates[i][1]-15))
                elif nodelist0[i]==0:
                    screen.blit(rednodeoff, (nodecoordinates[i][0]-15, nodecoordinates[i][1]-15))
            elif i%2==1:
                if nodelist0[i]==1:
                    screen.blit(purplenodeon, (nodecoordinates[i][0]-15, nodecoordinates[i][1]-15))
                elif nodelist0[i]==0:
                    screen.blit(purplenodeoff, (nodecoordinates[i][0]-15, nodecoordinates[i][1]-15))
    if startloopnum>0:
        for p in range(0, 2040, 1):
            neuronreach=0
            n2=0
            lists = {}
            n5=0
            n6=n6+1
            n10=0
            n20=0
            n30=0
            n40=0
            n50=0
            listno = 0
            nodedifflist=[]
            bluenodedifflist=[]
            rednodedifflist=[]
            greennodedifflist=[]
            purplenodedifflist=[]
            if p%4==0:
                nodelist0=[]
                nodelist1=[]
                for i in range(0, 16, 1):
                    for n in range(0, 16, 1):
                        nodelist0.append(int(data["out_samps1"] [(p//4), i, n]))
                        nodelist1.append(int(data["out_samps1"] [(p//4)+1, i, n]))
            for n in range(0, 256, 1):
                if nodelist0[n]==nodelist1[n]:
                    pass
                elif nodelist0[n]!=nodelist1[n]:
                    nodedifflist.append((nodelist0[n], n))
            for n in bluenodegroup:
                for i in nodedifflist:
                    if i[1]==n:
                        bluenodedifflist.append(n)
            for n in rednodegroup:
                for i in nodedifflist:
                    if i[1]==n:
                        rednodedifflist.append(n)
            for n in greennodegroup:
                for i in nodedifflist:
                    if i[1]==n:
                        greennodedifflist.append(n)
            for n in purplenodegroup:
                for i in nodedifflist:
                    if i[1]==n:
                        purplenodedifflist.append(n)
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
                for i in range(0, 16, 1):
                    for n in range(0, 16, 1):
                        if (65+(i*50))<416 and (65+(n*50))<416:
                            if nodelist0[(n+(i*16))]==1:
                                screen.blit(bluenodeon, (nodecoordinates[n+(i*16)][0]-15, nodecoordinates[n+(i*16)][1]-15))
                            elif nodelist0[(n+(i*16))]==0:
                                screen.blit(bluenodeoff, (nodecoordinates[n+(i*16)][0]-15, nodecoordinates[n+(i*16)][1]-15))
                        elif (65+(i*50))>416 and (65+(n*50))<416:
                            if nodelist0[(n+(i*16))]==1:
                                screen.blit(greennodeon, (nodecoordinates[n+(i*16)][0]-15, nodecoordinates[n+(i*16)][1]-15))
                            elif nodelist0[(n+(i*16))]==0:
                                screen.blit(greennodeoff, (nodecoordinates[n+(i*16)][0]-15, nodecoordinates[n+(i*16)][1]-15))
                        elif (65+(i*50))<416 and (65+(n*50))>416:
                            if nodelist0[(n+(i*16))]==1:
                                screen.blit(rednodeon, (nodecoordinates[n+(i*16)][0]-15, nodecoordinates[n+(i*16)][1]-15))
                            elif nodelist0[(n+(i*16))]==0:
                                screen.blit(rednodeoff, (nodecoordinates[n+(i*16)][0]-15, nodecoordinates[n+(i*16)][1]-15))
                        elif (65+(i*50))>416 and (65+(n*50))>416:
                            if nodelist0[(n+(i*16))]==1:
                                screen.blit(purplenodeon, (nodecoordinates[n+(i*16)][0]-15, nodecoordinates[n+(i*16)][1]-15))
                            elif nodelist0[(n+(i*16))]==0:
                                screen.blit(purplenodeoff, (nodecoordinates[n+(i*16)][0]-15, nodecoordinates[n+(i*16)][1]-15))
                if n6%4==0:
                    changenodes(bluenodedifflist)
                    print(bluenodedifflist)
                if n6%4==1:
                    changenodes(greennodedifflist)
                    print(greennodedifflist)
                if n6%4==2:
                    changenodes(rednodedifflist)
                    print(rednodedifflist)
                if n6%4==3:
                    changenodes(purplenodedifflist)
                    print(purplenodedifflist)
                print(n6)
    startloopnum=startloopnum+1
    
    #Continuously update the screen
    pygame.display.update()
