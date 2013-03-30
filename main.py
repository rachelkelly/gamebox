import random
global hero = input("what is your mighty and powerful call? ")
print("greetings,",hero,".")
print("\nYou encounter a",monster,"!")

#### heyo!  all these monster defs, I don't think the internal HP
#### values need to have different variables, 'cos they're not globals!

def monsterOne():
	monsterHP = 8

def monsterTwo():
	monsterHP = 13

def monsterThree():
	monsterHP = 21

def monsterFour():
	monsterHP = 34

def monsterFive():
	monsterHP = 55

def main():
	monster = random.randint(0,4)
	if monster == 0:
		monsterLevelOne()
	elif monster == 1:
		monsterLevelTwo()
	elif monster == 2:
		monsterLevelThree()


def monsterLevelOne():
	monsterHP = random.randrange(13,21)
	monsterHP

def monsterLevelTwo():
	monsterHP = random.randrange(21,34)

def magic(monster):
	spellDict = {"fire","ice","lightning"}
	spell = input("what spell will you cast?")
	if spell in spellDict:
		##if spell == "fire"? can I do this?
		##not sure if I even need a dict here.  could just be a bunch of if/elifs?
		print("you cast",spell,"on",monster".")

def items():
	itemDict = dict()
	file = open("items.txt","r")


def battleMenu():
	battleChoice = input("do you want to (h)it with your sword, cast (m)agic, or use an (i)tem? ")
	if battleChoice == "h":
		melee(monster)
	elif battleChoice == "m":
		magic(monster)
	elif battleChoice == "i":
		items()
	else:
		print("try again",hero,".")
		battleMenu()

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
