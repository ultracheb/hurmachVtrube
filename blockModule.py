import random

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

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

    def setPos(self, rangeX, rangeY):
        self.rect.x = random.randrange(rangeX)
        self.rect.y = random.randrange(rangeY)

    def setChange(self, rangeXdown, rangeXup, rangeYdown, rangeYup):
        self.change_x = random.randrange(rangeXdown, rangeXup)
        self.change_y = random.randrange(rangeYdown, rangeYup)

    def setBoundary(self, leftBoun, topBoun, rightBoun, downBow):
        self.left_boundary = leftBoun
        self.top_boundary = topBoun
        self.right_boundary = rightBoun
        self.bottom_boundary = downBow


    def update(self):
        """ Called each frame. """
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
            self.change_x *= -1

        if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.change_y *= -1
