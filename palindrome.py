#create an empty list
list = []
#take user input
input = input("What is your word? ")
#set i to 0
i = 0

#create abstraction function
def abstraction(n):
    #set initial number of vowels to 0
    numofvowels = 0
    #put user input into list
    list.append(input)
    #turn all letters into lowercase
    input.lower()
    #find length of input
    length = len(input)
    #count number of vowels
    for i in range (length):
        if input[i] == "a" or input[i] == "e" or input[i] == "i" or input[i] == "o" or input[i] == "u":
            numofvowels = numofvowels + 1
        i += 1
    #make string backwards
    backwards = input[::-1]
    #strip spaces in the backwards string
    palindrome_back = backwards.replace(" ", "")
    #strip spaces in input
    no_spaces = input.replace(" ", "")
    #check if string is a palindrome
    if palindrome_back == no_spaces:
        print("The string is a palindrome")
    else:
        print("The string isn't a palindrome")

    #print statements
    print("The length of the string is", length)
    print("There are", numofvowels, "number of vowels")
    print(backwards)

#call function
abstraction(input)
