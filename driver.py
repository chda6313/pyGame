import os, sys, random

class toScrap():
	def __init__(self):
		self.distance = 1
		self.difficulty =1
		self.t = 1
		self.bounty = 1
		self.loot = {}
		self.m = 0
		
class ship():
	def __init__(self):
		self.fuel = 0
		self.armor = 0
		self.engines = 1
		self.weapons = {}
		self.lifeSupport = 1
		self.crewSize = 1
		self.Size = 1
		self.crewMembers = {}#list of crewmates
		self.shields = 1
		self.speed = 1
		self.turning = 1
		self.money = 50


class levelMap():
	def __init__(self):
		self.enemies = []
		self.enemyLocation = []
		self.objective = []
		self.vision = []
		self.traps = {}

class crewMate():
	def __init__(self):
		self.moveSpeed = 1
		self.weapon = 1
		self.carryWeight = 1
		self.health = 1
		self.armor = 1
		self.energy = 1









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


    #NATHAN save file CODE GOES HERE
file = open("PlayerShipSave.txt","w")

file.write("SAVE INFO GOES HERE")

file.close()


#countdown
#upgrade screen
