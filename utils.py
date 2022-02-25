class Counter:
    def __init__(self, value=0):
        self.__value = value

    def increase(self, num):
        self.__value += num

    def decrease(self, num):
        self.__value -= num

    def getValue(self):
        return self.__value


class Colors:
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)
    GRAY = (128, 128, 128)
    darkGray = (64, 64, 64)
    GREEN=(0,255,0)
    PINK=(255, 175, 175)


class CollisionInfo:
    def __init__(self, point, collideAble):
        self.__point = point
        self.__collideAble = collideAble

    def collisionPoint(self):
        return self.__point

    def collisionObject(self):
        return self.__collideAble


class GameEnvironment:
    def __init__(self):
        self.__collideAbles = []

    def addCollidable(self, c):
        self.__collideAbles.append(c)

    def getClosestCollision(self, trajectory):
        closestCollision = None
        closestPoint = None
        for c in self.__collideAbles:
            point = trajectory.closestIntersectionToStartOfLine(c.getCollisionRectangle())
            if point is not None:
                if closestCollision is None:
                    closestCollision = c
                    closestPoint = point
                elif point - trajectory.start() < closestPoint - trajectory.start():
                    closestCollision = c
                    closestPoint = point
        if closestCollision is None:
            return None
        return CollisionInfo(closestPoint, closestCollision)

    def getCollideables(self):
        return self.__collideAbles
