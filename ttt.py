#################################################
#...............................................#
#...... First project ever by teh.f4ll3n .......#
#.......... https://github.com/uns3en ..........#
#........ A simple game of Tic Tac Toe .........#
#...............................................#
#............ Licence: GNU GPLv2 ...............#
# ..............................................#
#################################################  




#imports
import os, sys, platform
 
#vars
global winCond
winCond = 0
field = ['1','2','3','4','5','6','7','8','9']
player = 1
turn = 0
 
#clear screen
def clear_screen():
	if platform.system() == "Windows":
		os.system('cls')
	elif platform.system() == "Linux" or platform.system() == "Linux2":
		os.system('clear')
	elif platform.system() == "Darwin":
		os.system('clear')

#clear pre-run output
clear_screen()

#initial print
print('This is a game of Tic Tac Toe.')
print('You make your move by entering available field number.\n')

#define field draw function
def draw_field():
	print( '   |   |   ')
	print(' {f[0]} | {f[1]} | {f[2]} '.format(f=field))
	print('   |   |   ')
	print('-' * 11)
	print('   |   |   ')
	print(' {f[3]} | {f[4]} | {f[5]} '.format(f=field))
	print('   |   |   ')
	print('-' * 11)
	print('   |   |   ')
	print(' {f[6]} | {f[7]} | {f[8]} '.format(f=field))
	print('   |   |   ')
	print('\n')
 
#define check win conditions function
def checkWinCond():
	if (field[0] == field [1] == field[2]):
		return 2
	elif (field[3] == field [4] == field[5]):
		return 2
	elif (field[6] == field [7] == field[8]):
		return 2
	elif (field[0] == field [3] == field[6]):
		return 2
	elif (field[1] == field [4] == field[7]):
		return 2
	elif (field[2] == field [5] == field[8]):
		return 2
	elif (field[0] == field [4] == field[8]):
		return 2
	elif (field[2] == field [4] == field[6]):
		return 2
	else:
		return 0
 
#main loop
while winCond == 0:
	try:
		while winCond == 0 and turn < 9:   
			draw_field()
			print('Turn ' + str(turn + 1))
			tempVal = int(input ('Player ' + str(player) + ', please enter the field number: '))
			clear_screen()
			if field[tempVal-1] in ['X', 'O']:# or 0 > tempVal > 9:
				clear_screen()
				print('This is not a valid field\n')
				continue
			else:
				if player == 1:
					field[tempVal-1] = 'X'
					#check win condition, break if met, set winCond = 2
					if checkWinCond() == 2:
						winCond = checkWinCond()
						break
					player = 2
					turn = turn + 1
				else:
					field[tempVal-1] = "O"
					#check win condition, break if met, set winCond = 2
					#check win condition, break if met, set winCond = 2
					if checkWinCond() == 2:
						winCond = checkWinCond()
						break
					player = 1
					turn = turn + 1
	except KeyboardInterrupt:
		print('\nKeyboardInterrupt received. Terminated.')
		break
	except:
		clear_screen()
		print('Please enter a number between 1 and 9.')
	finally:
		if (winCond == 0 and turn == 9):
			print('Draw. Neither player wins.')
		elif (winCond == 2):
			draw_field()
			print('Player ' + str(player) + ' wins!')