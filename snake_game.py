import pygame
import random

# --- Constants ---
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SNAKE_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# --- Pygame Initialization ---
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
CLOCK = pygame.time.Clock()

# --- Game Functions ---
def draw_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(SCREEN, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

def draw_food(food_pos):
    pygame.draw.rect(SCREEN, RED, (food_pos[0], food_pos[1], SNAKE_SIZE, SNAKE_SIZE))

def generate_food():
    x = random.randrange(0, SCREEN_WIDTH - SNAKE_SIZE, SNAKE_SIZE)
    y = random.randrange(0, SCREEN_HEIGHT - SNAKE_SIZE, SNAKE_SIZE)
    return [x, y]

# --- Main Game Loop ---
def game_loop():
    game_over = False
    game_close = False

    # Snake initial position and direction
    snake_head = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]
    snake_body = [snake_head]
    
    # Initial food position
    food_pos = generate_food()

    score = 0

    # Initial direction (right)
    direction = "RIGHT"
    change_to = direction

    # --- Game Over Message and Score Display ---
    font_style = pygame.font.SysFont(None, 50)
    score_font = pygame.font.SysFont(None, 35)

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        SCREEN.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])

    def show_score(score):
        value = score_font.render("Your Score: " + str(score), True, WHITE)
        SCREEN.blit(value, [0, 0])

    while not game_close:
        while game_over:
            SCREEN.fill(BLACK)
            message("You Lost! Press Q-Quit or R-Restart", RED)
            show_score(score) # Display final score
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_close = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = True
                        game_over = False
                    if event.key == pygame.K_r:
                        game_loop() # Restart the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # Validate direction change
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Move the snake
        if direction == 'UP':
            snake_head[1] -= SNAKE_SIZE
        if direction == 'DOWN':
            snake_head[1] += SNAKE_SIZE
        if direction == 'LEFT':
            snake_head[0] -= SNAKE_SIZE
        if direction == 'RIGHT':
            snake_head[0] += SNAKE_SIZE

        # Add new head to snake body
        snake_body.insert(0, list(snake_head))
        
        # --- Collision Detection ---
        # Wall collision
        if snake_head[0] >= SCREEN_WIDTH or snake_head[0] < 0 or \
           snake_head[1] >= SCREEN_HEIGHT or snake_head[1] < 0:
            game_over = True

        # Food eating logic
        if snake_head[0] == food_pos[0] and snake_head[1] == food_pos[1]:
            score += 1
            food_pos = generate_food()
        else:
            snake_body.pop()

        # Self-collision
        for x in snake_body[1:]:
            if x[0] == snake_head[0] and x[1] == snake_head[1]:
                game_over = True

        SCREEN.fill(BLACK)
        draw_snake(snake_body)
        draw_food(food_pos)
        show_score(score) # Display current score
        pygame.display.update()

        CLOCK.tick(FPS)

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()
