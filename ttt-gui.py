import os, platform, pygame
pygame.init()

windowHeight = 450
windowWidth = 450

gameWindow = pygame.display.set_mode([windowWidth, windowHeight])
pygame.display.set_caption('TicTacToe', 'Xs vs 0s. Fight!')
#gameWindow.fill((0, 0, 0))
run = True
bgImage = pygame.image.load("img/field.png").convert()

while run:
	gameWindow.fill(0)
	gameWindow.blit(bgImage, (0, 0))
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0) 