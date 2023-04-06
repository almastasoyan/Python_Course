'''1. Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.'''

x = input("enter name ")
y = {
    "key": 
     "Luke, I am your"
     }
if x == "Darth Vader":
    print(y["key"][:] + " father")
elif x == "Liya":
    print(y["key"][:] + " sisther")
elif x == "Han":
    print(y["key"][:] + " brother in law.")      
elif x == "R2D2":
    print("biib biibib bib")




'''2. Create a function that takes damage and speed (attacks per second) and returns the amount of damage after a given time.
Examples
40, 5, "second"  ➞ 200
100, 1, "minute" ➞ 6000
2, 100, "hour" ➞ 720000
Notes
Return "invalid" if damage or speed is negative.'''

x = "minute"
y = 100
if x == "second":
        z = 5
elif x == "minute":
        z = 60
elif x == "hour":
        z = 3600

print(y* z)
       



'''3. Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.'''

x = ["A", 0, "Edabit", 1729, "Python", "1729"]

print ([i for i in x if isinstance(i,int)])




'''4. Create a function that takes a number as an argument and returns True or False depending on whether the number is symmetrical or not. A number is symmetrical when it is the same as its reverse'''

x = 44444
y = str(x)
z = (y[::-1])
print(z == y)




'''5. Create a function that changes all the elements in a list as follows:'''

result = []
x = ["a", 12, True]
for i in x:
    if (isinstance(i,str)):
        result.append(f'{i.title()[:]}!')

    if (isinstance(i,int) and (i % 2 == 0)):
        result.append(i +1 )
   
    if (isinstance(i,bool)):
         result.append(not(i))
print(result)




'''6. Create a function that takes a string s and returns a list of two-paired characters. If the string has an odd number of characters, add an asterisk * in the final pair.'''

x = "airforces"
n = 2
if len(x) % 2 == 0:
    print([x[i:i+n] for i in range(0, len(x), n)])

else:
     y = (f'{x[:]}*')
     print([y[i:i+n] for i in range(0, len(y), n)])  
  



'''7. Create a function that takes two parameters and, if both parameters are strings, add them as if they were integers or if the two parameters are integers, concatenate them.'''

x = '1'
y = 2
if isinstance(x,int) and isinstance(y,int):
    print(str(x) + str(y))

if isinstance(x,str) and isinstance(y,str):
    print (int(x)+ int(y))

else:
    print(None)




'''8. Write a function that does the following operations: adding, subtracting, dividing, or multiplying values. It is simply referred to as variable operation variable. Of course, the variables have to be defined, but in this challenge the variables will be defined for you. All you have to do is look at the variables, do some string to integer conversions, use some if conditionals, and combine them based on the operation.
The numbers and operation will be given as strings, and you should return the value as a string as well.
divide, go ahead and round down to an integer.'''

x = "0"
y = "3"
z =  "divide"

if z == "add":
  print(str(int(x) + int(y)))

elif z == "subtract": 
  print(str(int(x) - int(y)))

elif z =="divide":
    if x =="0" or y == "0":
      print("undefined")
    else:
      print(str(int(x) // int(y)))




'''9. Check if the given string consists of only letters and spaces and if every letter is in lower case.'''

x = "python"
if(any(i.islower() for i in x) and not any(i.isdigit() for i in x)):
    print(True)
else:
    print(False)




'''10. Write a function that takes a list and determines whether it's strictly increasing, strictly decreasing, or neither.'''

x = [3, 2, 1]

if x[0] < x[0+1] and x[1] < x[1+1]:
    print("increasing")

elif x[0] > x[0+1] and x[1] > x[1+1]:
    print("decreasing")

else:
    print("neither")



