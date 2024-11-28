import math       ## Needed for math.ceil 
gallonPaint = 400 ## One gallon of paint covers 400 sq. ft
oneFtFloor  = 9   ## 9 of 4"x4" tiles to cover 1 sq. ft 

######## Data input
print()
print(" "*6 + ">>>Please enter the following room data in feet.<<<")
roomLength = int(input("Please enter the room length: "))
roomWidth  = int(input("Please enter the room width: " ))
roomHeight = int(input("Please enter the room height: "))

######## Area calculations
areaWall_L  = 2*( roomLength * roomHeight)
areaWall_H  = 2*( roomWidth * roomHeight )
areaCeiling = roomLength * roomWidth
totalArea   = areaWall_H + areaWall_L + areaCeiling
print()
print("- Total area is", totalArea, "sq. ft")

######## Paint needed
paintNeed = totalArea / gallonPaint
print("-- Needed paint:", paintNeed, "gallons.")
paintNeed = math.ceil(paintNeed) #### to round up the needed gallons
print("--- We need approximately", paintNeed, "gallons of paint.")

######## Number of tiles needed (4"x4")
floorArea = roomLength * roomWidth * oneFtFloor
print('---- Number of 4"x4" tiles needed:', floorArea, 'tiles.')

