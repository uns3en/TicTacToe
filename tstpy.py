#imports
import os, pygame
import time
pygame.init()

#declaring vars
windowHeight = 450
windowWidth = 450
player = 1
turn = 0
winner = 0
run = True
result = True
WHITE = (255, 255, 255)
fieldVal = ([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
winLine = 0

#define image vars
bgImage = pygame.image.load("img/field.png")

#defining main window size and caption
gameWindow = pygame.display.set_mode([windowWidth, windowHeight])
pygame.display.set_caption('Tic-Tac-Toe', 'Xs vs Os. Fight!')

#draw playing field
gameWindow.fill(0)
gameWindow.blit(bgImage, (0, 0))
pygame.display.update()
while run:
	for event in pygame.event.get():
		#quit in even of closing game (break infinite loop without having to kill the python process)
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)