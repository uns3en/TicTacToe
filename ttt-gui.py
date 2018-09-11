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

#loading images to vars
bgImage = pygame.image.load("img/field.png")
xMark = pygame.image.load("img/x-mark.png")
oMark = pygame.image.load("img/o-mark.png")
p1Winner = pygame.image.load("img/p1wins.png")
p2Winner = pygame.image.load("img/p2wins.png")
pDraw = pygame.image.load("img/draw.png")

#declaring vars
windowHeight = 450
windowWidth = 450
player = 1
turn = 0
winner = 0
run = True
result = True
WHITE = (255, 255, 255)
GREY = (180, 180, 180)
fieldVal = ([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
winLine = 0

#defining main window size and caption
gameWindow = pygame.display.set_mode([windowWidth, windowHeight])
pygame.display.set_caption('Tic-Tac-Toe', 'Xs vs Os. Fight!')

#defining main field drawing method
def draw_field():
	#display game window with an image background
	gameWindow.fill(0)
	gameWindow.blit(bgImage, (0, 0))
	#loop through array to fetch updated values
	for i in range(0,3):
		for j in range (0,3):
			if fieldVal[i][j] == 'x':
				gameWindow.blit(xMark, (i*150, j*150))
			if fieldVal[i][j] == 'o':
				gameWindow.blit(oMark, (i*150, j*150))
			j = j + 1
		i = i + 1

#define check win conditions method
def checkWinCond():
	if (fieldVal[0][0] == fieldVal[0][1] == fieldVal[0][2]):
		return False, 1
	if (fieldVal[1][0] == fieldVal[1][1] == fieldVal[1][2]):
		return False, 2
	if (fieldVal[2][0] == fieldVal[2][1] == fieldVal[2][2]):
		return False, 3
	if (fieldVal[0][0] == fieldVal[1][0] == fieldVal[2][0]):
		return False, 4
	if (fieldVal[0][1] == fieldVal[1][1] == fieldVal[2][1]):
		return False, 5
	if (fieldVal[0][2] == fieldVal[1][2] == fieldVal[2][2]):
		return False, 6
	if (fieldVal[0][0] == fieldVal[1][1] == fieldVal[2][2]):
		return False, 7
	if (fieldVal[2][0] == fieldVal[1][1] == fieldVal[0][2]):
		return False, 8
	else:
		return True, 0

#define draw win line
def draw_line(a):
	if a == 1:
		pygame.draw.line(gameWindow, GREY, (75, 30), (75, 420), 3)
	elif a == 2:
		pygame.draw.line(gameWindow, GREY, (225, 30), (225, 420), 3)
	elif a == 3:
		pygame.draw.line(gameWindow, GREY, (375, 30), (375, 420), 3)
	elif a == 4:
		pygame.draw.line(gameWindow, GREY, (30, 75), (420, 75), 3)
	elif a == 5:
		pygame.draw.line(gameWindow, GREY, (30, 225), (420, 225), 3)
	elif a == 6:
		pygame.draw.line(gameWindow, GREY, (30, 375), (420, 375), 3)
	elif a == 7:
		pygame.draw.line(gameWindow, GREY, (30, 30), (420, 420), 3)
	elif a == 8:
		pygame.draw.line(gameWindow, GREY, (420, 30), (30, 420), 3)

#define draw winner alert
def draw_winner(b):
	if b == 1:
		gameWindow.blit(p1Winner, (75, 150))
	elif b == 2:
		gameWindow.blit(p2Winner, (75, 150))
	elif b == 0:
		gameWindow.blit(pDraw, (75, 150))

#main loop
#def main_game():
while run and turn < 9:
	try:
		draw_field()
		pygame.display.update()
		for event in pygame.event.get():
			
			#quit in even of closing game (break infinite loop without having to kill the python process)
			if event.type == pygame.QUIT:
				pygame.quit()
				exit(0)
			
			# get mouse click coords
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				mousePosX, mousePosY = pygame.mouse.get_pos()
				mousePos = mousePosX, mousePosY

				#update field value and chech if game is won
				if player == 1 and fieldVal[mousePosX//150][mousePosY//150] not in ['x', 'o']:
					fieldVal[mousePosX//150][mousePosY//150] = 'x'
					turn = turn + 1
					run, winLine = checkWinCond()
					if run == False:
						winner = 1
					player = 2
				elif player == 2 and fieldVal[mousePosX//150][mousePosY//150] not in ['x', 'o']:
					fieldVal[mousePosX//150][mousePosY//150] = 'o'
					turn = turn + 1
					run, winLine = checkWinCond()
					if run == False:
						winner = 2
					player = 1
	except KeyboardInterrupt:
		break

#main_game()

#post-game loop to display results
while result:
	if run == False:
		draw_field()
		draw_line(winLine)
		draw_winner(winner)
		pygame.display.update()
	elif turn == 9:
		draw_field()
		draw_winner(winner)
		pygame.display.update()
	for event in pygame.event.get():
		#quit in even of closing game (break infinite loop without having to kill the python process)
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)	