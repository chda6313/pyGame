import os, sys, random, classes, qolFunctions


def __main__():
	#make a ship
	PlayerShip = classes.ship()
	PlayerShip.money = 500
	qolFunctions.saveGame(PlayerShip)
	PlayerShip.money = 300
	PlayerShip = qolFunctions.CharlieLoadGame()


__main__()