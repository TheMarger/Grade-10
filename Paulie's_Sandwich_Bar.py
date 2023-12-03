import os, time, random, sys

def GameMenu():
    global Shop_Rating
    global multiplier
    global cash
    global seperater
    global colors
    global playing
    playing = True
    while playing:
        os.system('cls')
        print(f"""\n{colors.BOLD + colors.UNDERLINE + "Welcome To Paulie's Sandwich bar!" + colors.END}\n 
    Order Station      {colors.BOLD + "Enter [O]" + colors.END}
    {seperater}
    Upgrades           {colors.BOLD + "Enter [U]" + colors.END}
    {seperater}
    Rewards            {colors.BOLD + "Enter [R]" + colors.END}
    {seperater}   
    Settings           {colors.BOLD + "Enter [S]" + colors.END}
    {seperater} 
    Information        {colors.BOLD + "Enter [I]" + colors.END}
    {seperater}
    Exit               {colors.BOLD + "Enter [X]" + colors.END}
                                            Cash: {colors.GREEN + colors.BOLD + str(cash) + colors.END}
                                            Multiplier: {colors.PURPLE + colors.BOLD + str(multiplier) + colors.END}
                                            Shop Rating: {colors.CYAN + colors.BOLD + str(Shop_Rating) + colors.END}\n""")
        val = input("> ")
        if val == 'O' or val == 'o':
            DoOrderStation()
        elif val == 'S' or val == 's':
            DoSettings()
        elif val == 'I' or val == 'i':
            DoInformation()
        elif val == 'X' or val == 'x':
            exit()
        elif val == "U" or val == 'u':
            DoUpgrades()
        elif val == 'R' or val == 'r':
            DoRewards()
        else:
            print("Please enter a defined option")
            time.sleep(1)
            
def DoUpgrades():
    global Shop_Rating
    global playing
    global multiplier
    while playing == True:
        os.system('cls')
        print(f"""\n
Upgrade cash multiplier. (Current: {multiplier}), {colors.BOLD + 'enter [M]' + colors.END}
Upgrade Shop Rating. (Current: {Shop_Rating}), {colors.BOLD + 'enter [S]' + colors.END}    
To exit, {colors.BOLD + 'enter [X]' + colors.END}
          """)
        val = input("> ")
        if val == 'M' or val == 'm':
            if multiplier == 'LOCKED':
                multiplier = 1
            else:
                multiplier += 1
        elif val == 'S' or val == 's':
            if Shop_Rating == 'LOCKED':
                Shop_Rating = '*'
            elif Shop_Rating == '* * * * *':
                print("Max Shop Rating reached")
                time.sleep(1)
            else:
                Shop_Rating += ' *'
        elif val == 'X' or val == 'x':
            GameMenu()
        else:
            print("Enter a defined option")
            time.sleep(1)
            
def DoRewards():
    pass

def DoInformation():
    global playing
    global colors
    while playing:
        os.system('cls')
        print(f"""\nChoose Inquiry:\n
{colors.BOLD + colors.UNDERLINE + 'Order Station:' + colors.END} enter [O]
{colors.BOLD + colors.UNDERLINE + 'Upgrades:' + colors.END} enter [U]
{colors.BOLD + colors.UNDERLINE + 'Rewards:' + colors.END} enter [R]  
{colors.BOLD + colors.UNDERLINE + 'Settings' + colors.END} enter [S]
{colors.BOLD + colors.UNDERLINE + 'Information' + colors.END} enter [I]
{colors.BOLD + colors.UNDERLINE + 'Cash' + colors.END} enter [C]
{colors.BOLD + colors.UNDERLINE + 'Multipliers' + colors.END} enter [M]
{colors.BOLD + colors.UNDERLINE + 'Shop Rating' + colors.END} enter [H]
              """)
        inquiry = input("> ")
        if inquiry == 'O' or inquiry == 'o':
            os.system('cls')
            print(f"""
{colors.BOLD + colors.UNDERLINE + 'Order Station:' + colors.END} \n
The order station is where the customer selected order is broken into 
sections, with each ingrediant having it's own random difficulty. This difficulty 
will be averaged by default, and be displayed at the top of the screen (this can 
be shanged in settings to show the numeral level of difficulty for more precision). 
The game will wait for you to input that you're ready and begin to ask you a random
math question based on the formula for each ingrediant difficulty. This gamemode is 
where you can earn cash, shop rating, and levels for your restaurant. Specialized 
gamemodes may vary providing their own synopsis.               
              
              """)
            WhatNext = input("Go Back? (Y/N): ")
            if WhatNext == "N" or WhatNext == "n":
                GameMenu()
            else:
                pass

def DoSettings():
    global OverallRating
    global OverallScore
    global playing
    global colors
    global ChangeAVGDisplay
    while playing == True:
        os.system('cls')
        if ChangeAVGDisplay == False:
            ScaleForm = "Average"
        else:
            ScaleForm = "Numerical"
        print(f"""\n
Change average difficulty scale form (Current: {ScaleForm}), {colors.BOLD + 'enter [N]' + colors.END}    
To exit, {colors.BOLD + 'enter [X]' + colors.END}
          """)
        val = input("> ")
        if val == 'N' or val == 'n':
            if ChangeAVGDisplay == False:
                ChangeAVGDisplay = True
            else:
                ChangeAVGDisplay = False
        elif val == 'X' or val == 'x':
            GameMenu()
        else:
            print("Enter a defined option")
            time.sleep(1)
            
def DoOrder(Menu):
    global OverallScore
    global OverallRating
    global ratings
    order = []
    ratings = []
    
    breadRAW = random.choice(Menu.breads)
    bread = breadRAW[0]
    ratings.append(breadRAW[1])
    order.append(bread)
    
    vegetablesRAW = random.choice(Menu.vegetables)
    vegetables = vegetablesRAW[0]
    ratings.append(vegetablesRAW[1])
    order.append(vegetables)
    
    saucesRAW = random.choice(Menu.sauces)
    sauces = saucesRAW[0]
    ratings.append(saucesRAW[1])
    order.append(sauces)
    
    meatsRAW = random.choice(Menu.meats)
    meats = meatsRAW[0]
    ratings.append(meatsRAW[1])
    order.append(meats)
    
    OverallScore = 0
    OverallRating = 0
    
    for i in range(len(ratings)):
        OverallScore += ratings[i]
    
    if OverallScore <= 5:
        OverallRating = 0
    elif OverallScore > 5 and OverallScore < 9:
        OverallRating = 1
    else:
        OverallRating = 2
    
    for i in range(len(ratings)):
        if ratings[i] == 1:
            ratings[i] = colors.BOLD + colors.GREEN + 'Easy' + colors.END
        elif ratings[i] == 2:
            ratings[i] = colors.BOLD + colors.YELLOW + 'Medium' + colors.END
        else:
            ratings[i] = colors.BOLD + colors.RED + 'Hard' + colors.END
        
    return order
    

def DoOrderStation():
    os.system('cls')
    global cash
    global seperater
    global Menu
    global playing
    global colors
    global level
    global ratings
    global OverallRating
    global OverallScore
    global ChangeAVGDisplay
    order = DoOrder(Menu)
    difficulties = [['Easy', 1], ['Medium', 2], ['Hard', 3]]
    DifficultyRaw = difficulties[OverallRating]
    level = DifficultyRaw[1]
    Difficulty = DifficultyRaw[0]
    if ChangeAVGDisplay == False:
        if level == 1:
            print(f"\n\nDiffuculty: {colors.BOLD + colors.GREEN + Difficulty + colors.END}\n{seperater}")
        elif level == 2:
            print(f"\n\nDiffuculty: {colors.BOLD + colors.YELLOW + Difficulty + colors.END}\n{seperater}")
        else:
            print(f"\n\nDiffuculty: {colors.BOLD + colors.RED + Difficulty + colors.END}\n{seperater}")
    else:
        if level == 1:
            print(f"\n\nDiffuculty: {colors.BOLD + colors.GREEN + str(OverallScore) + colors.END}\n{seperater}")
        elif level == 2:
            print(f"\n\nDiffuculty: {colors.BOLD + colors.YELLOW + str(OverallScore) + colors.END}\n{seperater}")
        else:
            print(f"\n\nDiffuculty: {colors.BOLD + colors.RED + str(OverallScore) + colors.END}\n{seperater}")
    
    print(f"""\n Customer Order: \n
Bread:  {order[0]} [{ratings[0]}]
Vegetables:  {order[1]} [{ratings[1]}]
Sauces:  {order[2]} [{ratings[2]}]
Meats:  {order[3]} [{ratings[3]}]\n
{seperater}""")
    
    while playing == True:
        print(colors.CYAN + colors.BOLD + "[S] - Variables" + colors.END)
        print(colors.RED + colors.BOLD + "\n[R] - Ready" + colors.END)
        print(colors.BOLD + '\n[X] - Exit' + colors.END)
        val = input("> ")
        if val == 'X' or val == 'x':
            GameMenu()
        elif val == 'R' or val == 'r':
            delete_multiple_lines(6)
            DoSandwichMaker()
        elif val == 'S' or val == 's':
            delete_multiple_lines(6)
            DoVariables()
        else:
            print("Please enter a defined option")
            time.sleep(1)
            delete_multiple_lines(7)
        
def DoSandwichMaker():
    global cash
    global cash_color
    global ratings
    global playing
    global SeshCash
    global multiplier
    SeshCash = 0
    CorrectAns = []
    NumCorrect = 0 
    for i in range(len(ratings)): 
        operation = ['+', '-', '*', '/']
        num1 = random.randint(1, 100) 
        num2 = random.randint(1, 100)
        num3 = random.randint(1, 100)
        print(f"Ingredient {i+1} Level: {ratings[i]}")
        if ratings[i] == '\x1b[1m\x1b[92mEasy\x1b[0m':
            opr = random.choice(operation[0:2])
            if opr == operation[0]:
                answer = num1 + num2
            else:
                answer = num1 - num2
            print(f"{num1} {opr} {num2}")
        elif ratings[i] == '\x1b[1m\x1b[93mMedium\x1b[0m':
            opr = random.choice(operation[2:4])
            if opr == operation[2]:
                answer = num1 * num2
            else:
                answer = num1 / num2
            print(f"{num1} {opr} {num2}")
        else:
            opr1 = random.choice(operation)
            opr2 = random.choice(operation)
            if opr1 == operation[0]:
                answer1 = num1 + num2
            elif opr1 == operation[1]:
                answer1 = num1 - num2
            elif opr1 == operation[2]:
                answer1 = num1 * num2
            else:
                answer1 = num1 / num2
            if opr2 == operation[0]:
                answer2 = answer1 + num3
            elif opr2 == operation[1]:
                answer2 = answer1 - num3
            elif opr2 == operation[2]:
                answer2 = answer1 * num3
            else:
                answer2 = answer1 / num3
            answer = answer2
            print(f"({num1} {opr1} {num2}) {opr2} {num3}")
        
        while playing:    
            try:
                response = float(input("Answer: "))
            except:
                print("Please input a number value")
                time.sleep(2)
                delete_multiple_lines(2)
            else:
                break
                
        if response == answer.__round__(2): 
            print(f"Good Job!\n{cash_color} + 1")
            SeshCash += 1
            NumCorrect += 1
            CorrectAns.append(1)
            time.sleep(2)
            delete_multiple_lines(5)
        else:
            print(("Incorrect!"))
            CorrectAns.append(0)
            time.sleep(2)
            delete_multiple_lines(4)
    else:
        os.system("cls")
        
        SeshMultiplier = 0
        
        for i in range(len(CorrectAns)):
            if CorrectAns[i] == 1:
                CorrectAns[i] = colors.BOLD + colors.GREEN + "COMPLETE" + colors.END
            else:
                CorrectAns[i] = colors.BOLD + colors.RED + "FAILED" + colors.END
                
        if NumCorrect <= 1:
            SeshMultiplier = 1
        elif NumCorrect == 2:
            SeshMultiplier = 1.25
        elif NumCorrect == 3:
            SeshMultiplier = 1.5
        else:
            SeshMultiplier = 2 
        
        if multiplier != 'LOCKED':
            TotalSeshCash = (SeshCash * SeshMultiplier) * multiplier
            cash += (SeshCash * SeshMultiplier) * multiplier
        else:
            TotalSeshCash = SeshCash * SeshMultiplier
            cash += SeshCash * SeshMultiplier
        
        print(f"""\nOrder Complete!
\nOrder Invoice:\n
Bread:  {CorrectAns[0]}
{seperater} 
Vegetables: {CorrectAns[1]}
{seperater}
Meat:   {CorrectAns[2]}
{seperater}
Sauce:  {CorrectAns[3]}
              """)
        
        if NumCorrect < len(Shop_Rating.split()) and Shop_Rating != "LOCKED":
            print(f"Customer Satisfaction Score = {colors.BOLD + colors.RED + str(NumCorrect) + colors.END}")
        elif NumCorrect == len(Shop_Rating.split()) and Shop_Rating != "LOCKED":
            print(f"Customer Satisfaction Score = {colors.BOLD + colors.YELLOW + str(NumCorrect) + colors.END}")
        else:
            print(f"Customer Satisfaction Score = {colors.BOLD + colors.GREEN + str(NumCorrect) + colors.END}")
            
        print(f"""{seperater}
Session Cash Multiplier = {colors.BOLD + colors.PURPLE + str(SeshMultiplier) + colors.END}
Game Cash Multiplier = {colors.BOLD + colors.PURPLE + str(multiplier) + colors.END}
{seperater}
Total Cash Earned = {colors.BOLD + colors.GREEN + str(TotalSeshCash) + colors.END}

              """)
        
        
        while playing:
            PlAgn = input("Play again? (Y/N): ")
            if PlAgn == "Y" or PlAgn == 'y':
                DoOrderStation()
            elif PlAgn == "N" or PlAgn == 'n':
                GameMenu()
            else:
                print("Please enter a defined option")
                time.sleep(2)
                delete_multiple_lines(2)
                
def DoVariables():
    pass

class Menu:
    breads = [['regular', 1], ['sesame', 2], ['old-fashioned',3], ['4-cheese', 1], ['italian', 2], ['Chicago style', 3]]
    vegetables = [['tomato', 1], ['cucumber', 2], ['carrot', 3], ['peppers', 1], ['jalapeno', 2], ['onion', 3]]
    sauces = [['mayonnaise', 1], ['teriyaki', 2], ['ketchup', 3], ['mustard', 1], ['relish', 2], ['Hot sauce', 3]]
    meats = [['salami', 1], ['pepperoni', 2], ['chicken', 3], ['beef', 1], ['pork', 2], ['bacon', 3]]

class colors:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def delete_multiple_lines(n=1):
    """Delete the last line in the STDOUT."""
    for _ in range(n):
        sys.stdout.write("\x1b[1A")  # cursor up one line
        sys.stdout.write("\x1b[2K")  # delete the last line

seperater = "----------------------------------------------------------------"
cash = 0
multiplier = 'LOCKED'
Shop_Rating = "LOCKED"
cash_color = colors.GREEN + colors.BOLD + "Cash:" + colors.END 
ChangeAVGDisplay = False
print("POO")   
#start = GameMenu()

