with open('/Users/Fred/Documents/AdventOfCode/Day1/day1.txt') as f:
    lines = f.read()

# print(lines.split('\n\n'))
elves = lines.split('\n\n')

sums = []

for elf in elves:
    cals = elf.split('\n')
    sum = 0
    for x in cals:
        sum = sum + int(x)
    sums.append(sum)

# Elf carrying max calories
print(max(sums))

# Top3 elves carrying calories
top1 = max(sums)
sums.remove(top1)
top2 = max(sums)
sums.remove(top2)
top3 = max(sums)
sums.remove(top3)
print(top1 + top2 +top3)
