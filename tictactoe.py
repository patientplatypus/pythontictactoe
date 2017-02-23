
from random import randint


def check4winner(gamearray):
	counthorizontalplayer = 0
	countverticalplayer = 0
	countforwardslashplayer = 0
	countbackwardslashplayer = 0
	counthorizontalcomputer = 0
	countverticalcomputer = 0
	countforwardslashcomputer = 0
	countbackwardslashcomputer = 0

	for x in range(0,3):
		counthorizontalplayer = 0
		counthorizontalcomputer = 0
		for y in range(0,3):
			if gamearray[x][y] == 2:
				counthorizontalplayer += 1
			if gamearray[x][y] == 1:
				counthorizontalcomputer += 1
		if counthorizontalplayer == 3:
			print("Player wins horizontally!")
			return True
		if counthorizontalcomputer == 3:
			print("Computer wins horizontally!")
			return True

	for x in range(0,3):
		countverticalplayer = 0
		countverticalcomputer = 0
		for y in range(0,3):
			if gamearray[y][x] == 2:
				countverticalplayer += 1
			if gamearray[y][x] == 1:
				countverticalcomputer += 1
		if countverticalplayer == 3:
			print("Player wins vertically!")
			return True
		if countverticalcomputer == 3:
			print("Computer wins vertically!")
			return True


	for x in range(0,3):
		if gamearray[x][x] == 2:
			countforwardslashplayer += 1
		if gamearray[x][x] == 1:
			countforwardslashcomputer += 1

	if countforwardslashplayer == 3:
		print("Player wins diagonally!")
		return True
	if countforwardslashcomputer == 3:
		print("Computer wins diagonally!")
		return True


	for x in range(0,3):
		if gamearray[x][2-x] == 2:
			countbackwardslashplayer += 1
		if gamearray[x][2-x] == 1:
			countbackwardslashcomputer += 1

	if countbackwardslashplayer == 3:
		print("Player wins diagonally!")
		return True
	if countbackwardslashcomputer == 3:
		print("Computer wins diagonally!")
		return True

	return False



class computercontrol():

	def __init__(self, gamearray):
		self.gamearray = gamearray

	def computercanwinthisturn(self):
		counthorizontal = 0
		countvertical = 0
		countforwardslash = 0
		countbackwardslash = 0

		for x in range(0,3):
			counthorizontal = 0
			for y in range(0,3):
				if self.gamearray[x][y] == 1:
					counthorizontal += 1
			if counthorizontal == 2:
				for y in range(0,3):
					if self.gamearray[x][y] == 0:
						self.gamearray[x][y] = 1
						return True

		for x in range(0,3):
			countvertical = 0
			for y in range(0,3):
				if self.gamearray[y][x] == 1:
					countvertical += 1
			if countvertical == 2:
				for y in range(0,3):
					if self.gamearray[y][x] == 0:
						self.gamearray[y][x] = 1
						return True

		for x in range(0,3):
			if self.gamearray[x][x] == 1:
				countforwardslash += 1
			if countforwardslash == 2:
				for x in range(0,3):
					if self.gamearray[x][x] == 0:
						self.gamearray[x][x] = 1
						return True

		for x in range(0,3):
			if self.gamearray[x][2-x] == 1:
				countbackwardslash += 1
			if countbackwardslash == 2:
				for x in range(2,-1):
					if self.gamearray[x][2-x] == 0:
						self.gamearray[x][2-x] = 1
						return True
		return False

	def playercanwinnextturn(self):
		counthorizontal = 0
		countvertical = 0
		countforwardslash = 0
		countbackwardslash = 0

		for x in range(0,3):
			counthorizontal = 0
			for y in range(0,3):
				if self.gamearray[x][y] == 2:
					counthorizontal += 1
			if counthorizontal == 2:
				for y in range(0,3):
					if self.gamearray[x][y] == 0:
						self.gamearray[x][y] = 1
						return True

		for x in range(0,3):
			countvertical = 0
			for y in range(0,3):
				if self.gamearray[y][x] == 2:
					countvertical += 1
			if countvertical == 2:
				for y in range(0,3):
					if self.gamearray[y][x] == 0:
						self.gamearray[y][x] = 1
						return True

		for x in range(0,3):
			if self.gamearray[x][x] == 2:
				countforwardslash += 1
			if countforwardslash == 2:
				for x in range(0,3):
					if self.gamearray[x][x] == 0:
						self.gamearray[x][x] = 1
						print("got to forwardslashplayer is true")
						return True

		for x in range(0,3):
			if self.gamearray[x][2-x] == 2:
				countbackwardslash += 1
			if countbackwardslash == 2:
				for x in range(0,3):
					if self.gamearray[x][2-x] == 0:
						self.gamearray[x][2-x] = 1
						return True
		return False

	def attempt2inrow(self):
		counthorizontal = 0
		countvertical = 0
		countforwardslash = 0
		countbackwardslash = 0

		for x in range(0,3):
			counthorizontal = 0
			for y in range(0,3):
				if self.gamearray[x][y] == 1:
					counthorizontal += 1
				if self.gamearray[x][y] == 2:
					counthorizontal = 3
			if counthorizontal == 2:
				for y in range(0,3):
					if self.gamearray[x][y] == 0:
						self.gamearray[x][y] = 1
						return True

		for x in range(0,3):
			countvertical = 0
			for y in range(0,3):
				if self.gamearray[y][x] == 1:
					countvertical += 1
				if self.gamearray[y][x] == 2:
					countvertical = 3
			if countvertical == 2:
				for y in range(0,3):
					if self.gamearray[y][x] == 0:
						self.gamearray[y][x] = 1
						return True

		for x in range(0,3):
			if self.gamearray[x][x] == 1:
				countforwardslash += 1
			if self.gamearray[x][x] == 2:
				countforwardslash = 3
			if countforwardslash == 2:
				for x in range(0,3):
					if self.gamearray[x][x] == 0:
						self.gamearray[x][x] = 1
						return True

		for x in range(0,3):
			if self.gamearray[x][2-x] == 1:
				countbackwardslash += 1
			if self.gamearray[x][2-x] == 2:
				countbackwardslash = 3
			if countbackwardslash == 2:
				for x in range(0,3):
					if self.gamearray[x][2-x] == 0:
						self.gamearray[x][2-x] = 1
						return True
		return False

	def thenrandom(self):
		isempty = False

		for x in range(0,3):
			for y in range(0,3):
				if self.gamearray[x][y] == 0:
					isempty = True

		if isempty == False: 
			print("We have a tie!")
			return "tie"

		while True:				
			xrandom = randint(0,2) 
			yrandom = randint(0,2)
			if self.gamearray[xrandom][yrandom] == 0:
				self.gamearray[xrandom][yrandom] = 1
				break








print("We are going to play Tic Tac Toe!")


gamearray = [[0,0,0],[0,0,0],[0,0,0]]

print(gamearray)

print("    0 | 1 | 2 ")

for x in range(0,3):
	print("")
	print(str(x) + " |", end='')
	for y in range(0,3):
		if gamearray[x][y] == 0:
			print("___|", end='')
		if gamearray[x][y] == 1:
			print("_X_|", end='')
		if gamearray[x][y] == 2:
			print("_O_|", end='')

print("")





while True:
	while True:
		row = ""
		column = ""
		row = input("Please input which row you would like to move to: ")
		column = input("Please input which column you would like to move to: ")
		try:
			if (int(row) <= 2 and int(row) >= 0) and (int(column) <= 2 and int(column) >= 0) and (gamearray[int(row)][int(column)] == 0):
				print("row: ", str(int(row)), " column: ", str(int(column)))
				break
		except ValueError:
			print("Please only put in integer values between 0 and 2 corresponding to empty spaces on the game board!")


	gamearray[int(row)][int(column)] = 2

	if check4winner(gamearray) == True:
		print("    0 | 1 | 2 ")

		for x in range(0,3):
			print("")
			print(str(x) + " |", end='')
			for y in range(0,3):
				if gamearray[x][y] == 0:
					print("___|", end='')
				if gamearray[x][y] == 1:
					print("_X_|", end='')
				if gamearray[x][y] == 2:
					print("_O_|", end='')

		print("")
		break


	computersturn = computercontrol(gamearray)
	cancomputerwin = computersturn.computercanwinthisturn()
	if cancomputerwin == False:
		cancomputerblock = computersturn.playercanwinnextturn()
		if cancomputerblock == False:
			computer2inrow = computersturn.attempt2inrow()
			if computer2inrow == False:
				computerrandom = computersturn.thenrandom()

	print(gamearray)
	print("    0 | 1 | 2 ")

	for x in range(0,3):
		print("")
		print(str(x) + " |", end='')
		for y in range(0,3):
			if gamearray[x][y] == 0:
				print("___|", end='')
			if gamearray[x][y] == 1:
				print("_X_|", end='')
			if gamearray[x][y] == 2:
				print("_O_|", end='')

	print("")

	if computerrandom == "tie":
		break

	if check4winner(gamearray) == True:
		break


