import os, sys, random, classes, qolFunctions


def __main__():
	#make a ship
	PlayerShip = classes.ship()
	PlayerShip.fuel = 100
	qolFunctions.saveGame(PlayerShip)
	PlayerShip.fuel = 0
	PlayerShip = qolFunctions.loadGame()
	print(PlayerShip.fuel)


__main__()