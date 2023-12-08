import pygame
from vector import Vector2
from constants import *
import numpy as np


class Node(object):
    def __init__(self, x, y):
        self.position = Vector2(x,y)
        self.neighbors = {UP: None, DOWN: None, LEFT: None, RIGHT:None }


    def render(self, screen):
        for n in self.neighbors.keys():
            if self.neighbors[n] is not None:
                line_start = self.position.asTuple()
                line_end = self.neighbors[n].position.asTuple()
                pygame.draw.line(screen, WHITE, line_start, line_end, 4)
                pygame.draw.circle(screen, RED, self.position.asInt(), 12)


class NodeGroup(object):
    def __init__(self):
        self.level = level
        self.nodesLUT = {}
        self.nodeSymbols = ['+']
        self.pathSymbols = ['.']
        data = self.readMazeFile(level)
        self.createNodeTable(data)
        self.connectHorizontally(data)
        self.connectVertically(data)
            
    def render(self, screen):
        for node in self.nodeList:
            node.render(screen)
    
    def readMazeFile(self, textfile):
        return np.loadtxt(txtfile, dtype='<U1')

    def createNodeTable(self, data, xoffset=0, yoffset=0):
        for row in list(range(data.shape[0])):
            for col in list(range(data.shape[1])):
                if data[row][col] in self.nodeSymbols:
                    x, y = self.constructKey(col+xoffset, row+yoffset)
                    self.nodesLUT[(x,y)] = Node(x, y)

    def constructKey(self, x, y):
        return x* TILEWIDTH, y*TILEHEIGHT
