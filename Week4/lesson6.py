x = "6"
z = int(input(x))
print(z)



x = True
y = (str(x))
print(isinstance(y,str))



person=input('Enter name ->')
x= "Luke, I am your father" 
y = 'Luke, I am your sister'
z = 'Luke, I am your brother in law' 
i = "Biiib biib biib"
print(x * (person == "Darth Vader") + y * (person == 'Leia') + z * (person == 'Han')+ i * (person=="R2D2"))


x = "Bob Jane"
y = "something"
print(y, x)


x = "Celebration"
y =(x.count('a'))+ (x.count('e')) + (x.count('i')) + (x.count('o'))+(x.count('u'))
print(y)


x = eval("13 > 44 > 33 > 1")
print(x)



x = 'minnie mouse'
y = '?'
z = (x.replace("a", y)).replace("e",y).replace("i",y).replace("o",y).replace("u",y)
print(z)


x = "1234"
print((len(x) == 4 and 6) and (x.isdigit()) and ( not ' ' in x))