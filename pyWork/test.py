uName = input("please write your name: ")
day = [["monday ", 0],
       ["tuesday ", 0],
       ["wednesday ", 0],
       ["thursday ", 0],
       ["friday ", 0],
       ["saturday ", 0],
       ["sunday ", 0]]
avg = 0

# ask section
for n in range(len(day)):
    hWatching = int(input("how many hours were you watching tv on " + str(day[n][0])))
    print(hWatching, " on ", day[n][0])
    avg += hWatching
    day[n][1] = hWatching
avg /= len(day)  # len() finds the length of a variable

# print section
for i in range(len(day)):
    print(day[i][1], "on ", day[i][0])
print(avg, " is your average.")
