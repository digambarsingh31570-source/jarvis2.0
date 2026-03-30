# a = int(input("Enter three digit number : "))
# digit1 = a%10
# digit2 = (a//10) % 10
# digit3 = a//100
# sum_digit = digit1 + digit2 + digit3
# print("total sum of digit: ", sum_digit)
# a1 = int(input("enter your first number : "))
# a2 = int(input("Enter your second number : "))
# reminder = a1 - (a2*(a1//a2))
# print("Total reminder is : ",reminder)
# aadhar = 45
# uchai = 97
# print("total area of triangle : ", 1/2*aadhar*uchai)
#logical operators
# corect_username = "admin cast"
# correct_password = "1234"
# username = input("Enter username : ")
# password = input("Enter your password : ")
# if username.lower() == corect_username and password == correct_password:
#     print("login successfull")
# else:
#     print("login failed..")
# a = int(input("Enter your digit sir : "))
# b = int(input("Enter your secon digit sir : "))
# if a < 0 and b > 0:
#     print("atleast one number is negative.")
# else:
#     print("invalid syntax")
#assigment operators
# ch = input("enter a character: ")
# if len(ch) == 1 and ch.isalpha():
#     if ch.lower() in "aeiou":
#         print("it is vowel.")
#     else:
#         print("it is consonent")
# else:
#     print("invalid-syntax")
# num = int(input("Enter your number : "))
# if num >= 0:
#     root = int(num**0.5)
#     if root*root == num:
#         print("this number have a perfect square..")
#     else:
#         print("this number does'nt have a perfect square..")
# else:
#     print("Negative number can not be perfect squares.")
# units = int(input("Enter units sir : "))
# if units <= 100:
#     bill = units*5
# elif units <= 200:
#     bill = (100*5)+(units-100)*7
# else:
#     bill = (100*5)+(100*7)+(units-200)*10
# print("total bill = ", bill)
# num  = float(input("Enter number : "))
# if num == int(num):
#     print("this number is integer value.")
# else:
#     print("this number is decimal value..")
# a = int(input("Enter your first number:"))
# b = int(input("Enter your scond number : "))
# c = int(input("Enter your third number : "))
# if a*a + b*b == c*c or a*a == b*b + c*c or  b*b == c*c+a*a:
#     print("this is perfect triangle")
# else:
#     print("not a right triangle.")
# correct_username = "admin"
# correct_password = "12345"
# attempt = 0
# while attempt < 3:
#     username = input("Enter your username sir : ")
#     password = input("Enter password:")
#     if username == correct_username and password == correct_password:
#         print("Login successfull")
#         break
#     else:
#         attempt += 1
#         print("Wrong credentials")
# if attempt == 3:
#     print("Warning too many failed attempts")
# num = int(input("Ente number : "))

# sum = 0
# temp = num
# while temp > 0:
#     digit = temp%10
#     sum += digit**3
#     temp //= 10
# if num == sum:
#     print(num,"is an amstrong number.")
# else:
#     print(num,"is not an amstrong number.")
# a = int(input("enter side a : "))
# b = int(input("Enter sider b :"))
# c = int(input("enter side c : "))
# if a == b == c:
#     print("EQuilateral triangle..")
# elif a == b or b==c or c == a:
#     print("isosceles triangle..")
# else:
#     print("scalene Triangle...")
# ch = input("enter value sir : ")
# if ch.islower():
#     print("lowercase letter..")
# elif ch.isupper():
#     print("upper casse letter..")
# elif ch.isdigit():
#     print("digit")
# else:
#     print("special charactr's..")
# math = float(input("enter your marks sir : "))
# chem  = float(input("Enter your chemistry marks : "))
# phy = float(input("enter physhics marks : "))
# if math >= 35 and chem >= 35 and phy >= 35:
#     calc_avg = (math + chem + phy)/3
#     print("average:", calc_avg)
#     if calc_avg >= 75:
#         print("distinction")
#     elif calc_avg >= 60:
#         print("first class")
#     else:
#         print("pass")
# else:
#     print("Fail(one and more subjects below 35.)")
# num = int(input("enter your number : "))
# if num > 0:
#     if num%2 == 0:
#         if num%4 == 0:
#             print("number is divisiable by 4.")
#         else:
#             print("even but not divisiable by 4.")
#     else:
#         print("Odd positive..")
# else:
#     print("Negative or zero")
# temp = int(input("Enter temprature : "))
# if temp>0:
#     if temp <= 10:
#         print("extreme cold.")
#     else:
#         print("")
# if temp <= 30:
#     print("normel")
# else:
#     print("hot")
# password = input("enter password : ")
# if len(password) >= 8:
#     has_digit = False
#     has_upper = False
#     for ch in password:
#         if ch.isdigit():
#             has_digit = True
#         if ch.isupper():
#             True
#     if has_digit:
#         if has_upper:
#             print("strong password...")
#         else:
#             print("medium password")
#     else:
#         print("Weak password (no digit)")
# else:
#     print("weak password (length < 8)")
# score = int(input("Enter your exam score : "))
# if score >= 90:
#     print("Grade A")
# else:
#     if score >= 75:
#         print("grade b")
#     else: 
#         print("grade c")
# username = input("Enter username : ")
# role = input("Enter your role : ")
# if username == "saksham":
#     if role == "admin":
#         print("Full access")
#     else:
#         if role == "editor":
#             print("edit access")
#         else:
#             print("view only..")
# else:
#     print("user not found...")
# n = int(input("Enter a number sir : "))
# count = 0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         count += 1
# print("total count is :", count)
# n = int(input("enter number sir : "))
# if n < 0:
#     n = -n

# count = 0
# if n == 0:
#     count = 1
# else:
#     for i in str(n):
#         count += 1
# print("number of digits:",count)
# ch = input("enter characters: ")
# count = 0
# for chr in ch:
#     if chr in "aeiouAeiou":
#         count += 1
# print("total count is : ", count)
# n = int(input("enter your digit sir : "))
# sign = -1 if n < 0 else 1
# n = abs(n)

# rev = 0
# while n > 0:
#     digit = n%10
#     rev = rev*10+digit
#     n = n//10
# rev = rev*sign
# print("Reversed number :", rev)
# n = int(input("enter number : "))
# a =0
# b = 1
# for i in range(n):
#     print(a, end="")
#     c = a+b
#     a = b
#     b = c
# n = int(input("Enter number : "))
# if n <= 1:
#     print("not prime")
# else:
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             print("not prime")
#             break
#     else:
#             print("prime")
# n = int(input("Enter number sir : "))
# if n <= 1:
#     print("not prime")
# else:
#     is_prime = True
#     for i in range(2, n):
#         if i%n == 0:
#             is_prime = False
#     if is_prime:
#         print("Prime")
#     else:
#         print("not prime")
# n = int(input("Enter digit sir : "))
# for i in range(1, n+1):
#     if(n%i == 0):
#         print(i,end="")
# n = int(input("enter number : "))
# largest = 0
# while n > 0:
#     digit = n%10

#     if digit > largest:
#         largest = digit
#     n = n//10
# print(largest)
