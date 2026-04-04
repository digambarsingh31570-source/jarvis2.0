# for i in range(1,5):
#     for j in range(1,5):
#         if  j<=5-i:
#             print("*", end=" ")
#         else:
#             print("", end=" ")
#     print()
# for i in range(1, 5):
#     for j in range(1, 5):
#         if j>=i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# for i in range(1, 5):
#     for j in range(1, 8):
#         if j>=5-i and j <= 3+i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# n = int(input("enter number's sir : "))
# count = 0
# while n>0:
#     n = n//10
#     count = count+1
# print(count)
# num = int(input("Enter number sir : "))
# original = num
# pal = 0
# while num > 0:
#     digit = num%10
#     pal = pal*10+digit
#     num = num//10
# if original == pal:
#     print("True")
# else:
#     print("False")
# n = int(input("Enter number sir : "))
# a = 0
# b = 1
# count = 0
# while count < n:
#     print(a)
#     c = a+b
#     a = b
#     b = c
#     count = count+1
# num = int(input("Enter number sir : "))
# i = 2
# is_prime = True
# while i < num:
#     if num%i == 0:
#         is_prime = False
#         break
#     i += 1
# print(is_prime)
# n = int(input("Enter number sir : "))
# b = int(input("Enter digit sir : "))
# count = 0
# while n>0:
#     digit = n%10
#     if digit == b:
#         count += 1
#     n = n//10
# print(count)
# base = int(input("Enter base sir : "))
# power = int(input("Enter power sir : "))
# result = 1
# while power>0:
#     result = result*base
#     power = power- 1

# print(result)
# n = int(input("enter number : "))
# binary = ""
# while n > 0:
#     rem = n%2
#     binary = str(rem)+binary
#     n = n//2
# print(binary)
# a = int(input("Enter number sir : "))
# b = int(input("Enter second number sir : "))
# while b != 0:
#     r = a%b
#     a = b
#     b = r
# print(a)
# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))
# max_num = max(a, b)
# while True:
#     if max_num %a == 0 and max_num %b == 0:
#         print(max_num)
#         break
#     max_num += 1
# correct_password = "saksham8081"
# while True:
#     n = input("Enter number sir : ")
#     if n == correct_password:
#         print("stopped")
#         break
# balance = 44556;
# while True:
#     withdrawl = int(input("Enter withdrawl amount : "))
#     if withdrawl <= balance:
#         balance = balance-withdrawl
#         print("Remaindin balance")
#     else:
#         print("insuficient balance.")
#         break
#     while True:
#     print("\n1. Add")
#     print("2. Subtract")
#     print("3. multiply")
#     print("4. Exit")

#     choice = int(input("Enter choice : "))
#     if choice == 4:
#         print("Program exited")
#         break
#     a = int(input("Enter first number : "))
#     b = int(input("Enter second number : "))
#     if choice == 1:
#         print("Result : ",a+b)
#     elif choice == 2:
#         print("Result: ", a-b)
#     elif choice == 3:
#         print("result: ",a*b)
#     else:
#         print("Invalid-syntax")
# for i in range(1, 5):
#     for j in range(1, 8):
#         if j>=5-i and j<=3+i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# for i in range(1, 5):
#     for j in range(1, 8):
#         if j<=5-i or j>=3+i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# for i in range(1, 5):
#     for j in range(1, 5):
#         if j<=i:
#             print(j, end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# sentence = input("Enter sentence : ")
# words = sentence.split()
# for word in words:
#     i = len(word)-1
#     while i >=0:
#         print(word[i], end=" ")
#         i -= 1
#     print(end=" ")
# word = input("Enter characer sir : ")
# vowel = "aeiou"
# count = 0
# index = 0
# while index < len(word):
#     if word[index].lower() not in vowel and word[index].isalpha():
#         count += 1
#     index += 1
# print("number of consonent :", count)
num = int(input("Enter your number sir : "))
i = 0
is_perfect_square = False
while i*i <= num:
    if(i*i == num):
        is_perfect_square = True
        break
    i += 1
if is_perfect_square:
    print("True")
else:
    print("False")
for i in range(1, 4):
    print("table of i : ", i)
    for j in range(1, 11):
        print(i*j, end=" ")
    print()
for i in range(1, 4):
    for j in range(1, i+2):
        if j == 2:
            continue
        print(j, end=" ")
    print()
for i in range(1, 5):
    if i == 3:
        i += 1
        continue
    for j in range(1, 5):
        if j<=i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
target = 8
found = False
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == target:
            print("found at postition : ", i, j)
            found = True
            break
    if found:
        break
for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            print(f"({i}, {j})")
            break
        print(f"({i}, {j})")
for i in range(1, 6):
    for j in range(1, 6):
        if i == 1 or i == 5 or j == 1 or j == 5:
            continue
        print("*", end=" ")
    print()
correct_password = "1234"
for attempts in range(1, 4):
    username = input("Enter password sir : ")
    if username == correct_password:
        print("Login successufll..")
    else:
        print("wrong password..")
        if attempts == 3:
            print("Account locked..")
num = 1
for i in range(1, 5):
    for j in range(1, i+1):
        if num%4 == 0:
            pass
        print(num, end=" ")
        num += 1
    print()
matrix = [
    [2, 4, 5],
    [3, 6, 7],
    [1, 8, 9]
]
for i in range(len(matrix)):
    row_sum = 0
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
        row_sum += matrix[i][j]
    print("sum=", row_sum)
    if row_sum > 10:
        break
num = 1
for i in range(1, 6):
    for j in range(1, 6):
        if num %3 == 0:
            print("Fizz", end=" ")
            num+= 1
            continue
        if num%5 == 0:
            print("Buzz", end=" ")
            num += 1
            continue
    print(num, end=" ")
    num+= 1
print()
for i in range(1, 7):
    if i == 4:
        break
    for j in range(1, i+1):
        print("*", end=" ")
    print()
correct_pasword = "1234"
for attempts in range(1, 4):
    password = input("Enter password : ")
    if len(password) < 4:
        print("too short")
        continue
    if password == correct_pasword:
        print("Login successfull...")
        break
    else:
        print("wrong password..")

target = 5
found = False
for i in range(1, 11):
    for j in range(1, 11):

        if i*j == target:
            print("found pair : ", i,j)
            found = True
            break
        if found:
            break
n = 4
for i in range(1, n+1):
    if i == n:
        break
    print(" "*(n-i)+"*"*(2*i-1))
for i in range(n, 0, -1):
    print(" "*(n-i)+ "*"*(2*i-1))
num = 1
stop = False
for i in range(1, 11):
    for j in range(1, 11):
        if num == 57:
            stop = True
            break
        print(num, end=" ")
        num += 1
    print()

    if stop:
        break
list1 = [23, 34, 45]
list2 = [12, 32, 54]
for i in list1:
    for j in list2:
        if(i+j)%2 == 0:
            continue
        print(i,j)
