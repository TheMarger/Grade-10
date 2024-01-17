import os, time, random, sys, re


def GameMenu():
    # Define global variables that will be used in this function
    global Shop_Rating
    global multiplier
    global cash
    global seperater
    global colors
    global playing, Store_Keybind, Order_Station_Keybind, Upgrades_Keybind,Rewards_Keybind,Settings_Keybind
    global Name, customers, FirstOpening,Information_Keybind
    # Set playing flag to True to enter the main game loop
    playing = True
    # Start the main game loop
    while playing:
        # Clear the console screen
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
                    # Set playing flag to False to exit the main loop
                    playing = False
                elif choice == "N" or choice == "n":
                    # If not exiting, go back to the game menu
                    GameMenu()
                else:
                    # Prompt the user to enter a valid option
                    print("Please enter a defined option")
                    time.sleep(1)
                    # Clear the console screen and go back to the top of the loop
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

def DoStore():
    # Define global variables that will be used in this function
    global Name, FirstOpening, multiplier, Shop_Rating, Shop_Rating_Cost, cash, playing, multiplier_cost

    # Check if it's the first time the store is being opened
    if FirstOpening == True:
        # If it's the first time, loop until the user decides to proceed
        while playing == True:
            # Clear the console screen
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
        # Clear the console screen
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


def DoShop():
    global Order1_time, Order2_time, Order3_time, Inventory_Slot, cpm_Reset, cpm_current_time_sec, cpm_start_time, cpm_current_time_min, current_time_sec, StaffNum, Ratings1, Ratings2, Ratings3, Order1, Order2, Order3, Ovr_Ratings1, Ovr_Ratings2, Ovr_Ratings3, Ovr_Scores1, Ovr_Scores2, Ovr_Scores3, multiplier, Shop_Rating, Shop_Rating_Cost, Shop_Multiplier, cash, playing, multiplier_cost, StaffNum, customers, cpm, Staff_Cost
    while playing == True:
        os.system('cls')
        if Shop_Rating == "LOCKED":
            print("Dishes Dirty, Wash Them? [W]")
        if Shop_Rating != "LOCKED" and multiplier != "LOCKED":
            cpm = (((customers + len(Shop_Rating.split())) * Shop_Multiplier) * (multiplier))
        elif Shop_Rating == "LOCKED" and multiplier != "LOCKED":
            cpm = (((customers + 0) * Shop_Multiplier) * (multiplier))
        else:
            cpm = (((customers + 0) * Shop_Multiplier) * (1))

        cpm = cpm.__round__(2)

        if customers == 0:
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

              """)
        elif customers == 1:
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

              """)
        elif customers == 2:
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

              """)

        else:
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

              """)

        val = input("> ")
        if val == 'X' or val == 'x':
            DoStore()
        elif val == 'C' or val == 'c':
            if customers < len(Shop_Rating.split()):
                if customers < 3:
                    if customers == 0:
                        customers += 1
                        Order1_RAW = DoOrder()
                        Order1 = Order1_RAW[0]
                        Ratings1 = Order1_RAW[1]
                        Ovr_Ratings1 = Order1_RAW[2]
                        Ovr_Scores1 = Order1_RAW[3]
                        Order1_time = time.time()
                        print("Customer Enters!\nComplete their order soon!")
                        time.sleep(1)
                    elif customers == 1:
                        customers += 1
                        Order2_RAW = DoOrder()
                        Order2 = Order2_RAW[0]
                        Ratings2 = Order2_RAW[1]
                        Ovr_Ratings2 = Order2_RAW[2]
                        Ovr_Scores2 = Order2_RAW[3]
                        Order2_time = time.time()
                        print("Customer Enters!\nComplete their order soon!")
                        time.sleep(1)
                    else:
                        customers += 1
                        Order3_RAW = DoOrder()
                        Order3 = Order3_RAW[0]
                        Ratings3 = Order3_RAW[1]
                        Ovr_Ratings3 = Order3_RAW[2]
                        Ovr_Scores3 = Order3_RAW[3]
                        Order3_time = time.time()
                        print("Customer Enters!\nComplete their order soon!")
                        time.sleep(1)
                else:
                    print("Complete current orders to allow more customers!")
                    time.sleep(1)
            else:
                print("More Shop Rating Required!")
                time.sleep(1)

        elif val == 'R' or val == 'r':
            DoShop()
        elif val == 'W' or val == 'w':
            if Shop_Rating == "LOCKED":
                DoDishes()
            else:
                pass
        elif val == 'M' or val == 'm':
            ex = False
            cpm_current_time_sec = time.time() - cpm_start_time
            cpm_current_time_min = int(cpm_current_time_sec / 60)
            Cash_Earned = cpm * cpm_current_time_min
            while ex == False:
                if cpm_Reset == True:
                    cash += (Cash_Earned * Shop_Multiplier)
                    Cash_Earned = 0
                    cpm_start_time = time.time()
                    print("Claimed!")
                    time.sleep(1)
                    cpm_Reset = False
                else:
                    pass
                os.system('cls')

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
                      """)
                inval = input("> ")
                if inval == 'c' or inval == 'C':
                    cpm_Reset = True
                elif inval == 'x' or val == 'X':
                    DoShop()
                else:
                    print("Please enter a defined value")
                    time.sleep(1)




        elif val == 't' or val == 'T':
            prompt = input(f"Would you like to purchase 1 staff for {Staff_Cost} cash? (y/n): ")
            if prompt == 'y' or prompt == 'Y':
                if cash >= Staff_Cost:
                    cash -= Staff_Cost
                    StaffNum += 1
                    Staff_Cost = StaffNum * 200
                    Shop_Multiplier += 1
                else:
                    print("Not enough cash!")
                    time.sleep(1)

        else:
            print("Please enter a defined option")
            time.sleep(1)  

def DoDishes():
    global cash, Shop_Rating, colors

    while Shop_Rating == "LOCKED":
        os.system("cls")

        print(f"""

Welcome to the dishes gamemode!

This is where you can unlock your shop rating!

Press [P] to begin!    

              """)

        val = input("> ")
        if val == 'P' or val == 'p':
            points = 0
            Choices = ['w', 'a', 's', 'd']
            while points < 5:
                os.system('cls')
                letter = random.choice(Choices)
                print(f"""
    Enter the the letter eblow in under 1 seconds and gain a point
    5 points = WIN!

    -------------------------------------------------------------------------
    Letter = {letter}
    -------------------------------------------------------------------------     
                      """)
                start = time.time()
                val = input("> ")
                if val:
                    end = time.time() - start
                    if val == letter and end < 1:
                        points += 1
                        print(colors.BOLD + colors.GREEN + "POINTS + 1" + colors.END)
                        time.sleep(1)
                    elif val == letter and end > 1:
                        print(colors.BOLD + colors.YELLOW + "TOO SLOW!" + colors.END)
                        time.sleep(1)
                    else:
                        print(colors.BOLD + colors.RED + "WRONG LETTER!" + colors.END)
                        time.sleep(1)
            else:
                Shop_Rating = '*'




def DoInventory():
    global multiplier,Customer_Wait_Time, Shop_Rating, PerkApplied, Shop_Rating_Cost, Shop_Multiplier, cash, playing, multiplier_cost, StaffNum, DungeonMultiplier, customers, cpm, Items_Page, Inventory_Slot, Item_Values, Staff_Cost
    while playing == True:
        os.system('cls')

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
        CommonItems = [Items.DUSTY_BROOM, Items.RUST_BUCKET, Items.CHUM_SIGN]
        RareItems = [Items.KELP_SEVICHE_HAT, Items.TACO_TUESDAY_STICKER, Items.MACRONALD_DONALD]
        LegendItems = [Items.GOLDEN_TUXEDO, Items.GOLDEN_GLOVES, Items.PLATINUM_TOWEL]
        MythicItems = [Items.HOLY_DUSTY_BROOM, Items.HOLY_RUST_BUCKET]

        if not PerkApplied:
            for i in Item_Values:
                if Item_Values[i]['is_equipped'] == colors.BOLD + colors.GREEN + "EQUIPPED" + colors.END:
                    Inventory_Slot = i
                    if Inventory_Slot == "DUSTY_BROOM":
                        Shop_Multiplier += 0.25
                    elif Inventory_Slot == "RUST_BUCKET":
                        Staff_Cost *= 0.75
                    elif Inventory_Slot == "CHUM_SIGN":
                        StaffNum += 1
                        cpm += 1
                    elif Inventory_Slot == "KELP_SEVICHE_HAT":
                        StaffNum += 1
                        Shop_Multiplier += 0.5
                    elif Inventory_Slot == "TACO_TUESDAY_STICKER":
                        Shop_Multiplier += 1
                        StaffNum += 2
                    elif Inventory_Slot == "MACRONALD_DONALD":
                        Customer_Wait_Time *= 2
                        Shop_Multiplier += 1
                    elif Inventory_Slot == "GOLDEN_TUXEDO":
                        DungeonMultiplier += 2
                        Staff_Cost *= 1.5
                        StaffNum += 2
                    elif Inventory_Slot == "GOLDEN_GLOVES":
                        cpm *= 1.5
                        DungeonMultiplier += 2
                        StaffNum += 2
                    elif Inventory_Slot == "PLATINUM_TOWEL":
                        multiplier *= 2
                        Customer_Wait_Time *= 3
                    elif Inventory_Slot == "HOLY_DUSTY_BROOM":
                        Customer_Wait_Time *= 2
                        multiplier += 1
                        cpm += 1
                        DungeonMultiplier += 2
                    elif Inventory_Slot == "HOLY_RUST_BUCKET":
                        Customer_Wait_Time *= 3
                        multiplier += 2
                        cpm += 1
                        Staff_Cost *= 0.5
                    PerkApplied = True
                    break
                else:
                    Inventory_Slot = []
            
            
        print("Currently Equipped Item: ", colors.BOLD + str(Inventory_Slot) + colors.END)


        if Items_Page == 1:

            print(f"""

                           {CommonItems[0]}              

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}       
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        elif Items_Page == 2:

            print(f"""

                           {CommonItems[1]}              

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}       
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        elif Items_Page == 3:

            print(f"""

                           {CommonItems[2]}              

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}       
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        elif Items_Page == 4:

            print(f"""

                           {RareItems[0]}

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}                     
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        elif Items_Page == 5:

            print(f"""

                           {RareItems[1]}          

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}       
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        elif Items_Page == 6:

            print(f"""

                           {RareItems[2]} 

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}                     
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        elif Items_Page == 7:

            print(f"""

                           {LegendItems[0]} 

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}                     
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        elif Items_Page == 8:

            print(f"""

                           {LegendItems[1]}    

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}                     
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        elif Items_Page == 9:

            print(f"""

                           {LegendItems[2]} 

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}                     
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        elif Items_Page == 10:

            print(f"""

                           {MythicItems[0]} 

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}                     
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        elif Items_Page == 11:

            print(f"""

                           {MythicItems[1]} 

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}                     
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              

              """)
        else:
            pass

        val = input("> ")
        if val == '>':
            if Items_Page < 11:
                Items_Page += 1
            else:
                print("No following page!")
                time.sleep(1)
        elif val == '<':
            if Items_Page > 1:
                Items_Page -= 1
            else:
                print("No following page!")
                time.sleep(1)
        elif val == 'x' or val == 'X':
            Items_Page = 1
            DoStore()
        elif val == 'c' or val == 'C':       
            if Items_Page == 1:
                item = "DUSTY_BROOM"
            elif Items_Page == 2:
                item = "RUST_BUCKET"
            elif Items_Page == 3:
                item = "CHUM_SIGN"
            elif Items_Page == 4:
                item = "KELP_SEVICHE_HAT"
            elif Items_Page == 5:
                item = "TACO_TUESDAY_STICKER"
            elif Items_Page == 6:
                item = "MACRONALD_DONALD"
            elif Items_Page == 7:
                item = "GOLDEN_TUXEDO"
            elif Items_Page == 8:
                item = "GOLDEN_GLOVES"
            elif Items_Page == 9:
                item = "PLATINUM_TOWEL"
            elif Items_Page == 10:
                item = "HOLY_DUSTY_BROOM"
            elif Items_Page == 11:
                item = "HOLY_RUST_BUCKET"
            else:
                item = None

            if multiplier != "LOCKED" and Shop_Rating != "LOCKED":

              if Inventory_Slot != [] and Inventory_Slot != list(Item_Values)[Items_Page-1]:
                  print("Unequip current item prior to equipping new one")
                  time.sleep(1)
              elif Item_Values[item]["is_locked"] == colors.RED + colors.BOLD + "LOCKED" + colors.END:
                  print("Item Locked!")
                  time.sleep(1)
              elif Item_Values[item]["is_equipped"] == colors.BOLD + colors.GREEN + "EQUIPPED" + colors.END:
                  Item_Values[item]["is_equipped"] = colors.BOLD + colors.PURPLE + "UNEQUIPPED" + colors.END
                  print(colors.BOLD + colors.RED + "UNEQUIPPED" + colors.END)
                  if Inventory_Slot == "DUSTY_BROOM":
                      Shop_Multiplier -= 0.25
                  elif Inventory_Slot == "RUST_BUCKET":
                      Staff_Cost /= 0.75
                  elif Inventory_Slot == "CHUM_SIGN":
                      StaffNum -= 1
                      cpm -= 1
                  elif Inventory_Slot == "KELP_SEVICHE_HAT":
                      StaffNum -= 1
                      Shop_Multiplier -= 0.5
                  elif Inventory_Slot == "TACO_TUESDAY_STICKER":
                      Shop_Multiplier -= 1
                      StaffNum -= 2
                  elif Inventory_Slot == "MACRONALD_DONALD":
                      Customer_Wait_Time /= 2
                      Shop_Multiplier -= 1
                  elif Inventory_Slot == "GOLDEN_TUXEDO":
                      DungeonMultiplier -= 2
                      Staff_Cost /= 1.5
                      StaffNum -= 2
                  elif Inventory_Slot == "GOLDEN_GLOVES":
                      cpm /= 1.5
                      DungeonMultiplier -= 2
                      StaffNum -= 2
                  elif Inventory_Slot == "PLATINUM_TOWEL":
                      multiplier /= 2
                      Customer_Wait_Time /= 3
                  elif Inventory_Slot == "HOLY_DUSTY_BROOM":
                      Customer_Wait_Time /= 2
                      multiplier -= 1
                      cpm -= 1
                      DungeonMultiplier -= 2
                  elif Inventory_Slot == "HOLY_RUST_BUCKET":
                      Customer_Wait_Time /= 3
                      multiplier -= 2
                      cpm -= 1
                      Staff_Cost /= 0.5
                  else:
                     print("remove error")
                     time.sleep(1)
                  PerkApplied = False  
                  time.sleep(1)
              else:
                  Item_Values[item]["is_equipped"] = colors.BOLD + colors.GREEN + "EQUIPPED" + colors.END
                  print(Item_Values[item]['is_equipped'])
                  print("Item Equipped!")
                  time.sleep(1)
            else:
              print("Multiplier and Shop Rating have to be unlocked to equip items!")
              time.sleep(1)
  

        else:
            print("Please enter a defined option")
            time.sleep(1)

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

def DoUpgrades():
    global Shop_Rating
    global playing
    global multiplier
    global multiplier_cost
    global Shop_Rating_Cost
    global cash 
    global seperater

    while playing == True:
        os.system('cls')


        if multiplier != 'LOCKED':
            if multiplier >= 5:
                multiplier_cost = "MAX"
            else:
                multiplier_cost = int(multiplier ** 5)
        else:
            pass
        if Shop_Rating != 'LOCKED':
            if len(Shop_Rating.split()) >= 5:
                Shop_Rating_Cost = 'MAX'
            else:
                Shop_Rating_Cost = len(Shop_Rating.split()) * 25
        else:
            pass

        print(f"""\n
Upgrade cash multiplier. (Current: {multiplier}), {colors.BOLD + 'enter [M]' + colors.END}, cost: [{multiplier_cost}]
{seperater}
Upgrade Shop Rating. (Current: {Shop_Rating}), {colors.BOLD + 'enter [S]' + colors.END}, cost: [{Shop_Rating_Cost}] \n  
To exit, {colors.BOLD + 'enter [X]' + colors.END}
          """)
        val = input("> ")
        if val == 'M' or val == 'm':
            if multiplier == 5:
                print("Max multiplier reached")
                time.sleep(1)
            else:
                if multiplier != 'LOCKED':
                    if cash >= multiplier_cost:
                        cash -= multiplier_cost
                        multiplier += 1
                    else:
                        print("Not enough cash!")
                        time.sleep(1)
                else:
                    print("Multiplier Locked!")
                    time.sleep(1)
        elif val == 'S' or val == 's':
            if Shop_Rating == '* * * * *':
                print("Max Shop Rating reached")
                time.sleep(1)
            else:
                if Shop_Rating != 'LOCKED':
                    if cash >= Shop_Rating_Cost:
                        cash -= Shop_Rating_Cost
                        Shop_Rating += ' *'
                    else:
                        print("Not enough cash!")
                        time.sleep(1)
                else:
                    print("Shop Rating Locked!")
                    time.sleep(1)
        elif val == 'X' or val == 'x':
            GameMenu()
        else:
            print("Enter a defined option")
            time.sleep(1)

def DoRewards():
    global Spin_Overide, Cash_start_time, Spin_start_time, Dungeon_start_time, cash, multiplier, Shop_Rating, Shop_Rating_Cost, multiplier_cost, seperater, start_time, colors, Cash_Reset
    global Rewards_Page, Dungeon_Cooldown, Spin_Period, section, Last_Dungeon_Score, High_Dungeon_Score
    Rewards_Page = 1

    Cash_current_time_sec = time.time() - Cash_start_time
    Spin_current_time_sec = time.time() - Spin_start_time
    Dungeon_current_time_sec = time.time() - Dungeon_start_time
    Cash_current_time_min = int(Cash_current_time_sec / 60)
    Spin_current_time_min = int(Spin_current_time_sec / 60)
    Dungeon_current_time_min = int(Dungeon_current_time_sec / 60)
    Cash_Earned = Cash_current_time_min / 5
    while playing == True:
        if Cash_Reset == True:
            cash += Cash_Earned
            Cash_Earned = 0
            Cash_start_time = time.time()
            print("Claimed!")
            time.sleep(1)
            Cash_Reset = False
        else:
            pass
        Dungeon_Time_To_Wait_Min = Dungeon_Cooldown - Dungeon_current_time_min
        Dungeon_Time_To_Wait_Countdown = colors.CYAN + colors.BOLD + f"{Dungeon_Time_To_Wait_Min}" + colors.END
        if Dungeon_Time_To_Wait_Min < 0:
            Dungeon_Time_To_Wait_Countdown = colors.BG_CYAN + colors.BOLD + "   READY!   " + colors.END 
        Spin_Time_To_Wait_Min = Spin_Period - Spin_current_time_min
        Spin_Time_To_Wait_Countdown = colors.CYAN + colors.BOLD + f"{Spin_Time_To_Wait_Min}" + colors.END
        if Spin_Time_To_Wait_Min < 0 or Spin_Overide == True:
            Spin_Time_To_Wait_Countdown = colors.BG_GREEN + colors.BOLD + "   READY!   " + colors.END 


        os.system('cls')

        print(colors.BOLD + colors.BG_RED + colors.ITALIC + " REWARDS " + colors.END)
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
        if Rewards_Page == 1: 
            print(f"""
{section.ONE}

Enter [>] for next page  
Enter [<] for previous page
Enter [X] to exit                               Current page: {colors.DARKCYAN + colors.BOLD + str(Rewards_Page) + colors.END}                                                                                                                       
Enter [R] to refresh
                """)
        elif Rewards_Page == 2:
            print(f"""
{section.TWO}

Enter [F] to skip cooldown
Enter [>] for next page
Enter [<] for previous page
Enter [X] to exit                               Current page: {colors.DARKCYAN + colors.BOLD + str(Rewards_Page) + colors.END}
Enter [R] to refresh
                """)
        elif Rewards_Page == 3:
            print(f"""
{section.THREE}

Enter [>] for next page
Enter [<] for previous page
Enter [X] to exit                               Current page: {colors.DARKCYAN + colors.BOLD + str(Rewards_Page) + colors.END}
Enter [R] to refresh
                """)

        elif Rewards_Page == "SPIN":
            print(f"""
{section.SPIN}


Enter [<] for previous page
Enter [X] to exit                               Current page: {colors.DARKCYAN + colors.BOLD + str(Rewards_Page) + colors.END}
Enter [R] to refresh
                """)
        val = input("> ")
        if val == 'C' or val == 'c':
            if Rewards_Page == 1:
                Cash_Reset = True
            else:
                pass
        elif val == '>':
            if Rewards_Page == 3 or Rewards_Page == "SPIN" or Rewards_Page == "Dungeon":
                print("No next page")
                time.sleep(1)
            else:
                Rewards_Page += 1
        elif val == '<':
            if Rewards_Page == 1:
                print("No previous page")
                time.sleep(1)
            elif Rewards_Page == "SPIN":
                Rewards_Page = 2
            else:
                Rewards_Page -= 1 
        elif val == 'X' or val == 'x':
            Rewards_Page = 1
            GameMenu()
        elif val == 'R' or val == 'r':
            DoRewards()
        elif val == 'S' or val == 's':
            if Rewards_Page == 2:
                if Spin_Time_To_Wait_Min < 0 or Spin_Overide == True:
                    os.system('cls')

                    Rewards_Page = "SPIN"
                else:
                    print("SPIN NOT READY")
                    time.sleep(1)
            else:
                print("Please enter a denfined value")
                time.sleep(1)
        elif val == 'f' or val == 'F':
            if Rewards_Page == 2:
                skip_cost = 200 * int(Spin_Time_To_Wait_Min)
                prompt = input(f"Would you like pay {skip_cost} to skip cooldown? (y/n): ")
                if prompt == 'y' or prompt == 'Y':
                    if cash >= skip_cost:
                        cash -= skip_cost
                        Spin_Overide = True
                    else:
                        print("Not enough cash")
                        time.sleep(1)
                elif prompt == 'n' or prompt == 'N':
                    DoRewards()
                else:
                    print("Please enter a defined value")
                    time.sleep(1)
        elif val == 'P' or val == 'p':
          if Rewards_Page == "SPIN":
            Spin_start_time = time.time()
            Spin_Overide = False
            DoSpin()
          else:
            print("Please enter a denfined value")
            time.sleep(1)
        elif val == 'M' or val == 'm':
            if Rewards_Page == 3:
                if Dungeon_Time_To_Wait_Min < 0:
                    Dungeon_start_time = time.time()
                    DoDungeon()
                else:
                    print("Dungeon NOT READY")
                    time.sleep(1)
            else:
                print("Please enter a denfined value")
                time.sleep(1) 
        else:
            print("Please enter a denfined value")
            time.sleep(1)

def DoDungeon():
    global playing, cash, multiplier, Shop_Rating, Shop_Rating_Cost, multiplier_cost, seperater, section
    global ratings, DungeonMultiplier, Dungeon_Cooldown, High_Dungeon_Score, Last_Dungeon_Score

    while playing == True:
        os.system('cls')

        print(section.Dungeon)
        val = input("> ")
        if val == 'D' or val == 'd':
            operation = ['+', '-', '*', '/']
            Wrong = False
            SeshCash = 0
            NumCorrect = 0
            Tries_Counter = 1
            DifficultyCounter = 0

            while Wrong == False:
                os.system('cls')

                if Tries_Counter == 2:
                    Wrong = True

                num1 = random.randint(1, 100)
                num2 = random.randint(1, 100)
                opr1 = random.choice(operation)
                if opr1 == operation[0]:
                  DifficultyCounter += 0.5  
                  answer = num1 + num2
                elif opr1 == operation[1]:
                  DifficultyCounter += 0.5  
                  answer = num1 - num2
                elif opr1 == operation[2]:
                  DifficultyCounter += 1.25
                  answer = num1 * num2
                else:
                  DifficultyCounter += 1.75
                  answer = num1 / num2

                print(f"{num1} {opr1} {num2}")

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
                  time.sleep(2)
                  delete_multiple_lines(5)
                else:
                  print(("Incorrect!"))
                  Tries_Counter += 1
                  time.sleep(2)
                  delete_multiple_lines(4)
            else:
              os.system("cls")

              if isinstance(multiplier, int):
                TotalSeshCash = (SeshCash * DungeonMultiplier) * multiplier
              else:
                TotalSeshCash = (SeshCash * DungeonMultiplier) * 1

              if isinstance(TotalSeshCash, str):
                TotalSeshCash = 0

              cash += TotalSeshCash

              HighScore = False

              if NumCorrect > High_Dungeon_Score:
                High_Dungeon_Score = NumCorrect
                HighScore = True

              Last_Dungeon_Score = NumCorrect 



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

              if HighScore == True:
                print(f"{colors.BOLD + colors.YELLOW + 'New High Score!' + colors.END}")


              while playing:
                Choice = input("> ")
                if Choice == "X" or Choice == 'x':
                  DoRewards()
                else:
                    print("Please enter a defined option")
                    time.sleep(1)
                    delete_multiple_lines(2)

def DoSpin():
    global Item_Values, colors
    CommonItems = ["DUSTY_BROOM", "RUST_BUCKET", "CHUM_SIGN"]
    RareItems = ["KELP_SEVICHE_HAT", "TACO_TUESDAY_STICKER", "MACRONALD_DONALD"]
    LegendItems = ["GOLDEN_TUXEDO", "GOLDEN_GLOVES", "PLATINUM_TOWEL"]
    MythicItems = ["HOLY_DUSTY_BROOM", "HOLY_RUST_BUCKET"]

    Item_Rolled = random.choice(list(Item_Values.keys()))
    if Item_Rolled in CommonItems:
        Item_Rarity = colors.BOLD + colors.BROWN + "COMMON" + colors.END
    elif Item_Rolled in RareItems:
        Item_Rarity = colors.BOLD + colors.BLUE + "RARE" + colors.END
    elif Item_Rolled in LegendItems:
        Item_Rarity = colors.BOLD + colors.YELLOW + "LEGEND" + colors.END
    else:
        Item_Rarity = colors.BOLD + colors.PURPLE + "MYTHIC" + colors.END

    for i in Item_Values:
        if i == Item_Rolled:
            Item_Values[i]['is_locked'] = colors.BOLD + colors.CYAN + "UNLOCKED" + colors.END

    Ex = False
    while Ex == False:
        os.system("cls")
        print(f"You Rolled...............................\nWait For It..............\n OMG\n You Recieved a {Item_Rarity}\n It's....................................\n {colors.BOLD + str(Item_Rolled) + '!' + colors.END}")

        print(f'\n\n\n{colors.BOLD + colors.PURPLE + str(Item_Rolled) + " UNLOCKED" + colors.END}\n\n\n')

        val = input("Go Back? (y/n): ")
        if val == 'y' or val == 'Y':
            DoRewards()
        elif val == 'n' or val == 'N':
            GameMenu()
        else:
            print("Please enter a devined value")
            time.sleep(1)

def DoInformation():
    global playing
    global colors
    global seperater
    while playing:
        os.system('cls')

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
        inquiry = input("> ")
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
        elif inquiry.lower() == 'u':
            os.system('cls')
            print(f"""
{colors.BOLD + colors.UNDERLINE + 'Upgrades:' + colors.END} \n
The Upgrades is where you can upgrade your shop multiplier and increase your shop rating!           
              """)
            input("Press Enter to return to the main menu...")
        elif inquiry.lower() == 'r':
            os.system('cls')
            print(f"""
{colors.BOLD + colors.UNDERLINE + 'Rewards:' + colors.END} \n
Rewards is where you can earn passive income, complete a math dungeon game mode, or spin the lucky wheel for an item!           
              """)
            input("Press Enter to return to the main menu...")
        elif inquiry.lower() == 's':
            os.system('cls')
            print(f"""
{colors.BOLD + colors.UNDERLINE + 'Settings:' + colors.END} \n
The Settings allow you to customize various aspects of the game, such as how difficulties are displayed and other game options.           
              """)
            input("Press Enter to return to the main menu...")
        elif inquiry.lower() == 'i':
            os.system('cls')
            print(f"""
{colors.BOLD + colors.UNDERLINE + 'Information:' + colors.END} \n
This section provides general information about the different game modes and how they function within the game.           
              """)
            input("Press Enter to return to the main menu...")
        elif inquiry.lower() == 'c':
            os.system('cls')
            print(f"""
{colors.BOLD + colors.UNDERLINE + 'Cash:' + colors.END} \n
The Cash mode allows you to earn currency within the game, which can be used for various purposes such as purchasing upgrades.           
              """)
            input("Press Enter to return to the main menu...")
        elif inquiry.lower() == 'm':
            os.system('cls')
            print(f"""
{colors.BOLD + colors.UNDERLINE + 'Multipliers:' + colors.END} \n
The Multipliers mode allows you to increase your shop's efficiency by applying multipliers to certain aspects of your business.           
              """)
            input("Press Enter to return to the main menu...")
        elif inquiry.lower() == 'h':
            os.system('cls')
            print(f"""
{colors.BOLD + colors.UNDERLINE + 'Shop Rating:' + colors.END} \n
The Shop Rating mode is where you can view and improve your shop's rating, which is essential for attracting more customers and growing your business.           
              """)
            input("Press Enter to return to the main menu...")
        elif inquiry.lower() == 'x':
            GameMenu()
        else:
            print("Please enter a valid option.")
            input("Press Enter to continue...")


def DoSettings():
    global OverallRating, keybinds
    global OverallScore
    global playing
    global colors, Order_Station_Keybind, Settings_Keybind, Rewards_Keybind, Store_Keybind, Upgrades_Keybind, Information_Keybind
    global ChangeAVGDisplay, DisplayCustomers
    global Name
    while playing == True:
        os.system('cls')

        if ChangeAVGDisplay == False:
            ScaleForm = "Average"
        else:
            ScaleForm = "Numerical"
        if DisplayCustomers == False:
            display = "Regular"
        else:
            display = "Promt"
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
        val = input("> ")
        if val == 'D' or val == 'd':
            if ChangeAVGDisplay == False:
                ChangeAVGDisplay = True
            else:
                ChangeAVGDisplay = False
        elif val == 'N' or val == 'n':
            NewName = input("Enter New Name: ")
            Name = NewName
        elif val == 'C' or val == 'c':
            if DisplayCustomers == False:
                DisplayCustomers = True
            else:
                DisplayCustomers = False
        elif val == 'X' or val == 'x':
            GameMenu()
        elif val == 'M' or val == 'm':
            print("\nEnter the new keybind for each action:")
            new_keybinds = {}
            for action in [
                "Store",
                "Order Station",
                "Rewards",
                "Settings",
                "Information",
                "Upgrades",
            ]:
                valid_keybind = False
                while valid_keybind == False:
                    new_key = input(f"New key for {action}: ").upper()
                    if new_key in [Store_Keybind, Order_Station_Keybind, Rewards_Keybind, Settings_Keybind, Information_Keybind, Upgrades_Keybind]:
                        print(f"Key '{new_key}' is already assigned to another action.")
                        time.sleep(1)
                        delete_multiple_lines(2)
                    elif len(new_key) == 1 and new_key.isalpha():
                        valid_keybind = True
                        globals()[f"{action.replace(' ', '_')}_Keybind"] = new_key
                        new_keybinds[action] = new_key
                    else:
                        print("Invalid key. Please enter a single alphabetical character.")
                        time.sleep(1)
                        delete_multiple_lines(2)
            else:
                print(colors.BOLD + colors.GREEN + "KEYBINDS UPDATED" + colors.END)
                time.sleep(1)

def DoOrder():
    global Menu
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

    if OverallScore <= 7:
        OverallRating = 0
    elif OverallScore > 7 and OverallScore < 11:
        OverallRating = 1
    elif OverallScore > 10 and OverallScore < 12:
        OverallRating = 2
    else:
        OverallRating = 3

    for i in range(len(ratings)):
        if ratings[i] == 1:
            ratings[i] = colors.BOLD + colors.GREEN + 'Easy' + colors.END
        elif ratings[i] == 2:
            ratings[i] = colors.BOLD + colors.YELLOW + 'Medium' + colors.END
        elif ratings[i] == 3:
            ratings[i] = colors.BOLD + colors.RED + 'Hard' + colors.END
        else:
            ratings[i] = colors.BOLD + colors.PURPLE + 'EXTREME' + colors.END

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


def ResetOrders(ratings):
    global cash
    global cash_color
    global Ratings1, Ratings2, Ratings3, Order1, Order2, Order3
    global playing,Ovr_Scores1, Ovr_Scores2, Ovr_Scores3, Ovr_Ratings1, Ovr_Ratings2, Ovr_Ratings3
    global SeshCash, Order1_time, Order2_time, Order3_time
    global multiplier, operation, customers
    if ratings == Ratings1:
        Order1 = Order2
        Order1_time = Order2_time
        Ratings1 = Ratings2
        Ratings2 = Ratings3
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
    elif ratings == Ratings2:
        Order2 = Order3
        Order2_time = Order3_time
        Ratings2 = Ratings3
        Ovr_Ratings2 = Ovr_Ratings3
        Ovr_Scores2 = Ovr_Scores3
        Order3 = []
        Order3_time = 0
        Ratings3 = []
        Ovr_Ratings3 = 0
        Ovr_Scores3 = 0
    else:
        Order3 = []
        Order3_time = 0
        Ratings3 = []
        Ovr_Ratings3 = 0
        Ovr_Scores3 = 0

    customers -= 1    


def DoOrderStation(order, ratings, OverallRating, OverallScore):
    os.system('cls')
    global cash
    global seperater
    global Menu
    global playing
    global colors
    global level
    global ratings1, ratings2, ratings3
    global ChangeAVGDisplay, customers, NumOrders, Order1, Order2, Order3        
    difficulties = [['Easy', 1], ['Medium', 2], ['Hard', 3], ['EXTREME', 4]]
    DifficultyRaw = difficulties[OverallRating]
    level = DifficultyRaw[1]
    Difficulty = DifficultyRaw[0] 
    if ChangeAVGDisplay == False:
        if level == 1:
            print(f"\n\nDiffuculty: {colors.BOLD + colors.GREEN + Difficulty + colors.END}\n{seperater}")
        elif level == 2:
            print(f"\n\nDiffuculty: {colors.BOLD + colors.YELLOW + Difficulty + colors.END}\n{seperater}")
        elif level == 3:
            print(f"\n\nDiffuculty: {colors.BOLD + colors.RED + Difficulty + colors.END}\n{seperater}")
        else:
            print(f"\n\nDiffuculty: {colors.BOLD + colors.PURPLE + Difficulty + colors.END}\n{seperater}")
    else:
        if level == 1:
            print(f"\n\nDiffuculty: {colors.BOLD + colors.GREEN + str(OverallScore) + colors.END}\n{seperater}")
        elif level == 2:
            print(f"\n\nDiffuculty: {colors.BOLD + colors.YELLOW + str(OverallScore) + colors.END}\n{seperater}")
        elif level == 3:
            print(f"\n\nDiffuculty: {colors.BOLD + colors.RED + str(OverallScore) + colors.END}\n{seperater}")
        else:
            print(f"\n\nDiffuculty: {colors.BOLD + colors.PURPLE + str(OverallScore) + colors.END}\n{seperater}")

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
            DoOrderMenu()
        elif val == 'R' or val == 'r':
            delete_multiple_lines(6)
            DoSandwichMaker(ratings)
        elif val == 'S' or val == 's':
            delete_multiple_lines(6)
            DoVariables()
        else:
            print("Please enter a defined option")
            time.sleep(1)
            delete_multiple_lines(7)

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

        upd = ResetOrders(ratings)

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

def DoVariables():
    pass

class Menu:
    breads = [['regular', 1], ['sesame', 2], ['old-fashioned',3], ['4-cheese', 1], ['italian', 2], ['Chicago style', 3], ['Golden Yeast', 4]]
    vegetables = [['tomato', 1], ['cucumber', 2], ['carrot', 3], ['peppers', 1], ['jalapeno', 2], ['onion', 3], ['Golden Root', 4]]
    sauces = [['mayonnaise', 1], ['teriyaki', 2], ['ketchup', 3], ['mustard', 1], ['relish', 2], ['Hot sauce', 3], ['Golden Drool', 4]]
    meats = [['salami', 1], ['pepperoni', 2], ['chicken', 3], ['beef', 1], ['pork', 2], ['bacon', 3], ['Golden Ham', 4]]

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


def delete_multiple_lines(n=1):
    for i in range(n):
        sys.stdout.write("\x1b[1A")  # cursor up one line
        sys.stdout.write("\x1b[2K")  # delete the last line

Order1 = []
Order2 = []
Order3 = []
Ratings1 = []
Ratings2 = []
Ratings3 = []
Ovr_Ratings1 = 0
Ovr_Ratings2 = 0
Ovr_Ratings3 = 0
Ovr_Scores1 = 0
Ovr_Scores2 = 0
Ovr_Scores3 = 0
Order1_time = 0
Order2_time = 0
Order3_time = 0
NoOrder = ['NaN', 'NaN', 'NaN', 'NaN', 'NaN']
NoRatings = ['NaN', 'NaN', 'NaN', 'NaN', 'NaN']

FirstOpening = True

OrderPage = 0

PerkApplied = False

Store_Keybind = 'S'
Order_Station_Keybind = 'O'
Rewards_Keybind = 'R'
Settings_Keybind = 'C'
Information_Keybind = 'I'
Upgrades_Keybind = 'U'

start_time = time.time()
Cash_start_time = time.time()
cpm_start_time = time.time()
Spin_start_time = time.time()
Dungeon_start_time = time.time()
Inventory_Slot = []
seperater = "----------------------------------------------------------------"
cash = 0
multiplier = "LOCKED"
Shop_Rating = "LOCKED"
multiplier_cost = "LOCKED"
Shop_Rating_Cost = "LOCKED"
Name = "Paulie's"
cpm = 0
StaffNum = 0
Staff_Cost = 1
customers = 0
Customer_Wait_Time = 300
Shop_Multiplier = 1
DungeonMultiplier = 1
Last_Dungeon_Score = 0
High_Dungeon_Score = 0
Rewards_Page = 1
Items_Page = 1
DisplayCustomers = False
cash_color = colors.GREEN + colors.BOLD + "Cash:" + colors.END 
Cash_Reset = False
cpm_Reset = False
Spin_Period = 15
Spin_Overide = False
Dungeon_Cooldown = 30
current_time_sec = time.time() - start_time
current_time_min = int(current_time_sec / 60)
cpm_current_time_min = int(current_time_sec / 60)
ChangeAVGDisplay = False

start = GameMenu()
