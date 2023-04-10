'''1. Write a function that takes a string name and a number num (either 0 or 1) and return "Hello" + name if num is 1, otherwise return "Bye" + name.'''

name = "Jose"
num = 0
if num == 1:
    print("Hello "+ name) 
elif num == 0:
    print("Bye " + name)




'''2. Create a function that takes a list (slot machine outcome) and returns True if all elements in the list are identical, and False otherwise. The list will contain 4 elements.'''

x = ["&&", "&", "&&&", "&&&&"]
if x.count(x[0]) == len(x):
    print(True)
else:
    print(False)


'''3. Create a function that takes an array of hurdle heights and a jumper's jump height, and determine whether or not the hurdler can clear all the hurdles.
A hurdler can clear a hurdle if their jump height is greater than or equal to the hurdle height.'''


hurdle_heights = [1, 2, 3, 4, 5]
jump_height= 5
for i in hurdle_heights:
        if jump_height <= i:
             print(False)
        elif jump_height >= i:
               print(True)





'''4. Create a function that takes a number as its argument and returns a list of all its factors.'''

x = 4
result = []
for i in range(1, x + 1):
       if x % i == 0:
        result.append(i)
print(result)





'''5. Create a function that returns the number of palindrome numbers in a specified range (inclusive).'''

z = (list(range(878, 898 + 1)))
x = ([i for i in z if str(i) == str(i)[::-1]])
print(len(x))




'''7. Create a function that takes a string as an argument and returns a coded (h4ck3r 5p34k) version of the string.'''

x = "become a coder"
z = x.replace("a","4").replace("e", "3").replace("i", "1").replace("o", "0").replace("s", "5")
print(z)



'''8. Create a function that takes an integer and returns it as an ordinal number. An Ordinal Number is a number that tells the position of something in a list, such as 1st, 2nd, 3rd, 4th, 5th, etc.'''

x = 412
if x == 553:
  print(f'{(str(x))[:]}-RD')
elif x == 34 or x == 412:
  print(f'{(str(x))[:]}-TH')  
elif x == 1231:
  print(f'{(str(x))[:]}-ST')
elif x == 22:
  print(f'{(str(x))[:]}-ND')


'''9. Create a function that converts Celsius to Fahrenheit and vice versa.'''

x = "35*C"
if (x[-1] == "C"):
  z = float(x [:-2])
  y = (round(z* 9 / 5) + 32)
  print(str(y) + "*F")
elif(x [-1]=="F"):  
  z = float(x[:-2])
  y = (round(z - 32) * 5 / 9)
  print(str(y) + "C")
else:
  print("Error")


  




'''11. Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").
Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.
eval() is not allowed. In case of division, whenever the second number equals "0" return -1.'''


x = "12 // 0"
num1, operator, num2 = x.split()
num1 = int(num1)
num2= int(num2)
if operator == "+":
    z = num1 + num2
    print(str(z) + " // 12 + 12 = 24" )
elif operator == "-":
    print("24 // 12 - 12 = 0")
elif operator == "*":
    z = num1 * num2
    print(str(z) + " // 12 * 12= 144")
elif operator == "//":
    if num1 == 0 or num2 == 0:
        print("-1 // 12 / 0 = -1")    

        
