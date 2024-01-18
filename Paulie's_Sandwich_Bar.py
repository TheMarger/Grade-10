#import all required modules 
import os, time, random, sys, re

#function for game menu
def GameMenu():
    # Define global variables that will be used in this function
    global Shop_Rating
    global multiplier
    global cash
    global seperater
    global colors
    global playing, Store_Keybind, Order_Station_Keybind, Upgrades_Keybind,Rewards_Keybind,Settings_Keybind
    global Name, customers, FirstOpening,Information_Keybind
    # Set playing check to True to enter the main game loop
    playing = True
    # Start the main game loop
    while playing:
        # clear the console screen
        os.system('cls')

        # Check if DisplayCustomers is True
        if DisplayCustomers == True:
            # Display the menu with customers
            print(f"""\n{colors.BOLD + colors.UNDERLINE + "Welcome To " + Name + " Sandwich bar!" + colors.END}\n
Store              {colors.BOLD + "Enter ["+Store_Keybind+"]" + colors.END}
{seperater}
Order Station      {colors.BOLD + "Enter ["+Order_Station_Keybind+"]" + colors.END}
{seperater}
Upgrades           {colors.BOLD + "Enter ["+Upgrades_Keybind+"]" + colors.END}
{seperater}
Rewards            {colors.BOLD + "Enter ["+Rewards_Keybind+"]" + colors.END}
{seperater}   
Settings           {colors.BOLD + "Enter ["+Settings_Keybind+"]" + colors.END}
{seperater} 
Information        {colors.BOLD + "Enter ["+Information_Keybind+"]" + colors.END}
{seperater}
Exit               {colors.BOLD + "Enter [X]" + colors.END}
                                        Cash: {colors.GREEN + colors.BOLD + str(cash.__round__(2)) + colors.END}
                                        Multiplier: {colors.PURPLE + colors.BOLD + str(multiplier) + colors.END}
                                        Shop Rating: {colors.CYAN + colors.BOLD + str(Shop_Rating) + colors.END}\n

                                        |------------------------
                                        |
                                        | Current Customers: {customers}
                                        |
                                        """)
        else:
            # Display the menu without customers
            print(f"""\n{colors.BOLD + colors.UNDERLINE + "Welcome To " + Name + " Sandwich bar!" + colors.END}\n
Store              {colors.BOLD + "Enter ["+Store_Keybind+"]" + colors.END}
{seperater}
Order Station      {colors.BOLD + "Enter ["+Order_Station_Keybind+"]" + colors.END}
{seperater}
Upgrades           {colors.BOLD + "Enter ["+Upgrades_Keybind+"]" + colors.END}
{seperater}
Rewards            {colors.BOLD + "Enter ["+Rewards_Keybind+"]" + colors.END}
{seperater}   
Settings           {colors.BOLD + "Enter ["+Settings_Keybind+"]" + colors.END}
{seperater} 
Information        {colors.BOLD + "Enter ["+Information_Keybind+"]" + colors.END}
{seperater}
Exit               {colors.BOLD + "Enter [X]" + colors.END}
                                        Cash: {colors.GREEN + colors.BOLD + str(cash.__round__(2)) + colors.END}
                                        Multiplier: {colors.PURPLE + colors.BOLD + str(multiplier) + colors.END}
                                        Shop Rating: {colors.CYAN + colors.BOLD + str(Shop_Rating) + colors.END}\n""")
        # Get user input
        val = input("> ")
        # Check if it's the first time the menu is opened
        if FirstOpening == True:
            # If not in the store, prompt the user to set up the store first
            if val != Store_Keybind and val != Store_Keybind.lower():
                print("Please set up store first!")
                time.sleep(1)
                # Restart the game menu
                GameMenu()
            else:
                # If in the store, go to the store menu
                DoStore()
        # Check if the user wants to go to the order station
        if val == Order_Station_Keybind or val == Order_Station_Keybind.lower():
            #Open the order menu
            DoOrderMenu() 
        # Check if the user wants to go to the store
        elif val == Store_Keybind or val == Store_Keybind.lower():
            #open the store menu
            DoStore()
        # Check if the user wants information
        elif val == Information_Keybind or val == Information_Keybind.lower():
            #Open the information menu
            DoInformation()
        # Check if the user wants to exit
        elif val == 'X' or val == 'x':
            # Ask for confirmation before exiting
            while playing:
                choice = input(f"Are you sure you want to exit? (Y/N): ")
                if choice == "Y" or choice == "y":
                    os.system('cls')
                    # Print exit message and wait before exiting
                    print(f"""
                    \n\n\n\n\n\n
                    {colors.BOLD + colors.UNDERLINE + 
                    'Thank you for playing!' + colors.END}

                    """)
                    time.sleep(2)
                    # Set playing check to False to exit the main loop
                    playing = False
                elif choice == "N" or choice == "n":
                    # If not exiting, go back to the game menu
                    GameMenu()
                else:
                    # Prompt the user to enter a valid option
                    print("Please enter a defined option")
                    time.sleep(1)
                    # cls the console screen and go back to the top of the loop
                    delete_multiple_lines(2)
        # Check if the user wants to go to the upgrades menu
        elif val == Upgrades_Keybind or val == Upgrades_Keybind.lower():
            DoUpgrades()
        # Check if the user wants to go to the rewards menu
        elif val == Rewards_Keybind or val == Rewards_Keybind.lower():
            DoRewards()
        # Check if the user wants to go to the settings menu
        elif val == Settings_Keybind or val == Settings_Keybind.lower():
            DoSettings()
        # Check if the user wants to access the developer menu
        elif val == '$menu$':
            DoDevMenu()
        else:
            # If none of the above options are selected, prompt the user to enter a valid option
            print("Please enter a defined option")
            time.sleep(1)

# Function for Store menu
def DoStore():
    # Define global variables that will be used in this function
    global Name, FirstOpening, multiplier, Shop_Rating, Shop_Rating_Cost, cash, playing, multiplier_cost

    # Check if it's the first time the store is being opened
    if FirstOpening == True:
        # If it's the first time, loop until the user decides to proceed
        while playing == True:
            # cls the console screen
            os.system('cls')

            # Display the welcome message and options
            print(f"""
    Welcome to Paulie's Sandwish Bar, this is a game where you run your own sandwich tycoon
    and make as much money as you can!

    To open your store for business enter [N] to set the name of your store!
    (Enter [P] to leave it as default, you can change it later in settings*)            

    Enter [X] to EXIT              
                  """)
            # Get user input
            val = input("> ")
            # Check user input
            if val == 'X' or val == 'x':
                # If the user wants to exit, go back to the game menu
                GameMenu()
            elif val == 'N' or val == 'n':
                # If the user wants to set a new name, prompt for input and set the name
                NewName = input("Enter New Name: ")
                Name = NewName
                print("Successfully Set!")
                # Set FirstOpening to False to indicate that the store has been set up
                FirstOpening = False
                # Restart the store menu
                DoStore()
            elif val == 'P' or val == 'p':
                # If the user wants to leave the default name, set FirstOpening to False
                FirstOpening = False
                # Restart the store menu
                DoStore()
            else:
                # If the user enters an invalid option, prompt them to enter a valid one
                print("Please enter a defined option")
                time.sleep(1)

    # If it's not the first time opening the store
    while playing == True:
        # cls the console screen
        os.system('cls')

        # Display the store and inventory options
        print(f"""
|----------------------------------------------------------------|
|                              |                                 |
|   {colors.BOLD + colors.UNDERLINE + colors.CYAN + "SHOP" + colors.END}                       |   {colors.BOLD + colors.UNDERLINE + colors.PURPLE + "INVENTORY" + colors.END}                     |
|                              |                                 |
|  |---|---|---|---|---|---|   |  |--------------------------|   |                                 
|  |                       |   |  |                          |   |
|  |   |------| |------|   |   |  |  |--------------------|  |   |
|  |   |      | |      |   |   |  |  |                    |  |   |
|  |   |------| |------|   |   |  |  |  |--------------|  |  |   |
|  |                       |   |  |  |  |--------------|  |  |   |
|  |       |-------|       |   |  |  |                    |  |   |
|  |       |   |   |       |   |  |  |--------------------|  |   |
|  |       |   |   |       |   |  |                          |   |
|  |---|---|---|---|---|---|   |  |--------------------------|   |                                 
|                              |                                 |
|----------------------------------------------------------------|              

Enter [S] to enter SHOP
Enter [I] to enter INVENTORY

Enter [X] to EXIT              
              """)
        # Get user input
        val = input("> ")
        # Check user input
        if val == 'X' or val == 'x':
            # If the user wants to exit, go back to the game menu
            GameMenu()
        elif val == 'I' or val == 'i':
            # If the user wants to enter the inventory, go to the inventory menu
            DoInventory()
        elif val == 'S' or val == 's':
            # If the user wants to enter the shop, go to the shop menu
            DoShop()
        else:
            # If the user enters an invalid option, prompt them to enter a valid one
            print("Please enter a defined option")
            time.sleep(1)

# Function for Shop menu
def DoShop():
    #Define global variable
    global Order1_time, Order2_time, Order3_time, Inventory_Slot, cpm_Reset, cpm_current_time_sec, cpm_start_time, cpm_current_time_min, current_time_sec, StaffNum, Ratings1, Ratings2, Ratings3, Order1, Order2, Order3, Ovr_Ratings1, Ovr_Ratings2, Ovr_Ratings3, Ovr_Scores1, Ovr_Scores2, Ovr_Scores3, multiplier, Shop_Rating, Shop_Rating_Cost, Shop_Multiplier, cash, playing, multiplier_cost, StaffNum, customers, cpm, Staff_Cost
    while playing == True: #Check if playing variable is true
        os.system('cls') #clear the screen
        if Shop_Rating == "LOCKED": #check if Shop rating is locked
            print("Dishes Dirty, Wash Them? [W]") #print acces to the gamemode
        if Shop_Rating != "LOCKED" and multiplier != "LOCKED": #check if Shop rating is not locked and multiplier is also not locked
            cpm = (((customers + len(Shop_Rating.split())) * Shop_Multiplier) * (multiplier)) #set cash/min as the # of customers + number of shop rating stars * shop multipilier * multiplier  
        elif Shop_Rating == "LOCKED" and multiplier != "LOCKED": #check if Shop rating is locked and multiplier is not locked
            cpm = (((customers + 0) * Shop_Multiplier) * (multiplier)) #set cash/min
        else: #otherwise
            cpm = (((customers + 0) * Shop_Multiplier) * (1)) #set cash/min

        cpm = cpm.__round__(2) #round cash/min to the second decimal point

        if customers == 0: #if customers are 0
            print(f"""
|-----------------------------------------------------------------------------------------------|
|   Customers: {colors.PURPLE + colors.UNDERLINE + str(customers) + colors.END}                                                      Shop Rating: {colors.BLUE + colors.UNDERLINE + str(Shop_Rating) + colors.END}       
|-----------------------                                              Equipped Item: {colors.YELLOW + str(Inventory_Slot) + colors.END}            
|   Cash/min: {colors.GREEN + colors.UNDERLINE + str(cpm) + '/min' + colors.END}                                                                             |
|-----------------------                                                                        |
|   Multiplier: {colors.RED + colors.UNDERLINE + str(multiplier) + colors.END}                                                                               |
|-----------------------                                                                        |
|   Shop Multiplier: {colors.BLUE + colors.UNDERLINE + str(Shop_Multiplier) + colors.END}                                                                          |
|-----------------------                                                            Staff: {colors.CYAN + str(StaffNum) + colors.END}    |
|                                                                                     -----     |
|                                                                                     |O O|     |
|                                                                                     |-|-|     |
|      Press [C] for Customer                                                           |       |
|                                                                                |\    /|\      |
|    |   _______________      |                                                  |--------------|
|    |          |             |                                                  | Enter [T]    |
|    |______    |      _______|                                                  | to hire      |
|    |     |    |      |      |                                                  | staff        |
|    |     |    |      |      |                                                  |              |
|-----------------------------------------------------------------------------------------------|            

Enter [R] to refresh page
Enter [C] for Customer
Enter [M] for CPM page

Enter [X] to EXIT              

              """) #output screen with no customers
        elif customers == 1: #if there is 1 customer
            print(f"""
|-----------------------------------------------------------------------------------------------|
|   Customers: {colors.PURPLE + colors.UNDERLINE + str(customers) + colors.END}                                                      Shop Rating: {colors.BLUE + colors.UNDERLINE + str(Shop_Rating) + colors.END}       |
|-----------------------                                              Equipped Item: {colors.YELLOW + colors.UNDERLINE + str(Inventory_Slot) + colors.END}                          
|   Cash/min: {colors.GREEN + colors.UNDERLINE + str(cpm) + '/min' + colors.END}                                                                             |
|-----------------------                                                                        |
|   Multiplier: {colors.RED + colors.UNDERLINE + str(multiplier) + colors.END}                                                                          |
|-----------------------                                                                        |
|   Shop Multiplier: {colors.BLUE + colors.UNDERLINE + str(Shop_Multiplier) + colors.END}                                                                          |
|-----------------------                                                            Staff: {colors.CYAN + str(StaffNum) + colors.END}    |
|                                                                                     -----     |
|                                                                                     |O O|     |
|                                                                                     |-|-|     |
|      Press [C] for Customer          -----                                            |       |
|                                      | | |                                     |\    /|\      |
|    |   _______________      |          |                                       |--------------|
|    |          |             |         /|\                                      |  Enter [T]   |
|    |______    |      _______|          |                                       |  to hire     |
|    |     |    |      |      |          |                                       |  staff       |
|    |     |    |      |      |         /|\                                      |              |
|-----------------------------------------------------------------------------------------------|            

Enter [R] to refresh page
Enter [C] for Customer
Enter [M] for CPM page

Enter [X] to EXIT              

              """)#output screen with 1 customer
        elif customers == 2: #if there are 2 customers
            print(f"""
|-----------------------------------------------------------------------------------------------|
|   Customers: {colors.PURPLE + colors.UNDERLINE + str(customers) + colors.END}                                                      Shop Rating: {colors.BLUE + colors.UNDERLINE + str(Shop_Rating) + colors.END}       |
|-----------------------                                              Equipped Item: {colors.YELLOW + colors.UNDERLINE + str(Inventory_Slot) + colors.END}                          
|   Cash/min: {colors.GREEN + colors.UNDERLINE + str(cpm) + '/min' + colors.END}                                                                             |
|-----------------------                                                                        |
|   Multiplier: {colors.RED + colors.UNDERLINE + str(multiplier) + colors.END}                                                                          |
|-----------------------                                                                        |
|   Shop Multiplier: {colors.BLUE + colors.UNDERLINE + str(Shop_Multiplier) + colors.END}                                                                          |
|-----------------------                                                            Staff: {colors.CYAN + str(StaffNum) + colors.END}    |
|                                                                                     -----     |
|                                                                                     |O O|     |
|                                                                                     |-|-|     |
|      Press [C] for Customer          -----       __                                   |       |
|                                      |'|'|      /__\__                         |\    /|\      |
|    |   _______________      |          |        ['_']                          |--------------|
|    |          |             |         /|\         |                            | Enter [T]    |
|    |______    |      _______|          |         /|\                           | to hire      |
|    |     |    |      |      |          |          |                            | staff        |
|    |     |    |      |      |         /|\        /|\                           |              |
|-----------------------------------------------------------------------------------------------|            

Enter [R] to refresh page
Enter [C] for Customer
Enter [M] for CPM page

Enter [X] to EXIT              

              """)#output screen with 2 customers

        else: #othersise
            print(f"""
|-----------------------------------------------------------------------------------------------|
|   Customers: {colors.PURPLE + colors.UNDERLINE + str(customers) + colors.END}                                                      Shop Rating: {colors.BLUE + colors.UNDERLINE + str(Shop_Rating) + colors.END}       |
|-----------------------                                              Equipped Item: {colors.YELLOW + colors.UNDERLINE + str(Inventory_Slot) + colors.END}                          
|   Cash/min: {colors.GREEN + colors.UNDERLINE + str(cpm) + '/min' + colors.END}                                                                             |
|-----------------------                                                                        |
|   Multiplier: {colors.RED + colors.UNDERLINE + str(multiplier) + colors.END}                                                                          |
|-----------------------                                                                        |
|   Shop Multiplier: {colors.BLUE + colors.UNDERLINE + str(Shop_Multiplier) + colors.END}                                                                          |
|-----------------------                                                            Staff: {colors.CYAN + str(StaffNum) + colors.END}    |
|                                                                                     -----     |
|                                                                                     |O O|     |
|                                                              _                      |-|-|     |
|      Press [C] for Customer          -----       __         / \                       |       |
|                                      |'|'|      /__\__     <===>               |\    /|\      |
|    |   _______________      |          |        ['_']      [+_+]               |--------------|
|    |          |             |         /|\         |         ||                 | Enter [T]    |
|    |______    |      _______|          |         /|\     ()|  |()              | to hire      |
|    |     |    |      |      |          |          |      / |__| \              | staff        |
|    |     |    |      |      |         /|\        /|\       /  \                |              |
|-----------------------------------------------------------------------------------------------|            

Enter [R] to refresh page
Enter [C] for Customer
Enter [M] for CPM page

Enter [X] to EXIT              

              """)#output screen with 3 customer

        val = input("> ") #get input
        if val == 'X' or val == 'x': #if input is a form of 'x'
            DoStore() #go to the store page
        elif val == 'C' or val == 'c':#if input is a form of 'c'
            if customers < len(Shop_Rating.split()): #if # of customers is less than the number of stars in the shop rating
                if customers < 3: #if # of customers is less than 3
                    if customers == 0: # if customers are 0
                        customers += 1 #customers increase by 1
                        Order1_RAW = DoOrder() #Get return values of function
                        Order1 = Order1_RAW[0] #Set the order to a returned value
                        Ratings1 = Order1_RAW[1]#Set the Ratings to a returned value
                        Ovr_Ratings1 = Order1_RAW[2]#Set the order ovreall ratings to a returned value
                        Ovr_Scores1 = Order1_RAW[3]#Set the order overall score to a returned value
                        Order1_time = time.time()#Set the order start time to a returned value
                        print("Customer Enters!\nComplete their order soon!") #output that the customer is here
                        time.sleep(1) #wait 1 second
                    elif customers == 1:                
                        customers += 1 #customers increase by 1
                        Order2_RAW = DoOrder() #Get return values of function
                        Order2 = Order2_RAW[0] #Set the order to a returned value
                        Ratings2 = Order2_RAW[1]#Set the Ratings to a returned value
                        Ovr_Ratings2 = Order2_RAW[2]#Set the order ovreall ratings to a returned value
                        Ovr_Scores2 = Order2_RAW[3]#Set the order overall score to a returned value
                        Order2_time = time.time()#Set the order start time to a returned value
                        print("Customer Enters!\nComplete their order soon!") #output that the customer is here
                        time.sleep(1) #wait 1 second
                    else:
                        customers += 1 #customers increase by 1
                        Order3_RAW = DoOrder() #Get return values of function
                        Order3 = Order3_RAW[0] #Set the order to a returned value
                        Ratings3 = Order3_RAW[1]#Set the Ratings to a returned value
                        Ovr_Ratings3 = Order3_RAW[2]#Set the order ovreall ratings to a returned value
                        Ovr_Scores3 = Order3_RAW[3]#Set the order overall score to a returned value
                        Order3_time = time.time()#Set the order start time to a returned value
                        print("Customer Enters!\nComplete their order soon!") #output that the customer is here
                        time.sleep(1) #wait 1 second
                else: #otherwise
                    print("Complete current orders to allow more customers!") #output that max orders are reached
                    time.sleep(1) #wait 1 second
            else:#otherwise
                print("More Shop Rating Required!") #output that more Shop Rating is required
                time.sleep(1) #wait 1 second

        elif val == 'R' or val == 'r': #if input is a form of 'R'
            DoShop() #open shop menu
        elif val == 'W' or val == 'w': #if input is a form of 'W'
            if Shop_Rating == "LOCKED": #if shop rating is locked
                DoDishes() #Open dishes gamemode
            else: #otherwise
                pass #move forward
        elif val == 'M' or val == 'm': ##if input is a form of 'm'
            ex = False #set check variable
            cpm_current_time_sec = time.time() - cpm_start_time #get current time in seconds
            cpm_current_time_min = int(cpm_current_time_sec / 60) #get current time in minutes
            Cash_Earned = cpm * cpm_current_time_min #calculate cash earnded
            while ex == False: #check if variable is set to False
                if cpm_Reset == True: #if reset variable is set to True
                    cash += (Cash_Earned * Shop_Multiplier) # add to cash amount
                    Cash_Earned = 0 #reset cash earned
                    cpm_start_time = time.time() #start time
                    print("Claimed!") #output that it has been claimed
                    time.sleep(1) #wait 1 second
                    cpm_Reset = False #set reset variable to False
                else: #otherwise
                    pass # move forward
                os.system('cls') #clear screen

                print(f"""
    |-------------------------|              
    |                         |
    |        playtime:        |
    |-------------------------|
    |          {colors.UNDERLINE + colors.BOLD + colors.PURPLE + str(cpm_current_time_min) + ' min' + colors.END + '          |'}           
    |-------------------------|
    |                         |
    |         CPM: {colors.BOLD + colors.CYAN + str(cpm) + colors.END}/cpm        |     
    |                         |
    |-------------------------|
    |                         |
    | Click [C] To Claim: {colors.BOLD + colors.GREEN + str(int(Cash_Earned)) + colors.END + "   |"}
    |                         |
    |-------------------------|

    Enter [x] to exit        
                      """) # output cpm collect screen
                inval = input("> ") #get input
                if inval == 'c' or inval == 'C': #if input is a form of 'c'
                    cpm_Reset = True #set reset variable to True
                elif inval == 'x' or val == 'X': #if input is a form of 'X'
                    DoShop() #Open shop menu
                else: #otherwise
                    print("Please enter a defined value") #output incorrect input
                    time.sleep(1) #wait 1 second




        elif val == 't' or val == 'T': #if input is a form of 'T'
            #get input whether player wants to purchase staff
            prompt = input(f"Would you like to purchase 1 staff for {Staff_Cost} cash? (y/n): ")
            if prompt == 'y' or prompt == 'Y': #if input is a form of 'y'
                if cash >= Staff_Cost: #if cash is less than or equal to staff cost
                    cash -= Staff_Cost #cash is reduced by staff cost
                    StaffNum += 1 #staff number increased by 1
                    Staff_Cost = StaffNum * 200 #staff cost increased by number of staff x 200
                    Shop_Multiplier += 1 #shop multiplier increased by 1
                else: #otherwise
                    print("Not enough cash!") #output reason
                    time.sleep(1) #wait 1 second

        else: #otherwise
            print("Please enter a defined option") #output problem
            time.sleep(1) #wait 1 second  

# Function for unlocking the shop rating
def DoDishes():
    #set global variables
    global cash, Shop_Rating, colors
    # Loop until the shop rating is unlocked
    while Shop_Rating == "LOCKED":
        # Clear the screen
        os.system("cls")

        # Display the welcome message and instructions
        print("""
Welcome to the dishes gamemode!
This is where you can unlock your shop rating!
Press [P] to begin!    
        """)

        # Get user input
        val = input("> ")

        # If the user presses 'P' or 'p', start the game
        if val == 'P' or val == 'p':
            # Initialize points
            points = 0

            # Define the choices
            Choices = ['w', 'a', 's', 'd']

            # Loop until the user reaches 5 points
            while points < 5:
                # Clear the screen
                os.system('cls')

                # Generate a random letter
                letter = random.choice(Choices)

                # Display the game instructions and current letter
                print(f"""
Enter the letter {letter} below in under 1 second to gain a point.
5 points = WIN!

------------------------------------------------
Letter: {letter}
------------------------------------------------
                """)

                # Start the timer
                start = time.time()

                # Get user input
                val = input("> ")

                # Calculate the time taken
                end = time.time() - start

                # Check if the input is correct and within the time limit
                if val == letter and end < 1:
                    # add points and provide reason
                    points += 1
                    print(colors.BOLD + colors.GREEN + "POINTS + 1" + colors.END)
                    time.sleep(1)
                elif val == letter and end > 1:
                    # Provide output for being too slow
                    print(colors.BOLD + colors.YELLOW + "TOO SLOW!" + colors.END)
                    time.sleep(1)
                else:
                    # Provide feedback for wrong input
                    print(colors.BOLD + colors.RED + "WRONG LETTER!" + colors.END)
                    time.sleep(1)

            # If the user reaches 5 points, unlock the shop rating
            else:
                Shop_Rating = '*'

# Function for the inventory menu
def DoInventory():
    global multiplier,Customer_Wait_Time, Shop_Rating, PerkApplied, Shop_Rating_Cost, Shop_Multiplier, cash, playing, multiplier_cost, StaffNum, DungeonMultiplier, customers, cpm, Items_Page, Inventory_Slot, Item_Values, Staff_Cost
    #while main playing loop is True
    while playing == True:
        #clear screen
        os.system('cls')

        #Define a class to hold all item cards
        class Items:  
            DUSTY_BROOM = f"""
    |-------------------------|              
    | {Item_Values['DUSTY_BROOM']['is_locked']}      {Item_Values['DUSTY_BROOM']['is_equipped']} |
    |       Dusty Broom       |
    |-------------------------|
    |             {colors.UNDERLINE + colors.BOLD + colors.BROWN + str('COMMON') + colors.END + '             |'}           
    |-------------------------|
    |                         |
    |                         |
    | + 0.25x shop multiplier |
    |                         |
    |-------------------------|
    |                         |
    |   [C] To Equip/Unequip  |
    |-------------------------|        
            """
            KELP_SEVICHE_HAT = f"""
    |-------------------------|              
    | {Item_Values['KELP_SEVICHE_HAT']['is_locked']}      {Item_Values['KELP_SEVICHE_HAT']['is_equipped']} |
    |   Kelp Seviche Hat      |
    |-------------------------|
    |         {colors.UNDERLINE + colors.BOLD + colors.BLUE + 'RARE' + colors.END}          |           
    |-------------------------|
    |                         |
    |   + 0.5 shop multiplier |
    |   + 1 staff             |
    |                         |
    |-------------------------|      
    |                         |
    |   [C] To Equip/Unequip  |
    |-------------------------|        
            """
            GOLDEN_TUXEDO = f"""
    |-------------------------|              
    | {Item_Values['GOLDEN_TUXEDO']['is_locked']}      {Item_Values['GOLDEN_TUXEDO']['is_equipped']} |
    |     Golden Tuxedo       |
    |-------------------------|
    |         {colors.UNDERLINE + colors.BOLD + colors.YELLOW + 'LEGEND' + colors.END}          |           
    |-------------------------|
    |       - 0.5x staff cost |
    |       + 1 staff         |
    | + 2x Dungeon multiplier |
    |                         |
    |-------------------------|      
    |                         |
    |   [C] To Equip/Unequip  |
    |-------------------------|        
            """
            RUST_BUCKET = f"""
    |-------------------------|              
    | {Item_Values['RUST_BUCKET']['is_locked']}      {Item_Values['RUST_BUCKET']['is_equipped']} |
    |      Rust Bucket        |
    |-------------------------|
    |      {colors.UNDERLINE + colors.BOLD + colors.BROWN + 'COMMON' + colors.END}       |           
    |-------------------------|
    |                         |
    |                         |
    |    - 0.25x staff cost   |
    |                         |
    |-------------------------|      
    |                         |
    |   [C] To Equip/Unequip  |                         
    |-------------------------|        
            """
            TACO_TUESDAY_STICKER = f"""
    |-------------------------|              
    | {Item_Values['TACO_TUESDAY_STICKER']['is_locked']}      {Item_Values['TACO_TUESDAY_STICKER']['is_equipped']} |
    |  Taco Tuesday Sticker   |
    |-------------------------|
    |      {colors.UNDERLINE + colors.BOLD + colors.BLUE + 'RARE' + colors.END}       |           
    |-------------------------|
    |                         |
    |                         |
    |   + 2 staff             |
    |   + 1x shop multiplier  |
    |-------------------------|      
    |                         |
    |   [C] To Equip/Unequip  |
    |                         |
    |-------------------------|        
            """
            GOLDEN_GLOVES = f"""
    |-------------------------|              
    | {Item_Values['GOLDEN_GLOVES']['is_locked']}      {Item_Values['GOLDEN_GLOVES']['is_equipped']} |
    |      Golden Gloves      |
    |-------------------------|
    |     {colors.UNDERLINE + colors.BOLD + colors.YELLOW + 'LEGEND' + colors.END}       |           
    |-------------------------|
    |       + 0.5x cpm        |
    |       + 2 staff         |
    | + 2x Dungeon multiplier |
    |                         |
    |-------------------------|      
    |                         |
    |   [C] To Equip/Unequip  |
    |                         |
    |-------------------------|        
            """
            CHUM_SIGN = f"""
    |-------------------------|              
    | {Item_Values['CHUM_SIGN']['is_locked']}      {Item_Values['CHUM_SIGN']['is_equipped']} |
    |       Chum Sign         |
    |-------------------------|
    |      {colors.UNDERLINE + colors.BOLD + colors.BROWN + 'COMMON' + colors.END}       |           
    |-------------------------|
    |                         |
    |       + 1 staff         |
    |       + 1x c/min        |
    |                         |
    |-------------------------|      
    |                         |
    |   [C] To Equip/Unequip  |
    |                         |
    |-------------------------|        
            """
            MACRONALD_DONALD = f"""
    |-------------------------|              
    | {Item_Values['MACRONALD_DONALD']['is_locked']}      {Item_Values['MACRONALD_DONALD']['is_equipped']} |
    |   MacRonald Donald      |
    |-------------------------|
    |      {colors.UNDERLINE + colors.BOLD + colors.BLUE + 'RARE' + colors.END}       |           
    |-------------------------|
    |                         |
    |                         |
    | + double order wait time|
    |    + 1x shop multiplier |
    |-------------------------|      
    |                         |
    |   [C] To Equip/Unequip  |
    |                         |
    |-------------------------|        
            """
            PLATINUM_TOWEL = f"""
    |-------------------------|              
    | {Item_Values['PLATINUM_TOWEL']['is_locked']}      {Item_Values['PLATINUM_TOWEL']['is_equipped']} |
    |     Platinum Towel      |
    |-------------------------|
    |          {colors.UNDERLINE + colors.BOLD + colors.YELLOW + 'LEGEND' + colors.END}       |           
    |-------------------------|
    |                         |
    | + triple order wait time|
    |    + 2x game multiplier |
    |                         |
    |-------------------------|      
    |                         |
    |   [C] To Equip/Unequip  |
    |                         |
    |-------------------------|        
            """
            HOLY_DUSTY_BROOM = f"""
    |-------------------------|              
    | {Item_Values['HOLY_DUSTY_BROOM']['is_locked']}      {Item_Values['HOLY_DUSTY_BROOM']['is_equipped']} |
    |    Holy Dusty Broom     |
    |-------------------------|
    |         {colors.UNDERLINE + colors.BOLD + colors.PURPLE + 'MYTHICAL' + colors.END}       |           
    |-------------------------|                         
    |                         |
    |  + 1x game multiplier   |
    |  + 2x Dungeon multiplier|
    |  + 2x order wait time   |
    |  + 1x c/min             |
    |-------------------------|      
    |                         |
    |   [C] To Equip/Unequip  |
    |                         |
    |-------------------------|        
            """
            HOLY_RUST_BUCKET = f"""
    |-------------------------|              
    | {Item_Values['HOLY_RUST_BUCKET']['is_locked']}      {Item_Values['HOLY_RUST_BUCKET']['is_equipped']} |
    |    Holy Rust Bucket     |
    |-------------------------|
    |         {colors.UNDERLINE + colors.BOLD + colors.PURPLE + 'MYTHICAL' + colors.END}       |            
    |-------------------------|
    |                         |
    | + triple order wait time|
    |    + 1x c/min           |
    |    + 2x shop multiplier |
    |    - 0.5x staff cost    |
    |-------------------------|      
    |                         |
    |   [C] To Equip/Unequip  |
    |                         |
    |-------------------------|        
            """
        
        #determine Common rarity items
        CommonItems = [Items.DUSTY_BROOM, Items.RUST_BUCKET, Items.CHUM_SIGN] 
        #determine Rare rarity items
        RareItems = [Items.KELP_SEVICHE_HAT, Items.TACO_TUESDAY_STICKER, Items.MACRONALD_DONALD]
        #determine Legend rarity items
        LegendItems = [Items.GOLDEN_TUXEDO, Items.GOLDEN_GLOVES, Items.PLATINUM_TOWEL]
        #determine Mythic rarity items
        MythicItems = [Items.HOLY_DUSTY_BROOM, Items.HOLY_RUST_BUCKET]

        if not PerkApplied:  # Check if the perk has already been applied
            for i in Item_Values:  # Iterate through each item
                if Item_Values[i]['is_equipped'] == colors.BOLD + colors.GREEN + "EQUIPPED" + colors.END:  # Check if the item is equipped
                    Inventory_Slot = i  # Set the inventory slot to the current item
                    # Check inventory slot to item and apply its effects
                    if Inventory_Slot == "DUSTY_BROOM":
                        Shop_Multiplier += 0.25
                    # Check inventory slot to item and apply its effects
                    elif Inventory_Slot == "RUST_BUCKET":
                        Staff_Cost *= 0.75
                    # Check inventory slot to item and apply its effects
                    elif Inventory_Slot == "CHUM_SIGN":
                        StaffNum += 1
                        cpm += 1
                    # Check inventory slot to item and apply its effects
                    elif Inventory_Slot == "KELP_SEVICHE_HAT":
                        StaffNum += 1
                        Shop_Multiplier += 0.5
                    # Check inventory slot to item and apply its effects
                    elif Inventory_Slot == "TACO_TUESDAY_STICKER":
                        Shop_Multiplier += 1
                        StaffNum += 2
                    # Check inventory slot to item and apply its effects
                    elif Inventory_Slot == "MACRONALD_DONALD":
                        Customer_Wait_Time *= 2
                        Shop_Multiplier += 1
                    # Check inventory slot to item and apply its effects
                    elif Inventory_Slot == "GOLDEN_TUXEDO":
                        DungeonMultiplier += 2
                        Staff_Cost *= 1.5
                        StaffNum += 2
                    # Check inventory slot to item and apply its effects
                    elif Inventory_Slot == "GOLDEN_GLOVES":
                        cpm *= 1.5
                        DungeonMultiplier += 2
                        StaffNum += 2
                    # Check inventory slot to item and apply its effects
                    elif Inventory_Slot == "PLATINUM_TOWEL":
                        multiplier *= 2
                        Customer_Wait_Time *= 3
                    # Check inventory slot to item and apply its effects
                    elif Inventory_Slot == "HOLY_DUSTY_BROOM":
                        Customer_Wait_Time *= 2
                        multiplier += 1
                        cpm += 1
                        DungeonMultiplier += 2
                    # Check inventory slot to item and apply its effects
                    elif Inventory_Slot == "HOLY_RUST_BUCKET":
                        Customer_Wait_Time *= 3
                        multiplier += 2
                        cpm += 1
                        Staff_Cost *= 0.5
                    PerkApplied = True  # Set check to True to show the perk has been applied
                    break  # Exit the loop after applying the perk
                else: #otherwise
                    Inventory_Slot = []  # Reset Inventory Slot 


        #output current inventory slot
        print("Currently Equipped Item: ", colors.BOLD + str(Inventory_Slot) + colors.END)

        # check item page and output subsequent item card
        if Items_Page == 1:

            print(f"""

                           {CommonItems[0]}              

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}       
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        # check item page and output subsequent item card
        elif Items_Page == 2:

            print(f"""

                           {CommonItems[1]}              

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}       
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        # check item page and output subsequent item card
        elif Items_Page == 3:

            print(f"""

                           {CommonItems[2]}              

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}       
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        # check item page and output subsequent item card
        elif Items_Page == 4:

            print(f"""

                           {RareItems[0]}

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}                     
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        # check item page and output subsequent item card
        elif Items_Page == 5:

            print(f"""

                           {RareItems[1]}          

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}       
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        # check item page and output subsequent item card
        elif Items_Page == 6:

            print(f"""

                           {RareItems[2]} 

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}                     
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        # check item page and output subsequent item card
        elif Items_Page == 7:

            print(f"""

                           {LegendItems[0]} 

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}                     
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        # check item page and output subsequent item card
        elif Items_Page == 8:

            print(f"""

                           {LegendItems[1]}    

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}                     
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        # check item page and output subsequent item card
        elif Items_Page == 9:

            print(f"""

                           {LegendItems[2]} 

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}                     
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        # check item page and output subsequent item card
        elif Items_Page == 10:

            print(f"""

                           {MythicItems[0]} 

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}                     
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        # check item page and output subsequent item card
        elif Items_Page == 11:

            print(f"""

                           {MythicItems[1]} 

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}                     
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        else: #otherwise
            pass #move on

        val = input("> ")  # Ask for user input
        
        # Check if user input is '>'
        if val == '>':
            if Items_Page < 11:  # If current page is less than 11
                Items_Page += 1  # Increment current page
            else:
                print("No following page!")  # If already at the last page, print a message
                time.sleep(1)  # Wait for 1 second
        
        # Check if user input is '<'
        elif val == '<':
            if Items_Page > 1:  # If current page is greater than 1
                Items_Page -= 1  # Decrement current page
            else:
                print("No preceding page!")  # If already at the first page, print a message
                time.sleep(1)  # Wait for 1 second
        
        # Check if user input is 'x' or 'X'
        elif val == 'x' or val == 'X':
            Items_Page = 1  # Set current page to 1
            DoStore()  # Call the function DoStore()
        
        # Check if user input is 'c' or 'C'
        elif val == 'c' or val == 'C':
            # Assign item based on the current page
            if Items_Page == 1:
                item = "DUSTY_BROOM"
            # Assign item based on the current page
            elif Items_Page == 2:
                item = "RUST_BUCKET"
            # Assign item based on the current page
            elif Items_Page == 3:
                item = "CHUM_SIGN"
            # Assign item based on the current page
            elif Items_Page == 4:
                item = "KELP_SEVICHE_HAT"
            # Assign item based on the current page
            elif Items_Page == 5:
                item = "TACO_TUESDAY_STICKER"
            # Assign item based on the current page
            elif Items_Page == 6:
                item = "MACRONALD_DONALD"
            # Assign item based on the current page
            elif Items_Page == 7:
                item = "GOLDEN_TUXEDO"
            # Assign item based on the current page
            elif Items_Page == 8:
                item = "GOLDEN_GLOVES"
            # Assign item based on the current page
            elif Items_Page == 9:
                item = "PLATINUM_TOWEL"
            # Assign item based on the current page
            elif Items_Page == 10:
                item = "HOLY_DUSTY_BROOM"
            # Assign item based on the current page
            elif Items_Page == 11:
                item = "HOLY_RUST_BUCKET"
            # Assign item based on the current page
            else:
                item = None
        
            # Check if the multiplier and shop rating are not locked
            if multiplier != "LOCKED" and Shop_Rating != "LOCKED":
                # Check if the inventory slot is not empty and not the same as the selected item
                if Inventory_Slot != [] and Inventory_Slot != list(Item_Values)[Items_Page - 1]:
                    print("Unequip current item prior to equipping new one")
                    time.sleep(1)
                # Check if the selected item is locked
                elif Item_Values[item]["is_locked"] == colors.RED + colors.BOLD + "LOCKED" + colors.END:
                    print("Item Locked!")
                    time.sleep(1)
                # Check if the selected item is already equipped
                elif Item_Values[item]["is_equipped"] == colors.BOLD + colors.GREEN + "EQUIPPED" + colors.END:
                    #Unequip item
                    Item_Values[item]["is_equipped"] = colors.BOLD + colors.PURPLE + "UNEQUIPPED" + colors.END
                    #Output that item has been unequipped 
                    print(colors.BOLD + colors.RED + "UNEQUIPPED" + colors.END)
                    #check if inventory slot is certain item, then remove corresponding effect
                    if Inventory_Slot == "DUSTY_BROOM":
                        Shop_Multiplier -= 0.25
                    #check if inventory slot is certain item, then remove corresponding effect
                    elif Inventory_Slot == "RUST_BUCKET":
                        Staff_Cost /= 0.75
                    #check if inventory slot is certain item, then remove corresponding effect
                    elif Inventory_Slot == "CHUM_SIGN":
                        StaffNum -= 1
                        cpm -= 1
                    #check if inventory slot is certain item, then remove corresponding effect
                    elif Inventory_Slot == "KELP_SEVICHE_HAT":
                        StaffNum -= 1
                        Shop_Multiplier -= 0.5
                    #check if inventory slot is certain item, then remove corresponding effect
                    elif Inventory_Slot == "TACO_TUESDAY_STICKER":
                        Shop_Multiplier -= 1
                        StaffNum -= 2
                    #check if inventory slot is certain item, then remove corresponding effect
                    elif Inventory_Slot == "MACRONALD_DONALD":
                        Customer_Wait_Time /= 2
                        Shop_Multiplier -= 1
                    #check if inventory slot is certain item, then remove corresponding effect
                    elif Inventory_Slot == "GOLDEN_TUXEDO":
                        DungeonMultiplier -= 2
                        Staff_Cost /= 1.5
                        StaffNum -= 2
                    #check if inventory slot is certain item, then remove corresponding effect
                    elif Inventory_Slot == "GOLDEN_GLOVES":
                        cpm /= 1.5
                        DungeonMultiplier -= 2
                        StaffNum -= 2
                    #check if inventory slot is certain item, then remove corresponding effect
                    elif Inventory_Slot == "PLATINUM_TOWEL":
                        multiplier /= 2
                        Customer_Wait_Time /= 3
                    #check if inventory slot is certain item, then remove corresponding effect
                    elif Inventory_Slot == "HOLY_DUSTY_BROOM":
                        Customer_Wait_Time /= 2
                        multiplier -= 1
                        cpm -= 1
                        DungeonMultiplier -= 2
                    #check if inventory slot is certain item, then remove corresponding effect
                    elif Inventory_Slot == "HOLY_RUST_BUCKET":
                        Customer_Wait_Time /= 3
                        multiplier -= 2
                        cpm -= 1
                        Staff_Cost /= 0.5
                    else: #otherwise
                        #print error message
                       print("remove error")
                       time.sleep(1) #wait 1 second
                    PerkApplied = False  #change perk applied check to false
                    time.sleep(1) #wait 1 second
                else: #otherwise
                    # Equip the selected item
                    Item_Values[item]["is_equipped"] = colors.BOLD + colors.GREEN + "EQUIPPED" + colors.END
                    print(Item_Values[item]['is_equipped'])
                    print("Item Equipped!") #output success message
                    time.sleep(1)  # Wait for 1 second
            else: #otherwise
                print("Multiplier and Shop Rating have to be unlocked to equip items!") #output reason
                time.sleep(1)  # Wait for 1 second
        
        # If user input is none of the above options
        else:
            print("Please enter a defined option")  # Print a message asking for a defined option
            time.sleep(1)  # Wait for 1 second

def DoDevMenu():
    global multiplier, Shop_Rating, Shop_Rating_Cost, cash, playing, multiplier_cost, Dungeon_Cooldown, Spin_Period
    print("All changes occured here will be reflected when the menu is closed.")
    while playing:
        command = input("Dev Command > ")
        if "cash=" in command:
            new_cash_values = [int(num) for num in re.findall(r'\d+', command)]
            if new_cash_values:
                cash = new_cash_values[0]
                print(f"Updated cash value: {cash}")
                time.sleep(1)
            else:
                print("No numeric value found in the command.")
                time.sleep(1)
        elif "multi=" in command:
            new_multi_values = [int(num) for num in re.findall(r'\d+', command)]
            if new_multi_values:
                multiplier = new_multi_values[0]
                print(f"Updated multiplier value: {multiplier}")
                time.sleep(1)
            else:
                print("No numeric value found in the command.")
                time.sleep(1)
        elif "DunCool=" in command:
            new_Dungeon_values = [int(num) for num in re.findall(r'\d+', command)]
            if new_Dungeon_values:
                Dungeon_Cooldown = new_Dungeon_values[0]
                print(f"Updated Dungeon Cooldown value: {Dungeon_Cooldown}")
                time.sleep(1)
            else:
                print("No numeric value found in the command.")
                time.sleep(1)
        elif command == "X" or command == "x":
            GameMenu()

# Function for the upgrades menu
def DoUpgrades():
    # Declare global variables
    global Shop_Rating
    global playing
    global multiplier
    global multiplier_cost
    global Shop_Rating_Cost
    global cash 
    global seperater  

    # Loop while the main playing variable is True
    while playing:
        # Clear screen
        os.system('cls')

        if multiplier != 'LOCKED':  # Check if the multiplier is not locked
            if multiplier >= 5:  # Check if the multiplier is at its maximum value
                multiplier_cost = "MAX"  # Set the cost to "MAX" if the multiplier is at its maximum value
            else: #otherwise
                multiplier_cost = int(multiplier ** 5)  # Calculate the cost based on the current multiplier
        else: #otherwise
            pass  #do nothing

        if Shop_Rating != 'LOCKED':  # Check if the Shop Rating is not locked
            if len(Shop_Rating.split()) >= 5:  # Check if the Shop Rating has reached its maximum level
                Shop_Rating_Cost = 'MAX'  # Set the cost to "MAX" if the Shop Rating has reached its maximum level
            else: #otherwise
                Shop_Rating_Cost = len(Shop_Rating.split()) * 25  # Calculate the cost based on the current Shop Rating level
        else: #otherwise
            pass  # do nothing

        # output the upgrade options and their costs to the user
        print(f"""\n
Upgrade cash multiplier. (Current: {multiplier}), {colors.BOLD + 'enter [M]' + colors.END}, cost: [{multiplier_cost}]
{seperater}
Upgrade Shop Rating. (Current: {Shop_Rating}), {colors.BOLD + 'enter [S]' + colors.END}, cost: [{Shop_Rating_Cost}] \n  
To exit, {colors.BOLD + 'enter [X]' + colors.END}
          """)

        # Get user input
        val = input("> ")

        # if input lowercased / or is 'm'
        if val.lower() == 'm': 
            if multiplier == 5:  # Check if the multiplier is at maximum 
                print("Max multiplier reached")  # output that the maximum multiplier is reached
                time.sleep(1)  # wait 1 second
            else: #otherwise
                if multiplier != 'LOCKED':  # Check if the multiplier is not locked
                    if cash >= multiplier_cost:  # Check if the user has enough cash to upgrade the multiplier
                        cash -= multiplier_cost  # update the cost from cash
                        multiplier += 1  # Increase the multiplier by 1
                    else: #otherwise
                        print("Not enough cash!")  # output they don't have enough cash
                        time.sleep(1)  # wait 1 second
                else:#otherwise
                    print("Multiplier Locked!")  # output that the multiplier is locked
                    time.sleep(1)  # wait 1 second
        elif val.lower() == 's':  # Check if input is a form of 's'
            if Shop_Rating == '* * * * *':  # Check if the Shop Rating is already at its maximum level
                print("Max Shop Rating reached")  # output that the maximum Shop Rating is reached
                time.sleep(1)  # wait 1 second
            else:#otherwise
                if Shop_Rating != 'LOCKED':  # Check if the Shop Rating is not locked
                    if cash >= Shop_Rating_Cost:  # Check if the user has enough cash to upgrade the Shop Rating
                        cash -= Shop_Rating_Cost  # update the cash amount
                        Shop_Rating += ' *'  # Add a star to the Shop Rating 
                    else:#otherwise
                        print("Not enough cash!")  # output that they dont have enough cash
                        time.sleep(1)  # wait 1 second
                else:#otherwise
                    print("Shop Rating Locked!")  # output that the Shop Rating is locked
                    time.sleep(1)  # wait 1 second
        elif val.lower() == 'x':  # Check if input is a form of 'x'
            GameMenu()  # Open the Game Menu page
        else:#otherwise
            print("Enter a defined option")  # output to enter a valid option
            time.sleep(1)  # wait 1 second

# Function for the rewards menu 
def DoRewards():
    #Define global variables
    global Spin_Overide, Cash_start_time, Spin_start_time, Dungeon_start_time, cash, multiplier, Shop_Rating, Shop_Rating_Cost, multiplier_cost, seperater, start_time, colors, Cash_Reset
    global Rewards_Page, Dungeon_Cooldown, Spin_Period, section, Last_Dungeon_Score, High_Dungeon_Score
    
    # Set page to default of 1 
    Rewards_Page = 1

    # Calculate the time elapsed since Cash activity started
    Cash_current_time_sec = time.time() - Cash_start_time

    # Calculate the time elapsed since Spin activity started
    Spin_current_time_sec = time.time() - Spin_start_time

    # Calculate the time elapsed since Dungeon activity started
    Dungeon_current_time_sec = time.time() - Dungeon_start_time

    # Convert the time elapsed for Cash activity to minutes
    Cash_current_time_min = int(Cash_current_time_sec / 1)

    # Convert the time elapsed for Spin activity to minutes
    Spin_current_time_min = int(Spin_current_time_sec / 1)

    # Convert the time elapsed for Dungeon activity to minutes
    Dungeon_current_time_min = int(Dungeon_current_time_sec / 1)

    # Calculate the amount of cash earned 
    Cash_Earned = Cash_current_time_min / 5

    # Check if main playing variable is True
    while playing == True:
        # Check if reset variable is true
        if Cash_Reset == True:
            # Add the earned cash to the total cash
            cash += Cash_Earned

            # Reset the earned cash to zero
            Cash_Earned = 0

            # Reset the start time 
            Cash_start_time = time.time()

            # Print cash has been claimed
            print("Claimed!")

            # Wait  1 second
            time.sleep(1)

            # Reset cash reset 
            Cash_Reset = False
        else: #otherwise
            #continue the loop
            pass

        # Calculate the time remaining for Dungeon cooldown 
        Dungeon_Time_To_Wait_Min = Dungeon_Cooldown - Dungeon_current_time_min
        # store Dungen countdown
        Dungeon_Time_To_Wait_Countdown = colors.CYAN + colors.BOLD + f"{Dungeon_Time_To_Wait_Min}" + colors.END
        if Dungeon_Time_To_Wait_Min < 0: #if Dungen countdown is negative
            # Set cooldown display to "Ready"
            Dungeon_Time_To_Wait_Countdown = colors.BG_CYAN + colors.BOLD + "   READY!   " + colors.END

        # Calculate the time remaining for Spin 
        Spin_Time_To_Wait_Min = Spin_Period - Spin_current_time_min
        # store the display of the countdown
        Spin_Time_To_Wait_Countdown = colors.CYAN + colors.BOLD + f"{Spin_Time_To_Wait_Min}" + colors.END
        #if spin countdown is negative or it has been overriden
        if Spin_Time_To_Wait_Min < 0 or Spin_Overide == True:
            # store the display "READY!" in the countdown variable
            Spin_Time_To_Wait_Countdown = colors.BG_GREEN + colors.BOLD + "   READY!   " + colors.END



        os.system('cls') #clear screen

        #output page header
        print(colors.BOLD + colors.BG_RED + colors.ITALIC + " REWARDS " + colors.END)
        
        #define class storing the diffrent pages 
        class section:  
            ONE = f"""
    |-------------------------|              
    |                         |
    |        playtime:        |
    |-------------------------|
    |          {colors.UNDERLINE + colors.BOLD + colors.PURPLE + str(Cash_current_time_min) + ' min' + colors.END + '          |'}           
    |-------------------------|
    |                         |
    |    Earn 1 cash every:   |  
    |        5 minutes!       |     
    |                         |
    |-------------------------|
    |                         |
    | Click [C] To Claim: {colors.BOLD + colors.GREEN + str(int(Cash_Earned)) + colors.END + "   |"}
    |                         |
    |-------------------------|        
            """
            TWO = f"""
    |-------------------------|              
    |                         |
    |     {colors.BG_MAGENTA + colors.BOLD + "  SPIN TO WIN:  " + colors.END}    |
    |-------------------------|
    |      every:  {colors.UNDERLINE + colors.BOLD + colors.PURPLE + str(Spin_Period) + ' min' + colors.END + '     |'}           
    |-------------------------|
    |                         |
    |     Time To Wait:       |
    |         {Spin_Time_To_Wait_Countdown} min          |
    |                         |
    |-------------------------|
    |                         |
    |    {colors.BOLD + colors.RED + str("ENTER [S] TO SPIN") + colors.END + "    |"}
    |                         |
    |-------------------------|        
            """
            THREE = f"""
    |-------------------------|              
    |                         |
    |     {colors.BG_YELLOW + colors.BOLD + "  MATH Dungeon  " + colors.END}     |
    |-------------------------|
    |      every:  {colors.UNDERLINE + colors.BOLD + colors.PURPLE + str(Dungeon_Cooldown) + ' min' + colors.END + '     |'}           
    |-------------------------|
    |                         |
    |     Time To Wait:       |
    |        {Dungeon_Time_To_Wait_Countdown} min           |
    |                         |
    |-------------------------|
    |                         |
    |    {colors.BOLD + colors.RED + str("ENTER [M] TO START") + colors.END + "   |"}
    |                         |
    |-------------------------|       
            """

            SPIN = f"""
    |--------------------------------------------------------
    | Common      | Rare        | Legendary   | Mythical    | 
    |-------------|-------------|-------------|-------------|
    | Dusty Broom | kelp Seviche| Golden      | Holy Dusty  |          
    |             | Hat         | Tuxedo      | Broom       |          
    | Rust Bucket |             |             |             |          
    |             | Taco Tues-  | Golden      | Holy Rust   |          
    | Chum Sign   | day Sticker | Gloves      | Bucket      |          
    |             |             |             |             |          
    |             | MacRonald   | Platinum    |             |
    |             | Donald      | Towel       |             |
    |--------------------------------------------------------        

                            {colors.BOLD + colors.YELLOW + " ENTER [P] TO SPIN! " + colors.END}
            """

            Dungeon = f"""
    {colors.BOLD + colors.YELLOW + " WELCOME TO THE MATH Dungeon! " + colors.END}

|------------------------------------------------------------|
| What Is Dungeon?          | Previous Score  | High Score    | 
|--------------------------|-----------------|---------------|
| Math Dungeon is where     |                 |               |             
| you can earn money and   | {colors.UNDERLINE + str(Last_Dungeon_Score) + colors.END}               | {colors.RED + colors.UNDERLINE + str(High_Dungeon_Score) + colors.END}             |             
| rewards for your         |                 |               |             
| restaurant by completing |                 |               |             
| simple math questions!   |                 |               |             
| The gamemode runs until  |                 |               |
| a questions is got wrong.|                 |               |             
|                          |                 |               |
|                          |                 |               |  
|  Press [D] to Begin!     |                 |               |             
|                          |                 |               |             
|                          |                 |               |             
|                          |                 |               |             
|-------------------------------------------------------------

    """
        
        #if current page is 1 output the corresponding page from the class
        if Rewards_Page == 1: 
            print(f"""
{section.ONE}

Enter [>] for next page  
Enter [<] for previous page
Enter [X] to exit                               Current page: {colors.DARKCYAN + colors.BOLD + str(Rewards_Page) + colors.END}                                                                                                                       
Enter [R] to refresh
                """)
        #if current page is 2 output the corresponding page from the class
        elif Rewards_Page == 2:
            print(f"""
{section.TWO}

Enter [F] to skip cooldown
Enter [>] for next page
Enter [<] for previous page
Enter [X] to exit                               Current page: {colors.DARKCYAN + colors.BOLD + str(Rewards_Page) + colors.END}
Enter [R] to refresh
                """)
        #if current page is 3 output the corresponding page from the class
        elif Rewards_Page == 3:
            print(f"""
{section.THREE}

Enter [>] for next page
Enter [<] for previous page
Enter [X] to exit                               Current page: {colors.DARKCYAN + colors.BOLD + str(Rewards_Page) + colors.END}
Enter [R] to refresh
                """)
        #if current page is "SPIN" output the corresponding page from the class
        elif Rewards_Page == "SPIN":
            print(f"""
{section.SPIN}


Enter [<] for previous page
Enter [X] to exit                               Current page: {colors.DARKCYAN + colors.BOLD + str(Rewards_Page) + colors.END}
Enter [R] to refresh
                """)
        

        val = input("> ")  # Get user input

        # Check user input for different commands
        if val == 'C' or val == 'c':  # If the user inputs 'C' or 'c'
            if Rewards_Page == 1:  # If Rewards_Page is equal to 1
                Cash_Reset = True  # Set Cash_Reset to True
            else: #otherwise
                pass  # do nothing
        elif val == '>':  # If the user inputs '>'
            if Rewards_Page == 3 or Rewards_Page == "SPIN" or Rewards_Page == "Dungeon":  # If Rewards_Page is 3, "SPIN", or "Dungeon"
                print("No next page")  # Print "No next page"
                time.sleep(1)  # wait 1 second
            else:
                Rewards_Page += 1  # increase Rewards_Page by 1
        elif val == '<':  # If the user inputs '<'
            if Rewards_Page == 1:  # If Rewards_Page is 1
                print("No previous page")  # Print "No previous page"
                time.sleep(1)  # wait 1 second
            elif Rewards_Page == "SPIN":  # If Rewards_Page is "SPIN"
                Rewards_Page = 2  # Set Rewards_Page to 2
            else:
                Rewards_Page -= 1  # reduce Rewards_Page by 1
        elif val == 'X' or val == 'x':  # If the user inputs 'X' or 'x'
            GameMenu()  # open GameMenu page
        elif val == 'R' or val == 'r':  # If the user inputs 'R' or 'r'
            DoRewards()  # open Rewards page
        # Check if the user input is 'S' or 's'
        elif val == 'S' or val == 's':
            if Rewards_Page == 2:  # Check if the current Rewards_Page is 2
                if Spin_Time_To_Wait_Min < 0 or Spin_Overide == True:  # Check if Spin_Time_To_Wait_Min is less than 0 or Spin_Overide is True
                    os.system('clear')  # Clear screen
                    Rewards_Page = "SPIN"  # Set Rewards_Page to "SPIN"
                else: #otherwise
                    print("SPIN NOT READY")  # Print "SPIN NOT READY" 
                    time.sleep(1)  # wait 1 second
            else: #otherwise
                print("Please enter a defined value")  # Output "Please enter a defined value" 
                time.sleep(1)  # wait 1 second

        # Check if the user input is 'f' or 'F'
        elif val == 'f' or val == 'F':
            if Rewards_Page == 2:  # Check if the current Rewards_Page is 2
                skip_cost = 200 * int(Spin_Time_To_Wait_Min)  # Calculate skip_cost based on Spin_Time_To_Wait_Min
                prompt = input(f"Would you like pay {skip_cost} to skip cooldown? (y/n): ")  # Ask the user if they want to pay to skip cooldown
                if prompt == 'y' or prompt == 'Y':  # If the user input is 'y' or 'Y'
                    if cash >= skip_cost:  # Check if the user has enough cash
                        cash -= skip_cost  # reduce skip_cost from cash
                        Spin_Overide = True  # Set Spin_Overide to True
                    else: #otherwise
                        print("Not enough cash")  # Print "Not enough cash" 
                        time.sleep(1)  # wait 1 second
                elif prompt == 'n' or prompt == 'N':  # If the user input is 'n' or 'N'
                    DoRewards()  # open Rewards page
                else:  # otherwise
                    print("Please enter a defined value")  # Output "Please enter a defined value"
                    time.sleep(1)  # wait 1 second
        # Check if the user input is 'P' or 'p'
        elif val == 'P' or val == 'p':
            if Rewards_Page == "SPIN":  # Check if the current Rewards_Page is "SPIN"
                Spin_start_time = time.time()  # Set Spin_start_time to the current time
                Spin_Overide = False  # Set Spin_Overide to False
                DoSpin()  # open the spin page
            else: #otherwise
                print("Please enter a defined value")  # Output "Please enter a defined value" 
                time.sleep(1)  # wait 1 second
        
        # Check if the user input is 'M' or 'm'
        elif val == 'M' or val == 'm':
            if Rewards_Page == 3:  # Check if the current Rewards_Page is 3
                if Dungeon_Time_To_Wait_Min < 0:  # Check if Dungeon_Time_To_Wait_Min is less than 0
                    Dungeon_start_time = time.time()  # Set Dungeon_start_time to the current time
                    DoDungeon()  # open the dungeon page
                else: #otherwise
                    print("Dungeon NOT READY")  # Print "Dungeon NOT READY" 
                    time.sleep(1)  # wait 1 second
            else:#otherwise
                print("Please enter a defined value")  # Output "Please enter a defined value" 
                time.sleep(1)  # wait 1 second
        else:#otherwise
            print("Please enter a denfined value") #Output "Please enter a denfined value"
            time.sleep(1) #wait 1 second


#Define function for Dungeon gamemode
def DoDungeon():
    # Define global variables used in the function
    global playing, cash, multiplier, Shop_Rating, Shop_Rating_Cost, multiplier_cost, seperater, section
    global ratings, DungeonMultiplier, Dungeon_Cooldown, High_Dungeon_Score, Last_Dungeon_Score

    # Loop to keep the game running while the variable playing is True
    while playing == True:
        # Clear the screen
        os.system('cls')

        # Print the dungeon section
        print(section.Dungeon)
        
        # Get user input for the next action
        val = input("> ")

        # Check if the user input is 'D' or 'd'
        if val == 'D' or val == 'd':
            # Define math operations
            operation = ['+', '-', '*', '/']
            SeshCash = 0 #define session cash
            NumCorrect = 0 #define number of correct answers
            Wrong_Counter = 0 #define number of wrong answers
            DifficultyCounter = 0 #define difficulty counter

            # while questions wrong are less than 2
            while Wrong_Counter < 2:
                # Clear the screen
                os.system('cls')

                # Generate random number 1
                num1 = random.randint(1, 100)
                # Generate random number 2
                num2 = random.randint(1, 100)
                # Generate random operation
                opr1 = random.choice(operation)
                #if random operation is '+'
                if opr1 == operation[0]:
                  DifficultyCounter += 0.5  #increase difficulty counter by 0.5
                  answer = num1 + num2 #get answer
                #if random operation is '-'
                elif opr1 == operation[1]:
                  DifficultyCounter += 0.5   #increase difficulty counter by 0.5
                  answer = num1 - num2 #get answer
                #if random operation is '*'
                elif opr1 == operation[2]:
                  DifficultyCounter += 1.25 #increase difficulty counter by 1.25
                  answer = num1 * num2 #get answer
                #otherwise
                else:
                  DifficultyCounter += 1.75 #increase difficulty counter by 1.75
                  answer = num1 / num2 #get answer

                # Print the math question
                print(f"{num1} {opr1} {num2}")

                # while main game playing variable is True
                while playing:
                #try the following code     
                  try:
                     #get answer input 
                    response = float(input("Answer: "))
                    #if error occurs
                  except:
                      #prompt value error to user
                    print("Please input a number value")
                    time.sleep(1) #wait 1 second
                    delete_multiple_lines(2) #delete previous 2 lines from screen
                  else: #otherwise
                    break #end the loop

                # Check if the user's response is correct
                if response == answer.__round__(2):
                    #output praise message 
                  print(f"Good Job!\n{cash_color} + 1")
                  SeshCash += 1 #increase session cash by 1
                  NumCorrect += 1 #increase number of correct answers by 1
                  time.sleep(1) #wait 1 second
                  delete_multiple_lines(5) #delete previous 5 lines from screen
                else: #otherwise
                  print(("Incorrect!")) #ouput incorrect answer
                  Wrong_Counter += 1 #increase number of wrong answers by 1
                  time.sleep(1) #wait 1 second
                  delete_multiple_lines(4) #delete previous 4 lines from screen

            # otherwise
            else:
              os.system("cls") #clear screen

              #if the game multiplier is a number
              if isinstance(multiplier, int):
                  # Calculate the total session cash times game multiplier
                TotalSeshCash = (SeshCash * DungeonMultiplier) * multiplier
              else: #otherwise
                  # Calculate the total session cash times 1
                TotalSeshCash = (SeshCash * DungeonMultiplier) * 1

              # Check if TotalSeshCash is a string and set it to 0 if it is
              if isinstance(TotalSeshCash, str):
                TotalSeshCash = 0

              # Update the player's cash
              cash += TotalSeshCash

              #set high score to False
              HighScore = False
              
              # if number of correct answer is greater the previous high score
              if NumCorrect > High_Dungeon_Score:
                #update dungeon high score
                High_Dungeon_Score = NumCorrect
                #Set highscore check to True
                HighScore = True

              # Set the Last_Dungeon_Score to the number of correct answers
              Last_Dungeon_Score = NumCorrect 

              # Print the summary of the session's performance
              print(f"""{seperater}
              Questions Correct (Score): {NumCorrect}
              {seperater}
              Difficulty Score: {colors.UNDERLINE + str(DifficultyCounter) + colors.END}
              {seperater}
              Dungeon Cash Multiplier = {colors.BOLD + colors.PURPLE + str(DungeonMultiplier) + colors.END}
              {seperater}
              Game Cash Multiplier = {colors.BOLD + colors.PURPLE + str(multiplier) + colors.END}
              {seperater}
              Total Cash Earned = {colors.BOLD + colors.GREEN + str(TotalSeshCash) + colors.END}
              [X] Exit To Rewards Page
                  """)

              # Print "New High Score!" if the session's score is a new high score
              if HighScore == True:
                print(f"{colors.BOLD + colors.YELLOW + 'New High Score!' + colors.END}")

              # if the main game playing variable is True
              while playing:
                #get input
                Choice = input("> ")
                #if input is a form of 'x'
                if Choice == "X" or Choice == 'x':
                  DoRewards() #open rewards page
                else: #otherwise
                    print("Please enter a defined option") #output incorrect input
                    time.sleep(1) #wait 1 second
                    delete_multiple_lines(2) #delete previous 2 lines from screen

#define function for lucky spin menu
def DoSpin():
    # Declare global variables 
    global Item_Values, colors

    # Define Common items list
    CommonItems = ["DUSTY_BROOM", "RUST_BUCKET", "CHUM_SIGN"]
    # Define Rare items list
    RareItems = ["KELP_SEVICHE_HAT", "TACO_TUESDAY_STICKER", "MACRONALD_DONALD"]
    # Define Legend items list
    LegendItems = ["GOLDEN_TUXEDO", "GOLDEN_GLOVES", "PLATINUM_TOWEL"]
    # Define Mythic items list
    MythicItems = ["HOLY_DUSTY_BROOM", "HOLY_RUST_BUCKET"]

    # Randomly choose an item and determine its rarity
    Item_Rolled = random.choice(list(Item_Values.keys()))  # Randomly select an item from Item_Values dictionary
    if Item_Rolled in CommonItems:  # Check if the rolled item is in the CommonItems list
        Item_Rarity = colors.BOLD + colors.BROWN + "COMMON" + colors.END  # Set the item rarity as "COMMON"
    elif Item_Rolled in RareItems:  # Check if the rolled item is in the RareItems list
        Item_Rarity = colors.BOLD + colors.BLUE + "RARE" + colors.END  # Set the item rarity as "RARE"
    elif Item_Rolled in LegendItems:  # Check if the rolled item is in the LegendItems list
        Item_Rarity = colors.BOLD + colors.YELLOW + "LEGEND" + colors.END  # Set the item rarity as "LEGEND"
    else: #otherwise
        Item_Rarity = colors.BOLD + colors.PURPLE + "MYTHIC" + colors.END  # Set the item rarity as "MYTHIC"

    for i in Item_Values:  # Iterate over the keys in the Item_Values dictionary
        if i == Item_Rolled:  # Check if the current key matches the rolled item
            Item_Values[i]['is_locked'] = colors.BOLD + colors.CYAN + "UNLOCKED" + colors.END  # Update the status to "UNLOCKED"

    Ex = False  # Initialize the variable Ex as False
    while Ex == False:  # Continue looping while Ex is False
        # Clear the screen
        os.system("cls")

        # Print the rolled item and its rarity
        print(f"You Rolled...............................\nWait For It..............\n OMG\n You Received a {Item_Rarity}\n It's....................................\n {colors.BOLD + str(Item_Rolled) + '!' + colors.END}")

        # Print the unlocked item
        print(f'\n\n\n{colors.BOLD + colors.PURPLE + str(Item_Rolled) + " UNLOCKED" + colors.END}\n\n\n')

        # Prompt the user to go back or continue
        val = input("Go Back? (y/n): ")  # Get user input
        if val == 'y' or val == 'Y':  # If the user input is 'y' or 'Y'
            DoRewards()  # open rewards page
        elif val == 'n' or val == 'N':  # If the user input is 'n' or 'N'
            GameMenu()  # open game menu
        else: #otherwise
            print("Please enter a defined value")  # output 'enter a defined value'
            time.sleep(1)  # wait 1 second

#define information page function
def DoInformation():
    #define global variables
    global playing,colors,seperater
    
    #while main game playing variable is True
    while playing:
        #clear screen
        os.system('cls')

        #output page cover
        print(f"""\nChoose Inquiry:\n
{colors.BOLD + colors.UNDERLINE + 'Order Station:' + colors.END} enter [O]
{seperater}
{colors.BOLD + colors.UNDERLINE + 'Upgrades:' + colors.END} enter [U]
{seperater}
{colors.BOLD + colors.UNDERLINE + 'Rewards:' + colors.END} enter [R]
{seperater}  
{colors.BOLD + colors.UNDERLINE + 'Settings' + colors.END} enter [S]
{seperater}
{colors.BOLD + colors.UNDERLINE + 'Information' + colors.END} enter [I]
{seperater}
{colors.BOLD + colors.UNDERLINE + 'Cash' + colors.END} enter [C]
{seperater}
{colors.BOLD + colors.UNDERLINE + 'Multipliers' + colors.END} enter [M]
{seperater}
{colors.BOLD + colors.UNDERLINE + 'Shop Rating' + colors.END} enter [H]

Enter [X] to exit
              """)
        
        #get input
        inquiry = input("> ")
        # if input lowered/is 'o' then output brief synopsis of the order station
        if inquiry.lower() == 'o':
            os.system('cls')
            print(f"""
{colors.BOLD + colors.UNDERLINE + 'Order Station:' + colors.END} \n
The order station is where the customer-selected order is broken into 
sections, with each ingredient having its own random difficulty. This difficulty 
will be averaged by default and be displayed at the top of the screen (this can 
be changed in settings to show the numeral level of difficulty for more precision). 
The game will wait for you to input that you're ready and begin to ask you a random
math question based on the formula for each ingredient's difficulty. This game mode is 
where you can earn cash, shop rating, and levels for your restaurant. Specialized 
game modes may vary, providing their own synopsis.               
              """)
            input("Press Enter to return to the main menu...")
                # if input lowered/is 'o' then output brief synopsis of the order station
        # if input lowered/is 'u' then output brief synopsis of the upgrades menu
        elif inquiry.lower() == 'u':
            os.system('cls')
            print(f"""
{colors.BOLD + colors.UNDERLINE + 'Upgrades:' + colors.END} \n
The Upgrades is where you can upgrade your shop multiplier and increase your shop rating!           
              """)
            input("Press Enter to return to the main menu...")
                # if input lowered/is 'o' then output brief synopsis of the order station
        # if input lowered/is 'r' then output brief synopsis of the rewards menu
        elif inquiry.lower() == 'r':
            os.system('cls')
            print(f"""
{colors.BOLD + colors.UNDERLINE + 'Rewards:' + colors.END} \n
Rewards is where you can earn passive income, complete a math dungeon game mode, or spin the lucky wheel for an item!           
              """)
            input("Press Enter to return to the main menu...")
                # if input lowered/is 'o' then output brief synopsis of the order station
        # if input lowered/is 's' then output brief synopsis of the store menu
        elif inquiry.lower() == 's':
            os.system('cls')
            print(f"""
{colors.BOLD + colors.UNDERLINE + 'Settings:' + colors.END} \n
The Settings allow you to customize various aspects of the game, such as how difficulties are displayed and other game options.           
              """)
            input("Press Enter to return to the main menu...")
                # if input lowered/is 'o' then output brief synopsis of the order station
        # if input lowered/is 'i' then output brief synopsis of the information menu
        elif inquiry.lower() == 'i':
            os.system('cls')
            print(f"""
{colors.BOLD + colors.UNDERLINE + 'Information:' + colors.END} \n
This section provides general information about the different game modes and how they function within the game.           
              """)
            input("Press Enter to return to the main menu...")
                # if input lowered/is 'o' then output brief synopsis of the order station
        # if input lowered/is 'c' then output brief synopsis of the settings menu
        elif inquiry.lower() == 'c':
            os.system('cls')
            print(f"""
{colors.BOLD + colors.UNDERLINE + 'Cash:' + colors.END} \n
The Cash mode allows you to earn currency within the game, which can be used for various purposes such as purchasing upgrades.           
              """)
            input("Press Enter to return to the main menu...")
                # if input lowered/is 'o' then output brief synopsis of the order station
        # if input lowered/is 'm' then output brief synopsis of the game multiplier
        elif inquiry.lower() == 'm':
            os.system('cls')
            print(f"""
{colors.BOLD + colors.UNDERLINE + 'Multipliers:' + colors.END} \n
The Multipliers mode allows you to increase your shop's efficiency by applying multipliers to certain aspects of your business.           
              """)
            input("Press Enter to return to the main menu...")
                # if input lowered/is 'o' then output brief synopsis of the order station
        # if input lowered/is 'h' then output brief synopsis of the shop rating
        elif inquiry.lower() == 'h':
            os.system('cls')
            print(f"""
{colors.BOLD + colors.UNDERLINE + 'Shop Rating:' + colors.END} \n
The Shop Rating mode is where you can view and improve your shop's rating, which is essential for attracting more customers and growing your business.           
              """)
            input("Press Enter to return to the main menu...")
                # if input lowered/is 'o' then output brief synopsis of the order station
        #if input lowered/is 'x' 
        elif inquiry.lower() == 'x':
            GameMenu() # open game menu
        else:#otherwise
            print("Please enter a valid option.") #output valid option not inputted
            input("Press Enter to continue...") #get input to retart loop

#define settings page function
def DoSettings():
    # Declare global variables used in the function
    global OverallRating, keybinds
    global OverallScore
    global playing
    global colors, Order_Station_Keybind, Settings_Keybind, Rewards_Keybind, Store_Keybind, Upgrades_Keybind, Information_Keybind
    global ChangeAVGDisplay, DisplayCustomers
    global Name

    # while main game variable playing is True
    while playing == True:
        # Clear the screen
        os.system('cls')

        # if display change check is false
        if ChangeAVGDisplay == False:
            #set scale form variable to 'Average'
            ScaleForm = "Average"
        else: #otherwise
            #set scale form variable to 'Numerical'
            ScaleForm = "Numerical"

        # if display csutomers check is false
        if DisplayCustomers == False:
            #set display variable to 'Regular
            display = "Regular"
        #otherwise
        else:
            #set display variable to 'Prompt'
            display = "Prompt"

        # Display menu options and current settings
        print(f"""\n
    Change average difficulty scale form (Current: {ScaleForm}), {colors.BOLD + 'enter [D]' + colors.END} 
    {seperater} 
    Change store Name (Current: {Name}), {colors.BOLD + 'enter [N]' + colors.END}
    {seperater}
    Change customer prompt menu (Current: {display}), {colors.BOLD + 'enter [C]' + colors.END}
    {seperater}
    Change main menu keybinds, {colors.BOLD + 'enter [M]' + colors.END}

    To exit, {colors.BOLD + 'enter [X]' + colors.END}
              """)

        # Get user input
        val = input("> ")
        #if input is a form of 'd'
        if val == 'D' or val == 'd':
            # opposite the value of ChangeAVGDisplay
            ChangeAVGDisplay = not ChangeAVGDisplay
        #if input is a form of 'n'
        elif val == 'N' or val == 'n':
            # Prompt the user to enter a new name and update the Name variable
            NewName = input("Enter New Name: ")
            #set new name as name variable
            Name = NewName
        #if input is a form of 'c'
        elif val == 'C' or val == 'c':
            # opposite the value of DisplayCustomers
            DisplayCustomers = not DisplayCustomers
        #if input is a form of 'x'
        elif val == 'X' or val == 'x':
            # Return to the main game menu
            GameMenu()
        #if input is a form of 'm'
        elif val == 'M' or val == 'm':
            # Prompt the user to enter new keybinds for menu actions
            print("\nEnter the new keybind for each action:")
            new_keybinds = {} #make holder list for new keybinds
            
            # dictionary to store keybinds
            keybinds = {
                "Store": Store_Keybind,
                "Order Station": Order_Station_Keybind,
                "Rewards": Rewards_Keybind,
                "Settings": Settings_Keybind,
                "Information": Information_Keybind,
                "Upgrades": Upgrades_Keybind,
            }

            # Loop through each action in the keybinds dictionary 
            for action in keybinds:
                # valid keybind pre set to False 
                valid_keybind = False
                while valid_keybind == False:  # Continue looping until a valid keybind is entered
                    # Prompt the user to input a new keybind and auto convert it to uppercase
                    new_key = input(f"New key for {action}: ").upper()
                    if new_key in keybinds.values():  # Check if the new key is already used for another action
                        # display a message and prompt the user to enter a different key
                        print(f"Key '{new_key}' is already assigned to another action.")
                        time.sleep(1)  # Wait for 1 second 
                        delete_multiple_lines(2)  # Remove the last 2 lines from console
                    elif len(new_key) == 1 and new_key.isalpha():  # Check if the new key is a single alphabetical character
                        valid_keybind = True  # set valid_keybind to True
                        keybinds[action] = new_key  # Update the keybind in the dictionary for the current action
                    else: #otherwise
                        # display an error message
                        print("Invalid key. Please enter a single alphabetical character.")
                        time.sleep(1)  # Wait for 1 second 
                        delete_multiple_lines(2)  # Remove the last 2 lines from console 

            # update the variables with the new keybinds 
            Store_Keybind = keybinds["Store"]
            Order_Station_Keybind = keybinds["Order Station"]
            Rewards_Keybind = keybinds["Rewards"]
            Settings_Keybind = keybinds["Settings"]
            Information_Keybind = keybinds["Information"]
            Upgrades_Keybind = keybinds["Upgrades"]

#define order functional function
def DoOrder():
    # Declare global variables
    global Menu, OverallScore, OverallRating

    # Initialize lists to store the order and ratings
    order = []
    ratings = []

    # Randomly select bread from the menu
    breadRAW = random.choice(Menu.breads)
    bread = breadRAW[0]  # Extract the bread name
    ratings.append(breadRAW[1])  # Add bread rating to ratings list
    order.append(bread)  # Add bread to order list

    # Randomly select vegetables from the menu
    vegetablesRAW = random.choice(Menu.vegetables)
    vegetables = vegetablesRAW[0]  # Extract the vegetables name
    ratings.append(vegetablesRAW[1])  # Add vegetables rating to ratings list
    order.append(vegetables)  # Add vegetables to order list

    # Randomly select sauces from the menu
    saucesRAW = random.choice(Menu.sauces)
    sauces = saucesRAW[0]  # Extract the sauces name
    ratings.append(saucesRAW[1])  # Add sauces rating to ratings list
    order.append(sauces)  # Add sauces to order list

    # Randomly select meats from the menu
    meatsRAW = random.choice(Menu.meats)
    meats = meatsRAW[0]  # Extract the meats name
    ratings.append(meatsRAW[1])  # Add meats rating to ratings list
    order.append(meats)  # Add meats to order list

    # Initialize variables for overall score and rating
    OverallScore = 0
    OverallRating = 0

    # loop through the length of the ratings list
    for i in range(len(ratings)):
        #oncrease overall score by the rating at index
        OverallScore += ratings[i]

    #if overall score is less than or equal to 7
    if OverallScore <= 7:
        OverallRating = 0 #set overall rating to 0 
    #if overall score is greater than 7 and is less than 11
    elif OverallScore > 7 and OverallScore < 11:
        OverallRating = 1#set overall rating to 1
    #if overall score is greater than 10 and is less than 12
    elif OverallScore > 10 and OverallScore < 13:
        OverallRating = 2#set overall rating to 2
    #otherwise
    else:
        OverallRating = 3 #set overall rating to 3

    # Loop through the length of the ratings list
    for i in range(len(ratings)):
        if ratings[i] == 1:  # If the rating at index i is 1, set it to "Easy" with green color
            ratings[i] = colors.BOLD + colors.GREEN + 'Easy' + colors.END
        elif ratings[i] == 2:  # If the rating at index i is 2, set it to "Medium" with yellow color
            ratings[i] = colors.BOLD + colors.YELLOW + 'Medium' + colors.END
        elif ratings[i] == 3:  # If the rating at index i is 3, set it to "Hard" with red color
            ratings[i] = colors.BOLD + colors.RED + 'Hard' + colors.END
        else:  # If the rating at index i is not 1, 2, or 3, set it to "EXTREME" with purple color
            ratings[i] = colors.BOLD + colors.PURPLE + 'EXTREME' + colors.END


    # Return the order list, ratings list, overall rating, and overall score
    return order, ratings, OverallRating, OverallScore


def DoOrderMenu():
    global cash, Order1_time, Order2_time, Order3_time
    global seperater, Customer_Wait_Time    
    global Menu, Shop_Rating
    global playing
    global colors, NoOrder, NoRatings
    global level, Ovr_Scores1, Ovr_Scores2, Ovr_Scores3, Ovr_Ratings1, Ovr_Ratings2, Ovr_Ratings3
    global Ratings1, Ratings2, Ratings3
    global OverallRating, CurrentOrders
    global OverallScore
    global ChangeAVGDisplay, customers, NumOrders, Order1, Order2, Order3, Order_Page

    while playing == True:
        Order_Page = 0
        os.system('cls')

        print(f"""

You have {colors.BOLD + colors.PURPLE + str(customers) + colors.END} Orders Available.

Complete them to earn cash and unlock rewards!

Enter [O] to view current orders              

              """)
        if customers == 1:
            print(f"""
Enter [A] to complete order 1
                  """)
        if customers == 2:
            print("""
Enter [A] to complete order 1
Enter [B] to complete order 2     
                  """)
        if customers == 3:
            print("""
Enter [A] to complete order 1
Enter [B] to complete order 2   
Enter [C] to complete order 3  
                  """)

        val = input("> ")
        if val == "o" or val == "O":
            if customers >= 1:
                ExWord = False
                if Order1 != []:
                    ViewPage = 1
                elif Order2 != []:
                    ViewPage = 2
                elif Order3 != []:
                    ViewPage = 3
                while ExWord == False:
                    os.system("cls")

                    if ViewPage == 1:
                        order = Order1
                        ratings = Ratings1
                        TimeLeft = int((time.time() - Order1_time) - Customer_Wait_Time) * -1
                        if TimeLeft < 0:
                             TimeLeft = "FAILED"
                    elif ViewPage == 2:
                        order = Order2
                        ratings = Ratings2
                        TimeLeft = int((time.time() - Order2_time) - Customer_Wait_Time) * -1
                        if TimeLeft < 0:
                             TimeLeft = "FAILED"
                    elif ViewPage == 3:
                        order = Order3
                        ratings = Ratings3
                        TimeLeft = int((time.time() - Order3_time) - Customer_Wait_Time) * -1
                        if TimeLeft < 0:
                             TimeLeft = "FAILED"
                    if order == []:
                        order = NoOrder
                        ratings = NoRatings
                        TimeLeft = "NaN" 
                    print(f"""
    Bread:  {order[0]} [{ratings[0]}]
    Vegetables:  {order[1]} [{ratings[1]}]
    Sauces:  {order[2]} [{ratings[2]}]
    Meats:  {order[3]} [{ratings[3]}]\n  

    Time Left: {colors.BOLD + colors.CYAN + str(TimeLeft) + colors.END} seconds

    Enter [>] for next order
    Enter [>] for previous order
    Enter [X] to exit                                       Order: {colors.BOLD+colors.CYAN+str(ViewPage)+colors.END}
                              """)
                    InVal = input("> ")
                    if InVal == ">":
                        if ViewPage < 3:
                            ViewPage += 1
                        else:
                            print("No next page!")
                            time.sleep(1)
                    elif InVal == "<":
                        if ViewPage != 1:
                            ViewPage -= 1
                        else:
                            print("No next page!")
                            time.sleep(1)
                    elif InVal == "x" or InVal =='X':
                        ExWord = True
                    else:
                        print("Please enter defined option")
                        time.sleep(1)
            else:
                print("No Current Orders!")
                time.sleep(1)

        elif val == 'a' or val == 'A':
            if Order1 != []:
                Order_Page = 1
            else:
                print("Invalid")
                time.sleep(1)
        elif val == 'B' or val == 'b':
            if Order2 != []:
                Order_Page = 2
            else:
                print("Invalid")
                time.sleep(1)
        elif val == 'C' or val == 'c':
            if Order3 != []:
                Order_Page = 3
            else:
                print("Invalid")
                time.sleep(1)
        elif val == 'x' or val == 'X':
            GameMenu()



        if Order_Page == 1:
            if customers != 0:
                if time.time() - Order1_time < Customer_Wait_Time:
                    DoOrderStation(Order1, Ratings1, Ovr_Ratings1, Ovr_Scores1)
                else:
                    if Shop_Rating != "LOCKED":
                        print("Too slow, customer left!")
                        time.sleep(1)
                        Shop_Rating = Shop_Rating.replace("*", "", 1).replace(" ", "", 1)
                        print(colors.BOLD + colors.PURPLE + "SHOP RATING - 1" + colors.END)
                        time.sleep(1)
                        ResetOrders(Ratings1)
                    else:
                        print("Too slow, customer left!")
                        time.sleep(1)
                        ResetOrders(Ratings1)
        elif Order_Page == 2:
            if customers >= 2:
                if time.time() - Order2_time < Customer_Wait_Time:
                    DoOrderStation(Order2, Ratings2, Ovr_Ratings2, Ovr_Scores2)
                else:
                    if Shop_Rating != "LOCKED":
                        print("Too slow, customer left!")
                        Shop_Rating = Shop_Rating.replace("*", "", 1).replace(" ", "", 1)
                        print(colors.BOLD + colors.PURPLE + "SHOP RATING - 1" + colors.END)
                        time.sleep(1)
                        ResetOrders(Ratings2)
                    else:
                        print("Too slow, customer left!")
                        time.sleep(1)
                        ResetOrders(Ratings2)

        elif Order_Page == 3:
            if customers == 3:
                if time.time() - Order3_time < Customer_Wait_Time:
                    DoOrderStation(Order3, Ratings3, Ovr_Ratings3, Ovr_Scores3)
                else:
                    if Shop_Rating != "LOCKED":
                        print("Too slow, customer left!")
                        Shop_Rating = Shop_Rating.replace("*", "", 1).replace(" ", "", 1)
                        print(colors.BOLD + colors.PURPLE + "SHOP RATING - 1" + colors.END)
                        time.sleep(1)
                        ResetOrders(Ratings3)
                    else:
                        print("Too slow, customer left!")
                        time.sleep(1)
                        ResetOrders(Ratings3)
        else:
            pass

# define reset orders function
def ResetOrders(ratings):
    # Declare global variables 
    global cash
    global cash_color
    global Ratings1, Ratings2, Ratings3, Order1, Order2, Order3
    global playing, Ovr_Scores1, Ovr_Scores2, Ovr_Scores3, Ovr_Ratings1, Ovr_Ratings2, Ovr_Ratings3
    global SeshCash, Order1_time, Order2_time, Order3_time
    global multiplier, operation, customers
    
    # Check if the provided ratings match Ratings1
    if ratings == Ratings1:
        # Shift the values of Order2 and Order3 to Order1 and Order2 
        Order1 = Order2
        Order1_time = Order2_time
        # Shift the values of Ratings2 and Ratings3 to Ratings1 and Ratings2 
        Ratings1 = Ratings2
        Ratings2 = Ratings3
        # Set Order3 to an empty list and reset its related variables
        Order2 = Order3
        Order2_time = Order3_time
        Ovr_Ratings1 = Ovr_Ratings2
        Ovr_Ratings2 = Ovr_Ratings3
        Ovr_Scores1 = Order2_time
        Ovr_Scores2 = Ovr_Scores3
        Order3 = []
        Order3_time = 0
        Ratings3 = []
        Ovr_Ratings3 = 0
        Ovr_Scores3 = 0
    # If the provided ratings match Ratings2
    elif ratings == Ratings2:
        # Shift the values of Order3 to Order2
        Order2 = Order3
        Order2_time = Order3_time
        # Shift the value of Ratings3 to Ratings2
        Ratings2 = Ratings3
        # Reset Order3 and its related variables
        Order3 = []
        Order3_time = 0
        Ratings3 = []
        Ovr_Ratings3 = 0
        Ovr_Scores3 = 0
    # If the provided ratings don't match Ratings1 or Ratings2
    else:
        # Reset Order3 and its related variables
        Order3 = []
        Order3_time = 0
        Ratings3 = []
        Ovr_Ratings3 = 0
        Ovr_Scores3 = 0
    
    # reduce the number of customers by 1
    customers -= 1


#define Order station page function
def DoOrderStation(order, ratings, OverallRating, OverallScore):
    # define global variables
    global cash, seperator, Menu, playing, colors, level, ratings1, ratings2, ratings3, ChangeAVGDisplay, customers, NumOrders, Order1, Order2, Order3
    
    # Clear the console
    os.system('cls')
    
    # Define the difficulties is a list with corresponding numbers
    difficulties = [['Easy', 1], ['Medium', 2], ['Hard', 3], ['EXTREME', 4]]
    # get the raw difficulty from the list
    DifficultyRaw = difficulties[OverallRating]
    # get the level of difficulty from the raw difficulty
    level = DifficultyRaw[1]
    #get the difficulty from the raw difficulty
    Difficulty = DifficultyRaw[0] 

    # if change display check is false
    if ChangeAVGDisplay == False:
        #if level is 1
        if level == 1:
            #output average difficulty
            print(f"\n\nDiffuculty: {colors['BOLD'] + colors['GREEN'] + Difficulty + colors['END']}\n{seperator}")
        #if level is 2
        elif level == 2:
            #output average difficulty
            print(f"\n\nDiffuculty: {colors['BOLD'] + colors['YELLOW'] + Difficulty + colors['END']}\n{seperator}")
        #if level is 3
        elif level == 3:
            #output average difficulty
            print(f"\n\nDiffuculty: {colors['BOLD'] + colors['RED'] + Difficulty + colors['END']}\n{seperator}")
        #if level is 4
        else:
            #output average difficulty
            print(f"\n\nDiffuculty: {colors['BOLD'] + colors['PURPLE'] + Difficulty + colors['END']}\n{seperator}")
    else: #otherwise
        #if level is 1
        if level == 1:
            #output numerical difficulty
            print(f"\n\nDiffuculty: {colors['BOLD'] + colors['GREEN'] + str(OverallScore) + colors['END']}\n{seperator}")
        #if level is 2
        elif level == 2:
            #output numerical difficulty
            print(f"\n\nDiffuculty: {colors['BOLD'] + colors['YELLOW'] + str(OverallScore) + colors['END']}\n{seperator}")
        #if level is 3
        elif level == 3:
            #output numerical difficulty
            print(f"\n\nDiffuculty: {colors['BOLD'] + colors['RED'] + str(OverallScore) + colors['END']}\n{seperator}")
        #otherwise
        else:
            #output numerical difficulty
            print(f"\n\nDiffuculty: {colors['BOLD'] + colors['PURPLE'] + str(OverallScore) + colors['END']}\n{seperator}")

    # Print the customer order details
    print(f"""\n Customer Order: \n
Bread:  {order[0]} [{ratings[0]}]
Vegetables:  {order[1]} [{ratings[1]}]
Sauces:  {order[2]} [{ratings[2]}]
Meats:  {order[3]} [{ratings[3]}]\n
{seperator}""")

    # while main game playing function is True
    while playing == True:
        # Print the options
        print(colors['CYAN'] + colors['BOLD'] + "[S] - Variables" + colors['END'])
        print(colors['RED'] + colors['BOLD'] + "\n[R] - Ready" + colors['END'])
        print(colors['BOLD'] + '\n[X] - Exit' + colors['END'])

        # Get user input
        val = input("> ")

        # Check input lowercased/is 'x'
        if val.lower() == 'x':
            DoOrderMenu() #open order menu
        # Check input lowercased/is 'r'
        elif val.lower() == 'r':
            #delete previous 6 lines from console
            delete_multiple_lines(6)
            DoSandwichMaker(ratings) #open sandwich maker page
        # Check input lowercased/is 's'
        elif val.lower() == 's':
            #delete previous 6 lines from console
            delete_multiple_lines(6)
            DoVariables(order, ratings, OverallRating, OverallScore) # Open variables page
        else: #otherwise
            print("Please enter a defined option") #output error
            time.sleep(1) #wait 1 second
            delete_multiple_lines(7) #delete previous 7 lines from console

def DoSandwichMaker(ratings):
    global cash
    global cash_color
    global Ratings1, Ratings2, Ratings3, Order1, Order2, Order3
    global playing,Ovr_Scores1, Ovr_Scores2, Ovr_Scores3, Ovr_Ratings1, Ovr_Ratings2, Ovr_Ratings3
    global SeshCash
    global multiplier, operation, customers
    SeshCash = 0
    CorrectAns = []
    NumCorrect = 0 
    operation = ['+', '-', '*', '/']
    for i in range(len(ratings)): 
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
        if NumCorrect == 4:
            if multiplier == 'LOCKED':
                delete_multiple_lines(1)
                print(f"""{seperater}
{colors.BOLD + colors.UNDERLINE + colors.PURPLE + 'MULTIPLIER UNLOCKED!' + colors.END}\n""")
                multiplier = 1

        ResetOrders(ratings)

        while playing:
            PlAgn = input("Go Back? (Y/N): ")
            if PlAgn == "Y" or PlAgn == 'y':
                DoOrderMenu()
            elif PlAgn == "N" or PlAgn == 'n':
                GameMenu()
            else:
                print("Please enter a defined option")
                time.sleep(2)
                delete_multiple_lines(2)

# Define variables function
def DoVariables(order, ratings, OverallRating, OverallScore):
    # declare global variables
    global playing
    # while main game playing variable is True
    while playing:
        # Clear screen
        os.system('cls')
        # output the menu of available variables
        print("Variables Include:\n\nAddition [+]\nSubtraction [-]\nMultiplication [x] \nDivision [/]\n")
        # output exit key
        print("Enter [x] to exit\n")
        # Get user input
        val = input("> ")
        # If the user input lowercased/is 'x'
        if val.lower() == 'x':
            DoOrderStation(order, ratings, OverallRating, OverallScore) #open order station page
        else: #otherwise
            # output input error
            print("Please enter a defined option")
            time.sleep(1) #wait 1 second

        
    
#define class of all menu items
class Menu:
    breads = [['regular', 1], ['sesame', 2], ['old-fashioned',3], ['4-cheese', 1], ['italian', 2], ['Chicago style', 3], ['Golden Yeast', 4]]
    vegetables = [['tomato', 1], ['cucumber', 2], ['carrot', 3], ['peppers', 1], ['jalapeno', 2], ['onion', 3], ['Golden Root', 4]]
    sauces = [['mayonnaise', 1], ['teriyaki', 2], ['ketchup', 3], ['mustard', 1], ['relish', 2], ['Hot sauce', 3], ['Golden Drool', 4]]
    meats = [['salami', 1], ['pepperoni', 2], ['chicken', 3], ['beef', 1], ['pork', 2], ['bacon', 3], ['Golden Ham', 4]]

#define class of all color choices
class colors:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BROWN = '\033[0;33m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   ITALIC = '\033[3m'
   BG_BLACK = '\033[40m'
   BG_RED = '\033[41m'
   BG_GREEN = '\033[42m'
   BG_YELLOW = '\033[43m'
   BG_BLUE = '\033[44m'
   BG_MAGENTA = '\033[45m'
   BG_CYAN = '\033[46m'
   BG_WHITE = '\033[47m'

#define dcitionary of all inventory items alongside their equip and unlock values
Item_Values = {
  "DUSTY_BROOM": {
      "is_locked": colors.RED + colors.BOLD + "LOCKED" + colors.END,
      "is_equipped": colors.BOLD + colors.PURPLE + "UNEQUIPPED" + colors.END
  },
  "RUST_BUCKET": {
      "is_locked": colors.RED + colors.BOLD + "LOCKED" + colors.END,
      "is_equipped": colors.BOLD + colors.PURPLE + "UNEQUIPPED" + colors.END
  },
  "CHUM_SIGN": {
      "is_locked": colors.RED + colors.BOLD + "LOCKED" + colors.END,
      "is_equipped": colors.BOLD + colors.PURPLE + "UNEQUIPPED" + colors.END
  },
  "KELP_SEVICHE_HAT": {
      "is_locked": colors.RED + colors.BOLD + "LOCKED" + colors.END,
      "is_equipped": colors.BOLD + colors.PURPLE + "UNEQUIPPED" + colors.END
  },
  "TACO_TUESDAY_STICKER": {
      "is_locked": colors.RED + colors.BOLD + "LOCKED" + colors.END,
      "is_equipped": colors.BOLD + colors.PURPLE + "UNEQUIPPED" + colors.END
  },
  "MACRONALD_DONALD": {
      "is_locked": colors.RED + colors.BOLD + "LOCKED" + colors.END,
      "is_equipped": colors.BOLD + colors.PURPLE + "UNEQUIPPED" + colors.END
  },
  "GOLDEN_TUXEDO": {
      "is_locked": colors.RED + colors.BOLD + "LOCKED" + colors.END,
      "is_equipped": colors.BOLD + colors.PURPLE + "UNEQUIPPED" + colors.END
  },
  "GOLDEN_GLOVES": {
      "is_locked": colors.RED + colors.BOLD + "LOCKED" + colors.END,
      "is_equipped": colors.BOLD + colors.PURPLE + "UNEQUIPPED" + colors.END
  },
  "PLATINUM_TOWEL": {
      "is_locked": colors.RED + colors.BOLD + "LOCKED" + colors.END,
      "is_equipped": colors.BOLD + colors.PURPLE + "UNEQUIPPED" + colors.END
  },
  "HOLY_DUSTY_BROOM": {
      "is_locked": colors.RED + colors.BOLD + "LOCKED" + colors.END,
      "is_equipped": colors.BOLD + colors.PURPLE + "UNEQUIPPED" + colors.END
  },
  "HOLY_RUST_BUCKET": {
      "is_locked": colors.RED + colors.BOLD + "LOCKED" + colors.END,
      "is_equipped": colors.BOLD + colors.PURPLE + "UNEQUIPPED" + colors.END
  },

}

#define delete multiple lines variable
def delete_multiple_lines(n=1):
    #loop for the length of the parameter variable
    for i in range(n):
        sys.stdout.write("\x1b[1A")  # cursor up one line
        sys.stdout.write("\x1b[2K")  # delete the last line

# Lists to store orders and ratings for three orders
Order1 = []
Order2 = []
Order3 = []
Ratings1 = []
Ratings2 = []
Ratings3 = []

# Overall ratings and scores for three orders
Ovr_Ratings1 = 0
Ovr_Ratings2 = 0
Ovr_Ratings3 = 0
Ovr_Scores1 = 0
Ovr_Scores2 = 0
Ovr_Scores3 = 0

# Time for each order
Order1_time = 0
Order2_time = 0
Order3_time = 0

# Lists for when there are no orders or ratings available
NoOrder = ['NaN', 'NaN', 'NaN', 'NaN', 'NaN']
NoRatings = ['NaN', 'NaN', 'NaN', 'NaN', 'NaN']

# check for the first opening of the program (Inital is True)
FirstOpening = True

# Current page in the order station (Initial is 0)
OrderPage = 0

# check for if a perk has been applied (Inital is False)
PerkApplied = False

# Keybindings for different sections (Initial is 'S','O','R','C','I',U')
Store_Keybind = 'S'
Order_Station_Keybind = 'O'
Rewards_Keybind = 'R'
Settings_Keybind = 'C'
Information_Keybind = 'I'
Upgrades_Keybind = 'U'

# Start times for various timers
start_time = time.time()
Cash_start_time = time.time()
cpm_start_time = time.time()
Spin_start_time = time.time()
Dungeon_start_time = time.time()

# List to store current inventory item
Inventory_Slot = []

# Separator string for formatting
seperater = "----------------------------------------------------------------"

# Initial cash amount
cash = 0

# Initial multiplier (locked initially)
multiplier = 1  # "LOCKED"

# Shop rating (locked initially)
Shop_Rating = '*'  # "LOCKED"

# Cost of unlocking the multiplier and shop rating (locked initially)
multiplier_cost = "LOCKED"
Shop_Rating_Cost = "LOCKED"

# Name of the shop (Initial: "Paulie's")
Name = "Paulie's"

# Cash per minute (cpm)
cpm = 0

# Number of staff members
StaffNum = 0

# Cost of hiring staff
Staff_Cost = 1

# Number of customers
customers = 0

# Time a customer waits before leaving
Customer_Wait_Time = 300

# Multiplier for the shop's earnings
Shop_Multiplier = 1

# Multiplier for dungeon scores
DungeonMultiplier = 1

# Last and highest dungeon scores
Last_Dungeon_Score = 0
High_Dungeon_Score = 0

# Current page in the rewards and items sections
Rewards_Page = 1
Items_Page = 1

# check to display customers
DisplayCustomers = False

# Color for displaying cash
cash_color = colors.GREEN + colors.BOLD + "Cash:" + colors.END

# checks for resetting cash and cpm
Cash_Reset = False
cpm_Reset = False

# Variables for spin period and dungeon cooldown
Spin_Period = 0
Spin_Overide = False
Dungeon_Cooldown = 0

# Current time in seconds and minutes since the start of the program
current_time_sec = time.time() - start_time
current_time_min = int(current_time_sec / 60)
cpm_current_time_min = int(current_time_sec / 60)

# check to change the display of average values
ChangeAVGDisplay = False

# Start the game menu
start = GameMenu()

