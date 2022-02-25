class Sprite:
    def drawOn(self, win):
        pass

    def timePassed(self):
        pass


class Collidable:
    def getCollisionRectangle(self):
        pass

    def hit(self, hitter, collisionPoint, currentVelocity):
        pass


class HitListener:
    def hitEvent(self, beingHit, hitter):
        pass


class HitNotifier:
    def addHitListener(self, hl):
        pass

    def removeHitListener(self, hl):
        pass


class Animation:
    def doOneFrame(self, win):
        pass

    def shouldStop(self):
        pass


class LevelInformation:
    def numberOfBalls(self):
        pass

    def initialBallVelocities(self):
        pass

    def paddleSpeed(self):
        pass

    def paddleWidth(self):
        pass

    def levelName(self):
        pass

    def getBackground(self):
        pass

    def blocks(self):
        pass

    def numberOfBlocksToRemove(self):
        pass
