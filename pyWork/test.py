uName = input("please write your name: ")

###             files integration
with open('testDays.txt', 'r') as f:
    day = []

    for line in f:
        number_strings = line.split()

        day.append(number_strings)

print(day)

numb = len(day)
avg = 0

# ask section
for n in range(0, numb):

    hWatching = int(input("How many hours were you watching tv on " + day[n][0]))
    print(hWatching, " on ", day[n][0])
    avg += hWatching
    day[n][1] = hWatching
avg /= len(day)  # len() finds the length of a variable

# print section
for i in range(len(day)):
    print(day[i][1], "on ", day[i][0])
print(avg, " is your average.")

