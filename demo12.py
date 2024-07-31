import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
SNAKE_SIZE = 20
SNAKE_SPEED = 10
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize snake and food positions
snake_x = WIDTH // 2
snake_y = HEIGHT // 2
snake_speed_x = 0
snake_speed_y = 0
snake_body = [(snake_x, snake_y)]
food_x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
food_y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE

score = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_speed_y == 0:
                snake_speed_x = 0
                snake_speed_y = -SNAKE_SIZE
            elif event.key == pygame.K_DOWN and snake_speed_y == 0:
                snake_speed_x = 0
                snake_speed_y = SNAKE_SIZE
            elif event.key == pygame.K_LEFT and snake_speed_x == 0:
                snake_speed_x = -SNAKE_SIZE
                snake_speed_y = 0
            elif event.key == pygame.K_RIGHT and snake_speed_x == 0:
                snake_speed_x = SNAKE_SIZE
                snake_speed_y = 0

    # Update snake's position
    snake_x += snake_speed_x
    snake_y += snake_speed_y
    snake_body.insert(0, (snake_x, snake_y))

    # Check for collision with food
    if snake_x == food_x and snake_y == food_y:
        score += 1
        food_x = random.randint(0, (WIDTH - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
        food_y = random.randint(0, (HEIGHT - SNAKE_SIZE) // SNAKE_SIZE) * SNAKE_SIZE
    else:
        snake_body.pop()

    # Check for collision with the walls
    if snake_x < 0 or snake_x >= WIDTH or snake_y < 0 or snake_y >= HEIGHT:
        pygame.quit()
        sys.exit()

    # Check for self-collision
    if len(snake_body) > 1 and (snake_x, snake_y) in snake_body[1:]:
        pygame.quit()
        sys.exit()

    # Draw everything on the screen
    screen.fill(WHITE)
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))
    pygame.draw.rect(screen, RED, (food_x, food_y, SNAKE_SIZE, SNAKE_SIZE))

    pygame.display.update()

    # Control the game speed
    pygame.time.Clock().tick(SNAKE_SPEED)
