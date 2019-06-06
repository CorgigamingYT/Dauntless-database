import time
import os
def pp (text,pause):
    print(text)
    time.sleep(pause)
Embermane = {
    "Lesser Embermane":"""A fast and ferocious Behemoth that has not yet fed on enough blaze aether
to unleash fiery attacks on those who hunt it,
a Lesser Embermane is still not a quarry to be underestimated.
Its stats are as follows:
    Element type: Blaze (Fire)
    Danger level: 1
    armor type: Charrogg, Embermane or Hellion.
    Recommended weapon type: Boreus, Pangar or Skraev.
    Recommended weapon power level: 50
    Recommended armor power level: 50""",

    "Embermane":"""Many are the Slayers who have fallen prey to the furious energy of this blaze-feeding terror.
Fast and deadly, the Embermane is an inferno on four legs.
It's stats are as follows:
    Element type: Blaze (Fire)
    Danger level: 5
    Recommended armour type: Charrogg, Embermane or Hellion.
    Recommended weapon type: Boreus, Pangar or Skraev.
    Recommended weapon power level: 200
    Recommended armor power level: 200""",
    
    "Bloodfire Embermane":"""The dreaded Bloodfire variety of Embermane,
has been responsible for the destruction of countless woodland in the Shattered Isles.
It's stats are as follows,
    Element type: Blaze (Fire)
    Danger level: 10 (Normal), 15 (Heroic)
    Recommended armour type: Charrogg, Embermane or Hellion.
    Recommended weapon type: Boreus, Pangar or Skraev.
    Recommended weapon power level: 350 (Normal), 475 (Heroic)
    Recommended armour power level: 350 (Normal), 475 (Heroic)""",

    "Fiery Helm":"""The Fiery Helm is a piece of craftable armour in Dauntless.
It is crafted from Embermane reagents, and is part of the Embermane Armour set.
It's stats are as follows:
Level   Resistance     Crafting Materials
Base    25	       Rams (x40), [[|]] (x1), [[|]] (x1)
+1      35	       Rams (x10), Blaze Orb (x1)
+2	45             Rams (x15), Blaze Orb (x1)
+3	55             Rams (x25), Blaze Orb (x2)
+4	65             Rams (x35), Blaze Orb (x2)
+5	75             Rams (x40), Blaze Orb (x2)
+6	85             Rams (x55), Dull Arcstone (x3), Smoldering Bloodhide (x2), Blaze Orb (x3)
+7	95             Rams (x60), Dull Arcstone (x4), Blaze Orb (x3)
+8	105            Rams (x75), Dull Arcstone (x5), Shining Arcstone (x5), Blaze Orb (x3)
+9	115            Rams (x90), Dull Arcstone (x6), Shining Arcstone (x10), Blaze Orb (x4)
+10	125            Rams (x100), Dull Arcstone (x7), Shining Arcstone (x15), Bloodsoul Shard (x1), Smoldering Bloodhide (x3), Blaze Orb (x4)
+11	127.5          Rams (x150), Peerless Arcstone (x5)
+12	130            Rams (x150), Peerless Arcstone (x6)
+13	132.5          Rams (x150), Peerless Arcstone (x7)
+14	135            Rams (x150), Peerless Arcstone (x8)
+15	137.5          Rams (x150), Peerless Arcstone (x9)"""
	}
Behemoths = ["Charrogg", "Embermane", "Hellion", "Boreus", "Pangar", "Skraev", "Drask", "Nayzaga", "Stormclaw", "Kharabak", "Koshai", "Skarn", "Gnasher", "Quillshot", "Shrike", "Riftstalker", "Shrowd", "Rezakiri", "Valomyr"]
choice1  = input("Please enter the type of behemoth you are fighting: ").lower()
if choice1 == "charrogg":
    pp("Welcome to the world of the Charrogg.",3)
    pp("Do you want learn about the...",2)
    pp("""
1. Behemoth
2. Armour
3. Weapons
""",3)
    charr = input("Please choose the required area that needs to be learned about: ")
    if charr == "1":
        pp("So, to business, there are 2 types of Charrogg: ",3)
        pp("""
1. Behemoth
2. Armour
3. Weapons
""")
        if charrb == "1":
            pp("""A walking aether furnace with tough, armoured hide,
the Charrogg feeds on blaze energy,
and uses it to blast cruel jets of flame in all directions.""",2)
            #finish
elif choice1 == "embermane":
    pp("Welcome to the world of the embermane.",2)
    pp("Do you want learn about the...",2)
    pp("""
1. Behemoth
2. Armour
3. Weapons
""",3)
    ember = input("Please choose the required area that needs to be learned about: ")
    if ember == "1":
        pp("So, to business, there are 3 types of Embermane: ",2)
        pp("""
1. Lesser Embermane.
2. Normal Emebrmane.
3. Bloodfire Embermane.
""",3)
        emberb = input("Please choose the one you are fighting: ")
        if emberb == "1":
            pp("The Lesser Embermane...",3)
            print(Embermane.get("Lesser Embermane"))
            time.sleep(10)
            yorn = input("Do you want to learn about something else? ").lower()
            if yorn == "yes":
                os.startfile("dauntless database V2.py")
                exit()
            elif yorn == "no":
                pp("Thanks for using this code",2)
                exit()
        if emberb == "2":
            pp("The Normal Embermane...",3)
            print(Embermane.get("Embermane"))
            time.sleep(10)
            yorn = input("Do you want to learn about something else? ")
            if yorn == "yes" or "Yes":
                os.startfile("dauntless database V2.py")
                exit()
            if yorn == "no" or "No":
                pp("Thanks for using this code",2)
                exit()
        if emberb == "3":
            pp("The Bloodfire Embermane",3)
            print(Embermane.get("Bloodfire Embermane"))
            time.sleep(10)
            yorn = input("Do you want to learn about something else? ")
            if yorn == "yes" or "Yes":
                os.startfile("dauntless database V2.py")
                exit()
            if yorn == "no" or "No":
                pp("Thanks for using this code",2)
                exit()
    if ember == "2":
        pp("So then you have chosen to learn about the embermane armour.",3)
        pp("""The armour consists of:
1. The Fiery Helm,
2. The Fiery Breastplate,
3. The Fiery Gauntlets and
4. The Fiery Greaves
5. Entire Set
""",7)
        embera = input("Please enter the part of the armour you what to learn about: ")
        if embera == "1":
            pp("The Fiery Helm...",3)
            print(Embermane.get("Fiery Helm"))
            time.sleep(10)
            yorn = input("Do you want to learn about something else? ")
            if yorn == "yes" or "Yes":
                os.startfile("dauntless database V2.py")
                exit()
            if yorn == "no" or "No":
                pp("Thanks for using this code",2)
                exit()
#finish
elif choice1 == "hellion":
     pp("Welcome to the world at the all-powerful hellion, master of fire and blaze.",4)
     #finish
elif choice1 == "shelby":
    pp("R1P 5H3L8Y.",4)
    pp("*Memeorial anthem.*",4)
    pp("You will forever be remmbered",3)
    pp("R1P, Now and forever more.",3)
