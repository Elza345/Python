# nums = [5, 7 , 4 ,8 , True , "hello" , [5, 8 ]]
# nums[0] = 20
# nums[4] = 1
# print(nums[-1][1])
numbers = [5, 2, 7]
numbers.append(100)
numbers.insert(1, True)
b = [5, 0, 3]
numbers.extend(b)
# numbers.reverse()
numbers.sort()
numbers.pop(1)
numbers.remove(3)
# numbers.clear()
print(len(numbers))