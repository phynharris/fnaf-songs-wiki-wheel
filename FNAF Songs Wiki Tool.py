import random

"""
    Desc:
        - Validates integer input.
    Parameters:
        - test_string: The string being tested.
    Returns:
        - int(test_string): If the test_string is valid, it will return it as an int, otherwise it returns as False.
"""


def validNumber(test_string):
    # Base Case: test_string may neither be blank nor 0.
    if test_string == "" or test_string == "0":
        print("Error - Please enter a number. ")
        return False

    # Tests each character in test_string.
    # If a character is not a number, then it returns False.
    for character in test_string:
        if character not in NUMBERS:
            print("Error - That is not a valid number. ")
            return False

    return int(test_string)


"""
    Desc:
        - Reads the "song_creators.txt" file and puts each element into a list.
    Parameters:
        - None
    Returns:
        - pick_list: The list of creators.
"""


def creatorList():
    # Lists
    pick_list = []

    # Puts all creators in the txt file into a list.
    with open("song_creators.txt") as pick_creators_file:
        for creator in pick_creators_file:
            pick_list.append(creator.strip("\n"))

    return pick_list


"""
    Desc:
        - This function selects random creators from the song_creators.txt file and prints them for the user.
    Parameters:
        - Nothing
    Returns:
        - A list of creators turned into a string.
"""


def pickCreator():
    # Lists
    pick_creator_list = creatorList()
    creators_list = []

    # Asks the user to enter how many creators they want.
    pick_amount = validNumber(input("How many do you want to pick? "))
    while not pick_amount:
        print("Error. Invalid input.")
        pick_amount = validNumber(input("How many do you want to pick? "))

    # The number of creators selected is based on the pick_amount the user requested.
    for x in range(pick_amount):
        creator = random.randint(0, len(pick_creator_list) - 1)
        creators_list.append(pick_creator_list[creator])

    return "\n- ".join(creators_list)


"""
    Desc:
        - Strips the X's off of song_attributes if 9 or more of them have X's.
    Parameters:
        - att_list: The list of attributes
    Returns:
        - Nothing
"""


def stripX(att_list):
    # Variables
    X_counter = 0
    limit = (len(att_list) * 9) // 14

    # Counts the number of X-tagged attributes.
    for attribute in att_list:
        if attribute[0] == "X":
            X_counter += 1

    # If the number of tagged attributes exceeds the limit, the X's are stripped.
    if X_counter >= limit:
        for x in range(len(att_list)):
            if att_list[x][0] == "X":
                att_list[x] = att_list[x].strip("X ")

    return


"""
    Desc:
        - Reads the song_attributes.txt file.
        - Puts each line into a list of attributes.
    Parameters:
        - Nothing
    Returns:
        - att_list: The (newly created) list of attributes
"""


def readAttFile():
    # Lists
    att_list = []

    # Puts each line into att_list.
    with open("song_attributes.txt", "r") as attribute_file:
        for line in attribute_file:
            att_list.append(line.strip("\n"))

    # Calls the strip_X function which determines if the attribute list needs to be reset.
    stripX(att_list)

    return att_list


"""
    Desc:
        - Adds an X to the front of a selected attribute.
    Parameters:
        - att_list: The list of attributes.
        - picked_attribute: The attribute being amended in the list.
    Returns:
        - Nothing
"""


def appendX(att_list, picked_attribute):
    # Cycles through the attribute list until it finds the picked attribute.
    # Once found, appends an "X " to the front of it.
    for z in range(len(att_list)):
        if picked_attribute == att_list[z]:
            att_list[z] = "X " + att_list[z]
            return


"""
    Desc:
        - Picks as many attributes as the user requested.
    Parameters:
        - att_list: The list of attributes.
        - pick_amount: The amount of attributes the user wants.
    Returns:
        - pick_list: The list of attributes that have been picked.
"""


def attPicker(att_list, pick_amount):
    try:
        pick_amount = int(pick_amount)
    except ValueError:
        return

    # Lists
    pick_list = [''] * pick_amount

    # For-Loop that goes as long as the pick_amount.
    for x in range(pick_amount):
        # The attribute picked is randomly selected.
        # If the user must select an int.
        pick_list[x] = att_list[random.randint(0, len(att_list) - 1)]
        while pick_list[x][0] == "X":
            pick_list[x] = att_list[random.randint(0, len(att_list) - 1)]

        # Appends an "X " in front of the selected attribute.
        appendX(att_list, pick_list[x])

        # Checks if the attribute list needs to be reset.
        stripX(att_list)

    return pick_list


"""
    Desc:
        - Rewrites the song_attributes.txt file.
    Parameters:
        - att_list: The list of attributes.
    Returns:
        - Nothing
"""


def rewriteAttFile(att_list):
    # Opens the song_attributes.txt file in write mode.
    with open("song_attributes.txt", "w") as att_file:
        # Writes each attribute as its own line in the file.
        for attribute in att_list:
            att_file.writelines(attribute + "\n")


"""
    Desc:
        - Fetches song attributes for the user.
    Parameters:
        - Nothing
    Returns:
        - att_list: The list of selected song attributes - it is joined with ", ".
"""


def pickSong():
    # First prompts the user for how many attributes they want.
    # They must enter an int larger than 0.
    pick_amount = input("How many attributes do you want? ")
    while not validNumber(pick_amount):
        pick_amount = input("How many attributes do you want? ")
    # pick_amount = int(pick_amount)

    # Creates a list of song attributes.
    attributes_list = readAttFile()

    # Picks the attributes for the user.
    picked_att = attPicker(attributes_list, pick_amount)

    # Rewrites the song_attributes.txt file.
    rewriteAttFile(attributes_list)

    return ", ".join(picked_att)


"""
    Desc:
        - Used for re-ordering the list of song creators in abc order.
        - Compares each creator to each one in the list recursively.
    Parameters:
        - unordered_list: The unordered list of song creators.
        - index: Tracks where the function's position is in the unordered_list.
            - Defaulted to 0.
    Returns:
        - Base Case: If the current highest-value creator remains as so, then it is returned.
        - highest_creator: The creator with the lowest character value is set to the highest position in the file.
"""


def orderCreators(unordered_list, index=0):
    highest_creator = unordered_list[index]

    if len(unordered_list[0]) == 1:
        return unordered_list[index]

    for y in range(len(unordered_list)):
        if unordered_list[index].lower() > unordered_list[y].lower():
            highest_creator = orderCreators(unordered_list, y)

    return highest_creator


"""
    Desc:
        - Reorganizes song creators into abc order.
        - Overwrites the song_creators.txt file with the list.
    Parameters:
        - Nothing
    Returns:
        - Nothing
"""


def reorganizeCreators():
    red_creator_list = []
    reordered_list = []

    read_creators = open("song_creators.txt")
    for name in read_creators:
        fixed_name = ""

        for letter in name:
            fixed_name += letter.strip("\n")

        red_creator_list.append(fixed_name)

    read_creators.close()

    while red_creator_list:
        creator = orderCreators(list(red_creator_list))
        reordered_list.append(creator)
        red_creator_list.remove(creator)

    with open("song_creators.txt", "w") as rewrite_creators:
        for creator in reordered_list:
            rewrite_creators.writelines(creator + "\n")


"""
    Desc:
        - Picks random numbers for the user.
    Parameters:
        - Nothing.
    Returns:
        - A string of numbers joined together by commas.
"""


def pickNumbers():
    # Variables
    rand_list = []

    bound = validNumber(input("What is your bound? "))
    while not bound:
        bound = validNumber(input("What is your bound? "))

    iterations = validNumber(input("How many random numbers do you want? "))
    while not iterations:
        iterations = validNumber(input("How many random numbers do you want? "))

    for i in range(iterations):
        rand_list.append(str(random.randint(1, bound)))

    return ", ".join(rand_list)


"""
    Desc:
        - Adds new song creators to the song_creator.txt file.
    Parameters:
        - Nothing
    Returns:
        - Nothing
"""


def appendCreator():
    # Lists
    creators_list = creatorList()
    for x in range(len(creators_list)):
        creators_list[x] = creators_list[x].lower()

    # Open File
    creators_file = open("song_creators.txt", "a")

    new_creator = input("Who are you adding to the list? ")
    while not (new_creator.lower() == "quit" or new_creator.lower() == "q" or new_creator == ""):
        # Will not add creators who are already in the list.
        if new_creator.lower() not in creators_list:
            creators_file.write(new_creator + "\n")
            print(f"Added {new_creator}")
        else:
            print(f"{new_creator} is already in the list.")
        new_creator = input("Who are you adding to the list? ")

    # Close and Reoganize File
    creators_file.close()
    reorganizeCreators()


if __name__ == "__main__":
    # Lists
    ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
                                                        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    # Variables
    wheel = ""

    while wheel != "quit":
        wheel = input("\n1. Get creators (c) "
                      "\n2. Get song attributes (s) "
                      "\n3. Get random number (r) "
                      "\n4. Append into the file (a)"
                      "\n5. Quit (q)"
                      "\nEnter Here: ").lower()

        # If the user selects "creator", then it prints out a random creator from the list.
        if wheel == "creator" or wheel == "c":
            print("Your creator(s) are:\n- " + pickCreator())

        # If the user selects "song", then they must also enter how many attributes they want, and that they
        # shall receive.
        elif wheel == "song" or wheel == "s":
            print("The song theme is:", pickSong())

        # If the user selects "random", then they must enter two bounds (lower, then upper).
        # Then, they select how many random numbers they want, and it gives them to the user.
        elif wheel == "random" or wheel == "r":
            print("Your random number(s) is:", pickNumbers())

        elif wheel == "append" or wheel == "a":
            appendCreator()

        # Quits the program
        elif wheel == "quit" or wheel == "q":
            wheel = "quit"

        # If the input matches none of the above, then the user is given error and forced to retry.
        else:
            print("Error.")