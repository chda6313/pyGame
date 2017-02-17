import os, sys, random, classes, qolFunctions


def __main__():


##################################################HEY CHARLIE using money instead of fuel breaks the load function for some reason
##################################################Works with fuel but not money. Weird.

#make a ship
	PlayerShip = classes.ship()
	PlayerShip.name = "Serenity"
#give it attributes
	PlayerShip.money = 100
#save game
	qolFunctions.saveGame(PlayerShip)
#play game
	PlayerShip.money = 0
#load save file
	PlayerShip = qolFunctions.loadGame("Serenity_Save.txt")
#did it work?
	print(PlayerShip.fuel)


#This will create a random male name
	#name = qolFunctions.maleNameGen()
	#print("Here is a male name:")
	#print(name,"\n")

#This will create a random female name
	#name = qolFunctions.femaleNameGen()
	#print("And here is a female one:")
	#print(name,"\n")


#Playing with levelCreator
	#qolFunctions.levelCreator("Level1.txt")



__main__()