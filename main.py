# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # create groups of objects (just names for now)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    # put those groups into containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,) #note the comma, making this a tuple
    
    # create objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

        
    
    game_on = True
    while game_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False
        # Fill the screen with black
        screen.fill("black")
        
        # Draw the player
        for i in drawable:
            i.draw(screen)
        
        # update the things that need updating
        updatable.update(dt)

        # check for collisions
        for asteroid in asteroids:
            if asteroid.collision_check(player) == False:
                print("Game over!")
                game_on = False
        
        # Update the display
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    
    pygame.quit()

if __name__ == "__main__":
    main()