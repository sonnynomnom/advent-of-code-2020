# Advent of Code 2020 - Day 2

# Move each number from expense.txt into a list called expenses
with open('/Users/sonny/Desktop/passwords.txt', 'r') as file:
    policy = [line.strip() for line in file]
    # print(policy)

# Part 1

lowerbound = [int(line[0:line.find('-')]) for line in policy]
# print(lowerbound)

upperbound = [int(line[line.find('-')+1 : line.find(' ')]) for line in policy]
# print(upperbound)

alphabet = [line[line.find(' ')+1 : line.find(':')] for line in policy]
# print(alphabet)

passwords = [line[line.find(':')+2 : len(line)] for line in policy]
# print(passwords)

valid1 = 0

for index in range(len(policy)):
    count = 0 
    for character in passwords[index]: 
      if character == alphabet[index]:
        count += 1

    if count >= lowerbound[index] and count <= upperbound[index]:
        valid1 += 1

# print(valid)

# Part 2

valid2 = 0

for index in range(len(policy)):
    position1 = 0 
    position2 = 0
    if passwords[index][lowerbound[index]-1] == alphabet[index]:
        position1 += 1
    if passwords[index][upperbound[index]-1] == alphabet[index]:
        position2 += 1
    if (position1==1 and position2==0) or (position1==0 and position2==1):
        valid2 += 1
    # print(position1, position2, valid2)
print(valid2)