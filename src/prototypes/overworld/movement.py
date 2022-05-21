from turtle import width
import pygame, sys
from prototypes.overworld.game import Camera
from prototypes.overworld.entity import Npc, Player

pygame.init()

# Window initialization
# TODO: make settings in file / allow for changes with dev tools
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
npc = Npc()
camera = Camera()

# initialize start position
player.rect.x = 320
player.rect.y = 180

npc.rect.x = 200
npc.rect.y = 50

npc.image.fill((0, 255, 0))

sprites.add(player)
sprites.add(npc)

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

    # debug
    #print("playerX=", player.rect.x)
    #print("playerY=", player.rect.y)
    
    player.detectCollision([WIDTH, HEIGHT])
    sprites.update()
    window.fill(BG_COLOR)

    # update camera
    '''
    camera.move_camera(player.rect.x, player.rect.y, window)
    player.rect.x -= camera.x
    player.rect.y -= camera.y
    camera.reset()
    '''

    sprites.draw(window)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()