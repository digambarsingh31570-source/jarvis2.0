s = "hello"
# s = s.lower()
# count = s.count("a")+s.count("e")+s.count("i")+s.count("o")+s.count("u")
# print(count)
# s = "madam"
# cs = s[::-1]
# if s == cs:
#     print("palindrome...")

# else:
#     print("this is not palindrome..")
# str = "saksham singh is my name."
# total_letter = sum(str.count(ch) for ch in "abcdefghijklmnopqrstuvwxyz")
# vowel = sum(str.count(hm) for hm in "aeiouAEIOU")
# consonent = total_letter-vowel
# print(consonent)
# str = "saksham singh"
# count = str.count(" ")
# print(count)
# s = "i love python"
# result = " ".join(s.split()[::-1])
# print(result)
# str = "Saksham"
# str = str.lower()
# print("".join(set(str)))
s = "i love programing"
s = s.split()
logest = max(s, key=len)
print(logest)
s = "hello word"
s = s.title()
print(s)
s = "pYThon"
upper = sum(map(str.isupper, s))
lower = sum(map(str.islower, s))
print("upper: ", upper)
print("lower : ", lower)
s = "hello"
s = s.lower()
for v in "aeiou":
    s = s.replace(v, "*")
print(s)
s = "banana"
c = "n"
index = s.index(c)
print(index)
s = "aaabbc"
result = ""
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        result = result+s[i]+str(count)
        count = 1
#last charachter add karna zarrori hai
result = result+s[-1]+str(count)
print(result)
s = "aabbbbsddsdk"
max_len = 0
for i in range(len(s)):
    result = ""
    for j in range(i, len(s)):
        if s[j] not in  result:
            result += s[j]
        else:
            break
    max_len = max(max_len, len(result))
print(max_len)
s1 = "abcd"
s2 = "cdab"
if len(s1) == len(s2) and s2 in(s1+s1):
    print("True")
else:
    print("False")
s = "abc"
for i in range(len(s)):
    for j in range(i, len(s)):
        print(s[i:j+1])
s = "abc"
count = 0
for i in range(len(s)):
    for j in range(i, len(s)):
        count += 1
print("total count of substring..",count)
ch = "banana"
max_count = 0
result = ""
for chr in ch:
    count = ch.count(chr)
    if count>max_count:
        max_count = count
        result = chr
print(result)
s = "a,b,c"
delimiter = ","
result = []
word = ""
for chr in s:
    if chr != delimiter:
        word += chr
    else:
        result.append(word)
        word= ""
result.append(word)
print(result)
s = "()()"
count = 0
balanced = True
for ch in s:
    if ch == "(":
        count += 1
    else:
        count -= 1
    if count <0:
        balanced = False
        break
if count == 0 and balanced:
    print("True")
else:
    print("False")
s = "hello"
target = "ll"
for i in range(len(s)-len(target)+1):
    if s[i:i+len(target)] == target:
        print(i)
        break