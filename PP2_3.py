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
  else:
    num = str(num)
    print(" ")
  

#Do not alter the following code
#Comment out the following code when running your tests
'''
q1()
q2()
'''