#!/usr/bin/env python3
# Can't think of what to wear today?
# Input your wardrobe and 

# Find is hard-coded for first category only, needs to be able to search all
# Delete is not functional, yet
# svg file or database may work better than a 2D list for wardrobe

import random

# List clothing
def list(clothing):
    if len(clothing) == 0:
        print("There are no clothes in your wardrobe.\n")
        return
    else:
        for row in clothing:
            print(row)
        
# Add clothing
def add(clothing):
    more = input("Would you like to add a wardrobe piece (top or bottom)? (y/n) ")
    while more.lower() == "y":
        toporbottom = input("Top or bottom? (t/b) ")
        if toporbottom.lower() == "t": 
            description = input("Description: ")
            clothing[0].append(description)
            more = input("Would you like to enter another wardrobe piece? (y/n) ")
        elif toporbottom.lower() == "b":
            description = input("Description: ")
            clothing[1].append(description)
            more = input("Would you like to enter another wardrobe piece? (y/n) ")
    extra = input("Would you like to enter shoes or outerwear (such as a coat, hat or scarf)? (y/n) ")
    while extra.lower() == "y":
        shoeorcoat = input("Shoes or Outerwear? (s/o) ")
        if shoeorcoat.lower() == "s":
            description = input("Description: ")
            clothing[2].append(description)
            extra = input("Would you like to enter more? (y/n) ")
        else:
            description = input("Description: ")
            clothing[3].append(description)
            extra = input("Would you like to enter more? (y/n) ")

# Pick clothing
def pick(clothing):
    choice = input("Would you like a suggestion of what to wear today? (y/n): ")
    while choice.lower() == "y":
        print()
        print("Clothing Selection:")
        print()
        top = random.randint(0, len(clothing[0])-1)
        print (clothing[0][top])
        bottom = random.randint(0, len(clothing[1])-1)
        print(clothing[1][bottom])
        shoes = random.randint(0, len(clothing[2])-1)
        print(clothing[2][shoes])
        outer = random.randint(0, len(clothing[3])-1)
        print(clothing[3][outer])
        print()
        choice = input("Would you like another suggestion? (y/n): ")

# Find clothing
def find(clothing):
    search = input("Enter single search word: ")
    s = []
    s = [s for s in clothing[0] if search in s]
    print(s)

    #print(clothing.index(str_match))
    search = input("Enter additional search word: ")
    next_match = [s for s in clothing[0] if search in s]
    print(next_match)
    print()

# Display command options
def display_commands():
    print("COMMAND CENTER")
    print("List - List clothing")
    print("Add - Add clothing")
    print("Find - Find clothing")
    print("Del - Delete clothing")
    print("Pick - Pick an outfit")
    print("Exit - Exit program")
    
def main():
    print()
    print("      Welcome to")
    print("WHAT SHOULD I WEAR TODAY?")
    print("   Clothing Selector")
    print()
    clothing = [["red t-shirt", "white button down", "black t-shirt", "plaid flannel shirt", "grey sweater", "pink button down", "blue blouse"],
                ["jeans", "shorts", "navy skirt", "chinos", "black dress pants", "leggings"],
                ["Doc Martens", "running shoes", "sandals", "heeled sandals", "ballet flats", "moccasins", "cowboy boots", "Mary Janes"],
                ["cowboy hat", "jean jacket", "vest", "scarf", "cardigan", "beret", "newsboy cap"]] 
    
    display_commands()
    
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list(clothing)
        elif command.lower() == "add":
            add(clothing)
        elif command.lower() == "pick":
            pick(clothing)
        elif command.lower() == "find":
            find(clothing)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")

    print("\n Thanks, Bye!\n")

if __name__ == "__main__":
    main()