# Advent of Code 2020 - Day 4
# https://adventofcode.com/2020/day/4

import re

# Move each paragragph from day4.txt into a list called passports

f = open('/Users/sonny/Desktop/aoc2020/day4.txt', 'r')
data = f.read()
    
passports = []
splat = data.split("\n\n")

for number, paragraph in enumerate(splat, 1):
    passports += [str(paragraph) + '\n']
        
# print(passports[0])
# print(passports[1])
# print(passports[2])

# ========== Part 1 ==========

# valid = 0
# for passport in passports:
#     if 'byr' in passport and 'iyr' in passport and 'eyr' in passport and 'hgt' in passport and 'hcl' in passport and 'ecl' in passport and 'pid' in passport:
#        valid += 1
# print(valid)

byr = []
copy = ''

for passport in passports:
  if 'byr' in passport:
    copy = passport[passport.find('byr')+4 : len(passport)]
    if copy.find(' ') != -1 and copy.find(' ') < copy.find('\n'):
      byr += [int(copy[0 : copy.find(' ')])]
    else:
      byr += [int(copy[0 : copy.find('\n')])]
  else:
    byr += ['']

# print(byr)

iyr = []
copy = ''

for passport in passports:
  if 'iyr' in passport:
    copy = passport[passport.find('iyr')+4 : len(passport)]
    if copy.find(' ') != -1 and copy.find(' ') < copy.find('\n'):
      iyr += [int(copy[0 : copy.find(' ')])]
    else:
      iyr += [int(copy[0 : copy.find('\n')])]
  else:
    iyr += ['']


eyr = []
copy = ''

for passport in passports:
  if 'eyr' in passport:
    copy = passport[passport.find('eyr')+4 : len(passport)]
    if copy.find(' ') != -1 and copy.find(' ') < copy.find('\n'):
      eyr += [int(copy[0 : copy.find(' ')])]
    else:
      eyr += [int(copy[0 : copy.find('\n')])]
  else:
    eyr += ['']




valid = 0
x = 0

for passport in passports:
    if 'byr' in passport and byr[x] >= 1920 and byr[x] <= 2002 and 'iyr' in passport and iyr[x] >= 2010 and iyr[x] <= 2020 and 'eyr' in passport and eyr[x] >= 2020 and eyr[x] <= 2030 and 'hgt' in passport and 'hcl' in passport and 'ecl' in passport and 'pid' in passport:
       valid += 1
    x += 1

print(valid)
