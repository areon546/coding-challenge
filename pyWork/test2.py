
f = open('Days.txt', 'r+')  # opens the file 'days'

numb = len(open('Days.txt').readlines())    # counts the amount of lines in 'days'
print(numb)                                 # prints the result from L.4

day = []

day.append(f.readlines())   # adds the days in the file 'days' to the variable day

print(day)  # prints the 'day' variable
