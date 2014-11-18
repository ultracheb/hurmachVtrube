import pygame
import constants
import playerModule
from simulationModule import Simulation

__author__ = 'Vladislove'

class Screen:

    score = 0
    simulation = 0
    clock = 0
    player = 0
    screen_x = 300
    screen_y = 600
    screen = pygame.display.set_mode([screen_x, screen_y])

    def __init__(self):
        self.simulation = Simulation(self.screen_x, self.screen_y)
        self.simulation.generate()
        self.player = playerModule.Player(constants.RED, 20, 15)
        self.simulation.addSprite(self.player)
        self.clock = pygame.time.Clock()

    def redraw(self, fps):
        self.screen.fill(constants.BLACK)
        self.simulation.draw()
        # self.collisionWithPlayer()
        self.simulation.all_sprites_list.draw(self.screen)
        self.drawtext()
        # Limit to 60 frames per second
        self.clock.tick(fps)

    def drawtext(self):
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render(str(self.simulation.koef), 1, (255,255,0))
        self.screen.blit(label, (100, 50))

