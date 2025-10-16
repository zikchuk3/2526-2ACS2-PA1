'''

resources:
.items(): https://www.w3schools.com/python/ref_dictionary_items.asp
enumerate(): https://www.w3schools.com/python/ref_func_enumerate.asp
set(): https://www.w3schools.com/python/python_sets.asp
add(): https://www.w3schools.com/python/ref_set_add.asp
flatten a list: https://www.geeksforgeeks.org/python/python-flatten-list-to-individual-elements/
'''

import random
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
classes_list_english = ["English I", "English II", "English III", "English IV"]
classes_list_math = ["Geometry", "Algebra I", "Algebra II", "Pre-Calculus", "Calculus AB", "Calculus BC", "Statistics", "Linear Algebra", "Differiential Equations" ]
classes_list_history = ["Global I", "Global II", "American History"]
classes_list_science = ["Biology", "Chemistry", "Physics"]
#co_curric = ["Sophomore Co-Curric", "Junior Co-Corric", "Senior Co-Curric"]
classes_list_languages = ["Spanish I", "Spanish II", "Spanish III", "Spanish IV", "French I", "Frecnh II", "French III", "French IV", "Latin I", "Latin II", "Latin III", "Latin IV"]
electives = ["Free", "Admissions", "Library Helper", "CS1", "CS2", "CS3", "Digital Art & Animation", "Drawing", "Painting", "Art Seminar", "Computer Science Seminar", "Robotics", "Public Speaking", "Fibers & Fashion", "Photography", "Sports Psychology", "Ceramics", "History Capstone Seminar", "Research Seminar" ]
d_blocksF = ["Feild Hockey", "Swimming for Conditioning", "Cross Country", "Soccer", "Tennis", "Volleyball", "Yearbook", "Advanced Fitness", "Stagecraft", "Fall Play"]
d_blocksW = ["Basektball", "Rock Climbing", "Swim", "Model UN", "Advanced Fitness", "Yearbook", "Stagecraft", "Winter Musical"]
d_blocksS = ["Track & Feild", "Tennis", "Softball", "Lacrosse", "Advanced Fitness", "Nature Walks"]
e_blocks = ["Chorus", "Orchestra" ]

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


#add class
def add_class(schedule):
    #user says what they want to add
    mod = int(input("Enter the number of the mod you want to add a class to: "))
    valid_mods = [1, 2, 3, 4, 5, 6, 7]
    while mod not in valid_mods:
        print("Error. Please pick enter a number 1-7.")
        mod = int(input("Enter the number of the mod you want to add a class to: "))

    block = input("Enter the letter of the block you want to add the class in: ").upper()
    block_names = f"{block} Block"
    valid_blocks = ["a", "A", "B", "b", "C", "c", "D", "d", "E", "e"]
    while block not in valid_blocks:
        print("Error. Please pick enter: 'A', 'B', 'C', 'D', or 'E' !")
        block = input("Enter the letter of the block you want to add the class in: ").upper()
    if block == "a" or block == "A" or block == "B" or block == "b" or block == "C" or block == "c":
        added_class = input(f"Enter the name of the class you want to add to {block} Block: ")
        valid_classes_list = [classes_list_english, classes_list_history, classes_list_languages, classes_list_math, classes_list_science, electives]
        # had to flatten the list
        valid_classes = [x for sublist in valid_classes_list for x in sublist]
        while added_class not in valid_classes:
            print("Error. Please pick enter a valid class !")
            print(f"Here is the course calendar if you need reminding: {valid_classes}.")
            added_class = input(f"Enter the name of the class you want to add to {block} Block: ")
        schedule[mod - 1][block_names] = added_class
        print(f"You added {added_class} to Mod {mod}, {block} Block. ") 
        return schedule
    elif block == "D" or block == "d":
        added_sport = input(f"Enter the name of the sport you want to add to your Fall/Winter/Spring {block} Block: ")
        if mod == 1:
            valid_sports_listF = [d_blocksF]
            valid_sportsF = [x for sublist in valid_sports_listF for x in sublist]
            while added_sport not in valid_sportsF:
                print("Error. Please pick enter a valid Fall sport !")
                print(f"Here is the course calendar if you need reminding: {valid_sportsF}.")
                added_sport = input(f"Enter the name of the sport you want to add to your Fall {block} Block: ")
            schedule[mod][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You added {added_sport} to Mod your Fall {block} Block. ") 
            return schedule
        if mod == 2:
            valid_sports_listF = [d_blocksF]
            valid_sportsF = [x for sublist in valid_sports_listF for x in sublist]
            while added_sport not in valid_sportsF:
                print("Error. Please pick enter a valid Fall sport !")
                print(f"Here is the course calendar if you need reminding: {valid_sportsF}.")
                added_sport = input(f"Enter the name of the sport you want to add to your Fall {block} Block: ")
            schedule[mod - 2][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You added {added_sport} to your Fall {block} Block. ") 
            return schedule
        if mod == 3:
            valid_sports_listW = [d_blocksW]
            valid_sportsW = [x for sublist in valid_sports_listW for x in sublist]
            while added_sport not in valid_sportsW:
                print("Error. Please pick enter a valid Winter sport !")
                print(f"Here is the course calendar if you need reminding: {valid_sportsW}.")
                added_sport = input(f"Enter the name of the sport you want to add to your Winter {block} Block: ")
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
                print(f"Here is the course calendar if you need reminding: {valid_sportsW}.")
                added_sport = input(f"Enter the name of the sport you want to add to your Winter {block} Block: ")
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
                print(f"Here is the course calendar if you need reminding: {valid_sportsW}.")
                added_sport = input(f"Enter the name of the sport you want to add to your Winter {block} Block: ")
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
                print(f"Here is the course calendar if you need reminding: {valid_sportsS}.")
                added_sport = input(f"Enter the name of the sport you want to add to your Spring {block} Block: ")
            schedule[mod][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You added {added_sport} to your Spring {block} Block. ") 
            return schedule
        if mod == 7:
            valid_sports_listS = [d_blocksS]
            valid_sportsS = [x for sublist in valid_sports_listS for x in sublist]
            while added_sport not in valid_sportsS:
                print("Error. Please pick enter a valid Spring sport !")
                print(f"Here is the course calendar if you need reminding: {valid_sportsS}.")
                added_sport = input(f"Enter the name of the sport you want to add to your Spring {block} Block: ")
            schedule[mod - 2][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You added {added_sport} to your Spring {block} Block. ") 
            return schedule


#change class
def change_class(schedule):
    #user says what they want to add
    mod = int(input("Enter the number of the mod you want to change a class/d-block to: "))
    valid_mods = [1, 2, 3, 4, 5, 6, 7]
    while mod not in valid_mods:
        print("Error. Please pick enter a number 1-7.")
        mod = int(input("Enter the number of the mod you want to change a class/d-block to: "))

    block = input("Enter the letter of the block you want to change the class in: ").upper()
    block_names = f"{block} Block"
    valid_blocks = ["a", "A", "B", "b", "C", "c", "D", "d", "E", "e"]
    while block not in valid_blocks:
        print("Error. Please pick enter: 'A', 'B', 'C', 'D', or 'E' !")
        block = input("Enter the letter of the block you want to change the class in: ").upper()
    if block == "a" or block == "A" or block == "B" or block == "b" or block == "C" or block == "c":
        added_class = input(f"Enter the name of the class you want to change in {block} Block: ")
        valid_classes_list = [classes_list_english, classes_list_history, classes_list_languages, classes_list_math, classes_list_science, electives]
        # had to flatten the list
        valid_classes = [x for sublist in valid_classes_list for x in sublist]
        while added_class not in valid_classes:
            print("Error. Please pick enter a valid class !")
            print(f"Here is the course calendar if you need reminding: {valid_classes}.")
            added_class = input(f"Enter the name of the class you want to change in {block} Block: ")
        schedule[mod - 1][block_names] = added_class
        print(f"You added {added_class} to Mod {mod}, {block} Block. ") 
        return schedule
    elif block == "D" or block == "d":
        added_sport = input(f"Enter the name of the sport you want to add to your Fall/Winter/Spring {block} Block: ")
        if mod == 1:
            valid_sports_listF = [d_blocksF]
            valid_sportsF = [x for sublist in valid_sports_listF for x in sublist]
            while added_sport not in valid_sportsF:
                print("Error. Please pick enter a valid Fall sport !")
                print(f"Here is the course calendar if you need reminding: {valid_sportsF}.")
                added_sport = input(f"Enter the name of the sport you want to add to your Fall {block} Block: ")
            schedule[mod][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You added {added_sport} to Mod your Fall {block} Block. ") 
            return schedule
        if mod == 2:
            valid_sports_listF = [d_blocksF]
            valid_sportsF = [x for sublist in valid_sports_listF for x in sublist]
            while added_sport not in valid_sportsF:
                print("Error. Please pick enter a valid Fall sport !")
                print(f"Here is the course calendar if you need reminding: {valid_sportsF}.")
                added_sport = input(f"Enter the name of the sport you want to add to your Fall {block} Block: ")
            schedule[mod - 2][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You added {added_sport} to your Fall {block} Block. ") 
            return schedule
        if mod == 3:
            valid_sports_listW = [d_blocksW]
            valid_sportsW = [x for sublist in valid_sports_listW for x in sublist]
            while added_sport not in valid_sportsW:
                print("Error. Please pick enter a valid Winter sport !")
                print(f"Here is the course calendar if you need reminding: {valid_sportsW}.")
                added_sport = input(f"Enter the name of the sport you want to add to your Winter {block} Block: ")
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
                print(f"Here is the course calendar if you need reminding: {valid_sportsW}.")
                added_sport = input(f"Enter the name of the sport you want to add to your Winter {block} Block: ")
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
                print(f"Here is the course calendar if you need reminding: {valid_sportsW}.")
                added_sport = input(f"Enter the name of the sport you want to add to your Winter {block} Block: ")
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
                print(f"Here is the course calendar if you need reminding: {valid_sportsS}.")
                added_sport = input(f"Enter the name of the sport you want to add to your Spring {block} Block: ")
            schedule[mod][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You added {added_sport} to your Spring {block} Block. ") 
            return schedule
        if mod == 7:
            valid_sports_listS = [d_blocksS]
            valid_sportsS = [x for sublist in valid_sports_listS for x in sublist]
            while added_sport not in valid_sportsS:
                print("Error. Please pick enter a valid Spring sport !")
                print(f"Here is the course calendar if you need reminding: {valid_sportsS}.")
                added_sport = input(f"Enter the name of the sport you want to add to your Spring {block} Block: ")
            schedule[mod - 2][block_names] = added_sport
            schedule[mod - 1][block_names] = added_sport
            print(f"You added {added_sport} to your Spring {block} Block. ") 
            return schedule

'''
    #user says what they want to add
    block = input("Enter the block you want to change: ")
    if block in schedule:
        changed_class = input(f"Enter the new class you want to add to {block}. ")
        #setting something for the old class
        old_class = schedule[block]
        #then setting that to the new class 
        schedule[block] = changed_class
        print(f"You changed {old_class} to {changed_class} in your {block}. ")
    else: 
        print(f"{block} is not in your schedule.")
        user_input = input("Do you want to add a block? (y)es or (n)o. ")
        if user_input == "y":
            #go to add class!
            add_class()
        elif user_input == "no":
            print("Okay.")
    return schedule
'''

#drop class
def drop_class(schedule):
    for block in mod2:
        block = input("What block would you like to drop a class from? ")
        if block in schedule:
            user_input = input(f"What class would you like to drop from {block}? ")
            dropped_class = schedule.pop(block)
            print(f"You dropped {dropped_class} from {block}")
            break
    return schedule

def main():
    #welcome in the offic 
    print("Welcome to Mrs. Caroll's office.")
    print("Here is your current schedule: ")
    schedule = make_schedule()  
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
        drop_class()

    print("Here is your final schedule: ")
    for i, mod in enumerate(schedule, start=1):
        print()
        print(f"    Mod {i} ")
        for block, classe in mod.items():
            print(f"{block}: {classe}")

main()