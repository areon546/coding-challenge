# attempt at making each new line a secondary array

"""
f = open('Days.txt', 'r+')  # opens the file 'days'

numb = len(open('Days.txt').readlines())    # counts the amount of lines in 'days'
print(numb)                                 # prints the result from L.4

day = []
"""
# todo make the test2 example create a new secondary array for each line

"""
testsite_array = []
with open('topsites.txt') as my_file:
    for line in my_file:
        testsite_array.append(line)
This is possible because Python allows you to iterate over the file directly.

Alternatively, the more straightforward method, using f.readlines():

with open('topsites.txt') as my_file:
    testsite_array = my_file.readlines()


for i in range(0, numb):
    day.append(f.read(i))  # adds the days in the file 'days' to the variable day

#day.append(f.readlines())   # adds the days in the file 'days' to the variable day

print(day)  # prints the 'day' variable
"""

"""
day = []
with open('Days.txt') as f:
    for line in f:
        day.append(line)

print(day)

"""

"""
with open('Days.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
print(content)
"""
"""
with open('Days.txt', 'r') as f:
    array = [[str(n) for n in line.split()] for line in f]
print(array)
"""

with open('Days.txt', 'r') as f:
    day = []
    for line in f:
        number_strings = line.split()  # Split the line on runs of whitespace
        numbers = [str(n) for n in number_strings]  # Convert to integers
        day.append(numbers)  # Add the "row" to your list.
    print(day)

# The following line does the same thing, but in a more compact and Pythonic fashion:
    for line in f:
        day = [[str(n) for n in line.split()] for line in f]
    print(day)



with open('Days.txt', 'r') as f:
    day = []

    for line in f:
        day = [[str(n) for n in line.split()] for line in f]
    print(day)