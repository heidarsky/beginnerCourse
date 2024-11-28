
import os.path

def myFun(file):
    exitApp = False
    if file == " ":
        exitApp = True
    while not os.path.exists(file) and exitApp == False: #checks if file doesn't exist
        file = input("File not found. Try again: (enter blank space to stop) ")
        if file == " ":
            exitApp = True
    if exitApp == True:
       print("Thank you, Bye!")
    else:
        sellPrice = 0
        buyPrice = 10**999999    #for comparison purposes
        fileRead = open(file)    #reads file
        next(fileRead)           #skips header to read numbers only
        for line in fileRead:    #reads every line
            word = line.strip()  #strips line by line
            word = word.split(",")
            if float(word[2]) > sellPrice:
                sellPrice = float(word[2])    #high values
                sellDate = (word[0])    
            if float(word[3]) < buyPrice:
                buyPrice = float(word[3])    #low values
                buyDate = (word[0])
        maxProf = sellPrice - buyPrice   #per share
        valueRatio = sellPrice / buyPrice   #change in value
        #print(sellPrice, buyPrice, maxProf)
            
        print("Reading data ...")
        print("*"*40)
        print("The maximum profit is", round(maxProf, 2), "per share")
        print()
        print("Buy on", buyDate, "at a price of", round(buyPrice,2))
        print("Sell on", sellDate, "at a price of", round(sellPrice,2))
        print()
        print("Change in value ratio:", round(valueRatio,3))
        print("*"*40)
        fileName = input("Please enter the data file name: (blank space to exit) ")
        myFun(fileName)

fileName = input("Please enter the data file name: (blank space to exit) ")
myFun(fileName)
