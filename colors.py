original_colors = []
new_colors = []

def replace_word():
    target = input("Enter a target word: ")
    replace = input("Enter a replace word: ")
    replacements = 0

    for x in original_colors:
        new_colors.append(x)

        if x == target:
            new_colors.remove(x)
            new_colors.append(replace)
            replacements += 1

        else:
            continue

    print("The number of replacements are:  %s" % replacements)
    print("Here is the original list:  %s" % original_colors)
    print("Here is the new list:  %s" % new_colors)

def welcome():
    print("Welcome to this color thang!")

    while True:
        inp = input("Enter a color! Type 'STOP' to quit:  ")

        if inp.lower() == "stop":
            break

        original_colors.append(inp)

welcome()
replace_word()
