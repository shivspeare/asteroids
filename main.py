import pygame
import constants

def main():
    # Initialize the pygame
    pygame.init()
    print("Starting asteroids!")
    print(f'Screen width: {constants.SCREEN_WIDTH}')
    print(f'Screen height: {constants.SCREEN_HEIGHT}')

    # Set screen display size
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    while True:
        # Handle quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Set bg color to black
        screen.fill("black")

        # Refresh the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()