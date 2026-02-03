"""
#first
numList = [1,2,3,4,5]
print(numList[2:4])
strList = ["cow", "otter", "wasp"]
hi = strList[0][0]+strList[1][0]+strList[2][0]
print(hi)
"""

#first
numList = [1,2,3,4,5]
print(numList[2:4])
strList = ["cow", "otter", "wasp"]
statement = strList[0][0]+strList[1][0]+strList[2][0]
print(statement)

#scond
import random

def numb_game():
    num = random.randint(1, 100)
    print(num)
    user_input = 0
    guessList = []
    while user_input != num:
        user_input = int(input("input number"))
        if user_input == num:
            print("yay")
        if user_input > num:
            print("higher")
        guessList.append(user_input)
    guessList.sort(reverse=True)
    print(guessList)
    length = len(guessList)
    if length % 2 == 0:
        leftindex = (length/2)-1
        rightindex = length/2
        median = (guessList[int(leftindex)]+guessList[int(rightindex)])/2
        print(median)
    if length % 2 != 0:
        index = (length-1)/2
        median = guessList[index]
        print(median)

numb_game()

#third
list = []

def liscence_plate():
    input = input("What is your liscence plate")
    input.upper()
    if len(input)>7:
        input = input.replace("A", "")
        input = input.replace("E", "")
        input = input.replace("I", "")
        input = input.replace("O", "")
        input = input.replace("U", "")
    if len(input)>7:
        print("invalid")
        exit()
    input = input.replace("S", "5")
    if input[0] == 5:
        first = input.replace("5", "S")
        first = first[0]
        input = input.lstrip("S")
        input = first + input

    print(input)
liscence_plate()
    
"""
#second
import random

def number_game():
    num = random.randint(1,100)
    print(num)
    user_input = 0
    guessList = []
    while user_input != num:
        user_input = int(input("Input a number from 1-100: "))
        if user_input == num:
            print("Congratulations! You guessed the right number. You had", len(guessList)+1, "attempts.")
        if user_input > num:
            print("Your value is higher")
        if user_input<num:
            print("Your value is lower")
        guessList.append(user_input)
    guessList.sort(reverse = True)
    print(guessList)
    length = len(guessList)
    if length % 2 != 0:
        index = (length-1)/2
        median = guessList[int(index)]
        print("Your median is", median)
    else:
        left_index = (length/2)-1
        right_index = (length/2)
        middle_index = (left_index + right_index)/2
        median = (guessList[int(left_index)] + guessList[int(right_index)])/2
        print("Your median is", median)
        
number_game()


#third
list = []

def license_plate():
    user_input = input("Enter a license plate: ")
    user_input.upper()
    if len(user_input)>7:
        user_input = user_input.replace("A", "")
        user_input = user_input.replace("E", "")
        user_input = user_input.replace("I", "")
        user_input = user_input.replace("O", "")
        user_input = user_input.replace("U", "")
    if len(user_input)>7:
        print("Provide another license plate: ")
        exit()
    user_input = user_input.replace("S", "5")
    if user_input[0] == "5":
        firstCharacter = user_input.replace("5", "S")
        firstCharacter = firstCharacter[0]
        user_input = user_input.lstrip("S")
        user_input = firstCharacter + user_input
    print(user_input)
        
license_plate()


#second
import random

def number_game():
    user_input = 0
    guesses = []
    winningNum = random.randint(1,100)
    print(winningNum)
    while winningNum != user_input:
        user_input = int(input("Enter a number from 1-100: "))
        guesses.append(user_input)
        if user_input == winningNum:
            print("You guessed the right number! You had", len(guesses), "attempts.")
        if user_input > winningNum:
            print("Incorrect. Your number is too high")
        if user_input<winningNum:
            print("Incorrect. Your number is too low")
    guesses.sort(reverse=True)
    print(guesses)
    length = len(guesses)
    if length % 2 == 0:
        left_index = (length/2)-1
        right_index = length/2
        median = (guesses[int(left_index)] + guesses[int(right_index)])/2
        print(median)
    else:
        index = (length/2)
        median = guesses[int(index)]
        print(median)
number_game()
     

def licenseplate():
    license = input("Enter license plate  ")
    license.upper()
    if len(license) > 7:
        license = license.replace("A", "")
        license = license.replace("E", "")
        license = license.replace("I", "")
        license = license.replace("O", "")
        license = license.replace("U", "")
        print(license)
    if len(license) > 7:
        print("Invalid")
        exit()
    license = license.replace("S", "5")
    if license[0] == "5":
        firstCharacter = license.replace("5", "S")
        firstCharacter = license[0]
        license = license.lstrip("S")
        license = firstCharacter + license
    print(license)
licenseplate()
"""