import os, time, random, sys, re

def GameMenu():
    global Shop_Rating
    global multiplier
    global cash
    global seperater
    global colors
    global playing
    global Name, customers
    playing = True
    while playing:
        os.system('cls')
        if DisplayCustomers == True:
            print(f"""\n{colors.BOLD + colors.UNDERLINE + "Welcome To " + Name + " Sandwich bar!" + colors.END}\n
    Store              {colors.BOLD + "Enter [S]" + colors.END}
    {seperater}
    Order Station      {colors.BOLD + "Enter [O]" + colors.END}
    {seperater}
    Upgrades           {colors.BOLD + "Enter [U]" + colors.END}
    {seperater}
    Rewards            {colors.BOLD + "Enter [R]" + colors.END}
    {seperater}   
    Settings           {colors.BOLD + "Enter [C]" + colors.END}
    {seperater} 
    Information        {colors.BOLD + "Enter [I]" + colors.END}
    {seperater}
    Exit               {colors.BOLD + "Enter [X]" + colors.END}
                                            Cash: {colors.GREEN + colors.BOLD + str(cash) + colors.END}
                                            Multiplier: {colors.PURPLE + colors.BOLD + str(multiplier) + colors.END}
                                            Shop Rating: {colors.CYAN + colors.BOLD + str(Shop_Rating) + colors.END}\n

                                            |------------------------
                                            |
                                            | Current Customers: {customers}
                                            |
                                            """)
        else:
            print(f"""\n{colors.BOLD + colors.UNDERLINE + "Welcome To " + Name + " Sandwich bar!" + colors.END}\n
    Store              {colors.BOLD + "Enter [S]" + colors.END}
    {seperater}
    Order Station      {colors.BOLD + "Enter [O]" + colors.END}
    {seperater}
    Upgrades           {colors.BOLD + "Enter [U]" + colors.END}
    {seperater}
    Rewards            {colors.BOLD + "Enter [R]" + colors.END}
    {seperater}   
    Settings           {colors.BOLD + "Enter [C]" + colors.END}
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
            DoStore()
        elif val == 'I' or val == 'i':
            DoInformation()
        elif val == 'X' or val == 'x':
            while playing:
              choice = input(f"Are you sure you want to exit? (Y/N): ")
              if choice == "Y" or choice == "y":
                os.system('cls')
                print(f"""
                \n\n\n\n\n\n
                {colors.BOLD + colors.UNDERLINE + 
                'Thank you for playing!' + colors.END}
                
                """)
                time.sleep(2)
                playing = False
              elif choice == "N" or choice == "n":
                GameMenu()
              else:
                print("Please enter a defined option")
                time.sleep(1)
                delete_multiple_lines(2)
        elif val == "U" or val == 'u':
            DoUpgrades()
        elif val == 'R' or val == 'r':
            DoRewards()
        elif val == 'C' or val == 'c':
            DoSettings()
        elif val == '$menu$':
            DoDevMenu()
        else:
            print("Please enter a defined option")
            time.sleep(1)

def DoStore():
    global multiplier, Shop_Rating, Shop_Rating_Cost, cash, playing, multiplier_cost
    while playing == True:
        os.system('cls')
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
        val = input("> ")
        if val == 'X' or val == 'x':
            GameMenu()
        elif val == 'I' or val == 'i':
            DoInventory()
        elif val == 'S' or val == 's':
            DoShop()
        else:
            print("Please enter a definned option")
            time.sleep(1)
            
def DoShop():
    global multiplier, Shop_Rating, Shop_Rating_Cost, Shop_Multiplier, cash, playing, multiplier_cost, StaffNum, customers, cpm
    while playing == True:
        os.system('cls')
        print(f"""
|-----------------------------------------------------------------------------------------------|
|   Customers: {colors.PURPLE + colors.UNDERLINE + str(customers) + colors.END}                                                      Shop Rating: {colors.BLUE + colors.UNDERLINE + str(Shop_Rating) + colors.END}       |
|-----------------------                                                                        |
|   Cash/min: {colors.GREEN + colors.UNDERLINE + str(cpm) + '/min' + colors.END}                                                                             |
|-----------------------                                                                        |
|   Multiplier: {colors.RED + colors.UNDERLINE + str(multiplier) + colors.END}                                                                          |
|-----------------------                                                                        |
|   Shop Multiplier: {colors.BLUE + colors.UNDERLINE + str(Shop_Multiplier) + colors.END}                                                                          |
|-----------------------                                                            Staff: {colors.CYAN + str(StaffNum) + colors.END}    |
|                                                                                     -----     |
|                                                                                     |O O|     |
|                                                                                     |-|-|     |
|                                                                                       |       |
|                                                                                |\    /|\      |
|    |   _______________      |                                                  |--------------|
|    |          |             |                                                  |              |
|    |______    |      _______|                                                  |              |
|    |     |    |      |      |                                                  |              |
|    |     |    |      |      |                                                  |              |
|-----------------------------------------------------------------------------------------------|            
              
Enter [R] to refresh page

Enter [X] to EXIT              
              
              """)
        val = input("> ")
        if val == 'X' or val == 'x':
            DoStore()
        elif val == 'R' or val == 'r':
            DoShop()
        else:
            print("Please enter a defined option")
            time.sleep(1)

def DoInventory():
    global multiplier, Shop_Rating, Shop_Rating_Cost, Shop_Multiplier, cash, playing, multiplier_cost, StaffNum, customers, cpm, Items_Page
    while playing == True:
        os.system('cls')
        isLocked = False
        isEquipped = False
            
        class Items:  
            DUSTY_BROOM = f"""
    |-------------------------|              
    | {isLocked} {isEquipped} |
    |       Dusty Broom       |
    |-------------------------|
    |             {colors.UNDERLINE + colors.BOLD + colors.BROWN + str('COMMON') + colors.END + '             |'}           
    |-------------------------|
    |                         |
    |    + 1 customer/3min    |
    | + 0.25x shop multiplier |
    |                         |
    |-------------------------|
    |                         |
    |  [C] To Unlock/Equip    |
    |                         |
    |-------------------------|        
            """
            KELP_SEVICHE_HAT = f"""
    |-------------------------|              
    |  {isLocked} {isEquipped}|
    |   Kelp Seviche Hat      |
    |-------------------------|
    |         {colors.UNDERLINE + colors.BOLD + colors.BLUE + 'RARE' + colors.END}          |           
    |-------------------------|
    |                         |
    |   + 2 customer/5min     |
    |   + 1 staff             |
    |                         |
    |-------------------------|      
    |                         |
    |  [C] To Unlock/Equip    |
    |                         |
    |-------------------------|        
            """
            GOLDEN_TUXEDO = f"""
    |-------------------------|              
    |  {isLocked} {isEquipped}|
    |     Golden Tuxedo       |
    |-------------------------|
    |         {colors.UNDERLINE + colors.BOLD + colors.YELLOW + 'LEGEND' + colors.END}          |           
    |-------------------------|
    |                         |
    |       + 3 staff         |
    |    + 2x shop multiplier |
    |                         |
    |-------------------------|      
    |                         |
    |  [C] To Unlock/Equip    |
    |                         |
    |-------------------------|        
            """
            RUST_BUCKET = f"""
    |-------------------------|              
    |  {isLocked} {isEquipped}|
    |      Rust Bucket        |
    |-------------------------|
    |      {colors.UNDERLINE + colors.BOLD + colors.BROWN + 'COMMON' + colors.END}       |           
    |-------------------------|
    |                         |
    |    + 1 customer/3min    |
    |    + 0.25x staff cost   |
    |                         |
    |-------------------------|      
    |                         |
    |  [C] To Unlock/Equip    |
    |                         |
    |-------------------------|        
            """
            TACO_TUESDAY_STICKER = f"""
    |-------------------------|              
    |  {isLocked} {isEquipped}|
    |  Taco Tuesday Sticker   |
    |-------------------------|
    |      {colors.UNDERLINE + colors.BOLD + colors.BLUE + 'RARE' + colors.END}       |           
    |-------------------------|
    |                         |
    |   + 3 customer/5min     |
    |   + 2 staff             |
    |   + 1x shop multiplier  |
    |-------------------------|      
    |                         |
    |  [C] To Unlock/Equip    |
    |                         |
    |-------------------------|        
            """
            GOLDEN_GLOVES = f"""
    |-------------------------|              
    |  {isLocked} {isEquipped}|
    |      Golden Gloves      |
    |-------------------------|
    |     {colors.UNDERLINE + colors.BOLD + colors.YELLOW + 'LEGEND' + colors.END}       |           
    |-------------------------|
    |                         |
    |       + 2 staff         |
    |    + 2x shop multiplier |
    |                         |
    |-------------------------|      
    |                         |
    |  [C] To Unlock/Equip    |
    |                         |
    |-------------------------|        
            """
            CHUM_SIGN = f"""
    |-------------------------|              
    |  {isLocked} {isEquipped}|
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
    |  [C] To Unlock/Equip    |
    |                         |
    |-------------------------|        
            """
            MACRONALD_DONALD = f"""
    |-------------------------|              
    |  {isLocked} {isEquipped}|
    |   MacRonald Donald      |
    |-------------------------|
    |      {colors.UNDERLINE + colors.BOLD + colors.BLUE + 'RARE' + colors.END}       |           
    |-------------------------|
    |                         |
    |    + 1 customer/3min    |
    | + double order wait time|
    |    + 1x shop multiplier |
    |-------------------------|      
    |                         |
    |  [C] To Unlock/Equip    |
    |                         |
    |-------------------------|        
            """
            PLATINUM_TOWEL = f"""
    |-------------------------|              
    |  {isLocked} {isEquipped}|
    |     Platinum Towel      |
    |-------------------------|
    |     {colors.UNDERLINE + colors.BOLD + colors.YELLOW + 'LEGEND' + colors.END}       |           
    |-------------------------|
    |                         |
    | + triple order wait time|
    |    + 2x game multiplier |
    |                         |
    |-------------------------|      
    |                         |
    |  [C] To Unlock/Equip    |
    |                         |
    |-------------------------|        
            """
            HOLY_DUSTY_BROOM = f"""
    |-------------------------|              
    |  {isLocked} {isEquipped}|
    |    Holy Dusty Broom     |
    |-------------------------|
    |   {colors.UNDERLINE + colors.BOLD + colors.PURPLE + 'MYTHICAL' + colors.END}       |           
    |-------------------------|
    |                         |
    | + triple order wait time|
    |      + 1x c/min         |
    |     + 2x shop multiplier|
    |-------------------------|      
    |                         |
    |  [C] To Unlock/Equip    |
    |                         |
    |-------------------------|        
            """
            HOLY_RUST_BUCKET = f"""
    |-------------------------|              
    |  {isLocked} {isEquipped}|
    |    Holy Rust Bucket     |
    |-------------------------|
    |   {colors.UNDERLINE + colors.BOLD + colors.PURPLE + 'MYTHICAL' + colors.END}       |            
    |-------------------------|
    |                         |
    | + triple order wait time|
    |    + 1x c/min           |
    |    + 2x shop multiplier |
    |-------------------------|      
    |                         |
    |  [C] To Unlock/Equip    |
    |                         |
    |-------------------------|        
            """
        CommonItems = [Items.DUSTY_BROOM, Items.RUST_BUCKET, Items.CHUM_SIGN]
        RareItems = [Items.KELP_SEVICHE_HAT, Items.TACO_TUESDAY_STICKER, Items.MACRONALD_DONALD]
        LegendItems = [Items.GOLDEN_TUXEDO, Items.GOLDEN_GLOVES, Items.PLATINUM_TOWEL]
        MythicItems = [Items.HOLY_DUSTY_BROOM, Items.HOLY_RUST_BUCKET]
            
        if Items_Page == 1:
            
            isLocked = "UNLOCKED"
            isEquipped = False
            
            print(f"""
              
                           {CommonItems[0]}              

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}       
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              
              
              """)
        elif Items_Page == 2:
            
            isLocked = False
            isEquipped = False
            
            if isLocked == False:
                isLocked = colors.BOLD + colors.BG_MAGENTA + 'LOCKED' + colors.END
            else:
                isLocked = colors.BOLD + colors.BG_CYAN + 'UNLOCKED' + colors.END
                
            if isEquipped == False:
                isEquipped = colors.BOLD + 'READY' + colors.END            
            else:
                isEquipped = colors.BOLD + colors.YELLOW + 'EQUIPPED' + colors.END
            
            print(f"""
              
                           {CommonItems[1]}              

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}       
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              
              
              """)
        elif Items_Page == 3:
            
            isLocked = False
            isEquipped = False
            
            if isLocked == False:
                isLocked = colors.BOLD + colors.BG_MAGENTA + 'LOCKED' + colors.END
            else:
                isLocked = colors.BOLD + colors.BG_CYAN + 'UNLOCKED' + colors.END
                
            if isEquipped == False:
                isEquipped = colors.BOLD + 'READY' + colors.END            
            else:
                isEquipped = colors.BOLD + colors.YELLOW + 'EQUIPPED' + colors.END
            
            print(f"""
              
                           {CommonItems[2]}              

                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}       
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              
              
              """)
        elif Items_Page == 4:
            
            isLocked = False
            isEquipped = False
            
            if isLocked == False:
                isLocked = colors.BOLD + colors.BG_MAGENTA + 'LOCKED' + colors.END
            else:
                isLocked = colors.BOLD + colors.BG_CYAN + 'UNLOCKED' + colors.END
                
            if isEquipped == False:
                isEquipped = colors.BOLD + 'READY' + colors.END            
            else:
                isEquipped = colors.BOLD + colors.YELLOW + 'EQUIPPED' + colors.END
            
            print(f"""
              
                           {RareItems[0]}
                                     
                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}                     
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              
              
              """)
        elif Items_Page == 5:
            
            isLocked = False
            isEquipped = False
            
            if isLocked == False:
                isLocked = colors.BOLD + colors.BG_MAGENTA + 'LOCKED' + colors.END
            else:
                isLocked = colors.BOLD + colors.BG_CYAN + 'UNLOCKED' + colors.END
                
            if isEquipped == False:
                isEquipped = colors.BOLD + 'READY' + colors.END            
            else:
                isEquipped = colors.BOLD + colors.YELLOW + 'EQUIPPED' + colors.END
            
            print(f"""
              
                           {RareItems[1]}          
                           
                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}       
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              
              
              """)
        elif Items_Page == 6:
            
            isLocked = False
            isEquipped = False
            
            if isLocked == False:
                isLocked = colors.BOLD + colors.BG_MAGENTA + 'LOCKED' + colors.END
            else:
                isLocked = colors.BOLD + colors.BG_CYAN + 'UNLOCKED' + colors.END
                
            if isEquipped == False:
                isEquipped = colors.BOLD + 'READY' + colors.END            
            else:
                isEquipped = colors.BOLD + colors.YELLOW + 'EQUIPPED' + colors.END
            
            print(f"""
              
                           {RareItems[2]} 
                                    
                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}                     
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              
              
              """)
        elif Items_Page == 7:
            
            isLocked = False
            isEquipped = False
            
            if isLocked == False:
                isLocked = colors.BOLD + colors.BG_MAGENTA + 'LOCKED' + colors.END
            else:
                isLocked = colors.BOLD + colors.BG_CYAN + 'UNLOCKED' + colors.END
                
            if isEquipped == False:
                isEquipped = colors.BOLD + 'READY' + colors.END            
            else:
                isEquipped = colors.BOLD + colors.YELLOW + 'EQUIPPED' + colors.END
            
            print(f"""
              
                           {LegendItems[0]} 
                                    
                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}                     
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              
              
              """)
        elif Items_Page == 8:
            
            isLocked = False
            isEquipped = False
            
            if isLocked == False:
                isLocked = colors.BOLD + colors.BG_MAGENTA + 'LOCKED' + colors.END
            else:
                isLocked = colors.BOLD + colors.BG_CYAN + 'UNLOCKED' + colors.END
                
            if isEquipped == False:
                isEquipped = colors.BOLD + 'READY' + colors.END            
            else:
                isEquipped = colors.BOLD + colors.YELLOW + 'EQUIPPED' + colors.END
            
            print(f"""
              
                           {LegendItems[1]}    
                                 
                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}                     
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              
              
              """)
        elif Items_Page == 9:
            
            isLocked = False
            isEquipped = False
            
            if isLocked == False:
                isLocked = colors.BOLD + colors.BG_MAGENTA + 'LOCKED' + colors.END
            else:
                isLocked = colors.BOLD + colors.BG_CYAN + 'UNLOCKED' + colors.END
                
            if isEquipped == False:
                isEquipped = colors.BOLD + 'READY' + colors.END            
            else:
                isEquipped = colors.BOLD + colors.YELLOW + 'EQUIPPED' + colors.END
            
            print(f"""
              
                           {LegendItems[2]} 
                                    
                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}                     
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              
              
              """)
        elif Items_Page == 10:
            
            isLocked = False
            isEquipped = False
            
            if isLocked == False:
                isLocked = colors.BOLD + colors.BG_MAGENTA + 'LOCKED' + colors.END
            else:
                isLocked = colors.BOLD + colors.BG_CYAN + 'UNLOCKED' + colors.END
                
            if isEquipped == False:
                isEquipped = colors.BOLD + 'READY' + colors.END            
            else:
                isEquipped = colors.BOLD + colors.YELLOW + 'EQUIPPED' + colors.END
            
            print(f"""
              
                           {MythicItems[0]} 
                                    
                                                                 Page: {colors.BOLD + colors.RED + str(Items_Page) + colors.END}                     
Enter [>] for next page
Enter [<] for previous page

Enter [X] to EXIT              
              
              """)
        elif Items_Page == 11:
            
            isLocked = False
            isEquipped = False
            
            if isLocked == False:
                isLocked = colors.BOLD + colors.BG_MAGENTA + 'LOCKED' + colors.END
            else:
                isLocked = colors.BOLD + colors.BG_CYAN + 'UNLOCKED' + colors.END
                
            if isEquipped == False:
                isEquipped = colors.BOLD + 'READY' + colors.END            
            else:
                isEquipped = colors.BOLD + colors.YELLOW + 'EQUIPPED' + colors.END
            
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
            if Items_Page > 0:
                Items_Page -= 1
            else:
                print("No following page!")
                time.sleep(1)
        elif val == 'x' or val == 'X':
            Items_Page = 1
            DoStore()
        else:
            print("Please enter a defined option")
            time.sleep(1)




def DoDevMenu():
    global multiplier, Shop_Rating, Shop_Rating_Cost, cash, playing, multiplier_cost, Dungen_Cooldown, Spin_Period
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
            new_Dungen_values = [int(num) for num in re.findall(r'\d+', command)]
            if new_Dungen_values:
                Dungen_Cooldown = new_Dungen_values[0]
                print(f"Updated Dungen Cooldown value: {Dungen_Cooldown}")
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
            if multiplier >= 20:
                multiplier_cost = "MAX"
            else:
                multiplier_cost = int(multiplier ** 2.5)
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
            if multiplier == 20:
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
    global cash, multiplier, Shop_Rating, Shop_Rating_Cost, multiplier_cost, seperater, start_time, colors, Cash_Reset
    global current_time_min, current_time_sec, Rewards_Page, Dungen_Cooldown, Spin_Period, section
    current_time_sec = time.time() - start_time
    current_time_min = int(current_time_sec / 3)
    Cash_Earned = current_time_min / 5
    while playing == True:
        if Cash_Reset == True:
            cash += Cash_Earned
            Cash_Earned = 0
            current_time_min = 0
            current_time_sec = 0
            print("Claimed!")
            time.sleep(1)
            Cash_Reset = False
        else:
            pass
        Dungen_Time_To_Wait_Min = Dungen_Cooldown - current_time_min
        Dungen_Time_To_Wait_Countdown = colors.CYAN + colors.BOLD + f"{Dungen_Time_To_Wait_Min}" + colors.END
        if Dungen_Time_To_Wait_Min < 0:
            Dungen_Time_To_Wait_Countdown = colors.BG_CYAN + colors.BOLD + "   READY!   " + colors.END 
        Spin_Time_To_Wait_Min = Spin_Period - current_time_min
        Spin_Time_To_Wait_Countdown = colors.CYAN + colors.BOLD + f"{Spin_Time_To_Wait_Min}" + colors.END
        if Spin_Time_To_Wait_Min < 0:
            Spin_Time_To_Wait_Countdown = colors.BG_GREEN + colors.BOLD + "   READY!   " + colors.END 


        os.system('cls')
        print(colors.BOLD + colors.BG_RED + colors.ITALIC + " REWARDS " + colors.END)
        class section:  
            ONE = f"""
    |-------------------------|              
    |                         |
    |        playtime:        |
    |-------------------------|
    |          {colors.UNDERLINE + colors.BOLD + colors.PURPLE + str(current_time_min) + ' min' + colors.END + '          |'}           
    |-------------------------|
    |                         |
    |    Earn 1 cash every:   |  *Upgrade this by increasing your 
    |        5 minutes!       |     store rating!
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
    |     {colors.BG_YELLOW + colors.BOLD + "  MATH DUNGEN  " + colors.END}     |
    |-------------------------|
    |      every:  {colors.UNDERLINE + colors.BOLD + colors.PURPLE + str(Dungen_Cooldown) + ' min' + colors.END + '     |'}           
    |-------------------------|
    |                         |
    |     Time To Wait:       |
    |        {Dungen_Time_To_Wait_Countdown} min           |
    |                         |
    |-------------------------|
    |                         |
    |    {colors.BOLD + colors.RED + str("ENTER [M] TO START") + colors.END + "   |"}
    |                         |
    |-------------------------|       
            """

            SPIN = f"""
    |------------------------------------------------------------------|
    | Common      | Rare        | Legendary   | Mythical    | Upgrades |
    |-------------|-------------|-------------|-------------|----------|
    |             |             |             |             |          |
    |             |             |             |             |          |
    |             |             |             |             |          |
    |             |             |             |             |          | 
    |             |             |             |             |          |
    |             |             |             |             |          |
    |             |             |             |             |          |
    |------------------------------------------------------------------|        

                            {colors.BOLD + colors.YELLOW + " ENTER [P] TO SPIN! " + colors.END}
            """

            DUNGEN = f"""
    {colors.BOLD + colors.YELLOW + " WELCOME TO THE MATH DUNGEN! " + colors.END}

|--------------------------------------------------------------------------  |
| What Is Dungen?          | Previous Games  | Points Scored | Cash Earned |
|--------------------------|-----------------|---------------|-------------|
| Math Dungen is where     |                 |               |             |
| you can earn money and   |                 |               |             |
| rewards for your         |                 |               |             |
| restaurant by completing |                 |               |             |
| waves of math questions! |                 |               |             |
|                          |                 |               |             |
| Press [D] to Begin!      |                 |               |             | 
|                          |                 |               |             |
|                          |                 |               |             |
|                          |                 |               |             |  
|--------------------------------------------------------------------------| 
    
    """
        if Rewards_Page == 1: 
            print(f"""
{section.ONE}

Enter [>] for next page  
Enter [<] for previous page
Enter [X] to exit                               Current page: {colors.DARKCYAN + colors.BOLD + str(page) + colors.END}                                                                                                                       
Enter [R] to refresh
                """)
        elif Rewards_Page == 2:
            print(f"""
{section.TWO}

Enter [>] for next page
Enter [<] for previous page
Enter [X] to exit                               Current page: {colors.DARKCYAN + colors.BOLD + str(page) + colors.END}
Enter [R] to refresh
                """)
        elif Rewards_Page == 3:
            print(f"""
{section.THREE}

Enter [>] for next page
Enter [<] for previous page
Enter [X] to exit                               Current page: {colors.DARKCYAN + colors.BOLD + str(page) + colors.END}
Enter [R] to refresh
                """)

        elif Rewards_Page == "SPIN":
            print(f"""
{section.SPIN}


Enter [<] for previous page
Enter [X] to exit                               Current page: {colors.DARKCYAN + colors.BOLD + str(page) + colors.END}
Enter [R] to refresh
                """)
        val = input("> ")
        if val == 'C' or val == 'c':
            if page == 1:
                Cash_Reset = True
            else:
                pass
        elif val == '>':
            if page == 3 or page == "SPIN":
                print("No next page")
                time.sleep(1)
            else:
                page += 1
        elif val == '<':
            if page == 1:
                print("No previous page")
                time.sleep(1)
            elif page == "SPIN":
                page = 2
            else:
                page -= 1 
        elif val == 'X' or val == 'x':
            page=1
            GameMenu()
        elif val == 'R' or val == 'r':
            DoRewards()
        elif val == 'S' or val == 's':
            if page == 2:
                if Spin_Time_To_Wait_Min < 0:
                    os.system('cls')
                    page = "SPIN"
                else:
                    print("SPIN NOT READY")
                    time.sleep(1)
            else:
                print("Please enter a denfined value")
                time.sleep(1)
        elif val == 'P' or val == 'p':
          if page == "SPIN":
            DoSpin()
          else:
            print("Please enter a denfined value")
            time.sleep(1)
        elif val == 'M' or val == 'm':
            if page == 3:
                if Dungen_Time_To_Wait_Min < 0:
                    DoDungen()
                else:
                    print("DUNGEN NOT READY")
                    time.sleep(1)
            else:
                print("Please enter a denfined value")
                time.sleep(1) 
        else:
            print("Please enter a denfined value")
            time.sleep(1)
          
def DoDungen():
  global playing, cash, multiplier, Shop_Rating, Shop_Rating_Cost, multiplier_cost, seperater, section 
  while playing == True:
    os.system('cls')
    print(section.DUNGEN)
    val = input("> ")

def DoSpin():
  pass


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
            while playing:
                WhatNext = input("Go Back? (Y/N): ")
                if WhatNext == "N" or WhatNext == "n":
                    GameMenu()
                elif WhatNext == "Y" or WhatNext == "y":
                    break
                else:
                    print("Please enter a defined option")
                    time.sleep(1)
                    delete_multiple_lines(2)
        elif inquiry == 'U' or inquiry == 'u':
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
            while playing:
                WhatNext = input("Go Back? (Y/N): ")
                if WhatNext == "N" or WhatNext == "n":
                    GameMenu()
                elif WhatNext == "Y" or WhatNext == "y":
                    break
                else:
                    print("Please enter a defined option")
                    time.sleep(1)
                    delete_multiple_lines(2)
        elif inquiry == 'R' or inquiry == 'r':
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
            while playing:
                WhatNext = input("Go Back? (Y/N): ")
                if WhatNext == "N" or WhatNext == "n":
                    GameMenu()
                elif WhatNext == "Y" or WhatNext == "y":
                    break
                else:
                    print("Please enter a defined option")
                    time.sleep(1)
                    delete_multiple_lines(2)
        elif inquiry == 'S' or inquiry == 's':
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
            while playing:
                WhatNext = input("Go Back? (Y/N): ")
                if WhatNext == "N" or WhatNext == "n":
                    GameMenu()
                elif WhatNext == "Y" or WhatNext == "y":
                    break
                else:
                    print("Please enter a defined option")
                    time.sleep(1)
                    delete_multiple_lines(2)
        elif inquiry == 'I' or inquiry == 'i':
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
            while playing:
                WhatNext = input("Go Back? (Y/N): ")
                if WhatNext == "N" or WhatNext == "n":
                    GameMenu()
                elif WhatNext == "Y" or WhatNext == "y":
                    break
                else:
                    print("Please enter a defined option")
                    time.sleep(1)
                    delete_multiple_lines(2)
        elif inquiry == 'C' or inquiry == 'c':
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
            while playing:
                WhatNext = input("Go Back? (Y/N): ")
                if WhatNext == "N" or WhatNext == "n":
                    GameMenu()
                elif WhatNext == "Y" or WhatNext == "y":
                    break
                else:
                    print("Please enter a defined option")
                    time.sleep(1)
                    delete_multiple_lines(2)
        elif inquiry == 'M' or inquiry == 'm':
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
            while playing:
                WhatNext = input("Go Back? (Y/N): ")
                if WhatNext == "N" or WhatNext == "n":
                    GameMenu()
                elif WhatNext == "Y" or WhatNext == "y":
                    break
                else:
                    print("Please enter a defined option")
                    time.sleep(1)
                    delete_multiple_lines(2)
        elif inquiry == 'H' or inquiry == 'h':
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
            while playing:
                WhatNext = input("Go Back? (Y/N): ")
                if WhatNext == "N" or WhatNext == "n":
                    GameMenu()
                elif WhatNext == "Y" or WhatNext == "y":
                    break
                else:
                    print("Please enter a defined option")
                    time.sleep(1)
                    delete_multiple_lines(2)
        elif inquiry == 'X' or inquiry == 'x':
            GameMenu()
        else:
            print("Please enter a defined value")
            time.sleep(1)


def DoSettings():
    global OverallRating
    global OverallScore
    global playing
    global colors
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
Change Store Name (Current: {Name}), {colors.BOLD + 'enter [N]' + colors.END}
{seperater}
Change Customer prompt menu (Current: {display}), {colors.BOLD + 'enter [C]' + colors.END}

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
        else:
            print("Enter a defined option")
            time.sleep(1)

def DoOrder():
    global OverallScore
    global OverallRating
    global ratings
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
    global ChangeAVGDisplay, customers, NumOrders
    order = DoOrder()
    #NumOrders = 0
    #for i in range(customers):
     #   NumOrders += 1
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
        if NumCorrect == 4:
            if multiplier == 'LOCKED':
                delete_multiple_lines(1)
                print(f"""{seperater}
{colors.BOLD + colors.UNDERLINE + colors.PURPLE + 'MULTIPLIER UNLOCKED!' + colors.END}\n""")
                multiplier = 1

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

def delete_multiple_lines(n=1):
    for _ in range(n):
        sys.stdout.write("\x1b[1A")  # cursor up one line
        sys.stdout.write("\x1b[2K")  # delete the last line

start_time = time.time()
seperater = "----------------------------------------------------------------"
cash = float(0).__round__(2)
multiplier = 'LOCKED'
Shop_Rating = "LOCKED"
multiplier_cost = "LOCKED"
Shop_Rating_Cost = "LOCKED"
Name = "Paulie's"
cpm = 0
StaffNum = 0
customers = 0
Shop_Multiplier = 0
Rewards_Page = 1
Items_Page = 1
DisplayCustomers = False
cash_color = colors.GREEN + colors.BOLD + "Cash:" + colors.END 
Cash_Reset = False
Spin_Period = 15
Dungen_Cooldown = 0
current_time_sec = time.time() - start_time
current_time_min = int(current_time_sec / 60)
ChangeAVGDisplay = False  
start = GameMenu()
