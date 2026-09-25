# ex1
r = float(input('Enter radius :'))
pi = 3.14
area = pi * r ** 2
print(f"circle area = {area}")
# ex2
c = float(input("Enter Celsius Temperature:"))
convert = (c *1.8)+ 32
print(f"{c:g} (C) = {convert} (F)")
#ex3
num = int(input("Enter number: "))
prime = True
if num < 1:
    prime = False
else:
    for i in range(2, num + 1):
        if num % i == 0:
            prime = False
            break
        else:
            prime = True
if prime:
    print("it is a prime number")
else:
    print("it's not  prime number")
#ex4
num = int(input("Enter number: "))
z = 0
for i in range(1, num):
    if num % i == 0:
        z += i
if z == num and num > 0:
    print("Perfect number")
else:
    print("Not a perfect number")
#ex5
color_list =["Red", "Green", "Yellow","Blue","Violet"]
color = input("Enter your fav color: ")
if color in color_list:
    index = color_list.index(color)
    print(f"Your color is in {index} in my list")
else:
    print("Sorry, i couldn't find")
#ex6
range1 = list(range(0,7))
print(range1)
range2 = list(range(1,11,3))
print(range2)
range3 = list(range(5,0,-1))
print(range3)
range4 = list(range(6,-3,-2))
print(range4)
#ex7
def remove_dollar_sign(s):
    return s.replace("$", "")
text = "hhahhhahah$$$$hhaha"
fix = remove_dollar_sign(text)
print(text)
print("after delete ($)", fix)
#ex8
def extract_list(i):
    even_list = []
    for num in i:
        if num % 2 == 0:
            even_list.append(num)
    return even_list
list = [1,4,-5,10]
result = extract_list(list)
print(result)
#ex9
num = int(input("Enter the number:"))
fac = 1
for i in range(1, num+1):
    fac *= i
print(f"Factorial of {num} is {fac}")
#ex10
def all_devisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors
div = int(input("Enter a number: "))
result = all_devisors(div)
print(f"All divisors of {div} are: {result}")
#ex11
import math
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"The distance between points ({x1}, {y1}) and ({x2}, {y2}) is: {distance}")
#ex12
def point_rectangle(m,n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
print("rectangle 4x5: ")
point_rectangle(4, 5)