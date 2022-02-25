import pygame
from Game import Game
import os
import neat
import numpy as np
import sys

pygame.init()


def main():
    game = Game(800, 600)
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        game.loop()


def train_ai(genome, config, game):
    run = True
    net = neat.nn.FeedForwardNetwork.create(genome, config)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        game_inputs = game.get_inputs()
        p = game_inputs['paddle']
        balls = game_inputs['balls']
        blocks = game_inputs['blocks']
        v = balls[0].getVelocity()
        po = balls[0].getCenter().getPoint()
        inputs = [
            p.getCollisionRectangle().getWidth(), p.getCollisionRectangle().getUpperLeft().getX(),
            balls[0].getCenter().getX(), po[0], po[1], v.getDY()]
        for block in blocks:
            inputs.extend(block)
        output = net.activate(inputs)
        decision = output.index(max(output))
        if decision != 0:
            p.AIController(True if decision == 1 else False)
        game_info = game.loop()
        pygame.display.update()
        if game_info.balls == 0 or game_info.blocks == 0 or p.hits > 50:
            genome.fitness += game_info.score
            if game_info.blocks == 0:
                genome.fitness += 100
            break


def eval_genomes(genomes, config):
    width, height = 800, 600
    for i, (genome_id, genome) in enumerate(genomes):
        genome.fitness = 0
        game = Game(width, height)
        train_ai(genome, config, game)


def run_neat(config):
    if len(sys) > 1:
        check_point = sys[1]
    else:
        check_point = -1
    check_point_file = 'neat-checkpoint-' + str(check_point)
    if os.path.isfile(check_point_file):
        p = neat.Checkpointer.restore_checkpoint(check_point_file)
    else:
        p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))
    winner = p.run(eval_genomes, 100)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    run_neat(config)
