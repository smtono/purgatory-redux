from turtle import width
import pygame, sys
from prototypes.overworld.game import Camera, Direction
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

# Sprite groups
sprites = pygame.sprite.Group()
npcs = pygame.sprite.Group()

# sprites
player = Player()
npc1 = Npc()
npc2 = Npc()

# other game initializations
camera = Camera()

# initialize start position of player
player.rect.x = 320
player.rect.y = 180

# initialize start position of npcs
npc1.rect.x = 200
npc1.rect.y = 50
npc2.rect.x = 100
npc2.rect.y = 100

# color npcs
npc1.image.fill((0, 255, 0))
npc2.image.fill((0, 0, 255))

sprites.add(npc1)
sprites.add(npc2)
sprites.add(player)

npcs.add(npc1)
npcs.add(npc2)

while (game_running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            game_running = False
            exit()
        #elif event.type == pygame.KEYDOWN:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            #print("left")
            player.set_direction_moving(Direction.LEFT)
            player.move_left(5)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            #print("right")
            player.set_direction_moving(Direction.RIGHT)
            player.move_right(5)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            #print("down")
            player.set_direction_moving(Direction.DOWN)
            player.move_down(5)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            #print("up")
            player.set_direction_moving(Direction.UP)
            player.move_up(5)

    # debug
    #print("playerX=", player.rect.x)
    #print("playerY=", player.rect.y)
    
    # TODO: maybe make it so that the NPC does the collision detection?
    player.detect_collision([WIDTH, HEIGHT], npcs)
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