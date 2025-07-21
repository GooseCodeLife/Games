import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Pygame Text Example')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up font
font = pygame.font.SysFont(None, 48)

# Render the text
text_surface = font.render('Hello, Pygame!', True, WHITE)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with black
    screen.fill(BLACK)
    
    # Blit the text surface onto the display surface
    screen.blit(text_surface, (100, 100))
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
