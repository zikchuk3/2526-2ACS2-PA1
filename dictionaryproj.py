'''
Author: Zikora C
Program Title: Create your mod schedule!
Program desc: You can go to Mrs. Carroll's office and drop, add, or change a class/d-block/e-block.
resources:

::::::Reflection:::::
problems I faced:
- I struggled with making the schedule at first because I wanted to randomize it, I figured that out and put in the block comments what I did (I basically just did a for loop in range(7) with the dictionary instead of 7 different dictionaries and that helped a lot with future things)
- I struggled with making the add_class function at first because I needed to figure out how to put the user_input in the dictionary place, I had to do < block_names = f"{block} Block" > so that when I call the dictionary like this < schedule[mod - 1][block_names] > it puts the class in
- I wanted to restart the code and save the schedule, and I figured out that I can set the schedule to None so the first time it gives a new one, but when it restarts it will have the same one (see main function)

what I'm proud of:
- I am proud of doing so much so comfortably, I did not have to look up much stuff as compared to CS1 because I learned a lot
- having patience to do this
- being able to make the schedule eventually because that took up a lot of time

what I would add/change:
- I would organize it by grade so I could add co-curric
- I would stylize it more because this time I didn't get to space it out and make it more visually appealing
  - I would also import time so it can flow better
- there must be an easier way to do some of the things I did, so I would do that

Pledge: I have never given nor received external help on this assignment,
with the exception of the following sources:
.items(): https://www.w3schools.com/python/ref_dictionary_items.asp
enumerate(): https://www.w3schools.com/python/ref_func_enumerate.asp
set(): https://www.w3schools.com/python/python_sets.asp
add(): https://www.w3schools.com/python/ref_set_add.asp
flatten a list: https://www.geeksforgeeks.org/python/python-flatten-list-to-individual-elements/
None keyword: https://www.w3schools.com/python/ref_keyword_none.asp
Google - https://www.google.com
'''

import random
#deleted this
'''
#mods
mod1 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "D Block": "",
    "E Block": ""
}
mod2 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "D Block": "",
    "E Block": ""
}
mod3 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "D Block": "",
    "E Block": ""
}
mod4 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "D Block": "",
    "E Block": ""
}
mod5 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "D Block": "",
    "E Block": ""
}
mod6 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "D Block": "",
    "E Block": ""
}
mod7 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "D Block": "",
    "E Block": ""
}
'''
#lists of classes d blocks and e blocks
classes_list_english = ["ENGLISH I", "ENGLISH II", "ENGLISH III", "ENGLISH IV"]
classes_list_math = ["GEOMETRY", "ALGEBRA I", "ALGEBRA II", "PRE-CALCULUS", "CALCULUS AB", "CALCULUS BC", "STATISTICS", "LINEAR ALGEBRA", "DIFFERENTIAL EQUATIONS"]
classes_list_history = ["GLOBAL I", "GLOBAL II", "AMERICAN HISTORY"]
classes_list_science = ["BIOLOGY", "CHEMISTRY", "PHYSICS", "AP BIOLOGY", "AP CHEMISTRY", "AP PHYSICS"]
#co_curric = ["SOPHOMORE CO-CURRIC", "JUNIOR CO-CURRIC", "SENIOR CO-CURRIC"]
classes_list_languages = ["SPANISH I", "SPANISH II", "SPANISH III", "SPANISH IV", "FRENCH I", "FRENCH II", "FRENCH III", "FRENCH IV", "LATIN I", "LATIN II", "LATIN III", "LATIN IV", "AP SPANISH", "AP FRENCH", "AP LATIN"]
electives = ["FREE", "ADMISSIONS", "LIBRARY HELPER", "CS1", "CS2", "CS3", "DIGITAL ART & ANIMATION", "DRAWING", "PAINTING", "ART SEMINAR", "COMPUTER SCIENCE SEMINAR", "ROBOTICS", "PUBLIC SPEAKING", "FIBERS & FASHION", "PHOTOGRAPHY", "SPORTS PSYCHOLOGY", "CERAMICS", "HISTORY CAPSTONE SEMINAR", "RESEARCH SEMINAR"]
d_blocksF = ["FIELD HOCKEY", "SWIMMING FOR CONDITIONING", "CROSS COUNTRY", "SOCCER", "TENNIS", "VOLLEYBALL", "YEARBOOK", "ADVANCED FITNESS", "STAGECRAFT", "FALL PLAY"]
d_blocksW = ["BASKETBALL", "ROCK CLIMBING", "SWIM", "MODEL UN", "ADVANCED FITNESS", "YEARBOOK", "STAGECRAFT", "WINTER MUSICAL"]
d_blocksS = ["TRACK & FIELD", "TENNIS", "SOFTBALL", "LACROSSE", "ADVANCED FITNESS", "NATURE WALKS"]
e_blocks = ["CHORUS", "ORCHESTRA"]

#made an empty list/dictionary like this using a for loop because it I needed to call mods instead of 7 different mods
mods = []
for i in range(7):
    mods.append({
        "A Block": "",
        "B Block": "",
        "C Block": "",
        "D Block": "",
        "E Block": ""
    })

#making the schedule
def make_schedule():
    #so that the classes only show 3 times
    used_blocks = {}
    for i in range(7):
        # set is store multiple items in one variable, and I need to put the used classes somewhere
        used_blocks[i] = set() 


    classes = {
    #random choice of classes/dblocks for schedules 
    #will just make electives and e blocks add-able
    "english": random.choice(classes_list_english),
    "math": random.choice(classes_list_math),
    "history": random.choice(classes_list_history),
    "science": random.choice(classes_list_science),
    "lang": random.choice(classes_list_languages),
    }

    #random choice for d blocks and e block
    fall = random.choice(d_blocksF)
    winter = random.choice(d_blocksW)
    spring = random.choice(d_blocksS)
    ebs = random.choice(e_blocks)

    #to make a mod/block pair, then shuffle, and assign a class to that pair and in range(7) for each mod
    blocks = []
    for mod in range(7):
        for block in ["A Block", "B Block", "C Block"]:
            blocks.append((mod, block))
    random.shuffle(blocks)

    #classe because I can't use class
    #items is to get one of the subjects in classes dictionary
    for subject, classe in classes.items():
        used = 0
        while used < 3:
            mod, block = random.choice(blocks)
            #if the subject has not been used (3 times) and the mod.block pair is empty, add a class, add that class to used blocks, remove it from the blocks list, and do +1 used for that subject and class
            if subject not in used_blocks[mod] and mods[mod][block] == "":
                mods[mod][block] = classe
                used_blocks[mod].add(subject)
                blocks.remove((mod, block))
                used += 1

    #to give random elective
    for mod, block in blocks:
        mods[mod][block] = "Free"

    #enumerate takes an iterable (object that can be looped) and loops it at a certain start
    #this is so the mods list of dictionary starts at index 1 (but that index is technically 0 its just named 1) and just makes it easier 
    for i, mod in enumerate(mods, start=1):
        if i <= 2:
            mod["D Block"] = fall
        elif i <= 5:
            mod["D Block"] = winter
        else:
            mod["D Block"] = spring

        mod["E Block"] = ebs

    return mods

numbers = ["1", "2", "3", "4", "5", "6", "7"]

#add class
def add_class(schedule):
    #user says what they want to add
    mod_input = input("What mod would you like to add to? Enter a number 1-7: ")
    while mod_input in numbers:
        mod = int(mod_input)
        break
    else: 
        print("Invalid. Enter a number")
        mod = input("What mod would you like to add to? Enter a number 1-7: ")

    block = input("What block would you like to add to? Enter the letter of the block: ").upper()
    # so it can connect back to the dictionary
    valid_blocks = ["a", "A", "B", "b", "C", "c", "D", "d", "E", "e"]
    block_names = f"{block} Block"
    while block not in valid_blocks:
        print("Error. Please pick enter: 'A', 'B', 'C', 'D', or 'E' !")
        block = input("What block would you like to add to? Enter the letter of the block: ").upper()
    if block == "a" or block == "A" or block == "B" or block == "b" or block == "C" or block == "c":
        #had to do the mod - 1 because of the way index works 
        if schedule[mod - 1][block_names] == "Free":
            added_class = input(f"Enter the name of the class you want to add to {block} Block: ").upper()
            valid_classes_list = [classes_list_english, classes_list_history, classes_list_languages, classes_list_math, classes_list_science, electives]
            # had to flatten the list
            valid_classes = [x for sublist in valid_classes_list for x in sublist]
            while added_class not in valid_classes:
                print("Error. Please pick enter a valid class !")
                print(f"Here is the course calendar if you need reminding: {valid_classes}.")
                added_class = input(f"Enter the name of the class you want to add to {block} Block: ").upper()
            schedule[mod - 1][block_names] = added_class
            print(f"You added {added_class} to Mod {mod}, {block} Block. ") 
        else:
            print(f"You already have a class in Mod {mod}, {block} Block! ")
        return schedule
    
    #I made this here but realized I might not even need it because it is already full
    elif block == "D" or block == "d":
        added_sport = input(f"Enter the name of the sport you want to add to your Fall/Winter/Spring {block} Block: ").upper()
        schedule[mod - 1][block_names] = added_class
        if mod == 1:
            valid_sports_listF = [d_blocksF]
            valid_sportsF = [x for sublist in valid_sports_listF for x in sublist]
            while added_sport not in valid_sportsF:
                print("Error. Please pick enter a valid Fall sport !")
                print(f"Here are the fall sports if you need reminding: {valid_sportsF}.")
                added_sport = input(f"Enter the name of the sport you want to add to your Fall {block} Block: ").upper()
            schedule[mod][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You added {added_sport} to Mod your Fall {block} Block. ") 
            return schedule
        if mod == 2:
            valid_sports_listF = [d_blocksF]
            valid_sportsF = [x for sublist in valid_sports_listF for x in sublist]
            while added_sport not in valid_sportsF:
                print("Error. Please pick enter a valid Fall sport !")
                print(f"Here are the fall sports if you need reminding: {valid_sportsF}.")
                added_sport = input(f"Enter the name of the sport you want to add to your Fall {block} Block: ").upper()
            schedule[mod - 2][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You added {added_sport} to your Fall {block} Block. ")
            return schedule
        if mod == 3:
            valid_sports_listW = [d_blocksW]
            valid_sportsW = [x for sublist in valid_sports_listW for x in sublist]
            while added_sport not in valid_sportsW:
                print("Error. Please pick enter a valid Winter sport !")
                print(f"Here are the winter sports if you need reminding: {valid_sportsW}.")
                added_sport = input(f"Enter the name of the sport you want to add to your Winter {block} Block: ").upper()
            schedule[mod + 1][block_names] = added_sport
            schedule[mod][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You added {added_sport} to your Winter {block} Block. ") 
            return schedule
        if mod == 4:
            valid_sports_listW = [d_blocksW]
            valid_sportsW = [x for sublist in valid_sports_listW for x in sublist]
            while added_sport not in valid_sportsW:
                print("Error. Please pick enter a valid Winter sport !")
                print(f"Here are the winter sports if you need reminding: {valid_sportsW}.")
                added_sport = input(f"Enter the name of the sport you want to add to your Winter {block} Block: ").upper()
            schedule[mod - 2][block_names] = added_sport
            schedule[mod][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You added {added_sport} to your Winter {block} Block. ") 
            return schedule
        if mod == 5:
            valid_sports_listW = [d_blocksW]
            valid_sportsW = [x for sublist in valid_sports_listW for x in sublist]
            while added_sport not in valid_sportsW:
                print("Error. Please pick enter a valid Winter sport !")
                print(f"Here are the winter sports if you need reminding: {valid_sportsW}.")
                added_sport = input(f"Enter the name of the sport you want to add to your Winter {block} Block: ").upper()
            schedule[mod - 3][block_names] = added_sport
            schedule[mod - 2][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You added {added_sport} to your Winter {block} Block. ") 
            return schedule
        if mod == 6:
            valid_sports_listS = [d_blocksS]
            valid_sportsS = [x for sublist in valid_sports_listS for x in sublist]
            while added_sport not in valid_sportsS:
                print("Error. Please pick enter a valid Spring sport !")
                print(f"Here are the spring sports if you need reminding: {valid_sportsS}.")
                added_sport = input(f"Enter the name of the sport you want to add to your Spring {block} Block: ").upper()
            schedule[mod][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You added {added_sport} to your Spring {block} Block. ") 
            return schedule
        if mod == 7:
            valid_sports_listS = [d_blocksS]
            valid_sportsS = [x for sublist in valid_sports_listS for x in sublist]
            while added_sport not in valid_sportsS:
                print("Error. Please pick enter a valid Spring sport !")
                print(f"Here are the spring sports if you need reminding: {valid_sportsS}.")
                added_sport = input(f"Enter the name of the sport you want to add to your Spring {block} Block: ").upper()
            schedule[mod - 2][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You added {added_sport} to your Spring {block} Block. ") 
            return schedule


#change class
def change_class(schedule):
    #user says what they want to change
    mod_input = input("What mod would you like to change? Enter a number 1-7: ")
    while mod_input in numbers:
        mod = int(mod_input)
        break
    else: 
        print("Invalid. Enter a number")
        mod = input("What mod would you like to add to? Enter a number 1-7: ")

    block = input("What block would you like to change? Enter the letter of the block: ").upper()
    block_names = f"{block} Block"
    valid_blocks = ["a", "A", "B", "b", "C", "c", "D", "d", "E", "e"]
    while block not in valid_blocks:
        print("Error. Please pick enter: 'A', 'B', 'C', 'D', or 'E' !")
        block = input("What block would you like to change? Enter the letter of the block: ").upper()
    if block == "a" or block == "A" or block == "B" or block == "b" or block == "C" or block == "c":
        added_class = input(f"Enter the name of the class you want to change to your {block} Block: ").upper()
        valid_classes_list = [classes_list_english, classes_list_history, classes_list_languages, classes_list_math, classes_list_science, electives]
        # had to flatten the list
        valid_classes = [x for sublist in valid_classes_list for x in sublist]
        while added_class not in valid_classes:
            print("Error. Please pick enter a valid class !")
            print(f"Here is the course calendar if you need reminding: {valid_classes}.")
            added_class = input(f"Enter the name of the class you want to change to your {block} Block: ").upper()
        schedule[mod - 1][block_names] = added_class
        print(f"You changed your Mod {mod}, {block} Block to {added_class}. ") 
        return schedule
    #seperated the mods like this because it needed to be for each season not just the mod
    elif block == "D" or block == "d":
        added_sport = input(f"Enter the name of the sport you want to change to your Fall/Winter/Spring {block} Block: ").upper()
        if mod == 1:
            valid_sports_listF = [d_blocksF]
            valid_sportsF = [x for sublist in valid_sports_listF for x in sublist]
            while added_sport not in valid_sportsF:
                print("Error. Please pick enter a valid Fall sport !")
                print(f"Here are the fall sports if you need reminding: {valid_sportsF}.")
                added_sport = input(f"Enter the name of the sport you want to change to your Fall {block} Block: ").upper()
            schedule[mod][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You changed {added_sport} to your Fall {block} Block. ") 
            return schedule
        if mod == 2:
            valid_sports_listF = [d_blocksF]
            valid_sportsF = [x for sublist in valid_sports_listF for x in sublist]
            while added_sport not in valid_sportsF:
                print("Error. Please pick enter a valid Fall sport !")
                print(f"Here are the fall sports if you need reminding: {valid_sportsF}.")
                added_sport = input(f"Enter the name of the sport you want to change to your Fall {block} Block: ").upper()
            schedule[mod - 2][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You changed {added_sport} to your Fall {block} Block. ") 
            return schedule
        if mod == 3:
            valid_sports_listW = [d_blocksW]
            valid_sportsW = [x for sublist in valid_sports_listW for x in sublist]
            while added_sport not in valid_sportsW:
                print("Error. Please pick enter a valid Winter sport !")
                print(f"Here are the winter sports if you need reminding: {valid_sportsW}.")
                added_sport = input(f"Enter the name of the sport you want to change to your Winter {block} Block: ").upper()
            schedule[mod + 1][block_names] = added_sport
            schedule[mod][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You changed {added_sport} to your Winter {block} Block. ") 
            return schedule
        if mod == 4:
            valid_sports_listW = [d_blocksW]
            valid_sportsW = [x for sublist in valid_sports_listW for x in sublist]
            while added_sport not in valid_sportsW:
                print("Error. Please pick enter a valid Winter sport !")
                print(f"Here are the winter sports if you need reminding: {valid_sportsW}.")
                added_sport = input(f"Enter the name of the sport you want to change to your Winter {block} Block: ").upper()
            schedule[mod - 2][block_names] = added_sport
            schedule[mod][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You changed {added_sport} to your Winter {block} Block. ") 
            return schedule
        if mod == 5:
            valid_sports_listW = [d_blocksW]
            valid_sportsW = [x for sublist in valid_sports_listW for x in sublist]
            while added_sport not in valid_sportsW:
                print("Error. Please pick enter a valid Winter sport !")
                print(f"Here are the winter sports if you need reminding: {valid_sportsW}.")
                added_sport = input(f"Enter the name of the sport you want to change to your Winter {block} Block: ").upper()
            schedule[mod - 3][block_names] = added_sport
            schedule[mod - 2][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You changed {added_sport} to your Winter {block} Block. ") 
            return schedule
        if mod == 6:
            valid_sports_listS = [d_blocksS]
            valid_sportsS = [x for sublist in valid_sports_listS for x in sublist]
            while added_sport not in valid_sportsS:
                print("Error. Please pick enter a valid Spring sport !")
                print(f"Here is are the spring sports if you need reminding: {valid_sportsS}.")
                added_sport = input(f"Enter the name of the sport you want to change to your Spring {block} Block: ").upper()
            schedule[mod][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You changed {added_sport} to your Spring {block} Block. ") 
            return schedule
        if mod == 7:
            valid_sports_listS = [d_blocksS]
            valid_sportsS = [x for sublist in valid_sports_listS for x in sublist]
            while added_sport not in valid_sportsS:
                print("Error. Please pick enter a valid Spring sport !")
                print(f"Here is are the spring sports if you need reminding: {valid_sportsS}.")
                added_sport = input(f"Enter the name of the sport you want to change to your Spring {block} Block: ").upper()
            schedule[mod - 2][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You changed {added_sport} to your Spring {block} Block. ") 
            return schedule

#drop class
def drop_class(schedule):
    #user says what they want to drop
    mod_input = input("What mod would you like to drop something from? Enter a number 1-7: ")
    while mod_input in numbers:
        mod = int(mod_input)
        break
    else: 
        print("Invalid. Enter a number")
        mod = input("What mod would you like to add to? Enter a number 1-7: ")

    block = input("What block would you like to drop? Enter the letter of the block: ").upper()
    block_names = f"{block} Block"
    valid_blocks = ["a", "A", "B", "b", "C", "c", "D", "d", "E", "e"]
    while block not in valid_blocks:
        print("Error. Please pick enter: 'A', 'B', 'C', 'D', or 'E' !")
        block = input("What block would you like to drop? Enter the letter of the block: ").upper()
    if block == "a" or block == "A" or block == "B" or block == "b" or block == "C" or block == "c":
        current_class = schedule[mod - 1][block_names]
        schedule[mod - 1][block_names] = "Free"
        print(f"You dropped {current_class} from Mod {mod}, {block} Block. ") 
        return schedule
    #seperated the mods like this because it needed to be for each season not just the mod
    elif block == "D" or block == "d":
        if mod == 1:
            current_sport = schedule[mod - 1][block_names]
            schedule[mod][block_names] = "Free"
            schedule[mod - 1][block_names] = "Free"
            print(f"You dropped {current_sport} from your Fall {block} Block. ") 
            return schedule
        if mod == 2:
            current_sport = schedule[mod - 1][block_names]
            schedule[mod - 2][block_names] = "Free"
            schedule[mod - 1][block_names] = "Free"
            print(f"You dropped {current_sport} from your Fall {block} Block. ") 
            return schedule
        if mod == 3:
            current_sport = schedule[mod - 1][block_names]
            schedule[mod + 1][block_names] = "Free"
            schedule[mod][block_names] = "Free"
            schedule[mod - 1][block_names] = "Free"
            print(f"You dropped {current_sport} from your Winter {block} Block. ") 
            return schedule
        if mod == 4:
            current_sport = schedule[mod - 1][block_names]
            schedule[mod - 2][block_names] = "Free"
            schedule[mod][block_names] = "Free"
            schedule[mod - 1][block_names] = "Free"
            print(f"You dropped {current_sport} from your Winter {block} Block. ") 
            return schedule
        if mod == 5:
            current_sport = schedule[mod - 1][block_names]
            schedule[mod - 3][block_names] = "Free"
            schedule[mod - 2][block_names] = "Free"
            schedule[mod - 1][block_names] = "Free"
            print(f"You dropped {current_sport} from your Winter {block} Block. ") 
            return schedule
        if mod == 6:
            current_sport = schedule[mod - 1][block_names]
            schedule[mod][block_names] = "Free"
            schedule[mod - 1][block_names] = "Free"
            print(f"You dropped {current_sport} from your Spring {block} Block. ") 
            return schedule
        if mod == 7:
            current_sport = schedule[mod - 1][block_names]
            schedule[mod - 2][block_names] = "Free"
            schedule[mod - 1][block_names] = "Free"
            print(f"You dropped {current_sport} from your Spring {block} Block. ")
            return schedule

#copied from my hangman game lol
y_or_n = ["y", "n"]
def restart(schedule, choices = ["yes", "no"]):
    print("___________________________________________________________")
    player_input = input("Is there more you want to do? (y)es or (n)o: ").lower()
    while player_input not in choices:
        print("Invalid. Please enter ", choices, ".")
        player_input = input("Do you want to play again? (y)es or (n)o: ").lower()
    if player_input == "y":

        print("___________________________________________________________")
        print("                                                           ")
        print("                                                           ")
        print("                Okay, lets go back to the office....")
        print("                                                           ")
        print("                                                           ")
        print("___________________________________________________________")
        main(schedule)
    elif player_input == "n":
        print("                                                           ")
        print("Thanks for visiting!")
        print("        __________________๑ï")
        print("        ꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷")



def main(schedule = None):
    # I looked it up 
    # schedule = None so when I restart it can save the past schedule
    # if schedule = None it will create a new schedule, if not it saves the past schedule
    if schedule is None:
        schedule = make_schedule()

    #welcome in the offic 
    print("Welcome to Mrs. Caroll's office.")
    print("Here is your current schedule: ")
    for i, mod in enumerate(schedule, start=1):
        print()
        print(f"    Mod {i} ")
        for block, classe in mod.items():
            print(f"{block}: {classe}")


    user_input = input("Would you like to add, change, or drop a class? ").lower()
    valid_actions = ["add", "drop", "change"]
    while user_input not in valid_actions:
        print("Error. Please pick 'add', 'change' or 'drop'.")
        user_input = input("Would you like to add, change, or drop a class? ").lower()
    if user_input == "add":
        add_class(schedule)
    elif user_input == "change":
        change_class(schedule)
    elif user_input == "drop":
        drop_class(schedule)

    print("Here is your final schedule: ")
    for i, mod in enumerate(schedule, start=1):
        print()
        print(f"    Mod {i} ")
        for block, classe in mod.items():
            print(f"{block}: {classe}")

    restart(schedule, y_or_n)

main()