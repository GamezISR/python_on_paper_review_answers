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

