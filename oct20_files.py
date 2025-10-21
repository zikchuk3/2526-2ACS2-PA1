'''

my_schedule = open("schedule.txt")

#opens file and says it can acess it
print(my_schedule)

#allows us to see/read the file
print(my_schedule.read()) # prints whole thing

print(my_schedule.read(5)) #prints number of characters in ()

print(my_schedule.readline()) # to print specific lines

my_schedule.readline() # it read a lime w/o printing, skips to next line that you print
print(my_schedule.read(3))

'''