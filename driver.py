import os, sys, random, classes, qolFunctions


def __main__():
	#make a ship
	PlayerShip = classes.ship()
	#it has 500 money
	PlayerShip.money = 600
	#Let's save that
	qolFunctions.saveGame(PlayerShip)
	#Oh no, we lost 200 money
	PlayerShip.money = 300
	#so let's load our last save
	PlayerShip = qolFunctions.loadGame()
	#Oh good, it's all here
	print(str(PlayerShip.money))

__main__()