from circleshape import CircleShape
from constants import *
from shot import Shot
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.shot_group = []

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, shot_group):
        if self.shot_timer > 0:
            return
        else:
            # Create a directional vector pointing in the direction the player is facing
            shot_direction = pygame.Vector2(0, 1).rotate(self.rotation)
            # Scale it by the shot speed
            shot_velocity = shot_direction * PLAYER_SHOOT_SPEED
            # Create the new shot at the player's position with the calculated velocity
            new_shot = Shot(self.position.x, self.position.y, shot_velocity)
            # Add the new shot to the shot_group
            shot_group.add(new_shot)
            # Reset the shot timer
            self.shot_timer = PLAYER_SHOOT_COOLDOWN

    
    def update(self, dt, shot_group):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)  
        if keys[pygame.K_SPACE]:
            self.shoot(shot_group)
        if self.shot_timer > 0:
            self.shot_timer -= dt