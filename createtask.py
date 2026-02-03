"""def manage_inventory(inventory):
    while True:
        action = input("Enter 'add' to add an item, 'remove' to remove an item, or 'display' to see the inventory: ")
        if action == 'add':
            item = input("Enter an item to add to the inventory: ")
            inventory.append(item)
        elif action == 'remove':
            item = input("Enter an item to remove from the inventory: ")
            if item in inventory:
                inventory.remove(item)
            else:
                print("Item not found in inventory.")
        elif action == 'display':
            print("Current inventory:")
            for item in inventory:
                print(item)
        else:
            print("Invalid action. Please try again.")

def mainFunction():
    inventory = []
    manage_inventory(inventory)

if __name__ == "__main__":
    mainFunction()"""

def count(inventory):
    erasercount = inventory.count("erasers")
    staplercount = inventory.count("staplers")
    papercount = inventory.count("paper")
    pencilcount = inventory.count("pencils")
    print("You have", erasercount, "erasers,", staplercount, "stapler(s),", papercount, "piece(s) of paper, and", pencilcount, "pencil(s).")

def action(inventory):
    add_more = "No"
    while add_more.lower() == "no":
        user_input = input("Welcome to your classroom inventory! Enter 'add' to add an item, 'remove' to remove an item, or 'display' to view your inventory: ")
        if user_input.lower() == 'add':
            item = input("Which item would you like to add? (erasers, staplers, paper, pencils): ")
            inventory.append(item)
        elif user_input.lower() == 'remove':
            item = input("Which item would you like to remove? (erasers, staplers, paper, pencils): ")
            if item in inventory:
                inventory.remove(item)
            else:
                print("That item is not in your inventory")
        elif user_input.lower() == 'display':
            print("Your inventory:")
            for item in inventory:
                print(item)
        else:
            print("Unable to process that action. Please try again")
        add_more = input("Are you done editing your inventory? (Yes/No): ")
    count(inventory)

def mainFunction():
    inventory = []
    action(inventory)

mainFunction()
