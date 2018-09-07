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
windowHeight = 550
windowWidth = 450
fieldVal = ([[10, 20, 30], 
			 [40, 50, 60], 
			 [70, 80, 90]])
player = 1
turn = 0

#defining main window size
gameWindow = pygame.display.set_mode([windowWidth, windowHeight])
pygame.display.set_caption('Tic-Tac-Toe', 'Xs vs Os. Fight!')
run = True
bgImage = pygame.image.load("img/field.png")
xMark = pygame.image.load("img/x-mark.png")
oMark = pygame.image.load("img/o-mark.png")
WHITE = (255, 255, 255)

#define check win conditions method
def checkWinCond():
	if (fieldVal[0][0] == fieldVal[0][1] == fieldVal[0][2]):
		return False
	if (fieldVal[1][0] == fieldVal[1][1] == fieldVal[1][2]):
		return False
	if (fieldVal[2][0] == fieldVal[2][1] == fieldVal[2][2]):
		return False
	if (fieldVal[0][0] == fieldVal[1][0] == fieldVal[2][0]):
		return False
	if (fieldVal[0][1] == fieldVal[1][1] == fieldVal[2][1]):
		return False
	if (fieldVal[0][2] == fieldVal[1][2] == fieldVal[2][2]):
		return False
	if (fieldVal[0][0] == fieldVal[1][1] == fieldVal[2][2]):
		return False
	if (fieldVal[2][0] == fieldVal[1][1] == fieldVal[0][2]):
		return False
	else:
		return True

#defining main drawing method
def draw_field():
	#display game window with an image background
	gameWindow.fill(0)
	gameWindow.blit(bgImage, (0, 0))
	pygame.draw.line(gameWindow, WHITE, [0, 451], [450, 451], 2)
	for i in range(0,3):
		for j in range (0,3):
			if fieldVal[i][j] == 'x':
				gameWindow.blit(xMark, (i*150, j*150))
			if fieldVal[i][j] == 'o':
				gameWindow.blit(oMark, (i*150, j*150))
			j = j + 1
		i = i + 1
	pygame.display.flip()

#main loop
while run and turn < 9:
	draw_field()
	run = checkWinCond()
	for event in pygame.event.get():
		#quit in even of closing game (break infinite loop without having to kill the python process)
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
		# get mouse click coords
		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			mousePosX, mousePosY = pygame.mouse.get_pos()
			mousePos = mousePosX, mousePosY
			if player == 1:
				fieldVal[mousePosX//150][mousePosY//150] = 'x'
				player = 2
				turn = turn + 1
			else:
				fieldVal[mousePosX//150][mousePosY//150] = 'o'
				player = 1
				turn = turn + 1	
draw_field()