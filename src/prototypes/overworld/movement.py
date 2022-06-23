import pygame
from prototypes.overworld.game import Camera, Direction
from prototypes.overworld.game_objects import NPC
from prototypes.overworld.player import Player
from prototypes.overworld.player import PlayerInput

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
player = Player((255, 0, 0), 20, 20)
npc1 = NPC((0, 255, 0), 20, 20)
npc2 = NPC((0, 0, 255), 20, 20)

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
# npc1.image.fill((0, 255, 0))
# npc2.image.fill((0, 0, 255))

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

        # TODO: put in Player update() function
        # TODO: put this input into a god input function
        #       go to different functions based on input type
        #       depending on input, have different things happen
        #       WASD for movement
        #       E for interaction
        #       Esc for menu
        #       Mouse clicks for dialogue / battles
        input_detection = PlayerInput(player)
        input_detection.on_move(keys)

    # debug
    #print("playerX=", player.rect.x)
    #print("playerY=", player.rect.y)
    
    # TODO: maybe make it so that the NPC does the collision detection?
    npc1.detect_nearby(player)
    npc2.detect_nearby(player)

    # check for interactions by player w/ nearby NPC
    
    
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