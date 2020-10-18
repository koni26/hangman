

#list for words saved in system for player to select if requested instead of typing
words=["notebook","driver","keyboard","computer","retrospective"]
#list variables to keep found and failed words and also to check if player wins
letterlist=[]
foundletters=[]
failedletters=[]

#based on value of failure variable which indicates number of fails in guessing letter, function
#draws gallows and and parts of man
def drawman(failure):
    for i in range(10):
        if i==0:
            print("\u0020"*3 + "_"*8)
        elif i==9:
            print("\u0020" + "-"*4)
        elif i==1:
            print("\u0020"*2 + "|" + "\u0020"*8 + "|")
        elif i==2:
            if 0<failure<7:
                print("\u0020"*2 + "|" + "\u0020"*8 +  "O")
            else:
                print("\u0020"*2 + "|")
        elif i==3:
            if failure==2:
                print("\u0020"*2 + "|" + "\u0020"*8 +  "|")
            elif failure==3:
                print("\u0020"*2 + "|" + "\u0020"*8 +  "|" + "\\")
            elif failure in [4,5,6]:
                print("\u0020"*2 + "|" + "\u0020"*7 + "/" + "|" +  "\\" )
            else:
                print("\u0020"*2 + "|")
        elif i==4:
            if failure==5:
                print("\u0020"*2 + "|" + "\u0020"*7 + "/"  )
            elif failure==6:
                print("\u0020"*2 + "|" + "\u0020"*7 + "/ " + "\\"  )
            else:
                print("\u0020"*2 + "|")
        else:
            print("\u0020"*2 + "|")

#clear screen and back to first line first col
print(chr(27) + "[2J" + chr(27) + "[H")
#asking if player wants to select word from list or type him/herself desired word
answer=input("Do you want to pick a word from the list? ('Y' or 'N') : ")

#if answer positive, all words shows and player is asked to type number of desired word
#selected word assigned to variable 'Selectedword'
if answer=="Y" or answer=="y":
    for i in words:
        print(str(words.index(i)+1) + ".) " + i)
    number=0
    while int(number)<1 or int(number) > len(words):
        number=input("\nPlease type number of word you pick : ")
        if int(number) > len(words):
            print("\nPlease type number from list!\n")
            continue
        else:
            Selectedword=words[int(number)-1]
            break
#if answer negative, variable assigned to what player types as word
elif answer=="N" or answer=="n":
    Selectedword=input("Type word you selected : ")


#drawing letters and spaces based on already found letters
def drawletters():
    for i in range(len(Selectedword)):
        if letterlist[i] not in foundletters:
            print("_ ",end="")
        else:
            print(letterlist[i],end="")


#clear screen after word selection and get back to first line first col
print(chr(27) + "[2J" + chr(27) + "[H")

#letters go to list
for i in Selectedword:
    letterlist.append(i)

#it is beginning with zero falure and drawing gallows first
failure=0
drawman(failure)

#draw letters first time
print("\nHere is empty spaces for your word")
drawletters()


#until failure value becomes 6 which ends the game, it is checking if guessed letter are correct.
while failure!=6:
    guess=input("\nGuess a letter : ")
    #re-clean and write from first line first col
    print(chr(27) + "[2J" + chr(27) + "[H")
    #message for repeatedly entered letters
    if guess in foundletters or guess in failedletters:
        drawman(failure)
        print("\nAlready guessed letter '" + guess + "', try another!")
        print("Failed letters : " , failedletters)
        drawletters()
        continue
    #if letter is correct adding to space and checking if whole letters are found to determine winning
    if guess.lower() in (string.lower() for string in letterlist):
        foundletters.append(guess)
        drawman(failure)
        print("\nThats was correct !")
        print("Failed letters : " , failedletters)
        drawletters()
        if len(set(letterlist))==len(set(foundletters)):
            print("\nYOU WON !")
            break
    #if letter is wrong draws man and checking if game is finished.
    else:
        print(chr(27) + "[2J" + chr(27) + "[H")
        failedletters.append(guess)
        failure +=1
        drawman(failure)
        print("\nThat was wrong !")
        print("Failed letters : " , failedletters)
        drawletters()
        if failure==6:
            print("\nYOU LOST ! Word was '" + Selectedword + "'.")








