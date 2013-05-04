##copyright 2013 rachel kelly
##fightysandbox

import random
## necessary this guy below?  probably eventually.
from monsterlist.py import *

def main():
	global hero = input("what is your mighty and powerful call? ")
	print("greetings,",hero,".")
	if heroLevel > 40:
		monsterChoice = random.choice(monsters_level_four)
		if monsterChoice == bigboss:
			bigboss()
		elif monsterChoice == captainpantalon:
			captainpantalon()
		elif monsterChoice == sbvd:
			sbvd()
		else:
			# ????
	elif heroLevel > 30:
		monsterChoice = random.choice(monsters_level_three)
		if monsterChoice == yeti:
			yeti()
		elif monsterChoice == menacingvuvuzuela:
			menacingvuvuzuela()
		elif monsterChoice == orthoblap:
			orthoblap()
	elif heroLevel > 20:
		monsterChoice = random.choice(monsters_level_two)
		if monsterChoice == talkingyurt:
			talkingyurt()
		elif monsterChoice == bear:
			bear()
		elif monsterChoice == badwombat:
			badwombat()
	elif heroLevel > 10:
		monsterChoice = random.choice(monsters_level_one)
		if monsterChoice == squirrel:
			squirrel()
		elif monsterChoice == kindorc:
			kindorc()
		elif monsterChoice == bagodicks:
			bagodicks()
	elif heroLevel >= 1:
		monsterChoice = random.choice(monsters_level_oh)
		if monsterChoice == grue:
			grue()
		elif monsterChoice == babybadger:
			babybadger()
		elif monsterChoice == tinybutt:
			tinybutt()
	else:
		print("ERROR")
	print("\nYou encounter a",monster,"!")
	while currentMonsterHP >= 0:
		battleMenu(monsterChoice)
		## take some amt from currentmonsterhp
		## also gotta have some module for the monster hitting
		random.randint() #??

def battleMenu():
	menuChoice = input("do you want to hit via (m)elee, cast a (s)pell, or use an (i)tem?")
	if menuChoice == m:
		melee()
	elif menuChoice == s:
		magic()
	elif menuChoice == i:
		items()
	else:
		battleMenu()


def magic(monster):
	spellDict = {"fire","ice","lightning"}
	spell = input("what spell will you cast?")
	if spell in spellDict:
		##if spell == "fire"? can I do this?
		##not sure if I even need a dict here.  could just be a bunch of if/elifs?
		currentHP = monsterHP
		while currentHP >= 0:
			print("you cast",spell,"on",monster".")






def items():
	itemDict = dict()
	file = open("items.txt","r")

def hit(monsterHP):
	print("your sword connects!")
	damage = random.randint(1,5)

def miss(monsterHP):
	print("you miss.  sorry",hero,".")
	battleMenu()


def melee(monsterHP):
	while monsterHP > 0:
		print("you swing yer sword")
		choice = random.randint(0,3)
		if choice == 3:
			hit(monsterHP)
		elif choice == 0 or choice == 1 or choice == 2:
			miss(monsterHP)
