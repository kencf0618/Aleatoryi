import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
FPS = 30  # Frame rate

# Colors
GREEN = (0, 100, 0)
BLACK = (0, 0, 0)
DARK_GREEN = (0, 80, 0)
LIGHT_GREEN = (0, 255, 0)

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Retro CRT Number Generator")

# Load MICR font (ensure this font is installed on your system or use a TTF file)
try:
    font = pygame.font.Font(pygame.font.match_font("MICR"), 80)  # MICR font
except:
    print("MICR font not found. Using default font.")
    font = pygame.font.SysFont("monospace", 80)

# Function to generate two random nine-digit numbers
def generate_numbers():
    num1 = str(random.randint(100000000, 999999999))
    num2 = str(random.randint(100000000, 999999999))
    return num1, num2

# Function to create a flicker effect
def flicker():
    return random.choice([True, False, False, False])  # Flicker occasionally

# Function to render text with CRT glow
def render_text(text, x, y):
    text_surface = font.render(text, True, LIGHT_GREEN)
    glow_surface = font.render(text, True, GREEN)
    
    # Draw glow effect (slightly offset)
    screen.blit(glow_surface, (x - 2, y - 2))
    screen.blit(glow_surface, (x + 2, y + 2))
    
    # Draw main text
    screen.blit(text_surface, (x, y))

# Function to apply CRT scanlines
def draw_scanlines():
    for i in range(0, SCREEN_HEIGHT, 4):
        pygame.draw.line(screen, DARK_GREEN, (0, i), (SCREEN_WIDTH, i), 1)

# Function to apply screen curvature effect
def apply_curvature():
    for i in range(0, SCREEN_WIDTH, 10):
        pygame.draw.line(screen, DARK_GREEN, (i, 0), (i, SCREEN_HEIGHT), 1)

# Main loop
running = True
last_update = time.time()
num1, num2 = generate_numbers()

while running:
    screen.fill(GREEN)  # CRT background
    
    # Check if it's time to generate new numbers
    if time.time() - last_update > 3:
        num1, num2 = generate_numbers()
        last_update = time.time()
    
    # Random flicker effect
    if not flicker():
        render_text(num1, 100, 100)
        render_text(num2, 100, 220)

    # Apply CRT effects
    draw_scanlines()
    apply_curvature()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    pygame.time.delay(int(1000 / FPS))

pygame.quit()
