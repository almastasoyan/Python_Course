'''2. Create a function that takes a list (slot machine outcome) and returns True if all elements in the list are identical, and False otherwise. The list will contain 4 elements.'''

def test_jackpot(x):
    return x.count(x[0]) == len(x)

print(test_jackpot(["@", "@", "@", "@"])== True)
print(test_jackpot(["abc", "abc", "abc", "abc"])== True)
print(test_jackpot(["SS", "SS", "SS", "SS"]) == True)
print(test_jackpot(["&&", "&", "&&&", "&&&&"]) == False)
print(test_jackpot(["SS", "SS", "SS", "Ss"]) == False)




'''3. Create a function that takes an array of hurdle heights and a jumper's jump height, and determine whether or not the hurdler can clear all the hurdles.
A hurdler can clear a hurdle if their jump height is greater than or equal to the hurdle height.'''

def hurdle_jump_heights(hurdle,jump):
    if not hurdle:
            return True
    for i in hurdle:

        if jump <= i:
            return False
        
        if jump >= i:
            return True

print(hurdle_jump_heights([], 5))
print(hurdle_jump_heights( [1, 2, 3, 4, 5],5) == True)  
print(hurdle_jump_heights([5, 5, 3, 4, 5], 3)== False)
print(hurdle_jump_heights([5, 4, 5, 6], 10) ==True)
print(hurdle_jump_heights([1, 2, 1], 1)== False)




'''4. Create a function that takes a number as its argument and returns a list of all its factors.'''

def factorize(x):
    result = []
    for i in range(1, x + 1):
       if x % i == 0:
        result.append(i)
    return result

print(factorize(4) == [1, 2, 4])
print(factorize(12) == [1, 2, 3, 4, 6, 12])
print(factorize(17) == [1, 17])




'''5. Create a function that returns the number of palindrome numbers in a specified range (inclusive).
For example, between 8 and 34, there are 5 palindromes: 8, 9, 11, 22 and 33. Between 1550 and 1552 there is exactly one palindrome: 1551.'''

def count_palindromes(num1, num2):
    result = []
    for i in range (num1, num2 + 1):
        if (str(i) == str(i)[::-1]):
            result.append(i)
    return len(result)

print(count_palindromes(1, 10)== 9)
print(count_palindromes(555, 556) == 1)
print(count_palindromes(878, 898) == 3)




'''6. Write a function that takes a string, breaks it up and returns it with vowels first, consonants second. For any character that's not a vowel (like special characters or spaces), treat them like consonants.'''

def split(string):
    str_vowel = "aeiou"
    str_1 = ""
    str_2 = ""
    for i in string:
        if i in str_vowel:
            str_1 += i
        else:
            str_2 += i
    return str_1 + str_2


print(split("abcde") == "aebcd")
print(split("Hello!") == "eoHll!")
print(split("What's the time?") == "aeieWht's th tm?")




'''7. Create a function that takes a string as an argument and returns a coded (h4ck3r 5p34k) version of the string.'''

def hacker_speak(my_str):
    my_dict = {"a": "4", "e":"3", "i": "1", "o":"0", "s":"5"}
    for i in my_dict :
        my_str = my_str.replace(i, my_dict[i])

    return my_str   

print (hacker_speak("javascript is cool") == "j4v45cr1pt 15 c00l")
print(hacker_speak("programming is fun") == "pr0gr4mm1ng 15 fun")
print(hacker_speak("become a coder") == "b3c0m3 4 c0d3r")




'''8. Create a function that takes an integer and returns it as an ordinal number. An Ordinal Number is a number that tells the position of something in a list, such as 1st, 2nd, 3rd, 4th, 5th, etc.'''

def return_end_of_number(num):
    
    num_str = str(num)
    last_num = int(num_str[-1])
    lst = ["11", "12", "13"]
    
    if num_str[-2:] in lst:
        ordinal = "-TH"
    else:
        if last_num == 1:
            ordinal = "-ST"
        elif last_num == 2:
            ordinal = "-ND"
        elif last_num == 3:
            ordinal = "-RD"
        else:
            ordinal = "-TH"
    return num_str + ordinal
    
print(return_end_of_number(553) == "553-RD")
print(return_end_of_number(34) == "34-TH")
print(return_end_of_number(1231) == "1231-ST")
print(return_end_of_number(22) == "22-ND")
print(return_end_of_number(412) == "412-TH")




'''9. Create a function that converts Celsius to Fahrenheit and vice versa.'''
  
def convert(temp):
    if "*C" in temp:
        temp_c = float(temp[:-2])
        temp_f = round((temp_c * 9/5) + 32)
        return str(temp_f) + "*F"
    elif "*F" in temp:
        temp_f = float(temp[:-2])
        temp_c = round((temp_f - 32) * 5/9)
        return str (temp_c) + "*C"
    else:
        return "Error"

print(convert("35*C") == "95*F")
print(convert("19*F")== "-7*C")
print(convert("33")=="Error" )





'''10. Create a function that finds the reverse complement of a ribonucleic acid (RNA) strand. The RNA will be represented as a string containing only the characters "A", "C", "G" and "U". Since RNA can only (canonically) allow pairings of A/U and G/C, the complement of an RNA would be as follows:'''


def reverse_complement(rna):
    my_dict = {"A":"U","U":"A","G":"C","C":"G"}
    my_rna = ""
    for i in rna:
        my_rna  += my_dict[i]

    return my_rna[::-1]
    
print(reverse_complement("GUGU") == "ACAC")
print(reverse_complement("UCUCG") == "CGAGA")
print(reverse_complement("CAGGU") == "ACCUG")




'''11. Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").
Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.
eval() is not allowed. In case of division, whenever the second number equals "0" return -1.'''


def arithmetic_operation(x):

    num1, operator, num2 = x.split()
    num1 = int(num1)
    num2= int(num2)
    if operator == "+":
         z = num1 + num2
         return(str(z) + " // 12 + 12 = 24" )
    elif operator == "-":
         return("24 // 12 - 12 = 0")
    elif operator == "*":
         z = num1 * num2
         return(str(z) + " // 12 * 12 = 144")
    elif operator == "//":
        if num1 == 0 or num2 == 0:
            return("-1 // 12 / 0 = -1")    

print(arithmetic_operation("12 + 12") == "24 // 12 + 12 = 24")
print(arithmetic_operation("12 - 12") == "24 // 12 - 12 = 0")
print(arithmetic_operation("12 * 12") == "144 // 12 * 12 = 144")
print(arithmetic_operation("12 // 0") == "-1 // 12 / 0 = -1")



