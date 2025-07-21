import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Growing Image Example')

# Load the image
image = pygame.image.load('FinalMStanding.png').convert_alpha()
original_image_size = image.get_size()

# Initialize variables for resizing
scale_factor = 1
growth_rate = 1.01  # Image will grow by 1% each frame

# Set up the clock
clock = pygame.time.Clock()

# Main loop
running = True

def blit_image_fit(screen, image, rect):
    # Resize the image to fit the rectangle
    resized_image = pygame.transform.scale(image, (rect.width, rect.height))
    # Draw the resized image in the rectangle
    screen.blit(resized_image, rect.topleft)

def blit_image_fit(screen, image, scale,x):
    # Resize the image to fit the rectangle
    resized_image = pygame.transform.scale(image, (scale, scale))
    # Draw the resized image in the rectangle
    screen.blit(resized_image, x)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Resize the image
    scale_factor *= growth_rate
    new_size = (int(original_image_size[0] * scale_factor), int(original_image_size[1] * scale_factor))
    #resized_image = pygame.transform.scale(image, new_size)

    # Clear the screen
    screen.fill((0, 0, 0))  # Fill screen with black

    # Draw the resized image at the center
    x = (screen_width - new_size[0]) // 2
    y = (screen_height - new_size[1]) // 2

    blit_image_fit(screen,image, scale_factor, x )
    #screen.blit(resized_image, (x, y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
