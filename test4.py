import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("82-0")
clock = pygame.time.Clock()

colorb=(54, 55, 55)
colort=(255, 165, 0)
text = pygame.font.SysFont("Arial", 30)

button_rect = pygame.Rect(300, 250, 200, 60)
button_text = text.render("hi", True, colort)
text_rect = button_text.get_rect(center=button_rect.center)

while True:
    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.rect(screen, colort, button_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.init
            pygame.quit()
            sys.exit()
            
    if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                if button_rect.collidepoint(mouse_pos):
                    button_rect = pygame.Rect(310, 255, 175, 50)
                    font = pygame.font.SysFont("Arial", 25)
                    button_text = font.render("CLICK", True, text)
                    text_rect = button_text.get_rect(center=button_rect.center)
        
    screen.fill(colorb)      



            
