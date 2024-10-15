#Task 3: Add a function that prints out the entire list in a formatted way.

#Copying code from TheShoppingListMakerTask2

#Instantiating list outside of functions
pocket_burners = []

#Creating list function to add shopping items
def add_pocket_burners():
    while True:
        shopping_item = input("Enter a shopping item or type 'done' to finish: ")
        if shopping_item.lower() == 'done':
            break
        else:
#Adding title function for formatting
            pocket_burners.append(shopping_item.title())

#Creating code to remove items from the list that catches incorrect entries and reruns loop until done break without printing
def remove_pocket_burners():
    while True:
        try:
            remove_item = input("Is there an item you would like to remove? Please enter item, if not type 'done' to finish: ")
            remove_item = remove_item.title()
            if remove_item.lower() == 'done':
                break
            else:
                pocket_burners.remove(remove_item)
        except ValueError:
            print("Apologies, entry must be an item you have entered.")

#Creating function that prints out the entire list in a formatted way
def run_then_full_print():
#Calling both pocket burner functions to add and remove
    add_pocket_burners()
    remove_pocket_burners()
#Formatting list and printing
    print("Thank you, here is your updated list: ")
#Created list as str instantiating every item to a new line https://stackoverflow.com/questions/37372603/how-to-remove-specific-substrings-from-a-set-of-strings-in-python for reference
    print("\n".join(pocket_burners))

#Calling run and print function
run_then_full_print()