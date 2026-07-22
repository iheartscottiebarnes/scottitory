import pygame
import sys
import time
# 1. Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Button Example")
clock = pygame.time.Clock()

# 2. Define Colors and Fonts
COLOR_NORMAL = (50, 150, 255)    # Blue
COLOR_HOVER = (20, 100, 220)     # Darker Blue
COLOR_TEXT = (255, 255, 255)     # White
font = pygame.font.SysFont("Arial", 30)

# 3. Define Button Properties (x, y, width, height)
button_rect = pygame.Rect(300, 250, 200, 60)
button_text = font.render("hi", True, COLOR_TEXT)
# Center the text inside the button rect
text_rect = button_text.get_rect(center=button_rect.center)

# Main Game Loop
while True:
    # Get current mouse position
    mouse_pos = pygame.mouse.get_pos()
    
    # 4. Handle Input Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.init()
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button click
                # Check if mouse clicked inside the button
                if button_rect.collidepoint(mouse_pos):
                    button_rect = pygame.Rect(310, 255, 175, 50)
                    font = pygame.font.SysFont("Arial", 25)
                    button_text = font.render("CLICK", True, COLOR_TEXT)
                    text_rect = button_text.get_rect(center=button_rect.center)
        else:
            button_rect = pygame.Rect(300, 250, 200, 60)            
            font = pygame.font.SysFont("Arial", 30)
            button_text = font.render("CLICK", True, COLOR_TEXT)
            text_rect = button_text.get_rect(center=button_rect.center)

    # 5. Draw Everything
    screen.fill((30, 30, 30))  # Dark gray background
    
    # Change color dynamically when hovering
    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, COLOR_HOVER, button_rect)
    else:
        pygame.draw.rect(screen, COLOR_NORMAL, button_rect)
        
    # Draw text on top of the button
    screen.blit(button_text, text_rect)

    pygame.display.flip()
