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
#making a finction to print the dictionary to look better
def printdict(dict):
    for player in off:
        print(player)
    return

#inforing user how to make and update entries
name = input("What is your name? ")
print("Hello %s!" %name)
print("To make/update a entry in the Offense Dictionary type off.update({('position)' = ('player')})")
print("Also at anytime type printdict(off) to print out the Offense Dictionary")      
