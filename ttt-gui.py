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
import time
pygame.init()

#declaring vars
windowHeight = 550
windowWidth = 450
player = 1
turn = 0
winner = 0
run = True
result = True
WHITE = (255, 255, 255)
fieldVal = ([[10, 20, 30], 
			 [40, 50, 60], 
			 [70, 80, 90]])

#defining main window size and caption
gameWindow = pygame.display.set_mode([windowWidth, windowHeight])
pygame.display.set_caption('Tic-Tac-Toe', 'Xs vs Os. Fight!')

#define image vars
bgImage = pygame.image.load("img/field.png")
xMark = pygame.image.load("img/x-mark.png")
oMark = pygame.image.load("img/o-mark.png")


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


gameWindow.fill(0)
gameWindow.blit(bgImage, (0, 0))

#defining main drawing method
def draw_field():
	#display game window with an image background
	pygame.draw.line(gameWindow, WHITE, [0, 451], [450, 451], 2)
	pygame.font.SysFont('Helvetica', 10)
	for i in range(0,3):
		for j in range (0,3):
			if fieldVal[i][j] == 'x':
				gameWindow.blit(xMark, (i*150, j*150))
			if fieldVal[i][j] == 'o':
				gameWindow.blit(oMark, (i*150, j*150))
			j = j + 1
		i = i + 1
	pygame.display.update()


#main loop
while run and turn < 9:
	try:
		draw_field()
		for event in pygame.event.get():
			#quit in even of closing game (break infinite loop without having to kill the python process)
			if event.type == pygame.QUIT:
				pygame.quit()
				exit(0)
			# get mouse click coords
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				mousePosX, mousePosY = pygame.mouse.get_pos()
				mousePos = mousePosX, mousePosY
				if player == 1 and fieldVal[mousePosX//150][mousePosY//150] not in ['x', 'o']:
					fieldVal[mousePosX//150][mousePosY//150] = 'x'
					turn = turn + 1
					run = checkWinCond()
					if run == False:
						winner = 1
					player = 2
				elif player == 2 and fieldVal[mousePosX//150][mousePosY//150] not in ['x', 'o']:
					fieldVal[mousePosX//150][mousePosY//150] = 'o'
					turn = turn + 1
					run = checkWinCond()
					if run == False:
						winner = 2
					player = 1
	except KeyboardInterrupt:
		break

if run == False:
	print('Player ' + str(winner) + ' wins!')
elif turn == 9:
	print("It's a tie!")
draw_field()
while result:
	for event in pygame.event.get():
		#quit in even of closing game (break infinite loop without having to kill the python process)
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)