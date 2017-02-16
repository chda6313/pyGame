import os, sys, random, classes, qolFunctions


def __main__():
	PlayerShip = classes.ship()
	PlayerShip.money = 600
	qolFunctions.saveGame(PlayerShip)

__main__()



def returnTester(name=-1):
	mtns = 1
	plains = 3
	forest = 90


	if name == 'mountain':
		return mtns
	elif name == 'plains':
		return plains
	elif name == 'forest':
		return forest
	else:
		return None