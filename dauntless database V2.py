import time
import os
def pp (text,pause):
    print(text)
    time.sleep(pause)
Behemoths = ["Charrogg", "Embermane", "Hellion", "Boreus", "Pangar", "Skraev", "Drask", "Nayzaga", "Stormclaw", "Kharabak", "Koshai", "Skarn", "Gnasher", "Quillshot", "Shrike", "Riftstalker", "Shrowd", "Rezakiri", "Valomyr"]
choice1  = input("Please enter the type of behemoth you are fighting: ").lower()
if choice1 == "charrogg":
    pp("a",1)
elif choice1 == "embermane":
    pp("Welcome to the world of the embermane.",2)
    pp("Do you want learn about the...",2)
    pp("""
1. Behemoth
2. Armour
3. Weapons
""",3)
    ember = input("Please choose the required area that needs to be learnt about: ")
    if ember == "1":
        pp("So, to business, there are 3 types of Embermane: ",2)
        pp("""
1. Lesser Embermane.
2. Normal Emebrmane.
3. Bloodfire Embermane.
""",3)
        emberb = input("Please choose the one you are fighting: ")
        if emberb == "1":
            pp("So, the Lesser Embermane is the weakest behemeoth and the first thing you fight.",4)
            pp("""It's stats are as follows:
Element type: Blaze (Fire)
Danger level: 1
Recommended armour type: Charrogg, Embermane or Hellion.
Recommended weapon type: Boreus, Pangar or Skraev.
Recommended weapon power level: 50
Recommended armour power level: 50
""",10)
            yorn = input("Do you want toi learn about something else? ")
            if yorn == "yes" or "Yes":
                os.startfile("dauntless databaseV2.py")
                exit()
            if yorn == "no" or "No":
                pp("Thanks for using this code",2)
                exit()
        if emberb == "2":
            pp("So the normal embermane, it is tougher to take down than it's lesser brother and much more dangerous.",4)
            pp("""It's stats are as follows:
Element type: Blaze (Fire)
Danger level: 5
Recommended armour type: Charrogg, Embermane or Hellion.
Recommended weapon type: Boreus, Pangar or Skraev.
Recommended weapon power level: 200
Recommended armour power level: 200
""",10)
            yorn = input("Do you want toi learn about something else? ")
            if yorn == "yes" or "Yes":
                os.startfile("dauntless databaseV2.py")
                exit()
            if yorn == "no" or "No":
                pp("Thanks for using this code",2)
                exit()
        if emberb == "3":
            pp("So the bloodfire embermane, the toughest type of embermane.",3)
            pp("""It's stats are as follows,
Element type: Blaze (Fire)
Danger level: 10 (Normal), 15 (Heroic)
Recommended armour type: Charrogg, Embermane or Hellion.
Recommended weapon type: Boreus, Pangar or Skraev.
Recommended weapon power level: 350 (Normal), 475 (Heroic)
Recommended armour power level: 350 (Normal), 475 (Heroic)
""",10)
            yorn = input("Do you want toi learn about something else? ")
            if yorn == "yes" or "Yes":
                os.startfile("dauntless databaseV2.py")
                exit()
            if yorn == "no" or "No":
                pp("Thanks for using this code",2)
                exit()
#Embermane Done
elif choice1 == "hellion":
     print("c")
elif choice1 == "boreus":
    print("d")
elif  choice1 == "pangar":
    print("e")
elif choice1 == "skraev":
    print("f")
elif choice1 == "drask":
    print("g")
elif choice1 == "nayzaga":
    print("h")
elif choice1 == "stromclaw":
    print("i")
elif choice1 =="kharabak":
    print("j")
elif choice1 == "koshai":
    print("k")
elif choice1 == "skarn":
    print("l")
elif choice1 == "gnasher":
    print("m")
elif choice1 ==  "quillshot":
    print("n")
elif choice1 ==  "shrike":
    print("o")
elif choice1 == "riftstalker":
    print("p")
elif choice1 ==  "shrowd":
    print("q")
elif choice1 == "rezakiri":
    print("r")
elif choice1 ==  "valomyr":
    print("s")
