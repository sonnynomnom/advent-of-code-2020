# Advent of Code 2020 - Day 8
# https://adventofcode.com/2020/day/8

# Move each paragraph from day8.txt into a list called boot

with open('/Users/sonny/Desktop/aoc2020/day8.txt', 'r') as file:
  boot = [line.strip() for line in file]

# print(boot[0]) # acc +50
# print(boot[1]) # acc -11
# print(boot[2]) # nop +378

# ========== Part 1 ==========

# - acc increases or decreases a single global value called the accumulator by the value given in the argument.
# - jmp jumps to a new instruction relative to itself.
# - nop stands for No Operation - it does nothing.

accumulator = 0

previous_index = []
previous_boot = []

index = 0

while index not in previous_index:
  previous_index += [index]
  previous_boot += [boot[index]]

  if boot[index][:3] == 'acc':
    if boot[index][4] == '+':
      accumulator += int(boot[index][5:])
    else:
      accumulator -= int(boot[index][5:])
    index += 1

  elif boot[index][:3] == 'jmp':
    if boot[index][4] == '+':
      index += int(boot[index][5:])
    else:
      index -= int(boot[index][5:])

  elif boot[index][:3] == 'nop':
    index += 1

# print(boot[0][:3])         # acc
# print(boot[0][4])          # +
# print(int(boot[0][5:]))    # 50

# print(previous_index) 
# print(len(previous_index)) # 205

# print(previous_boot) 
# print(len(previous_boot))  # 205

print('Part 1 Accumulator:', accumulator) # 2025

# # ========== Part 2 ==========

# Somwhere in the program, either: 
# - A jmp is supposed to be a nop
# - A nop is supposed to be a jmp.

# print(len(boot))           # 654
# print(boot[653])           # jmp +1

for x in range(len(boot)):
  
  accumulator = 0
  index = 0

  previous_index2 = []
  previous_boot2 = []

  if boot[x][:3] == 'nop':
    boot[x] = boot[x].replace('nop', 'jmp')
  elif boot[x][:3] == 'jmp':
    boot[x] = boot[x].replace('jmp', 'nop')

  while index not in previous_index2:
    
    previous_index2 += [index]
    previous_boot2 += [boot[index]]
    # print(previous_index2)
    # print(previous_boot2)
    
    if boot[index][:3] == 'acc':
      if boot[index][4] == '+':
        accumulator += int(boot[index][5:])
      else:
        accumulator -= int(boot[index][5:])
      index += 1

    elif boot[index][:3] == 'jmp':
      if boot[index][4] == '+':
        index += int(boot[index][5:])
      else:
        index -= int(boot[index][5:])
    
    elif boot[index][:3] == 'nop':
      index += 1
    
    if index == 653:
      print("Part 2: Accumulator) 
      break
    
  if boot[x][:3] == 'jmp':
    boot[x] = boot[x].replace('jmp', 'nop')
  elif boot[x][:3] == 'nop':
    boot[x] = boot[x].replace('nop', 'jmp')
  
# print(previous_index2)
# print(previous_boot2)
# print('Part 2 Accumulator:', accumulator) # 1254, 127 too low. 2025, 3961 too high. 205 not right.