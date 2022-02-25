from interfaces import HitListener


class BallRemover(HitListener):
    def __init__(self, game, counter):
        self.__game = game
        self.__counter = counter

    def hitEvent(self, beingHit, hitter):
        hitter.removeFromGame(self.__game)
        self.__counter.decrease(1)


class BlockRemover(HitListener):
    def __init__(self, game, counter):
        self.__game = game
        self.__counter = counter

    def hitEvent(self, beingHit, hitter):
        beingHit.removeFromGame(self.__game)
        beingHit.removeHitListener(self)
        self.__counter.decrease(1)


class ScoreTrackingListener(HitListener):
    def __init__(self, counter):
        self.__counter = counter

    def hitEvent(self, beingHit, hitter):
        self.__counter.increase(5)
