#setting up dictionary
off = {
   'QB' : '',
   'RB' : '',
   'WR_1': '',
   'WR_2': '',
   'WR-3': '',
   'TE_1': '',
   'LT': '',
   'LG': '',
   'C': '',
   'RG': '',
   'RT':'',
   
    }

#setting up functions to make more user freindly
def printdict(a_dict):
    for key, value in a_dict.items():
        print("%s: %s" %(key , value))

def updateoff(position, player):
    off[position] = player
    

#Start of program
name = input("What is your name? ")
print("Hello %s, you are going to see postions pop up on you screen, \n"
      "please type out who you would like to put in that position." %name)

for key, value in off.items():
    print(key, value)
    playerInput = input()
    off[key] = playerInput

print("Here is your offensive line up as of now:")
print(printdict(off))

#main
while True:
    cmd = input("Now, do you want to [u]pdate a postion,[c]reate a postion,\n" 
                "[d]elte a position, or [e]xit with the final team? ")

    if cmd == "u":
        updatePO = input("What postion would you like to change the player playing? ")
        updatePA = input("What player would you like to put in that positon? ")
        updateoff(updatePO, updatePA)
        print("This is now your team: " + printdict(off) + "\n" )

    elif cmd == "c":
        createPO = input("What postion would you like to create, \n "
                          "remember to type '' around that postion. ")
        createPA = input("What player would you like to put in that postion? ")
        updateoff(createPO, createPA)
        print("This is now your team: " + printdict(off) + "\n" )

    elif cmd == "d":
            deletePO = input("What postion would you like to delete? ")
            map(off.pop, [deletePO])
            print("This is now your team: " + printdict(off) + "\n" )

    elif cmd == "e":
        print("Here is your final team: " + printdict(off) + "\n" )
        print("Thanks for making an offensive line up %s!" %name)
        break

    else:
        print("Please enter a valid action speified by [] around the letter in the /n"
              "action specified") 
        
        
