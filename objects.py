import pygame
import time
import random

class cell:
    def __init__(self, screen, x1, y1, cellSize, RowNum, ColumnNum):
        self.x1 = x1
        self.y1 = y1
        self.cellSize = cellSize                                                               #x1,x2,y1,y2 Are the points used Draw A Rectriangle 
        self.screen = screen
        self.RowNum = RowNum                                      
        self.ColumnNum = ColumnNum                                                             #row And Column Number Of This Cell In Grid
        self.isAlive = False                                                                   #is Cell Alive For This Genration
        self.willSurviveNextGen = False                                                        #can This Cell Survive In Next Genration
        self.aliveNeighbour = 0
        self.Color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  #setting A Random Color To This Cell
                                                                                                        
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x1, self.y1, self.cellSize, self.cellSize))
        pygame.draw.rect(self.screen, (0, 128, 128), (self.x1 + 2, self.y1 + 2, self.cellSize - 2, self.cellSize - 2))
        super().__init__()
    def update(self):                                                                          #if Cell Is Alive Then Draw Cell WIth Its Own Color, Else Draw A Cell With Black Color
        if self.isAlive:
            pygame.draw.rect(self.screen, (0, 0, 0),(self.x1, self.y1, self.cellSize, self.cellSize))
            pygame.draw.rect(self.screen, self.Color, (self.x1 + 2, self.y1 + 2, self.cellSize - 2, self.cellSize - 2))
        else:
            pygame.draw.rect(self.screen, (0, 0, 0),(self.x1, self.y1, self.cellSize, self.cellSize))
            pygame.draw.rect(self.screen, (0, 0, 0),(self.x1 + 2, self.y1 + 2, self.cellSize - 2, self.cellSize - 2))

    def countNeighboure(self, listOfCells):                                                    #count Alive Neighbours Of This Cell
        numberOfNeighBoure = 0
        currentCell = listOfCells[self.RowNum][self.ColumnNum]
        try:
            for i in range(-1, 2):
                for j in range(-1, 2):
                        if listOfCells[self.RowNum + i][self.ColumnNum + j].isAlive == True:
                            numberOfNeighBoure = numberOfNeighBoure + 1
            if self.isAlive:
                numberOfNeighBoure = numberOfNeighBoure - 1
        except :
            pass
        self.aliveNeighbour = numberOfNeighBoure

    def canThisCellBorn(self, listOfCells):                                                    #checking If The Cell Can Survie Next Gen
        self.countNeighboure(listOfCells)
        if (not self.isAlive) and self.aliveNeighbour == 3:
            self.willSurviveNextGen=True
        elif self.isAlive and (self.aliveNeighbour < 2 or self.aliveNeighbour > 3):
            self.willSurviveNextGen = False
        else:
            self.willSurviveNextGen = self.isAlive

    def updateGenration(self):                                                                 #updating Genration
        self.isAlive = self.willSurviveNextGen
            
       
       

class grid:
    listOfCells = []
    def __init__(self, cellSize, Height, Width, screen):            
        self.cellSize = cellSize
        self.Height = Height
        self.Width = Width
        self.screen = screen
        x = 0
        y = 0
        for i in range(0, self.Width // self.cellSize):
            newRow = []
            for j in range(0, self.Height // self.cellSize):
                listcell = cell(self.screen, i*cellSize, j*cellSize, self.cellSize, i, j)
                newRow.append(listcell)
                pygame.event.get() 
            self.listOfCells.append(newRow)
        
        


