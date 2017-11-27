import time

# Todo list
todolst = []

# HELP function
def instruct():
    outline()
    print("This is a program that will help you create a todo list! :)")
    outline()

# ADD function
def addone():
    outline()
    lst = input("What would you like to add to the list?" '\n'
    "> ")
    todolst.append(lst)
    outline()

# DELETE function
def delete():
    outline()
    view()
    rm_item = input("What would you like to remove?: ")
    todolst.remove(rm_item)
    outline()

# VIEW function; # Allow user to view todo list
def view():
    outline()
    position = 1
    print("Here is your list:")

    for item in todolst:
        print("%s. %s" % (position, item))
        position += 1

    outline()

# DONE function
def done():
    outline()
    print("BYE!!!!")
    outline()
    quit()


# Print Blank Lines function
def pb():
    print(" " * 6)

def outline():
    print("=" * 80)

# Welcome message for todos; create function
while True:

    inp = input("Welcome to the TODO Program!" '\n'
    '\n'
    "Here's a list of commands you can type at the prompt." '\n'
    '\n'
    "Type 'HELP' for helpful instructions." '\n'
    "Type 'CREATE' to create a new todo list." '\n'
    "Type 'ADD' to add a todo to an existing list." '\n'
    "Type 'DELETE' to delete an item for the list" '\n'
    "Type 'VIEW' to view your list" '\n'
    "Type 'DONE' to quit." '\n'
    '\n'
    "What would you like to do:" '\n'
    "> ")

    if inp.lower() == "help":
        pb()
        instruct()
        time.sleep(4)
        continue

    elif inp.lower() == "done":
        pb()
        done()

    elif inp.lower() == "add":
        pb()
        addone()
        time.sleep(1)
        continue

    elif inp.lower() == "delete":
        pb()
        delete()
        view()
        time.sleep(4)
        continue

    elif inp.lower() == "view":
        pb()
        view()
        time.sleep(4)
        continue

    else:
        outline()
        outline()
        print("Please type a command I understand.")
        outline()
        outline()
        time.sleep(4)
        continue
