import random

#mods
mod1 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "D Block": "",
    "E Block": "Nothing"
}
mod2 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "D Block": "",
    "E Block": "Nothing"
}
mod3 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "D Block": "",
    "E Block": "Nothing"
}
mod4 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "D Block": "",
    "E Block": "Nothing"
}
mod5 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "D Block": "",
    "E Block": "Nothing"
}
mod6 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "D Block": "",
    "E Block": "Nothing"
}
mod7 = {
    "A Block": "",
    "B Block": "",
    "C Block": "",
    "D Block": "",
    "E Block": "Nothing"
}

#lists of classes d blocks and e blocks
classes_list_english = ["English I", "English II", "English III", "English IV"]
classes_list_math = ["Geometry", "Algebra I", "Algebra II", "Pre-Calculus", "Calculus AB", "Calculus BC", "Statistics", "Linear Algebra", "Differiential Equations" ]
classes_list_history = ["Globral I", "Global II", "American History", "History Capstone Seminar", "Research Seminar"]
classes_list_science = ["Biology", "Chemistry", "Physics"]
#co_curric = ["Sophomore Co-Curric", "Junior Co-Corric", "Senior Co-Curric"]
classes_list_languages = ["Spanish I", "Spanish II", "Spanish III", "Spanish IV", "French I", "Frecnh II", "French III", "French IV", "Latin I", "Latin II", "Latin III", "Latin IV"]
electives = ["Free", "Admissions", "Library Helper", "CS1", "CS2", "CS3", "Digital Art & Animation", "Drawing", "Painting", "Art Seminar", "Computer Science Seminar", "Robotics", "Public Speaking", "Fibers & Fashion", "Photography", "Sports Psychology", "Ceramics" ]
d_blocksF = ["Feild Hockey", "Swimming for Conditioning", "Cross Country", "Soccer", "Tennis", "Volleyball", "Yearbook", "Advanced Fitness", "Stagecraft", "Fall Play"]
d_blocksW = ["Basektball", "Rock Climbing", "Swim", "Model UN", "Advanced Fitness", "Yearbook", "Stagecraft", "Winter Musical"]
d_blocksS = ["Track & Feild", "Tennis", "Softball", "Lacrosse", "Advanced Fitness", "Nature Walks"]
e_blocks = ["Chorus", "Orchestra" ]

#random choice of classes/dblocks for schedules 
#will just make electives and e blocks add-able
english = random.choice(classes_list_english)
math = random.choice(classes_list_math)
history = random.choice(classes_list_history)
science = random.choice(classes_list_science)
lang = random.choice(classes_list_languages)
classes = [english, math, history, science, lang]

fall = random.choice(d_blocksF)
winter = random.choice(d_blocksW)
spring = random.choice(d_blocksS)

#making the schedule
def make_schedule():
    for blocks in mod1:
        if blocks in ["A Block", "B Block", "C Block"]:
            return random.choice(classes)

#add class
def add_class(schedule):
    print("Here is your current schedule: ")
    for block in mod1:
        print(f"{block}: {mod1[block]}")
    for block in mod2:
        print(f"{block}: {mod2[block]}")
    for block in mod3:
        print(f"{block}: {mod3[block]}")
    for block in mod4:
        print(f"{block}: {mod4[block]}")
    for block in mod5:
        print(f"{block}: {mod5[block]}")
    for block in mod6:
        print(f"{block}: {mod6[block]}")
    for block in mod7:
        print(f"{block}: {mod7[block]}")

    #user says what they want to add
    block = input("Enter the block you want to add the class in: ")

    added_class = input(f"Enter the name of the class you want to add to {block}: ")
    #adding it
    schedule[block] = added_class
    print(f"You added {added_class} to {block}. ") 
    return schedule


#change class
def change_class(schedule):
    print("Here is your current schedule: ")
    for block in mod1:
        print(f"{block}: {mod1[block]}")
    for block in mod2:
        print(f"{block}: {mod2[block]}")
    for block in mod3:
        print(f"{block}: {mod3[block]}")
    for block in mod4:
        print(f"{block}: {mod4[block]}")
    for block in mod5:
        print(f"{block}: {mod5[block]}")
    for block in mod6:
        print(f"{block}: {mod6[block]}")
    for block in mod7:
        print(f"{block}: {mod7[block]}")

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

#drop class
def drop_class(schedule):
    print("Here is your current schedule: ")
    for block in mod1:
        print(f"{block}: {mod1[block]}")
    for block in mod2:
        print(f"{block}: {mod2[block]}")
    for block in mod3:
        print(f"{block}: {mod3[block]}")
    for block in mod4:
        print(f"{block}: {mod4[block]}")
    for block in mod5:
        print(f"{block}: {mod5[block]}")
    for block in mod6:
        print(f"{block}: {mod6[block]}")
    for block in mod7:
        print(f"{block}: {mod7[block]}")

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
    user_input = input("Would you like to add, change, or drop a class? ").lower()
    valid_actions = ["add", "drop", "change"]
    while user_input not in valid_actions:
        print("Error. Please pick 'add', 'change' or 'drop'.")
        user_input = input("Would you like to add, change, or drop a class? ").lower()
    if user_input == "add":
        add_class()
    elif user_input == "change":
        change_class()
    elif user_input == "drop":
        drop_class()

    print("Here is your final schedule: ")
    for block in mod1:
        print(f"{block}: {mod1[block]}")
    for block in mod2:
        print(f"{block}: {mod2[block]}")
    for block in mod3:
        print(f"{block}: {mod3[block]}")
    for block in mod4:
        print(f"{block}: {mod4[block]}")
    for block in mod5:
        print(f"{block}: {mod5[block]}")
    for block in mod6:
        print(f"{block}: {mod6[block]}")
    for block in mod7:
        print(f"{block}: {mod7[block]}")
main()