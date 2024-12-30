import pygame
import constants
import player
import asteroid
import asteroidfield
import shot

def main():
    # Initialize the pygame
    pygame.init()
    print("Starting asteroids!")
    print(f'Screen width: {constants.SCREEN_WIDTH}')
    print(f'Screen height: {constants.SCREEN_HEIGHT}')

    # Set screen display size
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    # Set clock
    Clock = pygame.time.Clock()
    dt = 0

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Initialize sprite groups containers
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (updatable, drawable, shots)

    # Create Player
    p = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    af = asteroidfield.AsteroidField()

    while True:
        # Handle quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Set bg color to black
        screen.fill("black")

        # Time delta
        dt = Clock.tick(60) / 1000

        # Update sprites
        for s in updatable:
            s.update(dt)

        # Draw sprites
        for s in drawable:
            s.draw(screen)
        
        # Check collisions
        for a in asteroids:
            # Asteroid and player collisions
            if a.check_collision(p):
                print("Game over!")
                exit()
            # Asteroid and shot collisions
            for s in shots:
                if s.check_collision(a):
                    s.kill()
                    a.split()

        # Refresh the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()