#################################################
#...............................................#
#.......... Second project by uns3en ...........#
#.......... https://github.com/uns3en ..........#
#........ A simple game of Tic-Tac-Toe .........#
#............... now with GUI ..................#
#............ Licence: GNU GPLv2 ...............#
# ..............................................#
#################################################

#imports
import os, pygame
pygame.init()

#declaring vars
windowHeight = 450
windowWidth = 450
#fieldVal = ['0','0','0','0','0','0','0','0','0']

#defining main window size
gameWindow = pygame.display.set_mode([windowWidth, windowHeight])
pygame.display.set_caption('Tic-Tac-Toe', 'Xs vs 0s. Fight!')
run = True
bgImage = pygame.image.load("img/field.png")
xMark = pygame.image.load("img/x-mark.png")
oMark = pygame.image.load("img/o-mark.png")

#main loop
while run:
	#display game window with an image background
	gameWindow.fill(0)
	gameWindow.blit(bgImage, (0, 0))
	#gameWindow.blit(xMark, (0, 0))
	#gameWindow.blit(oMark, (150, 150))
	pygame.display.flip()

	#quit in even of closing game (break infinite loop without having to kill the python process)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)