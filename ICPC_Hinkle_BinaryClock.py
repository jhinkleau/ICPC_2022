time = [int(num) for num in input()]
first = ""
for i in range(len(time)): # First Binary Number
    if(time[i] == 8 or time[i] == 9):
        first += "*"
    else:
        first += "."
    if(i == 1):
        first += "  "
    if i != 3:
        first += " "
print(first)
second = ""
for i in range(len(time)): # Second Binary Number
    if(time[i] != 4 and time[i] != 5 and time[i] != 6 and time[i] != 7):
        second += "."
    else:
        second += "*"
    if(i == 1):
        second += "  "
    if i != 3:
        second += " "
print(second)
third = ""
for i in range(len(time)): # Third Binary Number
    if(time[i] != 6 and time[i] != 3 and time[i] != 7 and time[i] != 2):
        third += "."
    else:
        third += "*"
    if(i == 1):
        third += "  "
    if i != 3:
        third += " "
print(third)
fourth = ""
for i in range(len(time)): # Fourth Binary Number
    if(time[i] != 9 and time[i] != 5 and time[i] != 1 and time[i] != 7 and time[i] != 3):
        fourth += "."
    else:
        fourth += "*"
    if i != 3:
        fourth += " "
    if(i == 1):
        fourth += "  "
print(fourth)