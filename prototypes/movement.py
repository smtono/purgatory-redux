import pygame

game_running = True
WIDTH = 640
HEIGHT = 360

pygame.init()
pygame.display.set_mode((WIDTH, HEIGHT)) # game window initialization

while (game_running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Usually wise to be able to close your program.
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("Player moved up!")
            elif event.key == pygame.K_a:
                print("Player moved left!")
            elif event.key == pygame.K_s:
                print("Player moved down!")
            elif event.key == pygame.K_d:
                print("Player moved right!")