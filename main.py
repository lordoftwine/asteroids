# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    game_on = True
    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
        # Fill the screen with black
        screen.fill("black")
        
        # Draw the player
        player.draw(screen)
        player.update(dt)
        
        # Update the display
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    
    pygame.quit()

if __name__ == "__main__":
    main()