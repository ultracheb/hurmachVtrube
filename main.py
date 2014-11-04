import pygame
from screenModule import Screen

pygame.init()
screen = Screen()
done = False

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # Limit to 60 frames per second
    screen.redraw(60)
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()