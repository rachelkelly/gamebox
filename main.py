import random

def main():
	enemyHP = 100
	hero = input("what is your mighty and powerful call? ")
	print("greetings,",hero,".")

def magic():
	spellDict = {"fire","ice","lightning"}
	spell = input("what spell will you cast?")
	if spell in spellDict:
		##if spell == "fire"? can I do this?
		##not sure if I even need a dict here.  could just be a bunch of if/elifs?

def items():
	


def battleMenu():
	battleChoice = input("do you want to (h)it with your sword, cast (m)agic, or use an (i)tem? ")
	if battleChoice == "h":
		melee()
	elif battleChoice == "m":
		magic()
	elif battleChoice == "i":
		items()
	else:
		print("try again bro")
		battleMenu()

def hit(enemyHP):
	print("your sword connects!")
	damage = random.randint(1,5)

def miss(enemyHP):
	print("you miss.  sorry",hero,".")
	battleMenu()


def melee(enemyHP):
	while enemyHP > 0:
		print("you swing yer sword")
		choice = random.randint(0,3)
		if choice == 3:
			hit()
		elif choice == 0 or choice == 1 or choice == 2:
			miss()
