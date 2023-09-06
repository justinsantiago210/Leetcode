# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

numList = [1,2,3,4,5,6,7]
target = 9



print(numList[5])

numList = numList[3] + numList[4]
print(numList)

if numList == target:
    print('you did it, it is 9!')
else:
    print('try again')
