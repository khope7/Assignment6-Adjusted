#Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

#Copying code from TheCalculatorAppTask1reworkTask1


#Defining main_menu to introduce user input
def main_menu():
#Creating while loop to catch for non-entries
    while True:
        choice = input("Hello Coding Master Erazo, what operation would you like to perform today?  Please choose: addition, subtraction, multiplication, or division: \n")
#Creating if elif statement to catch correct and incorrect entries
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
    a = float(input("What is the first number you would like to add? \n"))
    b = float(input("What is the second number you would like to add? \n"))
    addition = (a + b)
    print(f"Here is the addition of your two numbers:\n" + f"{addition:.2f}")       

#Defining Subtraction, converting string entries to float and printing
def subtraction():
    a = float(input("What is the first number you would like to subtract? \n"))
    b = float(input("What is the second number you would like to subtract? \n"))
    subtraction = (a - b)
    print(f"Here is the subtraction of your two numbers:\n" + f"{subtraction:.2f}")

#Defining Multiplication, converting string entries to float and printing
def multiplication():
    a = float(input("What is the first number you would like to multiply? \n"))
    b = float(input("What is the second number you would like to multiply? \n"))
    multiplication = (a * b)
    print(f"Here is the multiplication of your two numbers:\n" + f"{multiplication:.2f}")

#Defining Division, converting string entries to float and printing
def division():
    a = float(input("What is the first number you would like to divide? \n"))
    b = float(input("What is the second number you would like to divide? \n"))
    division = (a / b)
    print(f"Here is the division of your two numbers:\n" + f"{division:.2f}")

#Calling main_menu function to run
main_menu()