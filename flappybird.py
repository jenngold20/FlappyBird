import pygame
import random

# Initialize the game
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Set the colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set the bird dimensions and position
bird_width = 50
bird_height = 50
bird_x = 200
bird_y = 250

# Set the gravity and jump force
gravity = 0.5
jump_force = 10

# Set the pipe dimensions and gap size
pipe_width = 70
pipe_height = random.randint(100, 400)
pipe_gap = 200
pipe_x = screen_width

# Set the game over flag
game_over = False

# Set the score
score = 0
font = pygame.font.Font(None, 36)

# Load the bird image
bird_img = pygame.image.load("bird.png")

# Load the pipe images
pipe_top_img = pygame.image.load("pipe_top.png")
pipe_bottom_img = pygame.image.load("pipe_bottom.png")

# Function to display the score
def display_score(score):
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y -= jump_force

    # Update the bird position
    bird_y += gravity

    # Clear the screen
    screen.fill(black)

    # Draw the bird
    screen.blit(bird_img, (bird_x, bird_y))

    # Draw the pipes
    screen.blit(pipe_top_img, (pipe_x, pipe_height - pipe_gap))
    screen.blit(pipe_bottom_img, (pipe_x, pipe_height + pipe_gap))

    # Move the pipes
    pipe_x -= 5

    # Check for collision with the bird
    if bird_y < 0 or bird_y + bird_height > screen_height or pygame.Rect(bird_x, bird_y, bird_width, bird_height).colliderect(pygame.Rect(pipe_x, pipe_height - pipe_gap, pipe_width, pipe_height + pipe_gap)):
        game_over = True

    # Check if the pipe has passed the bird
    if pipe_x + pipe_width < bird_x:
        score += 1
        pipe_x = screen_width
        pipe_height = random.randint(100, 400)

    # Display the score
    display_score(score)

    # Update the screen
    pygame.display.update()

# Quit the game
pygame.quit()
