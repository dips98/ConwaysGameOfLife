import pygame
import time
import random
from objects import *

height=1000
width=1000                                          #default height and Width of screen
pygame.init()
screen=pygame.display.set_mode((height,width))
cellSize=20                                         #default Cell Size 
g=grid(cellSize,height,width,screen)                #making Grid with cellSize, Width and Height
mouseX, mouseY = pygame.mouse.get_pos()
global drawing,Genrations                           
drawing=True
Genrations=0

def drawAgain():                                    #udating Graphics On Screen
    for row in g.listOfCells:
        for cell in row:
            cell.update()                           #updating Each Cell In Grid
    pygame.display.flip()
def makeRandomPattern(listOfCells):                 #function To Genrate Random Grid Pattern 
    for i in range(len(listOfCells)):
        for j in range(len(listOfCells)):
            if random.randint(0,100)%2==0:
                listOfCells[i][j].isAlive=True
                listOfCells[i][j].update()
                pygame.display.flip()

def up_Date():                                      #updating Calculation
    global drawing,Genrations
    revent =pygame.event.get()
    for e in revent:
        if e.type== pygame.MOUSEBUTTONDOWN and drawing:
            x, y = pygame.mouse.get_pos()
            g.listOfCells[x//cellSize][y//cellSize].isAlive=not g.listOfCells[x//cellSize][y//cellSize].isAlive
                                                    #making Cell ALive On Selected Position
        if e.type== pygame.KEYDOWN :
            CurrentEvent=e
            if CurrentEvent.key==pygame.K_SPACE:
                drawing=not drawing
            if CurrentEvent.key==pygame.K_r:
                makeRandomPattern(g.listOfCells)
    if(not drawing):
        for row in g.listOfCells:                   #calulating For Each Cell In the Grid
            for cell in row:
                cell.canThisCellBorn(g.listOfCells)
        for row in g.listOfCells:                   #setting Next Genration
            for cell in row:
                cell.updateGenration()
        Genrations=Genrations+1   
        print("Genration :",Genrations)
        pygame.event.get() 
            

while True:                                         #running Whole Program In loop
    event=pygame.event.get() 
    drawAgain()                                     #drawing 
    up_Date()                                       #updating Calculations
    if not drawing:
        time.sleep(0.1)                             #waiting for time interval
