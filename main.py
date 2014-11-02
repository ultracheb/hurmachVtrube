import pygame
import blockModule
import playerModule
import constants

# Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 1200
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
# fluid_list = pygame.sprite.Group()

# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

for i in range(100):
    # This represents a block
    fluid = blockModule.Fluid(constants.WHITE, 1, 1)

    # Set a random location for the block
    fluid.setPos(screen_width, screen_height)
    fluid.setChange(-3, 4, -3, 4)
    fluid.setBoundary(0, 0, screen_width, screen_height)

    # Add the block to the list of objects
    # fluid_list.add(fluid)
    all_sprites_list.add(fluid)

# Create a red player block
player = playerModule.Player(constants.RED, 20, 15)
all_sprites_list.add(player)

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # Clear the screen
    screen.fill(constants.BLACK)

    # Calls update() method on every sprite in the list
    all_sprites_list.update()

    # See if the player block has collided with anything.
    # blocks_hit_list = pygame.sprite.spritecollide(player, fluid_list, True)
    #
    # # Check the list of collisions.
    # for fluid in blocks_hit_list:
    #     score +=1
    #     print(score)

    # Draw all the spites
    all_sprites_list.draw(screen)

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()