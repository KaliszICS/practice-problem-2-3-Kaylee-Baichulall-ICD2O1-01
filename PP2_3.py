'''
Lesson: Else if
Author: Kaylee Baichulall
Date Created: Oct 16, 2024
Date Last Modified: Oct 16, 2024
'''

def q1(): 
  word = input("In: ")
  if word [-2:] == "ey":
    print("-eys")
  elif word [-1:] == "y":
    print("-ies")
  elif word [-3:] == "ife":
    print("-ives")
  else:
    print("-s")

def q2(): 
  num = int(input("In: "))
  if num < 0:
    num = str(num)
    print(num + " is negative")
  elif num > 0:
    num = str(num)
    print(num + " is positive")

def q3():
  side1 = float(input("Input a number: "))
  side2 = float(input("Input a number: "))
  side3 = float(input("Input a number: "))
  if (side1 + side2) < side3 or (side1 + side3) < side2 or (side3 + side2) < side1:
    print("No Triangle")
  elif side1 == side2 and side2 == side3 and side1 == side3:
    print("Equilateral")
  elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles")
  else:
    print("Scalene")

#Do not alter the following code
#Comment out the following code when running your tests
'''
q1()
q2()
q3()
'''