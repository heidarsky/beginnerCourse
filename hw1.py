
def isMandelbrot(c):
    z = 0
    for i in range(1000):
        z = z**2 + c    # Z(n+1) = (Zn)^2 + c
        temp = abs(z)
        
        if temp > 2:
            return False
    return True

#width = 250 
#height = 125 
width = float(input("Please enter the width(for ex: 250): "))
height = float(input("Please enter the height(for ex: 125): "))
centerX = float(input("X coord (for ex: 0): "))
centerY = float(input("Y coord (for ex: -1): "))

for row in range(int(height)):
    for column in range(int(width)):
        y = 1 - 4*(row / (height-1) )
        x = -2 + 3*(column / (width-1) )
        z = complex(x, y)              #imaginary
        if x == centerX and y == centerY:
            print("+", end="")
        elif x == centerX:
            print("|", end="")
        elif y == centerY:
            print("-", end="")
        elif isMandelbrot(z):
            print("*", end="")
        else:
            print(" ", end="")
    print()
