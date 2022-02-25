from interfaces import Sprite
from geometry import Rectangle, Point
from utils import *
import pygame


class SpriteCollection:
    def __init__(self):
        self.__sprites = []

    def addSprite(self, s):
        self.__sprites.append(s)

    def notifyAllTimePassed(self):
        for s in self.__sprites:
            s.timePassed()

    def drawAllOn(self, win):
        for s in self.__sprites:
            s.drawOn(win)

    def getSprites(self):
        return self.__sprites


class LevelIndicator(Sprite):
    def __init__(self, rect, color, levelInfo):
        self.__rect = rect
        self.__color = color
        self.__levelInfo = levelInfo
        self.__font = pygame.font.SysFont("comicsans", 20)

    def drawOn(self, win):
        p = self.__rect.getUpperLeft().getPoint()
        width = self.__rect.getWidth()
        height = self.__rect.getHeight()
        pygame.draw.rect(win, self.__color, (p, width, height))
        level_name = "Level name : " + self.__levelInfo.levelName()
        level_name_box = self.__font.render(level_name, 1, (0, 0, 0))
        win.blit(level_name_box,
                 ((p[0] + (width + level_name_box.get_width()) / 2), p[1] + height - level_name_box.get_height() + 5,
                  10))

    def timePassed(self):
        pass

    def dToGame(self, gameLevel):
        gameLevel.addSprite(self)


class ScoreIndicator(Sprite):
    def __init__(self, rect, color, counter):
        self.__rect = rect
        self.__color = color
        self.__counter = counter
        self.__font = pygame.font.SysFont("comicsans", 20)

    def drawOn(self, win):
        p = self.__rect.getUpperLeft().getPoint()
        width = self.__rect.getWidth()
        height = self.__rect.getHeight()
        pygame.draw.rect(win, self.__color, (p[0],p[1], width, height))
        score_text = "Score : " + str(self.__counter.getValue())
        score_box = self.__font.render(score_text, 1, (0, 0, 0))
        win.blit(score_box,
                 ((p[0] + (width + score_box.get_width()) / 2), p[1] + height - score_box.get_height() + 5))

    def timePassed(self):
        pass

    def dToGame(self, gameLevel):
        gameLevel.addSprite(self)


class LivesIndicator(Sprite):
    def __init__(self, rect, color, counter):
        self.__rect = rect
        self.__color = color
        self.__counter = counter
        self.__font = pygame.font.SysFont("comicsans", 20)

    def drawOn(self, win):
        p = self.__rect.getUpperLeft().getPoint()
        width = self.__rect.getWidth()
        height = self.__rect.getHeight()
        pygame.draw.rect(win, self.__color, (p, width, height))
        lives_text = "Lives : " + str(self.__counter.getValue())
        lives_box = self.__font.render(lives_text, 1, (0, 0, 0))
        win.blit(lives_box,
                 ((p[0] + (width + lives_box.get_width()) / 2), p[1] + height - lives_box.get_height() + 5,
                  10))

    def timePassed(self):
        pass

    def dToGame(self, gameLevel):
        gameLevel.addSprite(self)
