# Advent of Code 2020 - Day 1

# Move each number from expense.txt into a list called expenses
with open('/Users/sonny/Desktop/expense_report.txt', 'r') as file:
    expenses = [int(line.strip()) for line in file]
    print(expenses)

# Part 1
for x in expenses:
    for y in expenses:
        if x + y == 2020:
            print(x * y)

# Part 2
for x in expenses:
    for y in expenses:
        for z in expenses: 
            if x + y + z == 2020:
                print(x * y * z)