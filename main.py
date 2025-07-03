from constants import *
import pygame 
import player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    
    while True:
        screen.fill((0,0,0))
        pygame.display.flip()
        time.tick(60)

        player = player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        player.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
