
numList = [1,2,3,4,5]
print(numList[2:4])
strList = ["cow", "otter", "wasp"]
hi = strList[0][0]+strList[1][0]+strList[2][0]
print(hi)



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
