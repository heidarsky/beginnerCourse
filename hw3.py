

def checkInput(choice):
    while choice < 0 or choice > 3 :
        print("Please enter a valid choice.")
        choice = int(input("Please enter your selection: "))
    return choice
    
def userIn():
    choice = int(input("Please enter your selection: "))
    choice = checkInput(choice)
    return choice

def interface():
    print("*"*40)
    print("1. Find the anagrams of a word")
    print("2. Display the anagram groups by word length")
    print("3. Display the anagram groups by group length")
    print("0. Exit")
    print("*"*40)
    print()

def mydictionary(words, h):
    mydict = {}
    for word in words[h]:
        mytup = tuple(sorted(word))
        if mytup in mydict:
            mydict[mytup].append(word)
        else:
            mydict[mytup] = [word]
    return mydict

def mainApp():
    words = {}
    try:
        with open("words.txt") as file:
            for line in file.readlines():
                myWord = line.strip()
                length = len(myWord)
                if length in words:
                    words[length].append(myWord)
                else:
                    words[length] = [myWord]
                
    except:
        print("File DNE")
    
    if choice == 0:  ## EXIT
        return choice
    
    if choice == 1:
        word = input("Please enter the word you wish to find: ")
        word = word.upper()
        length = len(word)
        found = 0
        for y in words[length]:
            if y == word:
                mydict = mydictionary(words, len(word))
                print("The anagrams for {} are:".format(word))
                ## ANAGRAMS 
                mytup = tuple(sorted(word))
                if mytup in mydict:
                    print(mydict[mytup])
                else:
                    print("{} doesn't exist.".format(word)) 
                found = 1
        if found == 0:
            print("{} doesn't exist".format(word))
                
    if choice == 2:
        lengthWords = int(input("Please enter the length of words to display (2-15): "))
        while lengthWords < 2 or lengthWords > 15 :
            print("Invalid input. Try again.")
            lengthWords = int(input("Please enter the length of words to display (2-15): "))
        print("The anagrams for {}-letter words are: ".format(lengthWords))
        
        mydict = {}
        for word in words[lengthWords]:
            mytup = tuple(sorted(word))
            if mytup in mydict:
                mydict[mytup].append(word)
            else:
                    mydict[mytup] = [word]
        for x in mydict:
            print(mydict[x])
        
    if choice == 3:
        groupSize = int(input("Please enter anagram group size (2-7): "))
        while groupSize < 2 or groupSize > 7:
            print("Invalid input. Try again")
            groupSize = int(input("Please enter anagram group size (2-7): "))
        print("The {}-word groups are:".format(groupSize))
        
        mydict = {}
        for word in words[groupSize]:
            mytup = tuple(sorted(word))
            if mytup in mydict:
                mydict[mytup].append(word)
            else:
                    mydict[mytup] = [word]
        for x in mydict:
            if len(mydict[x]) == groupSize:
                print(mydict[x])
        
### APP
anotherOne = True
interface() #print

while anotherOne == True:
    choice = userIn() #check input
    if choice == 0:   #0 is exit
        anotherOne = False
    mainApp() #run the app
    
print("Thank you!")
