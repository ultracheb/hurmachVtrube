import pygame
import blockModule
import constants

__author__ = 'Vladislove'

class Simulation:

    screen_width = 0
    screen_height = 0

    fluid_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()


    def __init__(self):
        self.screen_width = 500
        self.screen_height = 300

    def generate(self, number):

        for i in range(number):
            # This represents a block
            fluid = blockModule.Fluid(constants.WHITE, 1, 1)

            # Set a random location for the block
            fluid.setPos(self.screen_width, self.screen_height)
            fluid.setChange(-3, 4, -3, 4)
            fluid.setBoundary(0, 0, self.screen_width, self.screen_height)

            # Add the block to the list of objects
            self.fluid_list.add(fluid)
            self.all_sprites_list.add(fluid)

    def draw(self):
        self.all_sprites_list.update()

    def addSprite(self, fluid):
        self.all_sprites_list.add(fluid)