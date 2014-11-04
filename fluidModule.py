import random
import math

__author__ = 'Vladislove'

import pygame

class Fluid(pygame.sprite.Sprite):
    """
    This class represents the ball
    It derives from the "Sprite" class in Pygame
    """

    left_boundary = 0
    right_boundary = 0
    top_boundary = 0
    bottom_boundary = 0
    change_x = 0
    change_y = 0

    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its x and y position. """
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.setfirstmovemant()

    def setPos(self, rangeX, rangeY):
        self.rect.x = random.randrange(rangeX)
        self.rect.y = random.randrange(rangeY)

    def randfloat(self):
        return random.randrange(0, 1000) / 1000

    def setfirstmovemant(self):
        l = math.sqrt(self.randfloat())
        sin0 = math.sqrt(1 - l*l)
        phi = 2 * math.pi * self.randfloat()
        m = sin0 * math.cos(phi)

        self.change_x = l*10
        self.change_y = m*10

    def setmovement(self):
        l = math.sqrt(self.randfloat())
        sin0 = math.sqrt(1 - l*l)
        phi = 2 * math.pi * self.randfloat()
        m = sin0 * math.cos(phi)

        self.change_x = m*10
        self.change_y = l*10


    def setBoundary(self, leftBoun, topBoun, rightBoun, downBow):
        self.left_boundary = leftBoun
        self.top_boundary = topBoun
        self.right_boundary = rightBoun
        self.bottom_boundary = downBow


    def update(self):
        """ Called each frame. """
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.right >= self.right_boundary:
            self.change_x *= -1
            return True, True

        if self.rect.left <= self.left_boundary:
            self.change_x *= -1
            return True, False

        if self.rect.bottom >= self.bottom_boundary:
            self.setmovement()
            self.change_y *= -1
            return False, False

        if self.rect.top <= self.top_boundary:
            self.setmovement()
            return False, False


        return False, False
