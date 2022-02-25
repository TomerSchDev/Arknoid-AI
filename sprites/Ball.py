from interfaces import Sprite
from geometry import *
from utils import *
import math
import pygame


class Ball(Sprite):
    def __init__(self, center, radius, color, game):
        self.__center = center
        self.__r = radius
        self.__color = color
        self.__velocity = Velocity()
        self.__environment = None
        self.__game = game

    def getX(self):
        return math.round(self.__center.getX())

    def getY(self):
        return math.round(self.__center.getY())

    def getSize(self):
        return self.__r

    def getColor(self):
        return self.__color

    def getCenter(self):
        return self.__center

    def getVelocity(self):
        return self.__velocity

    def drawOn(self, win):
        if win is None:
            return
        pygame.draw.circle(win, self.__color, (self.__center.getPoint()), self.__r)
        pygame.draw.circle(win, (0, 0, 0), (self.__center.getPoint()), self.__r, 1)

    def timePassed(self):
        if (20 >= self.__center.getPoint()[0] or self.__center.getPoint()[0] >= 780) or (
                20 >= self.__center.getPoint()[1] or self.__center.getPoint()[1] >= 600):
            self.removeFromGame(self.__game)
            self.__game.ball_out()
        nextPoint = self.getVelocity().applyToPoint(self.__center)
        dx = self.getVelocity().getDX()
        dy = self.getVelocity().getDY()
        advanceX = abs(dx) / dx if dx != 0 else 0
        advanceY = abs(dy) / dy if dy != 0 else 0;
        nextPoint2 = Point(nextPoint.getX() + (advanceX * self.__r), nextPoint.getY() + (advanceY * self.__r))
        trajectory = Line(self.__center, nextPoint2)
        if self.__environment is None:
            self.__center = self.__velocity.applyToPoint(self.__center)
            return
        collisionInfo = self.__environment.getClosestCollision(trajectory)
        if collisionInfo is not None:
            self.__velocity = collisionInfo.collisionObject().hit(self, collisionInfo.collisionPoint(), self.__velocity)
            advanceX = 1
            advanceY = 1
            if collisionInfo.collisionPoint().getX() > self.__center.getX():
                advanceX = -1
            if collisionInfo.collisionPoint().getY() > self.__center.getY():
                advanceY = -1;
            x = collisionInfo.collisionPoint().getX() + (advanceX * self.__r)
            y = collisionInfo.collisionPoint().getY() + (advanceY * self.__r)
            nextPoint = Point(x, y)
        if abs(self.__velocity.getDY()) <= 0.2:
            self.__velocity = Velocity(self.__velocity.getDX(), 1)
        self.__center = nextPoint

    def setVelocity(self, v):
        self.__velocity = v

    def getGameEnvironment(self):
        return self.__environment

    def setGameEnvironment(self, gameEnvironment):
        self.__environment = gameEnvironment

    def addToGame(self, gameLevel):
        gameLevel.addSprite(self)
        self.__environment = gameLevel.getEnvironment()

    def removeFromGame(self, gameLevel):
        gameLevel.removeSprite(self)
