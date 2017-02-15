import os, sys, random, classes

if __name__ == "__main__":
	#make a new ship with name playership
	PlayerShip = ship()

	#check how much money we have
	print(PlayerShip.money)

	#cheat and add some more money
	PlayerShip.money += 500

	#check again:


	#make an enemy ship
	e1 = ship()
	#give it some loot
	e1.money = 200

	#when the player kills the ship and loots we should have a function that does:
	PlayerShip.money += e1.money
	e1.money = 0

	#we should have made some money, lets check:
	print(PlayerShip.money)


	#this is an example of how to call a method from an external source
	import first
	first.printinfo()


def saveGame(PlayerShip = ship()):
	#NATHAN save file CODE GOES HERE
	
	#what if we want more than one save?
	#try: savename = PlayerShip.name + "_Save.txt"
	#note: you might need to implement "self.name" in classes.py > ship() > __init__()
	
	
	file = open("PlayerShipSave.txt","w")

	file.write(str(PlayerShip.fuel))
	file.write(str(PlayerShip.armor))
	file.write(str(PlayerShip.engines))
	file.write(str(PlayerShip.weapons))
	file.write(str(PlayerShip.lifeSupport))
	file.write(str(PlayerShip.crewSize))
	file.write(str(PlayerShip.Size))
	file.write(str(PlayerShip.crewMembers))
	file.write(str(PlayerShip.shields))
	file.write(str(PlayerShip.speed))
	file.write(str(PlayerShip.turning))
	file.write(str(PlayerShip.money))

	file.close()

	file = open("PlayerShipSave.txt", "r")

	print (file.read())

def loadGame(shipName):
	#NATHAN WRITE THIS AS WELL
	
	#should create a new ship() with the proper attributes, and spit it out as a return value
	
	loadingShip = ship()

	###
	###
	###
	
	return loadingShip
