# Advent of Code 2020 - Day 6
# https://adventofcode.com/2020/day/6

# Move each paragraph from day6.txt into a list called customs

f = open('/Users/sonny/Desktop/aoc2020/day6.txt', 'r')
data = f.read()
    
customs = []
splat = data.split("\n\n")

for number, paragraph in enumerate(splat, 1):
    customs += [str(paragraph) + '\n']

# print(customs)
# print(len(customs))    

# print(customs[0])
# print(customs[1])

# ========== Part 1 ==========

# Take out '\n'
customs_new = [group.replace('\n', '') for group in customs]

# print(customs_new[0])
# print(customs_new[1])

# Get the unique characters
customs_uniques = [list(set(group)) for group in customs_new]

# print(customs_uniques[0])
# print(customs_uniques[1])

count1 = 0

for group in customs_uniques:
  count1 += len(group)

print(count1)

# ========== Part 2 ==========

count2 = 0

new_line = 0
group_new_lines = []

for group in customs:
  for index in range(len(group)):
    if group[index] == '\n':
      new_line += 1
  group_new_lines+=[new_line]
  new_line=0

print(group_new_lines)

counter = 0

for group in customs_new:
    print(group.count('a'))
    if group.count('a') >= group_new_lines[counter]:
      count2 += 1
    if group.count('b') >= group_new_lines[counter]:
      count2 += 1
    if group.count('c') >= group_new_lines[counter]:
      count2 += 1
    if group.count('d') >= group_new_lines[counter]:
      count2 +=1
    if group.count('e') >= group_new_lines[counter]:
      count2 +=1
    if group.count('f') >= group_new_lines[counter]:
      count2 +=1
    if group.count('g') >= group_new_lines[counter]:
      count2 +=1
    if group.count('h') >= group_new_lines[counter]:
      count2 +=1
    if group.count('i') >= group_new_lines[counter]:
      count2 +=1
    if group.count('j') >= group_new_lines[counter]:
      count2 +=1
    if group.count('k') >= group_new_lines[counter]:
      count2 +=1
    if group.count('l') >= group_new_lines[counter]:
      count2 +=1
    if group.count('m') >= group_new_lines[counter]:
      count2 +=1
    if group.count('n') >= group_new_lines[counter]:
      count2 +=1
    if group.count('o') >= group_new_lines[counter]:
      count2 +=1
    if group.count('p') >= group_new_lines[counter]:
      count2 +=1
    if group.count('q') >= group_new_lines[counter]:
      count2 +=1
    if group.count('r') >= group_new_lines[counter]:
      count2 +=1
    if group.count('s') >= group_new_lines[counter]:
      count2 +=1
    if group.count('t') >= group_new_lines[counter]:
      count2 +=1
    if group.count('u') >= group_new_lines[counter]:
      count2 +=1
    if group.count('v') >= group_new_lines[counter]:
      count2 +=1
    if group.count('w') >= group_new_lines[counter]:
      count2 +=1
    if group.count('x') >= group_new_lines[counter]:
      count2 +=1
    if group.count('y') >= group_new_lines[counter]:
      count2 +=1
    if group.count('z') >= group_new_lines[counter]:
      count2 +=1
    counter += 1

print(count2)