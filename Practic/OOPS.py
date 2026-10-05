class blinkit():
    def __init__(staf):

        staf.regular = "manoj","naman","naruto","aman","sasuke"
        staf.temp = "shreya","pooja","mummy","arjun", "zoya", "kabir", "megha", "rohan", "anya", "vikram", "riya"
        staf.morden =   "nova", "zenith", "aura", "nexus", "orbit", "cipher"
        staf.short = "loop", "sync", "vibe", "core", "flux", "dash"

    def display(staf):
        print("This is the data of blinkit staf Regular",staf.regular)
        print("This is the data of blinkit staf Temporary",staf.temp)
        print("This is the data of blinkit staf Short",staf.short)
        print("This is the data of blinkit staf Morden",staf.morden)

s1=blinkit()
s1.display()

