import pygame, sys
from prototypes.overworld.game import Camera
from prototypes.overworld.entity import Player

pygame.init()

# Window initialization
game_running = True
FPS = 60
WIDTH = 640
HEIGHT = 360
BG_COLOR = (0, 0, 0)

window = pygame.display.set_mode((WIDTH, HEIGHT)) # game window initialization
pygame.display.set_caption("Move Prototype")

clock = pygame.time.Clock()

# Sprite management
sprites = pygame.sprite.Group()
player = Player()
camera = Camera()

# initialize start position
player.rect.x = 320
player.rect.y = 180

sprites.add(player)

while (game_running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            game_running = False
            exit()
        #elif event.type == pygame.KEYDOWN:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            #print("left")
            player.move_left(5)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            #print("right")
            player.move_right(5)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            #print("down")
            player.move_down(5)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            #print("up")
            player.move_up(5)
    
    sprites.update()
    window.fill(BG_COLOR)

    # update camera
    camera.move_camera(player.rect.x, player.rect.y, window)
    player.rect.x -= camera.x
    player.rect.y -= camera.y
    camera.reset()

    sprites.draw(window)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()