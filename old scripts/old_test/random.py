from random import choice as rch

part_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
groupA = []
groupB = []

for i in range(0, 7):
    groupA.append(rch(part_num))
    part_num.remove(groupA[i])
    groupB.append(rch(part_num))
    part_num.remove(groupB[i])

print('Group A:', groupA)
print('Group B:', groupB)
print('Participants:', part_num)
