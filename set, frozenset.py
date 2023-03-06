# data = set('hello')
data = {5, 7, 4, 3, 5}


data.add(50)
data.update(['65 ' ,True, 4 ,5])
data.remove(True)
data.pop()
# data.clear()

nums = [5, 4, 8 , 9 ,5 ,5]
new_nums = set(nums)
new_data = frozenset([5, 4, 8 , 9 ,5 ,5,'65 ' ,True, 4 ,5])
print(new_data)