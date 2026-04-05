"""
BAN 5600 - Homework 2
Name: Ryan Cooper
Student ID: 855712999
Professor: Omar El Mghari
Date: 4/5/2026

PART 2 - The "postal service" of the digital world

1) Client/Server Architecture
In my case, Python would mostly work like a client. Since I work in supply
chain, I can imagine a Python script asking a system for order details,
shipment updates, or inventory information. The system that stores that
information would be the server, and my script would receive the response.
So I think of it like my script asking a question and the server sending
back the answer.

2) APIs
If I were creating an API for my work, one useful feature would be the
ability to check order or shipment status. For example, a user could enter
an order number and get back the current status, tracking details, or an
expected delivery date. That would save time because it would reduce the
need to manually check different systems.

3) DNS / fake website question
If the DNS system was hacked and changed my bank's website to a fake
server, the browser could still warn me if something looked wrong with the
website security. Real banking websites normally use HTTPS and valid
security certificates. If the fake site does not have the correct
certificate, the browser would usually show a warning that the connection
is not private or the site may not be secure.

4) Why this matters for Python automation
This matters because many Python automation tasks depend on sending
requests and receiving responses from other systems. In supply chain work,
that could mean checking order updates, tracking shipments, or pulling data
for reports. Understanding how this process works helps me see how Python
can be used in a practical and safe way for real business tasks.
"""

# I import math because I need math functions like sin, pi, sqrt, and log.
import math

# I import random because I need random decimal numbers for the Box-Muller formula.
import random

print("BAN 3110 - Homework 2")
print()

# --------------------------------------------------
# Question 1: Gaussian random number
# --------------------------------------------------
print("1) Gaussian random number using the Box-Muller formula")

# random.random() gives a random float between 0 and 1.
# The Box-Muller formula needs two random values, u and v.
u = random.random()
v = random.random()

# I use the Box-Muller formula to generate a Gaussian random number.
# math.sin() gives sine
# math.pi is the value of pi
# math.sqrt() gives square root
# math.log() gives natural log
z = math.sin(2 * math.pi * v) * math.sqrt(-2 * math.log(u))

# I print the values so the result can be seen clearly.
print("u =", u)
print("v =", v)
print("Z =", z)
print()

# --------------------------------------------------
# Question 2: Print two integers in ascending order
# --------------------------------------------------
print("2) Two integers in ascending order")

# I use input() to ask the user for values.
# I use int() because the question asks for integers.
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

# I use an if statement because I need to compare the two numbers.
# If a is smaller than or equal to b, I print them as a b.
# Otherwise, I print them as b a so the output is always ascending.
if a <= b:
    print(a, b)
else:
    print(b, a)

print()

# --------------------------------------------------
# Question 3: Strictly ascending or descending
# --------------------------------------------------
print("3) Check if three values are strictly ascending or descending")

# I use float() because double values can include decimals.
x = float(input("Enter x: "))
y = float(input("Enter y: "))
z2 = float(input("Enter z: "))

# This checks if x < y < z2 or x > y > z2.
# If either condition is true, the result will be True.
result = (x < y < z2) or (x > y > z2)

print(result)
print()

# --------------------------------------------------
# Question 4: Earthquake magnitude descriptor
# --------------------------------------------------
print("4) Earthquake magnitude descriptor")

# I use float() because earthquake magnitude can be a decimal number.
magnitude = float(input("Enter earthquake magnitude: "))

# I use if / elif / else because the answer depends on the range
# where the earthquake magnitude falls.
if magnitude < 2.0:
    descriptor = "Micro"
elif magnitude < 3.0:
    descriptor = "Very minor"
elif magnitude < 4.0:
    descriptor = "Minor"
elif magnitude < 5.0:
    descriptor = "Light"
elif magnitude < 6.0:
    descriptor = "Moderate"
elif magnitude < 7.0:
    descriptor = "Strong"
elif magnitude < 8.0:
    descriptor = "Major"
elif magnitude < 10.0:
    descriptor = "Great"
else:
    descriptor = "Meteoric"

print("A magnitude", magnitude, "earthquake is considered to be a", descriptor, "earthquake.")
print()

# --------------------------------------------------
# Question 5: range explanation
# --------------------------------------------------
print("5) Answer to print(range(1,22,3))")

# In Python 3, printing range directly shows the range object.
print("In Python 3, it prints: range(1, 22, 3)")

# These are the actual values created by that range.
print("The numbers in that range are: 1, 4, 7, 10, 13, 16, 19")
print()

# --------------------------------------------------
# Question 6: string code explanation
# --------------------------------------------------
print("6) Answer to the string code question")

# This is the original string.
s = 'I ate it.'

# upper() changes all letters to uppercase.
print(s.upper())

# count('t') counts how many times the letter t appears.
print(s.count('t'))

# split() breaks the sentence into a list of words.
w = s.split()
print(w)

print()
print("Explanation:")
print("s.upper() prints: I ATE IT.")
print("s.count('t') prints: 2")
print("s.split() prints: ['I', 'ate', 'it.']")
print()

print("===================")
print("AI Use Statement")
print("===================")
print("I used ChatGPT as a study support tool to help me")
print("understand parts of the assignment, especially Part 1")
print("where I needed to work with the Box-Muller formula for Gaussian random numbers.")
print("It helped me understand the formula, organize my code, and check my work.")
print("I reviewed the final file myself, ran the code on my own computer")
print("and I am responsible for the final submission and video walkthrough.")