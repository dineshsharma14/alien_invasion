import pygame,sys

def fun_game():
    screen = pygame.display.set_mode((600,800))
    pygame.display.set_caption("Fun Game")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                print(event.key)
                
        pygame.display.flip()

fun_game()
