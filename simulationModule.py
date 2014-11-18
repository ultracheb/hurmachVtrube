import pygame
import fluidModule
import constants

__author__ = 'Vladislove'

class Simulation:

    screen_width = 0
    screen_height = 0
    Limit = 100
    Number = 0
    N = 0
    Nt = 0
    koef = 0

    fluid_list = pygame.sprite.Group()
    all_sprites_list = pygame.sprite.Group()
    new_sprites_list = pygame.sprite.Group()


    def __init__(self, width, height):
        self.screen_width = width
        self.screen_height = height

    def generate(self):
        # for i in range(number):
            # This represents a block
        self.Number += 1
        fluid = fluidModule.Fluid(constants.WHITE, 1, 1)

        # Set a random location for the block
        fluid.set_pos(self.screen_height)
        fluid.set_boundary(0, 0, self.screen_width, self.screen_height)

        # Add the block to the list of objects
        self.fluid_list.add(fluid)
        self.all_sprites_list.add(fluid)

    def draw(self):
        self.new_sprites_list.empty()
        for fluid in self.all_sprites_list:
            flyout = fluid.update()
            if flyout is not None and flyout[0]:
                self.new_sprites_list.add(fluid)
                self.N += 1
                if flyout[1]:
                    self.Nt += 1

        for fluid in self.new_sprites_list:
            self.all_sprites_list.remove(fluid)
            self.Number -= 1

        if self.N is not 0:
            self.koef = self.Nt / self.N

        if self.Number < self.Limit:
            self.generate()

        # self.all_sprites_list.update()

    def addSprite(self, fluid):
        self.all_sprites_list.add(fluid)