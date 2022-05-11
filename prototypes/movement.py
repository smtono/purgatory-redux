import pygame
import player
from prototypes.player import Player

pygame.init()

# Window initialization
game_running = True
WIDTH = 640
HEIGHT = 360
BG_COLOR = (0, 0, 0)

window = pygame.display.set_mode((WIDTH, HEIGHT)) # game window initialization
clock = pygame.time.Clock()

# Sprite management
sprites = pygame.sprite.Group()
player = Player()

sprites.add(player)

while (game_running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            game_running = False
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.move_left(10)
            if keys[pygame.K_RIGHT]:
                player.move_right(10)
            if keys[pygame.K_DOWN]:
                player.move_down(10)
            if keys[pygame.K_UP]:
                player.move_up(10)
    
    sprites.update()
    window.fill(BG_COLOR)
    sprites.draw(window)
    # pygame.display.flip()
    clock.tick(60)

pygame.quit()