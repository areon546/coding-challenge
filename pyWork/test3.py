
'''
# THIS FIRST LINE WILL OPEN THE TEXT FILE WITH READ PERMISSION
with open('Days.txt', 'r') as f:
    # THIS LINE CREATES AN EMPTY ARRAY CALLED 'DAY'
    day = []

    # THIS LINE STARTS A LOOP WHICH WILL LOOP THROUGH EVERY LINE IN THE TEXT FILE CALLED DAYS (Look to the left to
    # see this text file)
    for line in f:
        # THIS LINE WILL SPLIT EACH LINE INTO A MINI LIST OF ITEMS AND STORE IT INTO THE LIST CALLED
        # ''NUMBER_STRINGS''. THE LINE WILL BE SPLIT WHEREVER THERE IS A 'WHITE SPACE'. THIS BASICALLY MEANS WHEREVER
        # THERE IS A SPACE ON THE LINE, THE LINE WILL BE SPLIT. SO FOR EXAMPLE, ON THE FIRST LINE WE HAVE ''MONDAY
        # 1'', SO THE LINE WILL BE SPLIT INTO 2 ITEMS; 'MONDAY' and '1' BECAUSE THERE IS A SPACE BETWEEN MONDAY AND 1
        # AND THE SPLIT() FUNCTIONS SPLITS THE STRING WHEREVER THERE IS A SPACE.
        number_strings = line.split()

        # NOW, WE CAN ADD THE MINI-LIST ABOVE (NUMBER_STRINGS) TO THE MAIN LIST CALLED 'DAY' AND THEN AS THIS LOOP
        # GOES ROUND FOR EACH LINE IN THE TEXT FILE, IT WILL KEEP ADDING MINI LISTS TO THE MAIN LIST CALLED DAY AND
        # THEN YOU END UP WITH A 2D LIST OR 2D ARRAY.
        day.append(number_strings)  # Add the "row" to your

print(day)
'''

'''
with open('Days.txt', 'r') as f:
    day = []

    for line in f:
        number_strings = line.split()

        day.append(number_strings)

print(day)
'''

'''
with open('testDays.txt', 'r') as f:
    day = []

    for line in f:
        day = [[str(n) for n in line.split()] for line in f]
    print(day)
'''

