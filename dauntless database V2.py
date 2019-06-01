import time
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
""")
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
