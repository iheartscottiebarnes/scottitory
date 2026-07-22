import pygame
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.draw.rect(screen, (0, 255, 0), (10, 10, 10, 10))

pygame.display.update()
x = 100
y = 100
speed_x = 0.5
speed_y = 0.5
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	if x <= 0 or x >= 400 - 100:
		speed_x *= -1
	if y <= 0 or y >= 400 - 100:
		speed_y *= -1

	screen.fill((0, 0, 0)) 
	
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		y -= 1
	if keys[pygame.K_s]:
		y += 1
	if keys[pygame.K_a]:
		x -= 1
	if keys[pygame.K_d]:
		x += 1
	if x <= 0 or x >= 400 - 100:
		speed_x = 0
	if y <= 0 or y >= 400 - 100:
		speed_y = 0
	pygame.draw.rect(screen, (0, 255, 0), (x, y, 10, 10))
	pygame.display.update()

pygame.quit()