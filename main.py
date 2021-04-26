"""
# ******************-:Basic Program:-********************


# 1.Python Program for factorial of a number

def factorial(num):
    return 1 if (num == 1 or num == 0) else num * factorial(num - 1);


n = int(input("Enter the number: "))
print("Factorial of", n, "is", factorial(n))



# 2.Python Program for simple interest

def s_i(p, r, t):
    return (p * r * t) / 100


principle = int(input("Enter the principle :"))
rate = int(input("Enter the interest rate :"))
time = int(input("Enter the time :"))
print("Simple Interest is: ", s_i(principle, rate, time))



# 3.Python Program for compound interest

def c_i(p, r, t):
    a = p * (pow((1 + r / 100), t))
    com_int = a - p
    print("Compound Interest: ", round(com_int, 2))


principle = int(input("Enter the principle :"))
rate = int(input("Enter the interest rate :"))
time = int(input("Enter the time :"))

c_i(principle, rate, time)



# 4.Python Program to check Armstrong Number

num = int(input("enter the number :"))
temp = num
rev = 0
while temp != 0:
    r = temp % 10
    rev = rev + pow(r, 3)
    temp = temp // 10
if rev == num:
    print("Armstrong Number")
else:
    print("Non Armstrong number")



# 5.Python Program for Program to find area of a circle


def area_circle(r):
    area = 3.142 * pow(r, 2)
    print("Area of circle =", round(area, 2), "meter square")


radius = float(input("Enter the radius of circle: "))
area_circle(radius)




# 6.Python program to print all Prime numbers in an Interval

num1 = int(input("Enter the start number :"))
num2 = int(input("Enter the end number :"))
for i in range(num1, num2 + 1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)


# 7.Python Program for n-th Fibonacci number

def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(9))



# 8.Python Program for How to check if a given number
# is Fibonacci number?

num = int(input("Enter the number: "))
sums = 0
a = 1
b = 1
if num == 0 or num == 1:
    print("Yes", num, "is fibonacci number ")
else:
    while sums < num:
        sums = a + b
        b = a
        a = sums
    if sums == num:
        print("Yes,", num, "is fibonacci number ")
    else:
        print("Not ,", num, "is not fibonacci number ")

# 9.Program to print ASCII Value of a character

char = input("Enter the Character:")
print("The ASCII Value of", char, "is", ord(char))


# 10.Python Program for Sum of squares of first n natural numbers

num = int(input("Enter the number: "))
total = 0
for i in range(num + 1):
    if i == 0 and i == 1:
        print(i)
    else:
        total = total + (i*i)

print(total)


# 11.Python Program for cube sum of first n natural numbers

num = int(input("Enter the number: "))
total = 0
for i in range(num + 1):
    if i == 0 and i == 1:
        print(i)
    else:
        total = total + (i*i*i)

print(total)


# 12.Remove " " from string without using pre-define function
st_name = " My  name is khan "
print("original string:", st_name)
st = ''
for i in range(0, len(st_name)):
    if st_name[i] == ' ':
        pass
    else:
        st = st + st_name[i]

print(st)


# ******************-:Array Program:-*******************


# 13.Python Program to find sum of array

total = 0
arr = [5, 6, 9, 7, 8, 6]
for i in arr:
    total += i

print("Sum of Array:", total)

# 14.Python Program to find largest element in an array

arr = [10, 21, 30, 25, 36, 29]
max_num = arr[0]
arr_len = len(arr)
for i in range(1, arr_len):
    if arr[i] > max_num:
        max_num = arr[i]

print("Maximum value: ", max_num)


# 15.Python Program for array rotation

arr = [5, 6, 7, 8, 9, 10]
arr_len = len(arr)
position = 3
rotate_from = 7
arr[:] = arr[position:arr_len] + arr[0:position]

print(arr)


# 16.Python Program for Find remainder of array
# multiplication divided by n

arr = [5, 6, 7, 8, 9, 10]
arr_len = len(arr)
n = 13
total = 1
for i in range(0, arr_len):
    total = total * arr[i]
reminder = total % n
print(total, reminder)


# 17.Python Program to check if given array is Monotonic

arr = [6, 5, 4, 4]
# arr = [5, 15, 20, 10]
inc = 1
dec = 1
arlen = len(arr) - 1
for i in range(0, arlen):
    if arr[i] >= arr[i + 1]:
        inc = inc + 1
    elif arr[i] <= arr[i + 1]:
        dec = dec + 1

if len(arr) == inc or len(arr) == dec:
    print("True")
else:
    print("False")

"""
# ********************-:List Programs:-*******************