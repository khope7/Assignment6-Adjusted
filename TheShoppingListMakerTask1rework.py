#Task 1: Write a function that lets the user add items to a list.

#Writing code allowing users to add items to a list without printing

#Creating list function to add shopping items
def add_pocket_burners():
    pocket_burners = []

    while True:
        shopping_item = input("Enter a shopping item or type 'done' to finish: ")
        if shopping_item.lower() == 'done':
            break
        else:
            pocket_burners.append(shopping_item)

add_pocket_burners()