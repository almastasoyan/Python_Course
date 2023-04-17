'''1. Create a function which returns the number of true values there are in an array.'''

def countTrue(my_list):
    result=[]
    for i in my_list:
        if i == True:
            result.append(i)
    return len(result)


print(countTrue([True, False, False, True, False])== 2 )
print(countTrue([False, False, False, False]) == 0)
print(countTrue([])==0) 




'''2. Create a function that validates whether a number n is within the bounds of lower and upper. Return false if n is not an integer.'''

def intWithinBounds(num1, num2, num3):

    if isinstance(num1,float) or num1 == num3:
        return False
    elif num1 >= num2 and num1 < num3:
        return True


print(intWithinBounds(3, 1 ,9) == True)
print(intWithinBounds(6, 1, 6)== False)
print(intWithinBounds(4.5, 3, 8) == False)




'''3. Create a function that takes three values:'''

def longestTime(h, m, s ):
    h_sec = h * 3600
    m_sec= m * 60
 
    max_time = max(h_sec, m_sec, s)
    if max_time== h_sec:
        return h
    elif max_time == m_sec:
        return m
    elif max_time == s:
        return s 


print(longestTime(1, 59, 3598)== 1)
print(longestTime(2, 300, 15000)== 300)
print(longestTime(15, 955, 59400)== 59400)  




'''4. Create a function that takes the month and year (as integers) and returns the number of days in that month.'''

def days(month, year):
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


print(days(2, 2018)==28)  
print(days(4, 654)==30)  
print(days(2, 200)==28)  
print(days(2, 1000)==28) 




'''5. Create a function that takes a string and censors words over four characters with *.'''

def censor(my_str):
    my_lst = my_str.split()
    result = []
    for i in my_lst:
        if len(i) > 4:
            result.append("*" * len(i))
        else:
            result.append(i)

    return " ".join(result)


print(censor("The code is fourty")  == "The code is ******")
print(censor("Two plus three is five") == "Two plus ***** is five")
print(censor("aaaa aaaaa 1234 12345") == "aaaa ***** 1234 *****")




'''6. Given a sentence, create a function that replaces every "a" as an article with "an absolute". It should return the same string without any change if it doesn't have any "a".'''

def absolute(x):
    my_list = x.split()
    result = []
    for i in my_list:
        if i == "a":
            result.append(len(i) * "an absolute")
        if i == "A":
            result.append(len(i) * "An absolute")
        else:
            result.append(i)
    return " ".join(result)        


print(absolute("I am a champion!!!")== "I am an absolute a champion!!!")
print(absolute("Such an amazing bowler.") == "Such an amazing bowler.")
print(absolute("A man with no haters.") == "An absolute man with no haters.")




'''7. Return an Array of Subarrays
Write a function that takes three arguments (x, y, z) and returns an array containing x subarrays (e.g. [[], [], []]), each containing y number of item z.'''

def matrix(x, y, z):
    
    result = []
    for i in range(x):       
        subarrays = [z] * y
        result.append(subarrays)
  
    return result


print(matrix(3, 2, 3) == [[3, 3], [3, 3], [3, 3]])
print(matrix(2, 1, "edabit") == [["edabit"], ["edabit"]])
print(matrix(3, 2, 0) == [[0, 0], [0, 0], [0, 0]])




'''8. Given a string of numbers separated by a comma and space, return the product of the numbers.'''

def multiplyNums(numbers):
    return eval(numbers.replace(", ", "*"))


print(multiplyNums("2, 3")==6)
print(multiplyNums("1, 2, 3, 4") == 24)
print(multiplyNums("54, 75, 453, 0") == 0)
print(multiplyNums("10, -2") == -20)




'''9. Create a function that takes a string road and returns the car that's in first place. The road will be made of "=", and cars will be represented by letters in the alphabet.'''

def firstPlace(str_road):
    
    if not str_road:
        return "No road available"
    result1= []
    result2 = []
    for i in str_road:
        if i == "=":
            result1.append(i)
        else:
            result2.append(i)

    return result2[-1]


print(firstPlace("====b===O===e===U=A==") == "A")
print(firstPlace("e==B=Fe") == "e")
print(firstPlace("proeNeoOJGnfl") == "l")





'''10. Create a function that takes an array of numbers between 1 and 10 (excluding one number) and returns the missing number.'''

def missingNum(my_list):
    x  = sum(range(1,11))
    my_list_sum = sum(my_list)
    return x - my_list_sum
 

print(missingNum([1, 2, 3, 4, 6, 7, 8, 9, 10]) == 5)
print(missingNum([7, 2, 3, 6, 5, 9, 1, 4, 8]) == 10)
print(missingNum([10, 5, 1, 2, 4, 6, 8, 3, 9]) == 7)







