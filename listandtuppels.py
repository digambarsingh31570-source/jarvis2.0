list = [1, 2, 4, 7, 8]
count = 0
for num in list:
    if num%2 == 0:
        count += 1
print(count)
nums = [1, 2, 3]
nums.reverse()
print(nums)
nums = [1, 2, 2, 3, 1]
nums = list(set(nums))
print(nums)
nums = [3, 1, 7, 5]
nums = sorted(nums)
ch = nums[-2]
print(ch)

list1 = [1, 2, 2, 3, 1]
unique = list(dict.fromkeys(list1))
print(unique)
a = [1, 2, 3]
b = [2, 3, 4]
list = []
for i in a:
    if i in b:
        list.append(i)
print(list)
nums = [1, 2, 3, 4]
nums = [nums[-1]] + nums[:-1]
print(nums)
matrix = [
    [1, 2],
    [3, 4]
]
list= []
for row in matrix:
    for item in row:
        list.append(item)
print(list)
nums = [1, 2, 3, 4, 5]
target = 6
list = []
for i in nums : 
    for j in range(i):
        if(i+j == 6):
            list.append((i, j))
print(list)
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
row = len(matrix)
coloum = len(matrix[0])
list = []
for j in range(coloum):
    new_row = []
    for i in range(row):
        new_row.append(matrix[i][j])
    list.append(new_row)
print(list)
nums = [1, 2, 3, 2, 4]
target = 2
list = []
for i in nums:
    if i != target:
        list.append(i)
print(list)
nums = [4, 3, 2, 1]
count = 0
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i]>nums[j]:
            count += 1
print(count)
nums = [1, 1, 2, 2, 2, 3]
freq = {}
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
result = sorted(nums, key=lambda x: freq[x])
print(result)
main = [1, 2, 3, 4, 5]
sub = [3, 4]
n = len(main)
m = len(sub)
found = False
for i in range(n-m+1):
    if main[i:i+m] == sub:
        found = True
        break
print(found)
nums = [1, 2, 3]
list = []
a = len(nums)
for i in range(a):
    for j in range(i+1, a):
        sum = [[nums[i],nums[j]]]
        list.extend((sum))
print(list)       