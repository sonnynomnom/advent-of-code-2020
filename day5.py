# Advent of Code 2020 - Day 5
# https://adventofcode.com/2020/day/5

import math

# Move each number from day5.txt into a list called boarding_passes

with open('/Users/sonny/Desktop/aoc2020/day5.txt', 'r') as file:
  boarding_passes = [line.strip() for line in file]

# print(boarding_passes[0])
# print(boarding_passes[1])
# print(boarding_passes[2])

# print(len(boarding_passes))    

# ========== Part 1 ==========

# 128 rows (0-127)
# 8 columns (0-7)

# F/B F/B F/B F/B F/B F/B F/B L/R L/R L/R

r_lower = 0
r_upper = 127

c_lower = 0
c_upper = 7

row = [r_lower, r_upper]
column = [c_lower, c_upper]

seat_ids = []

for boarding_pass in boarding_passes:

  for x in range(7):
    if (boarding_pass[x] == 'F'):
      r_upper = r_upper - math.ceil((r_upper-r_lower)/2)
    else:
      r_lower = r_lower + math.ceil((r_upper-r_lower)/2)
    row = [r_lower, r_upper] 
  for y in range(3):
    if (boarding_pass[y+7] == 'L'):
      c_upper = c_upper - math.ceil((c_upper-c_lower)/2)
    else:
      c_lower = c_lower + math.ceil((c_upper-c_lower)/2)
    column = [c_lower, c_upper]
  # print(row, column)
  seat_ids += [row[0]*8+column[0]]

  r_lower = 0
  r_upper = 127

  c_lower = 0
  c_upper = 7

print(seat_ids)

#            R        L        L
# (0-7) -> (4-7) -> (4-5) -> (4-4)

# ========== Part 2 ==========

seat_ids.sort()

# print(seat_ids)

answer = []

for x in range(len(seat_ids)):
  if (seat_ids[x] - seat_ids[x-1]) > 1:
    answer += [seat_ids[x]]

print(answer)

# 558 - 1 = 557