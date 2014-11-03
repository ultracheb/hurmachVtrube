import pygame
import constants
import playerModule
from simulationModule import Simulation

__author__ = 'Vladislove'

class Screen:

    score = 0
    simulation = 0
    clock = 0
    screen = pygame.display.set_mode([1000, 500])
    player = 0

    def __init__(self):
        self.simulation = Simulation()
        self.simulation.generate(100)
        self.player = playerModule.Player(constants.RED, 20, 15)
        self.simulation.addSprite(self.player)
        self.clock = pygame.time.Clock()

    def redraw(self, fps):
        self.screen.fill(constants.BLACK)
        self.simulation.draw()
        blocks_hit_list = pygame.sprite.spritecollide(self.player, self.simulation.fluid_list, True)

        # Check the list of collisions.
        for fluid in blocks_hit_list:
            self.score += 1
            print(self.score)

        self.simulation.all_sprites_list.draw(self.screen)
        # Limit to 60 frames per second
        self.clock.tick(fps)