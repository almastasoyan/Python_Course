def arithmetic_operation(my_str):
    num1, operator, num2 = my_str.split()
    num1 = int(num1)
    num2 = int(num2)
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1- num2
    elif operator == "*":
        return num1 * num2
    elif operator == "//":
        if num1 == 0 or num2 == 0:  
            return -1
        return num1 // num2
    
print(arithmetic_operation("12 + 12"))    


def is_disarium(num):
    total =0
    str_num = str(num)
    for i,j in enumerate(str_num):
       total += int(j) ** (i+1)
    return (total == num)


print(is_disarium(135))



def convert_to_hex(s):
    str1= ""  
    for i in s:
        str1 += str(ord(i))
    return str1

     

def check_score(s):
	my_dict = {'#':5,'O':3,'X':1,'!':-1,'!!':-3,'!!!':-5}
	total = 0
	for i in range(len(s)):
		for j in range(len(s[i])):
			total += my_dict[s[i][j]]
	if total < 0:
		return 0
	return total

print(check_score([["#", "!"],["!!", "X"]]))      



def convert_to_hex(s):
    str1= ""  
    for i in s:
        str1 += hex(ord(i))[2:] + " "
    return str1
print(convert_to_hex("hello world")) 

   

def tidy_link(url, name, *hover_text):
    if hover_text:
        return  f"[{name} ]( {url} {hover_text[0]})" 
    else:
        return  f"[ {name} ]( {url} )"

print(tidy_link("https://edabit.com/challenges", "this", "Go to the challenges!")) 
print(tidy_link("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "Click Me!"))




def pluralize(lst):
    res = []
    for i in lst:
        if lst.count(i) > 1:
            res.append(i + "s")
        else:
           res.append(i)
    return set(res)
   
print(pluralize(["cow", "pig", "cow", "cow"]))  




def censor_string(txt, lst, char):
    for i in lst:
        txt= txt.replace(i, char * len(i))
    return txt

print(censor_string("Today is a Wednesday!", ["Today", "a"], "-")) 




def uncensor(txt, vowels):
    for i in vowels:
        txt = txt.replace("*", i, 1)  
    return txt     
print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo")) 


import random

def randfloat(start,stop):
    num = random.uniform(start, stop)
    return num


print(randfloat(1.3, 5.6))



