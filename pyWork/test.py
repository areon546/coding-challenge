uName = input("please write your name: ")

#               file integration
with open('testDays.txt', 'r') as f:  # opens and closes the file in this loop
    day = []

    for line in f:  # counts lines in the file - f
        number_strings = line.split()  # number_strings goes through every line and makes it a list

        day.append(number_strings)  # adds the list in number_strings to the end of day

print(day)

numb = len(day)
avg = 0

# ask section
for n in range(numb):  # goes through all the days and asks the user how many hours on which day and stores it

    hWatching = int(input("How many hours were you watching tv on " + day[n][0]))
    #        asks how long you were watching the tv for

    print(hWatching, " on ", day[n][0])
    #       prints how long it was ,possibly unnecessary, on that day

    avg += hWatching
    #       adds the length of time watching too the average variable

    day[n][1] = hWatching

    # finds the average of how long
avg /= numb  # numb is length of a day

# print section
for i in range(numb):
    print(day[i][1], "on ", day[i][0])
print(avg, " is your average.")

print(day)
