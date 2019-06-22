"""
Presidential Initiative for Artificial Intelligence and 

Computing (PIAIC)

https://www.piaic.org

AI Program

Python Programming Assignment 1

Quarter I: 

AI-101 Fundamentals of Programming using Python

First Quarter 2019 (12 Weeks)



1. Calculate Area of a Circle

Write a Python program which accepts the radius of a circle from the user and compute the area.

Program Console Sample Output 1:

Input Radius: 0.5

Area of Circle with radius 0.5 is 0.7853981634

References:

https://www.mathsisfun.com/geometry/circle-area.html
"""
"""
from math import pi
radius = float(input("Input Radius: "))
area = pi * (radius ** 2)
print("Area of Circle with radius", radius, "is", area)
"""
"""
2. Check Number either positive, negative or zero

Write a Python program to check if a number is positive, negative or zero

Program Console Sample Output 1:

Enter Number: -1

Negative Number Entered

Program Console Sample Output 2:

Integer: 3

Positive Number Entered

Program Console Sample Output 3:

Integer: 0

Zero Entered
"""
"""
number = int(input("Enter Number: "))
if number > 0:
	print("Positive Number Entered")
elif number < 0:
	print("Negative Number Entered")
else:
	print("Zero Entered")
"""
"""
3. Divisibility Check of two numbers

Write a Python program to check whether a number is completely divisible by another number. Accept two integer 

values form the user

Program Console Sample Output 1:

Enter numerator: 4

Enter Denominator: 2

Number 4 is Completely divisible by 2
Program Console Sample Output 2:

Enter numerator: 7

Enter Denominator: 4

Number 7 is not Completely divisible by 4
"""
"""
numerator = int(input("Enter numerator: "))
denominator = int(input("Enter Denominator: "))
if numerator % denominator == 0:
	print("Number", numerator, "is Completely divisible by", denominator)
else:
	print("Number", numerator, "is not Completely divisible by", denominator)
"""
"""
4. Days Calculator

Write a Python program to calculate number of days between two dates

Program Console Output:

Enter a date in (dd/mm/yy) format: 12/12/2018

Enter a date in (dd/mm/yy) format: 16/12/2018

There are 4 days in between 12/12/2018 and 16/12/18
"""
"""
days_in_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date_1 = input("Enter a date in (dd/mm/yy) format: ")
date_2 = input("Enter a date in (dd/mm/yy) format: ")
days = int(date_2[:2]) - int(date_1[:2])
months = int(date_2[3:5]) - int(date_1[3:5])
years = int(date_2[-2:]) - int(date_1[-2:])
years_to_days = years * 365
months_to_days = 0
for m in range(int(date_1[3:5]), int(date_2[3:5])):
	months_to_days += days_in_months[m]
total_days = days + months_to_days + years_to_days
print("There are", total_days, "days in between", date_1, "and", date_2)
"""
"""
5. Calculate Volume of a sphere

Write a Python program to get the volume of a sphere, please take the radius as input from user

Program Console Output:

Enter Radius of Sphere: 1

Volume of the Sphere with Radius 1 is 4.18

Reference:

https://keisan.casio.com/exec/system/1223372883
"""
"""
from math import pi
radius = int(input("Enter Radius of Sphere: "))
sphere_volume = (4 / 3) * pi * (radius ** 3)
print("Volume of the Sphere with Radius", radius, "is", round(sphere_volume, 2))
"""
"""
6. Copy string n times

Write a Python program to get a string which is n (non-negative integer) copies of a given string. 

Program Console Output:

Enter String: Hi

How many copies of String you need: 4

4 Copies of Hi are HiHiHiHi
"""
"""
str = input("Enter String: ")

n = int(input("How many copies of String you need: "))

print(n, "Copies of", str, "are", str * n)
"""
"""
7. Check if number is Even or Odd

Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate 

message to the user

Program Console Output 1:

Enter Number: 4

4 is Even

Program Console Output 2:

Enter Number: 9

9 is Odd
"""
"""
num = int(input("Enter Number: "))
if num % 2 == 0:
	print(num, "is Even")
else:
	print(num, "is Odd")
"""
"""
8. Vowel Tester

Write a Python program to test whether a passed letter is a vowel or not

Program Console Output 1:

Enter a character: A

Letter A is Vowel

Program Console Output 2:

Enter a character: e

Letter e is Vowel
Program Console Output 2:

Enter a character: N

Letter N is not Vowel
"""
"""
chr = input("Enter a character: ")
if chr in "AEIOUaeiou":
	print("Letter", chr, "is Vowel")
else:
	print("Letter", chr, "is not Vowel")
"""
"""
9. Triangle area

Write a Python program that will accept the base and height of a triangle and compute the area

Program Console Sample 1:

Enter magnitude of Triangle base: 4

Enter Magnitude of Triangle Height: 4

Area of a Triangle with Height 4 and Base 4 is 8

Reference:

https://www.mathgoodies.com/lessons/vol1/area_triangle
"""
"""
base = int(input("Enter magnitude of Triangle base: "))

height = int(input("Enter Magnitude of Triangle Height: "))

triangle_area = int((1 / 2) * base * height)
print("Area of a Triangle with Height", height, "and Base", base, "is", triangle_area)
"""
"""
10. Calculate Interest

Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number 

of years

Program Console Sample 1:

Please enter principal amount: 10000

Please Enter Rate of interest in %: 0.1

Enter number of years for investment: 5

After 5 years your principal amount 10000 over an interest rate of 0.1 % will be 16105.1
"""
"""
principal = int(input("Please enter principal amount: "))

interest = float(input("Please Enter Rate of interest in %: "))

years = int(input("Enter number of years for investment: "))

new_principal = (principal * (1 + interest)) ** years

print("After", years, "years your principal amount", principal, "over an interest rate of", interest, "% will be",  new_principal / (10 ** 16))
"""
"""
11. Euclidean distance

Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

Program Console Sample 1:

Enter Co-ordinate for x1: 2

Enter Co-ordinate for x2: 4

Enter Co-ordinate for y1: 4

Enter Co-ordinate for y2: 4

Distance between points (2, 4) and (4, 4) is 2

Reference:

https://en.wikipedia.org/wiki/Euclidean_distance
"""
"""
x1 = int(input("Enter Co-ordinate for x1: "))

x2 = int(input("Enter Co-ordinate for x2: "))

y1 = int(input("Enter Co-ordinate for y1: "))

y2 = int(input("Enter Co-ordinate for y2: "))

distance = int((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1 / 2))

print(f"Distance between points ({x1}, {y1}) and ({x2}, {y2}) is {distance}")
"""
"""
12. Feet to Centimeter Converter

Write a Python program to convert height in feet to centimetres.

Program Console Sample 1:

Enter Height in Feet: 5

There are 152.4 Cm in 5 ft

Reference:

https://www.rapidtables.com/convert/length/feet-to-cm.html
"""
"""
feet = int(input("Enter Height in Feet: "))
cm = feet * 30.48
print("There are 152.4 Cm in 5 ft")
"""
"""
13. BMI Calculator

Write a Python program to calculate body mass index
Program Console Sample 1:

Enter Height in Cm: 180

Enter Weight in Kg: 75

Your BMI is 23.15

Reference:

https://www.thecalculatorsite.com/articles/health/bmi-formula-for-bmi-calculations.php
"""
"""
height = float(input("Enter Height in Cm: "))

weight = float(input("Enter Weight in Kg: "))

height *= (10 ** (-2))

bmi = weight / (height ** 2)

bmi = round(bmi, 2)

print(f"Your BMI is {bmi}")
"""
"""
14. Sum of n Positive Integers

Write a python program to sum of the first n positive integers

Program Console Sample 1:

Enter value of n: 5

Sum of n Positive integers till 5 is 15
"""
"""
n = int(input("Enter value of n: "))

n2 = sum(range(n + 1))

print(f"Sum of n Positive integers till {n} is {n2}")
"""
"""
15. Digits Sum of a Number

Write a Python program to calculate the sum of the digits in an integer

Program Console Sample 1:

Enter a number: 15

Sum of 1 + 5 is 6

Program Console Sample 2:

Enter a number: 1234

Sum of 1 + 2 + 3 + 4 is 10
"""
"""
num = input("Enter a number: ")
i, sum = 0, 0
print("Sum of", end = " ")
for n in num:
	sum += int(num[i])
	print(f"{n}", end = " ")
	if i < (len(num) - 1):
		print("+", end = " ")
	i += 1
print(f"is {sum}")
"""
"""
16. Decimal to Binary Converter

Write a Python program to convert an decimal integer to binary

Program Console Sample 1:

Enter a decimal number: 5

Binary Representation of 5 is 101

Program Console Sample 2:

Enter a decimal number: 32

Binary Representation of 32 is 100000

Reference:

https://www.rapidtables.com/convert/number/decimal-to-binary.html
"""
"""
dec_num = int(input("Enter a decimal number: "))
bin_num = ""
while True:
	bin_num += str(dec_num % 2)
	dec_num //= 2
	if dec_num == 0:
		break
bin_numb = bin_num
bin_num = ""
for i range(1, len(bin_num) + 1):
	bin_num += bin_numb[-i]
print(f"Binary Representation of {dec_num} is {bin_num}")
"""
"""
17. Binary to Decimal Converter

Write a program to convert binary number to Decimal number

Program Console Sample 1:

Enter a Binary number: 1101

Decimal Representation of 1101 is 13

Program Console Sample 2:

Enter a Binary number: 1001

Decimal Representation of 1001 is 9
Reference:

https://www.rapidtables.com/convert/number/binary-to-decimal.html
"""
"""
bin_num = input("Enter a Binary number: ")
dec_num = 0
i = 0
for digit in bin_num:
	dec_num += int(bin_num[i]) * (2 ** ((len(bin_num) - 1) - i))
	i += 1
print(f"Decimal Representation of {bin_num} is {dec_num}")
"""
"""
18. Vowel and Consonants Counter

Input a text and count the occurrences of vowels and consonant

Program Console Sample 1:

Enter text: QuickBrownFoxJumpsovertheDog

Vowels: 9

Consonants: 19
"""
"""
str = input("Enter text: ")
vowels = 0
consonants = 0
for chr in str:
	if chr in "AEIOUaeiou":
		vowels += 1
	elif not(chr.isalpha()):
		continue
	else:
		consonants += 1
print(f"Vowels: {vowels}")

print(f"Consonants: {consonants}")
"""
"""
19. Palindrome tester

Write a program to check whether given input is palindrome or not

Program Console Sample 1:

Enter text: AHA

Text AHA is Palindrome

Program Console Sample 2:

Enter text: Hello

Text Hello is not a Palindrome
"""
"""
str = input("Enter text: ")
str2 = str[::-1]
if str == str2:
	print(f"Text {str} is Palindrome")
else:
	print(f"Text {str} is not Palindrome")
"""
"""
20. Count Alphabets, Numbers and Special Characters

Write a Python program that accepts a string and calculate the number of digits and letters

Program Console Sample 1:

Enter text: Python 3.2

Numbers = 2

Alphabets = 6

Special Characters = 1

Spaces = 1 
"""
"""
str = input("Enter text: ")
alphabets = 0
digits = 0
spaces = 0
special = 0
for chr in str:
	if chr.isalpha():
		alphabets += 1
	elif chr.isdigit():
		digits += 1
	elif chr.isspace():
		spaces += 1
	else:
		special += 1
print(f"Numbers = {digits}")

print(f"Alphabets = {alphabets}")

print(f"Special Characters = {special}")

print(f"Spaces = {spaces}")
"""
"""
21. Write a Python program to construct the following pattern

* 

* * 

* * * 

* * * * 

* * * * * 

* * * * 

* * * 

* * 

*
"""
"""
ch = "*"
i = 0
while i < 10:
	if i < 5:
		j = i + 1
	else:
		j = 9 - i
	while j > 0:
		print(ch, end = " ")
		j -= 1
	print()
	print()
	i += 1
"""
"""
22. Write a Python program to construct the following pattern

1 

1 2 

1 2 3 

1 2 3 4 

1 2 3 4 5 

1 2 3 4 

1 2 3 

1 2

1
"""
"""
i = 0
while i < 10:
	if i < 5:
		j = 9 - i
	else:
		j = i + 1
	k = 1
	while j < 10:
		print(k, end = " ")
		k += 1
		j += 1
	print()
	print()
	i += 1
"""
"""
23. Write a Python program to construct the following pattern

1

22

333

4444

55555

666666

7777777

88888888

999999999

"""
"""
i = 1
while i < 10:
	j = 1
	while j <= i:
		print(i, end = "")
		j += 1
	print()
	print()
	i += 1
"""
"""
"""