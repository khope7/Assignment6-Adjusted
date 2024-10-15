#Task 2: Include a function to remove items from the list.

#Copying code from TheShoppingListMakerTask1

#Creating list function to add shopping items
pocket_burners = []

def add_pocket_burners():
    while True:
        shopping_item = input("Enter a shopping item or type 'done' to finish: ")
        if shopping_item.lower() == 'done':
            break
        else:
            pocket_burners.append(shopping_item)

#Creating code to remove items from the list that catches incorrect entries and reruns loop until done break without printing
def remove_pocket_burners():
    while True:
        try:
            remove_item = input("Is there an item you would like to remove? Please enter item, if not type 'done' to finish: ")
            if remove_item.lower() == 'done':
                break
            else:
                pocket_burners.remove(remove_item)
        except ValueError:
            print("Apologies, entry must be an item you have entered.")


add_pocket_burners()

remove_pocket_burners()