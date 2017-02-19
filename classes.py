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
		self.size = 1
		self.crewMembers = {}#list of crewmates
		self.shields = 1
		self.speed = 1
		self.turning = 1
		self.money = 50
		self.name = "Player Name"

class levelMap():
	def __init__(self):
		self.height = 30
		self.width = 30
		self.name = "Map Name"

class mapSquare():
	def __init__(self):
		self.coordinates = [0,0]
		self.terrain = "void"
		self.items = 0
		self.entities = []
		self.passable = 1

class crewMate():
	def __init__(self):
		self.moveSpeed = 1
		self.weapon = 1
		self.carryWeight = 10
		self.health = 5
		self.armor = 1
		self.energy = 3
		self.location = [0,0]
		self.square = mapSquare

class enemy():
	def __init__(self):
		self.moveSpeed = 1
		self.weapon = 1
		self.health = 5
		self.armor = 1
		self.energy = 3
		self.location = [0,0]
		self.square = mapSquare




