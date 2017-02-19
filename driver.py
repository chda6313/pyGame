import os, sys, random, classes, qolFunctions


def __main__():

#make a ship
	#PlayerShip = classes.ship()
	#PlayerShip.name = "Serenity"
#give it attributes
	#PlayerShip.money = 100
#save game
	#qolFunctions.saveGame(PlayerShip)
#play game
	#PlayerShip.money = 0
#load save file
	#PlayerShip = qolFunctions.loadGame("Serenity_Save.txt")
#did it work?
	#print(PlayerShip.money)

#This will create a random male name
	#name = qolFunctions.maleNameGen()
	#print("Here is a male name:")
	#print(name,"\n")

#This will create a random female name
	#name = qolFunctions.femaleNameGen()
	#print("And here is a female one:")
	#print(name,"\n")

#Playing with levelCreator
	map = qolFunctions.levelCreator("Level1.txt")
#Trying to dump map
	#qolFunctions.mapDump(map,"coordinates")

#Make crew member
	Nathan = classes.crewMate()
#Move him
	qolFunctions.moveCrewMate(Nathan,"[3, 4]",map)

	qolFunctions.mapDump(map,"entities")

	print("^^^^^^^^ This is the mapDump for entities in our map")

__main__()