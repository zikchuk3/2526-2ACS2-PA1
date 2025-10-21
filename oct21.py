my_schedule = open("schedule.txt") #by default opens in read mode, can open in write or append mode

#my_schedule = open("schedule.txt", "w") #write mode
#my_schedule.write("Changing content!") #overwrites all files contents

my_schedule = open("schedule.txt", "a") # append mode
my_schedule.write("\nLOOK AT NEW CONTENT") #adds to end of the file contents

'''
To create a new file in Python, just open one that doesnt exist in an edit mode
'''
#new_file = open("new_file.txt", "x") #just creates new file
#new_file.write("HI")

new_file = open("new_file.txt", "a") #can create file w/ append and write to
new_file.write("yo")


#write a while loop that looks for mod 2
'''
ps = True
print(my_schedule)
while ps:
    my_schedule.readline()
    my_schedule.readline()
    my_schedule.readline()
    my_schedule.readline()
    my_schedule.readline()
    print(my_schedule.readline())
    print(my_schedule.readline())
    print(my_schedule.readline())
    print(my_schedule.readline())
    break

'''

'''
#better way of while loop
line = my_schedule.readline()

while line != "Mod: 2\n": #need \n to indicate that it is a new line
    line = my_schedule.readline()
print(line) #give it a mod 2 label

#then write a for loop that prints out mod 2 schedule blocks
for i in range(3):
    print(my_schedule.readline())
'''
