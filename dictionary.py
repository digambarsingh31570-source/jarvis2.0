d = "banana"
freq = {}
for i in d:
    freq[i] = freq.get(i, 0) + 1
print(freq)
s = "i love coding i love python"
s = s.split()
freq = {}
for i in s:
    freq[i] = freq.get(i, 0)+1
print(freq)
d = {
    "a": 1,
    "b" : 2,

}
new_dict = {}
for key in d: 
    value = d[key]
    new_dict[value] = key
print(new_dict)
d= {
    "a" : 10,
    "b" : 25,
    "c" : 5,
}
max_key = None
largest = float('-inf')# sabse choti possible value
for key in d:
    value = d[key]
    if d[key] > largest:
        largest = d[key]
        max_key = key
print(max_key)


d= {
    "a" : 10,
    "b" : 25,
    "c" : 5,
}
sorted_dict = {}
for key in sorted(d):
    sorted_dict[key] = d[key]
print(sorted_dict)

d= {
    "a" : 10,
    "b" : 25,
    "c" : 5,
}

new_dict = {}
for key, value in sorted(d.items(), key = lambda x: x[1]):
    new_dict[key] = value
print(new_dict)
words = ["apple", "ant", "bat", "ball"]
group = {}
for word in words:
    first = word[0]
    if first in group:
        group[first].append(word)
    else:
        group[first] = [word]
print(group)
nums = {1, 2, 2, 3, 1}
freq = {}
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)
d = {
    "a" : 10,
    "b" : 20,
    "c" : 30,
}
target = 20
new_dict = {}
for key in d:
    if d[key] != target:
        new_dict[key] = d[key]
print(new_dict)
nums = [2, 7, 11, 15]
target = 9
n = len(nums)
for i in range(n):
    for j in range(i+1, n):
        if nums[i] + nums[j] == target:
            print([i, j])
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
group = {}
for word in words:
    key = " ".join(sorted(word))
    if key in group:
        group[key].append(word)
    else:
        group[key] = [word]
print(list(group.values()))
S = "aabbccdde"
freq = {}
for chr in S:
    freq[chr] = freq.get(chr, 0)+ 1

for ch in S:
    if freq[chr] == 1:
        print(chr)
        break
d1 = {
    "a" : 1,
    "b" : 2,
}
s2 = {
    "b" : 3,
    "c" : 4,
}
result = d1.copy()
for key in s2:
    if key in result:
        result[key] += s2[key]
    else:
        result[key] = s2[key]
print(result)

d1 = {
    "a" : 1,
    "b" : 2,
}
s2 = {
    "b" : 2,
    "a" : 1,
}
if len(d1) != len(s2):
    print(False)
else:
    equal = True
    for key in d1:
        if key not in s2 or d1[key] != s2[key]:
            equal = False
            break
        print(equal)

d = {
    "a": 1,
    "b" : 2,
    "c" : 1,
}
values = list(d.values())
duplicates = []
for v in values:
    if values.count(v)>1 and v not in duplicates:
        duplicates.append(v)
print(duplicates)

