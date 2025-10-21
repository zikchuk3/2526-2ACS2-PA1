my_schedule = open("schedule.txt")

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

#better way of while loop
line = my_schedule.readline()

while line != "Mod: 2\n": #need \n to indicate that it is a new line
    line = my_schedule.readline()
print(line) #give it a mod 2 label

#then write a for loop that prints out mod 2 schedule blocks
for i in range(3):
    print(my_schedule.readline())
