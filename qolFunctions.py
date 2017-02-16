import os, sys, random, classes, random, requests, re
from bs4 import BeautifulSoup

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

	file = open("Player Name_Save.txt","r") #########<---------HEY NATHAN NEEDS TO MAKE THIS SUCK LESS STILL
	loadingShip = classes.ship()
	count = 0
	for e in file:
		count = count+1
		if count == 2:
			loadingShip.name = e
		if count == 4:
			loadingShip.fuel = e
		if count == 6:
			loadingShip.armor = e
		if count == 8:
			loadingShip.engines = e
		if count == 10:
			loadingShip.weapons = e
		if count == 12:
			loadingShip.lifeSupport = e
		if count == 14:
			loadingShip.crewSize = e
		if count == 16:
			loadingShip.size = e
		if count == 18:
			loadingShip.crewMembers = e
		if count == 20:
			loadingShip.shields = e
		if count == 22:
			loadingShip.speed = e
		if count == 24:
			loadingShip.turning = e
		if count == 26:
			loadingShip.money = e

	file.close()

	
	return loadingShip

#####Nathan's Fancy Pantsy Name Generator
def maleNameGen():
	rollthedice = random.randint(1,3)
	if rollthedice == 1:
		#This file is where we can add our own names. Currently, it will pick our choice names a fifth of the time.
		file = open("cool_male_names.txt","r")
		nameList = []
		for line in file:
			nameList.append(line)
		name = random.choice(nameList)
		name = re.sub('\n', '', name)
		file.close()
###Holy crap I did it
###I think I'll outsource the random name generator
###Idea for making this work offline:
###Loop through website like 5,000 times, create a text doc with all results, and delete duplicates
	else:
		url = "http://www.behindthename.com/random/random.php?number=1&gender=m&surname=&norare=yes&nodiminutives=yes&all=no&usage_eng=1"
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text, "html.parser")
		for grabbedName in soup.findAll('a', {'class': 'plain'}):
			name = grabbedName.get('href')
			#shit keeps popping up from weird characters, this is to iron it out:
			name = re.sub('/name/', '', name)
			name = re.sub('-2', '', name)
			name = re.sub('-1', '', name)

	return name.title()

def femaleNameGen():
	rollthedice = random.randint(1,4)
	if rollthedice == 1:
		file = open("cool_female_names.txt","r")
		nameList = []
		for line in file:
			nameList.append(line)
		name = random.choice(nameList)
		name = re.sub('\n', '', name)
		file.close()
	else:
		url = "http://www.behindthename.com/random/random.php?number=1&gender=f&surname=&norare=yes&nodiminutives=yes&all=no&usage_eng=1"
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text, "html.parser")
		for grabbedName in soup.findAll('a', {'class': 'plain'}):
			name = grabbedName.get('href')
			#shit keeps popping up from weird characters, this is to iron it out:
			name = re.sub('/name/', '', name)
			name = re.sub('-2', '', name)
			name = re.sub('-1', '', name)

	return name.title()

######Nathan tried.
#def levelCreator():
	#file = open("Level1.txt", "r")
	#squareAtts = []
	#tileList = []
	#count = 0
	#for line in file:
		#count = count + 1
		#workingTile = line
		#workingTile = [x for x in workingTile.split(' ')]
		#for x in workingTile:
			#tileObject = classes.mapSquare()
			#tileObject.number = x
			#tileObject.terrain = x
			#tileObject.items = x
			#tileObject.altitude = x
			#tileObject.entities = x
			#tileObject.passable = x
			#tileObject.lineBreak = x
		#tileList.append(tileObject)
		#print(workingTile)
	#print(tileList)

