#create empty list
myList = []

#add inital items into empty list using append method
myList.append(76)
myList.append(92.3)
myList.append("hello")

#add inital items into empty list using concatenation
#create list for the last three items
lastThree = [True, 4, 76]
myList = myList + lastThree

#append "apple" and 76
myList.append("apple")
myList.append(76)

#insert the value of "cat" as the 3rd item
#insert the value 99 as the first item
myList.insert(2,"cat")
myList.insert(0, 99)

#find the position of "hello"
myList.index("hello")
numOf76 = myList.count(76)

#remove the first occurance of 76
myList.remove(76)

#remove True from the lsit
positionOfTrue = myList.index(True)
myList.pop(positionOfTrue)

#print statements
print(myList)
print("76 occurs", numOf76, "times")
