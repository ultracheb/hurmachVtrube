import random
import math

__author__ = 'Vladislove'

import pygame


def rand_float():
    return random.randrange(0, 1000) / 1000


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
        self.set_first_movement()

    def set_pos(self, range_y):
        self.rect.x = random.randrange(1, 2)
        self.rect.y = random.randrange(range_y)


    def set_first_movement(self):
        alpha = random.randrange(1, 179)
        alpha = math.radians(alpha)
        x = 10 * math.sin(alpha)
        y = 10 * math.cos(alpha)

        self.change_x = x
        self.change_y = y

    def set_movement(self):
        alpha = random.randrange(1, 179)
        alpha = math.radians(alpha)
        y = 10 * math.sin(alpha)
        x = 10 * math.cos(alpha)

        self.change_x = x
        self.change_y = y


    def set_boundary(self, leftBoun, topBoun, rightBoun, downBow):
        self.left_boundary = leftBoun
        self.top_boundary = topBoun
        self.right_boundary = rightBoun
        self.bottom_boundary = downBow


    def update(self):
        """ Called each frame. """
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.right >= self.right_boundary:
            return True, True

        if self.rect.left <= self.left_boundary:
            return True, False

        if self.rect.bottom >= self.bottom_boundary:
            self.set_movement()
            self.change_y *= -1
            return False, False

        if self.rect.top <= self.top_boundary:
            self.set_movement()
            return False, False

        return False, False
