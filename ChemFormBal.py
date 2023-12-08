import random, time, os, math

def DoSynthesis():
    while True:
        os.system("cls")
        num_reactents = int(input("Number of reactents: "))
        for i in range(num_reactents):
            atom = input(f"Enter molecule {i+1}: ")
            for i in range(len(atom)):
                pass
        

while True:
    os.system("cls")
    Conversion_Type = input("Synthesis or Decomposition? (1/2): ")
    Conversion_Type = int(Conversion_Type)
    if Conversion_Type == 1:
        DoSynthesis()
    elif Conversion_Type == 2:
        DoDecomposition()
    else:
        print("Unknown conversion")
        time.sleep(1)