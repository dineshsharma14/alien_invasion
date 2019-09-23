import sys,pygame
from frog import Frog
def game_run():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    frog = Frog(screen)
    pygame.display.set_caption("Firing frog")
    bg_color = (255,255,255)
    screen.fill(bg_color) # Using fill method of pygame.display on screen object

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moving_right = True
                elif event.key == pygame.K_LEFT:
                    moving_left = True
                elif event.key == pygame.K_UP:
                    moving_up = True
                elif event.key == pygame.K_DOWN:
                    moving_down = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    moving_right = False
                elif event.key == pygame.K_LEFT:
                    moving_left = False
                elif event.key == pygame.K_UP:
                    moving_up = False
                elif event.key == pygame.K_DOWN:
                    moving_down = False
        frog.update()            
        frog.blitme()
        pygame.display.flip()

game_run()
