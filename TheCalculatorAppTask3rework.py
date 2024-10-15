#Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.

#Copying code from TheCalculatorAppTask1reworkTask2

#Creating code to introduce user input
def main_menu():
    while True:
#Aware of improper greeting, future user read messages will be generalized
        choice = input("Hello Coding Master Erazo, what operation would you like to perform today?  Please choose: addition, subtraction, multiplication, or division: \n")

        if choice.lower() != "addition" and choice.lower() != "subtraction" and choice.lower() != "multiplication" and choice.lower() != "division":
            print("Unable to proceed, choice must be one of the mentioned operations. Please try again.")

        elif choice.lower() == "addition":
            addition()
            break
        elif choice.lower() == "subtraction":
            subtraction()
            break
        elif choice.lower() == "multiplication":
            multiplication()
            break
        elif choice.lower() == "division":
            division()
            break

#Defining Addition, converting string entries to float and printing
def addition():
#Created while loop to allow for user entry upon user non-entry
    while True:
#Created try except function to handle non-entry errors
        try:
            a = float(input("What is the first number you would like to add? \n"))
            b = float(input("What is the second number you would like to add? \n"))
            addition = (a + b)
            print(f"Here is the addition of your two numbers:" , f"{addition:.2f}")
            break
        except ValueError:
            print("Unable to proceed, your first choice must be a number. Please try again.")        

#Defining Subtraction, converting string entries to float and printing
def subtraction():
    while True:
#Created try except function to handle non-entry errors
        try:
            a = float(input("What is the first number you would like to subtract? \n"))
            b = float(input("What is the second number you would like to subtract? \n"))
            subtraction = (a - b)
            print(f"Here is the subtraction of your two numbers:" , f"{subtraction:.2f}")
            break
        except ValueError:
            print("Unable to proceed, your first choice must be a number. Please try again.") 

#Defining multiplication, converting string entries to float and printing
def multiplication():
    while True:
#Created try except function to handle non-entry errors
        try:
            a = float(input("What is the first number you would like to multiply? \n"))
            b = float(input("What is the second number you would like to multiply? \n"))
            multiplication = (a * b)
            print(f"Here is the multiplication of your two numbers:" , f"{multiplication:.2f}")
            break
        except ValueError:
            print("Unable to proceed, your first choice must be a number. Please try again.") 

#Defining division, converting string entries to float and printing
def division():
    while True:
#Created try except function to handle non-entry errors
        try:
            a = float(input("What is the first number you would like to divide? \n"))
            b = float(input("What is the second number you would like to divide? \n"))
#Including catch statement for user entry 0 for b
            if b == 0.0 and b == 0:
                print("Cannot divide by zero, yet. (perhaps if the world could agree on a variable specific to this equation then the answer would have a value... and break everything of course!)")
            else:
                division = (a / b)
                print(f"Here is the division of your two numbers:" , f"{division:.2f}")
                break
        except ValueError:
            print("Unable to proceed, your first choice must be a number. Please try again.")    

#Calling main_menu function to run
main_menu()