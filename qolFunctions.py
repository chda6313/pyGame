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
	file = open("Player Name_save.txt","r")

	loadingShip = classes.ship()
	loadingShip.name = file.readline(2)
	loadingShip.fuel = file.readline(4)
	loadingShip.armor = file.readline(6)
	loadingShip.engines = file.readline(8)
	loadingShip.weapons = file.readline(10)
	loadingShip.lifeSupport = file.readline(12)
	loadingShip.crewSize = file.readline(14)
	loadingShip.Size = file.readline(16)
	loadingShip.crewMembers = file.readline(18)
	loadingShip.shields = file.readline(20)
	loadingShip.speed = file.readline(22)
	loadingShip.turning = file.readline(24)
	loadingShip.money = file.readline(26)

	file.close()

	
	return loadingShip
