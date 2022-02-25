from interfaces import *
from geometry import *
from utils import *
import pygame


class Block(Collidable, Sprite, HitNotifier):
    def __init__(self, rect, color, num):
        self.__rect = rect
        self.__color = color
        self.__hit_listeners = []
        self.__id = num
        self.hits = 0

    def hit(self, hitter, collisionPoint, currentVelocity):
        self.__notifyHit(hitter)
        self.hits += 1
        currentDx = currentVelocity.getDX()
        currentDy = currentVelocity.getDY()
        lines = self.__rect.lineList()
        for line in lines:
            if line.isInLine(collisionPoint):
                if lines.index(line) % 2 == 0:
                    currentDy *= -1
                else:
                    currentDx *= -1
        return Velocity(currentDx, currentDy)

    def getCollisionRectangle(self):
        return self.__rect

    def __notifyHit(self, hitter):
        for listener in self.__hit_listeners:
            listener.hitEvent(self, hitter)

    def drawOn(self, win):
        p = self.__rect.getUpperLeft().getPoint()
        width = self.__rect.getWidth()
        height = self.__rect.getHeight()
        pygame.draw.rect(win, self.__color, (p[0], p[1], width, height))
        pygame.draw.rect(win, (0, 0, 0), (p[0], p[1], width, height), 1)

    def timePassed(self):
        pass

    def addToGame(self, game):
        game.addSprite(self)
        game.addCollidable(self)

    def removeFromGame(self, game):
        game.removeSprite(self)
        game.removeCollidable(self)
        x = game.blocks[self.__id][0]
        game.blocks[self.__id] = (x, 0)

    def addHitListener(self, hl):
        self.__hit_listeners.append(hl)

    def removeHitListener(self, hl):
        self.__hit_listeners.remove(hl)
