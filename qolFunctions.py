import os, sys, classes, random, requests, re
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

def loadGame(shipToOpen):####Run this like so: qolFunctions.loadGame("savefile.txt")

	file = open(shipToOpen,"r")
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
			name = re.sub('1', '', name)
			name = re.sub('/name/', '', name)
			name = re.sub('-', '', name)
			name = re.sub('2', '', name)
	return name.title()

def levelCreator(mapToOpen):####Run this like so: qolFunctions.levelCreator("thisisthemap.txt")
	file = open(mapToOpen, "r")
	vertCount = -1
	mapRows = []
	for line in file:
		vertCount = vertCount + 1
		rowSquares = []
		workingTile = line
		workingTile = [x for x in workingTile.split(' ')]
		horizCount = -1
		for x in workingTile:
			horizCount = horizCount + 1
			if x == '0':
				workingSquare = classes.mapSquare()
				workingSquare.terrain = "path"
				workingSquare.coordinates = [horizCount,vertCount]
				rowSquares.append(workingSquare)
			if x == '1':
				workingSquare = classes.mapSquare()
				workingSquare.terrain = "wall"
				workingSquare.coordinates = [horizCount,vertCount]
				workingSquare.passable = (0)
				rowSquares.append(workingSquare)
			if x == '2':
				workingSquare = classes.mapSquare()
				workingSquare.terrain = "water"
				workingSquare.coordinates = [horizCount,vertCount]
				rowSquares.append(workingSquare)
			if x == '3':
				workingSquare = classes.mapSquare()
				workingSquare.terrain = "spawn"
				workingSquare.coordinates = [horizCount,vertCount]
				rowSquares.append(workingSquare)
		mapRows.append(rowSquares)
	file.close()
	return mapRows

#ToDo Still need to make this normalize the length of printed attributes
def mapDump(map,attribute): ##### Run this like so: mapDump(whateveryoumadelevelCreatormake,"attributeyouwantdumped")
	count = -1
	for lists in map:
		row = []
		count = count + 1
		for squares in lists:
			if squares.coordinates[1] == count:
				row.append(getattr(squares, attribute))
		print(row)
