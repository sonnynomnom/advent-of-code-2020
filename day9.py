# Advent of Code 2020 - Day 9
# https://adventofcode.com/2020/day/9

# Move each paragraph from day9.txt into a list called data

with open('/Users/sonny/Desktop/aoc2020/day9.txt', 'r') as file:
  data = [int(line.strip()) for line in file]

# print(data[0]) # 22
# print(data[1]) # 16
# print(data[2]) # 24

# print(len(data)) # 1000

# ========== Part 1 ==========

twentyfive = [22, 16, 24, 45, 43, 46, 28, 38, 27, 49,42,12,48,8,6,13,26,39,18,9,1,33,7,34,15]

invalid = 0
have_pair = False

for x in range(24, 1000):

  have_pair = False

  for i in twentyfive:
    
    if i < data[x]:
        pair = data[x] - i
        if pair in twentyfive:
          # print(data[x], " --- first number:", i, "second number: ", pair)
          have_pair = True
          break
      
  if have_pair == False:
    invalid = data[x]
    # print("invalid: ", invalid)
    break

  twentyfive.pop(0)
  twentyfive.append(data[x])

# Part 1: 14360655

# ========== Part 2 ==========

invalid = 14360655

list = []

for x in range(1000):
  list = []
  for y in range(x+1, 1000):
    list.append(data[y])

    if len(list) > 2 and sum(list) == invalid:
      list.sort() 
      print(list)
      break

print(714065 + 1248266) # Part 2: 1962331