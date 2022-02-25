from interfaces import Sprite, Collidable
from geometry import *
import pygame
import math


class Paddle(Collidable, Sprite):
    def __init__(self, rect, color, speed):
        self.__rect = rect
        self.__speed = Point(speed, 0)
        self.__color = color
        self.__environment = None
        self.hits =0

    def setGameEnvironment(self, environment):
        self.__environment = environment

    def removeFromGame(self, gameLevel):
        gameLevel.removeSprite(self)
        gameLevel.removeCollidable(self)

    def getCollisionRectangle(self):
        return self.__rect

    def hit(self, hitter, collisionPoint, currentVelocity):
        currentDx = currentVelocity.getDX()
        currentDy = currentVelocity.getDY()
        newV = currentVelocity
        lines = self.__rect.lineList()
        for line in lines:
            if line.isInLine(collisionPoint):
                index = lines.index(line)
                if index % 2 == 1:
                    newV = Velocity(currentDx * -1, currentDy)
                else:
                    self.hits+=1
                    hitRegion = self.__hitRegion(collisionPoint)
                    ballSpeed = math.sqrt(currentDx ** 2 + currentDy ** 2)
                    regions = range(0, 181, 180 // 5)
                    angle = regions[hitRegion]+270
                    newV = Velocity.fromAngleAndSpeed(angle, ballSpeed)
        return newV

    def __hitRegion(self, hitPoint):
        x = hitPoint.getX()
        width = self.__rect.getWidth() / 5
        for i in range(6, -1, -1):
            border = self.__rect.getUpperLeft().getX() + (i * width)
            if x > border:
                return i
        return -1

    def drawOn(self, win):
        p = self.__rect.getUpperLeft().getPoint()
        width = self.__rect.getWidth()
        height = self.__rect.getHeight()
        pygame.draw.rect(win, self.__color, (p[0], p[1], width, height))
        pygame.draw.rect(win, (0, 0, 0), (p[0], p[1], width, height), 1)

    def timePassed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.__moveLeft()
        if keys[pygame.K_RIGHT]:
            self.__moveRight()

    def __moveLeft(self):
        movement = self.__speed * -1
        newPoint = self.__rect.getUpperLeft() + movement
        if newPoint.getX() <= 20:
            newPoint = Point(20, newPoint.getY())
        self.__rect = Rectangle(newPoint, self.__rect.getWidth(), self.__rect.getHeight())

    def __moveRight(self):
        newPoint = self.__rect.getUpperLeft() + self.__speed
        if newPoint.getX() >= 780 - self.__rect.getWidth():
            newPoint = Point(779 - self.__rect.getWidth(), newPoint.getY())
        self.__rect = Rectangle(newPoint, self.__rect.getWidth(), self.__rect.getHeight())

    def addToGame(self, gameLevel):
        gameLevel.addCollidable(self)
        gameLevel.addSprite(self)

    def AIController(self, left=True):
        if left:
            self.__moveLeft()
        else:
            self.__moveRight()
