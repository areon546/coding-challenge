uName = input("please write your name: ")
day = [["monday", 0], ["tuesday", 0], ["wednesday", 0], ["thursday", 0], ["friday", 0], ["saturday", 0], ["sunday", 0]]
uHours = []
avg = 0

# ask section
for n in day:
    hWatching = input("how many hours were you watching tv on " + n)
    # print (hWatching," on " , n)
    avg += int(hWatching)
    uHours.append(hWatching)
avg /= len(day)  # len() finds the length of a variable

# print section
for i in range(len(day)):
    print(i)
    print(uHours[i], " on ", day[i])
print(avg, " is your average.")
