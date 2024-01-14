import random

rand = random.randint(1, 5)
rando = random.randint(1, 3)
list = ['sword', 'bow', 'bomb']
c = " ".join(list)
pHP = 1000
bHP = 1000
quizScore = 0
bCount = 2
shield = 1
arrows = 5
sword = 2

quizScore = 0
wrong = 0
question = [
    "What is 200 / 25?", "What is 25 x 9?", "What is 3 + 2(6/2)?",
    "What is 25 + 10(9/3)?", "What is 38 x 11?", "418/2",
    "What is 5 x 6(25/5)?", "What is 9 x 90", "What is 41 / 41?"
]
answers = [8, 225, 9, 55, 418, 209, 150, 810, 1]


def quiz(score):
  global quizScore
  global wrong
  for x in range(0, 3):
    yes = int(input(random.choice(question)))
    if yes in answers:
      quizScore = quizScore + score
      print(
          "Nice you answered correctly, you've earned 200 points. You now have",
          quizScore, "points")
    else:
      wrong = wrong + 1
      print("Ouch you got it wrong, you didn't earn any points")
      print("You still have", quizScore, "points")
  return score


if rando == 1:
  print("battle")
elif rando == 2:
  #steal()
  print("stuff got stolen")
else:
  print("quiz time!")
  quiz(200)


def steal():
  random.shuffle(list)  #error with no attribute
  a = list.pop()
  b = list.pop()
  c = " ".join(list)
  print("Uh-oh the boss has stolen", a, "and", b)
  print("You can only use", c)


def random():
  global rando
  if rando == 1:
    steal()
  elif rando == 2:
    quiz(200)
  else:
    battle()


def ending():
  global pHP
  global bHP
  b = False
  if pHP <= 0:
    print("You Died")
    if quizScore >= 800:
      print("Achievement Got! SMART")
  elif bHP <= 0:
    print("You have slain the beast, you are the worthy one")
    while pHP <= 0 or bHP <= 0:
      yon = input("Would you like to play again Y/N?")
      enput = yon.lower()
      if enput == "yes":
        start()
      elif enput == "no":
        print("Thanks for playing")
        pHP = 1
        bHP = 1


def start():
  list = ['sword', 'bow', 'bomb', 'shield']
  pHP = 1000
  bHP = 1000
  quizScore = 0
  bCount = 2
  shield = 1
  arrows = 5
  sword = 2
  print("                      Are You Worthy")
  print(
      "There is a loud noise in the distance, you are curious and decide to explore it'\nYou have encountered the boss which has 1000 health points, does 200 damage each attack and can randomly take any two of your weapons\nYou have 1000 health and are equipped with a sword which does 500 damage, a bow with 5, each arrow doing 20 damage and two explosives which do 200 each.You may also use your shield once when the boss attacks"
  )
  print(
      "Both you and the boss may have a chance to perform a critical hit which does 1.5x damage or miss your attack "
  )


def boss():
  global pHP
  global rand
  global shield  #fix yes or no selection (if type anything not yes and no continues the attack instead of asking for another input)

  q = input("Would you like to use your shield? Yes/No")
  keew = q.lower()
  if keew == "yes":
    if shield > 0:
      print("You have blocked the attack!, you still have", pHP, "health")
      shield = shield - 1
      random()
    else:
      print("Your shield is broken, you cannot use it!")
      if rand == 1:
        pHP = pHP - 0
        print("The boss has missed its hit! You have", pHP, "health left")
        random()
      if rand == 2:
        pHP = pHP - 300
        print("The boss has critically hit you! You have", pHP, "health left")
        random()
      if rand == 3 or rand == 4 or rand == 5:
        pHP = pHP - 200
        print("The boss has hit you! You have", pHP, "health left")
  elif keew == "no":
    print("You will not use your shield")
    if rand == 1:
      pHP = pHP - 0
      print("The boss has hit you! You have", pHP, "health left")
      random()
    if rand == 2:
      pHP = pHP - 300
      print("The boss has critically hit you! You have", pHP, "health left")
      random()
    if rand == 3 or rand == 4 or rand == 5:
      pHP = pHP - 200
      print("The boss has hit you! You have", pHP, "health left")
      random()
  ending()


def sword():  #fix bugs / after boss health is less than 0
  global pHP
  global bHP
  global sword
  global rand
  if bHP > 0 and pHP > 0:
    if rand == 1:
      bHP = bHP - 0
      print("You missed your attack!", bHP)
      if pHP > 0 and bHP > 0:
        boss()
      ending()
    elif rand == 2:
      bHP = bHP - 750
      print("You have critically hit the boss!", bHP)
      if pHP > 0 and bHP > 0:
        boss()
      ending()
    elif rand == 3 or rand == 4 or rand == 5:
      bHP = bHP - 500
      print("You have hit the boss!", bHP)
      if pHP > 0 and bHP > 0:
        boss()
      ending()
  ending()


def bomb():
  global pHP
  global bHP
  global bCount
  global rand
  while bHP >= 0 or pHP >= 0:
    if bCount > 0:
      if rand == 1:
        bHP = bHP - 0
        bCount = bCount - 1
        print("You missed your attack!", bHP, "You have", bCount, "bombs left")
        boss()
      elif rand == 2:
        bHP = bHP - 300
        bCount = bCount - 1
        print("You have critically hit the boss!", bHP, "You have", bCount,
              "bombs left")
        boss()
      elif rand == 3 or rand == 4 or rand == 5:
        bHP = bHP - 200
        bCount = bCount - 1
        print("You have hit the boss!", bHP, "You have", bCount, "bombs left")
        boss()

    else:
      print("You have no more bombs!")
      battle()


def bow():
  global pHP
  global bHP
  global arrows
  global rand
  if arrows > 0:
    if rand == 1:
      bHP = bHP - 0
      arrows = arrows - 1
      print("You missed your attack!", bHP, arrows)
      boss()
    elif rand == 2:
      bHP = bHP - 300
      arrows = arrows - 1
      print("You have critically hit the boss!", bHP, arrows)
      boss()
    elif rand == 3 or rand == 4 or rand == 5:
      bHP = bHP - 200
      arrows = arrows - 1
      print("You have hit the boss!", bHP, arrows)
      boss()
  else:
    print("You have no more bombs!")
    battle()


def battle():
  while pHP > 0 and bHP > 0:
    print("These are your possible weapons", (list))
    sel = input("You are attacking now, what would you like to use?")
    x = sel.lower()
    while x in list:
      if x == "sword":
        sword()
      elif x == "bow":
        bow()
      else:
        bomb()
    print("\nChoose a valid weapon")
  ending()


random()