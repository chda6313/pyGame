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
		self.name = "Player Name"


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
		self.carryWeight = 10
		self.health = 5
		self.armor = 1
		self.energy = 3




