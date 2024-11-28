

def GCD(num, num2):
    while num2 > 0:
        num, num2 = num2, num%num2
    return num

def myfunc(width, height):
    lit = 0
    unlit = 0
    string = ""
    w = 0
    h = 0
    while height > h:
        height -=1
        w = 0
        while w < width:
            if ( w == 0 and height == 0 ):
                string += "L " #Laser
            elif GCD(w, height) == 1:
                string += "* "
                lit += 1
            elif ( w == 0 and height == 1 ) or ( w == 1 and height == 0 ): #direct
                string += "* "
                lit += 1
            else:
                string += ". "
                unlit += 1
            #print(height, w)
            w += 1
        string += "\n"
    return string, lit, unlit

print("Laser field simulation... ")
filename = input("Please enter output file name: ")

width = int(input("Please enter width: "))
while width < 0:
    print("please enter a valid value")
    width = int(input("Please enter width: "))

height = int(input("Please enter height: "))
while height < 0:
    print("please enter a valid value")
    height = int(input("Please enter height: "))
    
string, litmatch, unlit = myfunc(width, height)

file = open(filename, "w") #to write
file.write(string)
file.write("\nSimulation Complete!")
file.write("\nNumber of lit matches: " + str(litmatch))
file.write("\nNumber of unlit matches: " + str(unlit))
file.close()

#string, litmatch, unlit = myfunc(8, 6)
#string, litmatch, unlit = myfunc(10, 10)
#string, litmatch, unlit = myfunc(1000, 1000)

print(string)
print("\nSimulation complete!")
print("num of lit: {}".format(litmatch))
print("num of unlit: {}".format(unlit))

#print(GCD(4, 6)) # if == 1 it is lit - else not lit
