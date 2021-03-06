"""
1

Write an algorithm to input three different numbers, multiply the two larger numbers together and output the result. Use the variable: Number1, Number2, and Number3 for your numbers and Answer for your result
"""

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

if number1 < number2 and number1 < number3:
  answer = number2 * number3
elif number2 < number1 and number2 < number3:
  answer = number1 * number3
else:
  answer = number1 * number2
print("The two larger numbers multiplied is ", answer)


"""
2

Write an algorithm to input 1000 numbers. Count how many numbers are positive and how many numbers are zero. Then output the results.
"""
positive = 0
zero = 0

for i in range(1000):
  num = int(input("Enter a number"))
  if num > 0:
    positive = positive + 1
  elif num == 0:
    zero = zero + 1

print("This is how many positives entered: ", positive)
print("This is how many zeros entered: ", zero)

"""
3

Make an algorithm to input numbers, reject any numbers that are negative and count many numbers that are positive. When the number zero is input, the process ends and the count of positive numbers is output.
"""
counter = 0
while True:
  enter = int(input("Enter a number"))
  if enter < 0:
    print("Enter a non negative number.")
  elif enter > 0:
    counter = counter + 1
  else:
    break

print("This is how many positive numbers were entered: ", counter)


"""
4

Write an algorithm to input three different numbers, and then output the largest number.
"""

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
number_3 = int(input("Enter third number: "))

if number1 > number2 and number1 > number3:
  print(number_1, " is the largest number")
elif number2 > number1 and number2 > number3:
  print(number_2, " is the largest number")
else:
  print(number_3, " is the largest number")


"""
5

Write an algorithm in  using a single loop to print 50 names that have been stored in an array called Names.

"""

names = [] #can add names here

for i in names:
  print(i)
#or
for i in range(len(names)):
  print(names[i])




"""
6

Write an algorithm to:
Input a positive integer
Use the value to set up how many other numbers are to be input
Input these numbers
Calculate and output the total and the average of these numbers

"""

how_many_number = int(input("How many numbers do you want? "))
total = 0
for i in range(how_many_number):
  add = int(input("Enter a number: "))
  total = total + add

average = total / how_many_number
print("This is the total: ", total)
print("This is the average: ", average)


"""
7

FizzBuzz

The FizzBuzz challenge is a classic challenge that's used as an interview screening device for computer programmers. It's a very simple programming task but it's used to determine whether the job candidate can actually write code.

Problem Statement
You need to write a program that prints the numbers from 1 to 100 such that:

If the number is a multiple of 3, you need to print "Fizz" instead of that number.
If the number is a multiple of 5, you need to print "Buzz" instead of that number.
If the number is a multiple of both 3 and 5, you need to print "FizzBuzz" instead of that number.


"""

for i in range(1,101):
  if i % 5 == 0 and i % 3 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)

