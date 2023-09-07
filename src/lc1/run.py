# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

numList = [1,2,3,4,5,6,7]
target = 9
i = 0
x = 0


#
# print(numList[5])
#
# numList = numList[3] + numList[4]
# print(numList)
#
# if numList == target:
#     print('you did it, it is 9!')
# else:
#     print('try again')
#

## iterate through numList,
# if both numbers add to target, save to output and return the value of the iterators (which will be the indicies)



#------TESTING ENUMERATION----
#https://www.geeksforgeeks.org/enumerate-in-python/#
# l1 = [10,12,'hi',7,0.5]
# obj1 = enumerate(l1)
#
# print('Return Type ', type(obj1))
# print(list(obj1))
#
#
# for count, ele in enumerate(l1) :
#     print(count, ele)