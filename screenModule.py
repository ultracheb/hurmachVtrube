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
    screen = pygame.display.set_mode([1000, 500])

    def __init__(self):
        self.simulation = Simulation()
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


    def collisionWithPlayer(self):
        blocks_hit_list = pygame.sprite.spritecollide(self.player, self.simulation.fluid_list, True)

        # Check the list of collisions.
        for fluid in blocks_hit_list:
            self.score += 1
            print(self.score)