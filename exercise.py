#Exercise 2.1
'''
name = (input("Enter your name: "))
print(f"Hello, {name}")
'''
import math
import random
from random import randint

#Exercise 2.2
'''
radius = int(input("Enter a radius: "))
area = 3.14 *(radius**2)
print(f"The area is {area}")
'''
#Exercise 2.3
'''
length = int(input("Enter a length: "))
breadth =int(input("Enter a breadth: "))
area = length*breadth
perimeter =2*(length+breadth)
print(f"The area of rectangle is {area} and the perimeter is {perimeter}")
'''

#Exercise 2.4
'''
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num3 = int(input("Enter a third number: "))
sum = num1+num2+num3
product = num1*num2*num3
average = sum/3
print(f"The sume is {sum}, product is {product}, and average is {average}")
'''
#Exercise 2.5

talent = int(input("Enter a talents: "))
pounds = int(input("Enter a pounds: "))
lot = float(input("Enter a lot: "))
totalTalents = talent*20*32*13.3
totalPound = pounds*32*13.3
totalLots = lot*13.3
totalGrams = totalTalents + totalPound + totalLots
kilograms = int(totalGrams/1000)
grams = int(totalGrams % 1000)
print(f"The weight in modern units is {kilograms} kilograms and {grams} grams")


#Exercise 2.6
'''
num1 = randint(0,9)
num2 = randint(0,9)
num3 = randint(0,9)
num4 = randint(1,6)
num5 = randint(1,6)
num6 = randint(1,6)
num7 = randint(1,6)



print(f"The code1 is {num1}{num2}{num3}")
print(f"The code2 is {num4}{num5}{num6}{num7}")
'''