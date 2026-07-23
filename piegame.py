import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("yaya")



while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	mouse_x, mouse_y = pygame.mouse.get_pos()
	screen.fill((0, 0, 0)) 
	pygame.draw.circle(screen, (255, 255, 255), (mouse_x, mouse_y), 10)
	pygame.display.flip()
 
pygame.quit()
sys.exit()
