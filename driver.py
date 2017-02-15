import os, sys, random, classes, qolFunctions


def __main__():
	PlayerShip = classes.ship()
	PlayerShip.money = 600
	qolFunctions.saveGame(PlayerShip)

__main__()