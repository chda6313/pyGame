import os, sys, random, classes, qolFunctions


def __main__():
#make a ship
	PlayerShip = classes.ship()
#give it attributes
	PlayerShip.fuel = 100
#save game
	qolFunctions.saveGame(PlayerShip)
#play game
	PlayerShip.fuel = 0
#load save file
	PlayerShip = qolFunctions.loadGame()
#did it work?
	print(PlayerShip.fuel)


#This will create a random male name
	name = qolFunctions.maleNameGen()
	print("Here is a male name:")
	print(name,"\n")

#This will create a random female name
	name = qolFunctions.femaleNameGen()
	print("And here is a female one:")
	print(name,"\n")

#Playing with levelcreator
	qolFunctions.levelCreator()


__main__()