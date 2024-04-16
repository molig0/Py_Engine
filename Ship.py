ship = int(input("Introduceti marimea vaporului: "))

for x in range(1, 11):
    if x == ship:
        if x <= 5:
            print("W", end="")    #Corabie mica small_ship
        if x >5 :
            print ("wWw", end="") #Corabie mare big_ship
    else:
        print("~", end="")
