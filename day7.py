# Advent of Code 2020 - Day 7
# https://adventofcode.com/2020/day/7

# Move each line from day7.txt into a list called customs

with open('/Users/sonny/Desktop/aoc2020/day7.txt', 'r') as file:
  rules = [line.strip() for line in file]

# print(rules[0])    # muted lavender bags contain 5 dull brown bags, 4 pale maroon bags, 2 drab orange bags.
# print(rules[1])    # plaid aqua bags contain 1 posh violet bag, 5 pale yellow bags, 4 bright salmon bags.
# print(len(rules))  # 594

check = "shiny gold"
shiny = 0
new = ["shiny gold"]

# for line in rules:
#   if (check in line) and (check.split()[0:1] != line.split()[0:1]) and (check.split()[1:2] != line.split()[1:2]):
#     # print(line.split()[:2])
#     # print(' '.join(line.split()[:2]))
#     new += [' '.join(line.split()[:2])]
#     print(line)
#     shiny += 1

print(new)
print(shiny)       # 5

index = 0

while index != len(new):
  for line in rules:
    if (check in line) and (check.split()[0:1] != line.split()[0:1]) and (check.split()[1:2] != line.split()[1:2]):
      new += [' '.join(line.split()[:2])]
      print(new)
      shiny += 1
  index += 1
  check = new[index]

print("New ", new)
print("Shiny", shiny)








# for line in rules:
#   if "plaid organge" in line:
#     # print(line.split()[0:1])
#     # print(line.split()[1:2])
#     print(line)
#     # new += line.split()[:2] # first 2 words
#     shiny += 1


# SHINY GOLD

# pale magenta bags contain 4 posh tomato bags, 4 plaid blue bags, 2 shiny gold bags, 3 faded beige bags.
# shiny gold bags contain 3 wavy gold bags, 2 plaid chartreuse bags, 2 shiny lime bags, 5 dull indigo bags. (DELETE!)
# dull white bags contain 4 clear salmon bags, 2 shiny gold bags.
# clear yellow bags contain 1 shiny gold bag, 4 dotted beige bags, 4 dark lime bags.
# muted black bags contain 1 striped salmon bag, 1 shiny gold bag, 3 plaid gray bags.
# light black bags contain 1 dark plum bag, 1 shiny gold bag.

# plaid orange bags contain 5 faded green bags, 5 pale magenta bags.
# dim violet bags contain 2 clear tan bags, 5 pale magenta bags.
# light silver bags contain 2 vibrant plum bags, 2 pale magenta bags, 4 pale chartreuse bags, 3 plaid chartreuse bags.

# f = open('/Users/sonny/Desktop/aoc2020/day6.txt', 'r')
# data = f.read()
    
# customs = []
# splat = data.split("\n\n")

# for number, paragraph in enumerate(splat, 1):
#     customs += [str(paragraph) + '\n']

# # print(customs)
# print(len(customs))    

# print(customs[0])
# print(customs[1])

# ========== Part 1 ==========

# # Take out '\n'
# customs_new = [group.replace('\n', '') for group in customs]

# # print(customs_new[0])
# # print(customs_new[1])

# # Get the unique characters
# customs_uniques = [list(set(group)) for group in customs_new]

# # print(customs_uniques[0])
# # print(customs_uniques[1])

# count1 = 0

# for group in customs_uniques:
#   count1 += len(group)

# print(count1)

# # ========== Part 2 ==========

# # count2 = 0

# # new_line = 0
# # group_new_lines = []

# # for group in customs:
# #   for index in range(len(group)):
# #     if group[index] == '\n':
#       new_line += 1
#   group_new_lines+=[new_line]
#   new_line=0

# print(group_new_lines)

# counter = 0

# for group in customs_new:
#     print(group.count('a'))
#     if group.count('a') >= group_new_lines[counter]:
#       count2 += 1
#     if group.count('b') >= group_new_lines[counter]:
#       count2 += 1
#     if group.count('c') >= group_new_lines[counter]:
#       count2 += 1
#     if group.count('d') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('e') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('f') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('g') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('h') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('i') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('j') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('k') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('l') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('m') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('n') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('o') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('p') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('q') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('r') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('s') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('t') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('u') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('v') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('w') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('x') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('y') >= group_new_lines[counter]:
#       count2 +=1
#     if group.count('z') >= group_new_lines[counter]:
#       count2 +=1
#     counter += 1

# print(count2)