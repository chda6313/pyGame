import os, sys, random, classes

def saveGame(PlayerShip = classes.ship()):

	saveName = PlayerShip.name + "_Save.txt"
	file = open(saveName,"w")
	file.write("Name: " + "\n" + str(PlayerShip.name) + "\n")
	file.write("Fuel: " + "\n" + str(PlayerShip.fuel) + "\n")
	file.write("Armor: " + "\n" + str(PlayerShip.armor) + "\n")
	file.write("Engines: " + "\n" + str(PlayerShip.engines) + "\n")
	file.write("Weapons: " + "\n" + str(PlayerShip.weapons) + "\n")
	file.write("LifeSupport: " + "\n" + str(PlayerShip.lifeSupport) + "\n")
	file.write("CrewSize: " + "\n" + str(PlayerShip.crewSize) + "\n")
	file.write("Size: " + "\n" + str(PlayerShip.size) + "\n")
	file.write("CrewMembers: " + "\n" + str(PlayerShip.crewMembers) + "\n")
	file.write("shields: " + "\n" + str(PlayerShip.shields) + "\n")
	file.write("speed: " + "\n" + str(PlayerShip.speed) + "\n")
	file.write("turning: " + "\n" + str(PlayerShip.turning) + "\n")
	file.write("money: " + "\n" + str(PlayerShip.money) + "\n")

	file.close()

def loadGame():
	#NATHAN WRITE THIS AS WELL
	
	#should create a new ship() with the proper attributes, and spit it out as a return value
	file = open("Player Name_Save.txt","r")
	loadingShip = classes.ship()
	count = 0
	for e in file:
			count =+1
	if count ==2:
			loadingShip.name = e
	if count ==4:
			loadingShip.fuel = e


	file.close()

	
	return loadingShip
