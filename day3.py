# Advent of Code 2020 - Day 3

# Move each number from day3.txt into a list called map
with open('/Users/sonny/Desktop/aoc2020/day3.txt', 'r') as file:
    map = [line.strip()*2000 for line in file]
    # print(map[0])
    # print(map[1])
    # print(len(map))

# Part 1

index = 0
num_trees1 = 0

for line in map:
    if line[index] == '#':
       num_trees1 += 1
    index+=3

# print(num_trees1)
# 262

# Part 2

index = 0
num_trees2 = 0

for line in map:
    if line[index] == '#':
       num_trees2 += 1
    index+=7

print(num_trees2)

# Right 1, down 1: 78
# Right 3, down 1: 262
# Right 5, down 1: 66
# Right 7, down 1: 69

index = 0
index_vertical = 0
num_trees2 = 0

for line in map:
    if (index_vertical % 2 == 0):
      if line[index] == '#':
         num_trees2 += 1
      index+=1
    index_vertical+=1

print(num_trees2)

# Right 1, down 2: 29

print(78 * 262 * 66 * 69 * 29)