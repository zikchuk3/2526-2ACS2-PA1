mod1 = {
    "": "",
    "": "",
    "": "",
    "": "",
    "": ""
}
mod2 = {
    "": "",
    "": "",
    "": "",
    "": "",
    "": ""
}
mod3 = {
    "": "",
    "": "",
    "": "",
    "": "",
    "": ""
}
mod4 = {
    "": "",
    "": "",
    "": "",
    "": "",
    "": ""
}
mod5 = {
    "": "",
    "": "",
    "": "",
    "": "",
    "": ""
}
mod6 = {
    "": "",
    "": "",
    "": "",
    "": "",
    "": ""
}
mod7 = {
    "": "",
    "": "",
    "": "",
    "": "",
    "": ""
}

classes_list_english = ["English I", "English II", "English III", "English IV"]
classes_list_math = ["Geometry", "Algebra I", "Algebra II", "Pre-Calculus", "Calculus AB", "Calculus BC", "Statistics", "Linear Algebra", "Differiential Equations" ]
classes_list_history = ["Globral I", "Global II", "American History", "History Research"]
classes_list_science = ["Biology", "Chemistry", "Physics"]
classes_list_languages = ["Spanish I", "Spanish II", ]
electives = ["CS1", "CS2", "CS3", "Digital Art & Animation", "Drawing", "Painting", "Art Seminar", "Computer Science Seminar", "Robotics", "Public Speaking", "Fibers & Fashion", "Photography", "Sports Psychology", "Ceramics" ]
d_blocksF = ["Feild Hockey", "Swimming for Conditioning", "Cross Country", "Soccer", "Tennis", "Volleyball", "Yearbook", "Advanced Fitness", "Stagecraft"]
d_blocksW = ["Basektball", "Rock Climbing", "Swim", "Model UN", "Advanced Fitness", "Yearbook", "Stagecraft"]
d_blocksS = ["Track & Feild", "Tennis", "Softball", "Lacrosse", "Advanced Fitness", "Nature Walks"]
e_blocks = ["Chorus", ]

#add class
def add_class(schedule):
    print("Here is your current schedule: ")
    for block in mod2:
        print(f"{block}: {mod2[block]}")

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
    for block in mod2:
        print(f"{block}: {mod2[block]}")

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
    for block in mod2:
        print(f"{block}: {mod2[block]}")

    for block in mod2:
        block = input("What block would you like to drop a class from? ")
        if block in schedule:
            user_input = input(f"What class would you like to drop from {block}? ")
            dropped_class = schedule.pop(block)
            print(f"You dropped {dropped_class} from {block}")
            break
    return schedule

def main():
    print("Welcome to Mrs. Caroll's office.")
    user_input = input("Would you like to add, change, or drop a class? ").lower()
    valid_actions = ["add", "drop", "change"]
    while user_input not in valid_actions:
        print("Error. Please pick 'add', 'change' or 'drop'.")
        user_input = input("Would you like to add, change, or drop a class? ").lower()
    if user_input == "add":
        add_class(mod2)
    elif user_input == "change":
        change_class(mod2)
    elif user_input == "drop":
        drop_class(mod2)

    print("Here is your final schedule: ")
    for block in mod2:
        print(f"{block}: {mod2[block]}")
main()