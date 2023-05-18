class Calculator:

    def add(self, x, y):
        return x + y
    def subtract(self, x, y):
        return x - y
    def multiply(self, x, y):
        return x * y
    def divide(self, x, y):
        if y == 0:
            return "can't divide by zero"
        return x // y




calculator = Calculator()

print(calculator.add(10, 5) == 15)

print(calculator.subtract(10, 5) == 5)

print(calculator.multiply(10, 5) == 50)

print(calculator.divide(10, 0))



class Ones_threes_nines:
	
	def __init__(self, n):
		self.ones = n
		self.threes = n // 3
		self.nines = n // 9

y = Ones_threes_nines(5)
print(y.ones)




class Player():

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age= age
        self. height = height
        self.weight = weight
    
    def get_age(self):
        return f'{self.name} is age {self.age}'
	
    def get_height(self):
        return f'{self.name} is {self.height}cm'
	
		
    def get_weight(self):	
        return f'{self.name} weigs {self.weight}kg'
    

p1 = Player("David Jones", 25, 175, 75)

print(p1.get_age())
print(p1.get_height())
print(p1.get_weight())





class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname =  f'{self.firstname} {self.lastname}'
        self.email = f'{self.firstname.lower()}.{self.lastname.lower()}@company.com'
    


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")

print((emp_1.fullname) ==  "John Smith")

print((emp_2.email)  == "mary.sue@company.com")

print((emp_3.firstname) == "Antony")





class Name:
    def __init__(self, fname, lname):
        self.fname = fname.title()
        self.lname = lname.title()
        self.fullname= f'{fname.title()} {lname.title()}'
        self.initials = f'{fname.title()[0]}.{lname.title()[0]}'
        

a1 = Name("jon", "SMITH")


print(a1.fname)  #"John" 

print(a1.lname)  #"#Smith"

print(a1.fullname) # "John Smith"

print(a1.initials) # "J.S"






class Country:

    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        if area > 3000000  and population > 250000000:
            self.is_big = True
        else:
            self.is_big = False    
		
    def compare_pd(self, other):
        if (self.population / self.area) > (other.population / other.area):
            return f'{self.name}has a larger population density than {other.name}'
        else:
            return f'{other.name}has a larger population density than {self.name}'

        
australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

print(australia.is_big) #True
print(andorra.is_big)  #False
print(andorra.compare_pd(australia))  #"Andorra has a larger population density than Australia"        






class Person:
    def __init__(self, name,  foods_like, foods_hate):
        self.name = name
        self.foods_like = foods_like
        self.foods_hate = foods_hate

    def taste(self, food):
        if food in self.foods_like:
            return f'{self.name} eats the {"".join(self.foods_like)} and loves it!'
        elif food in self.foods_hate:
            return f'{self.name} eats the {"".join(self.foods_hate)} and hates it!!'
        elif food not in self.foods_like and  food not in self.foods_hate:
            return f'{self.name} eats the {food}!'


p1 = Person("Sam", ["ice cream"], ["carrots"])


print(p1.taste("ice cream")) #"Sam eats the ice cream and loves it!"
print(p1.taste("cheese")) #"Sam eats the cheese!"
print(p1.taste("carrots")) #"Sam eats the carrots and hates it!"






class Book:
    def __init__(self, title, author):
        self.title= title
        self.author= author

    def get_title(self):
        return f"Title: {self.title}"
    def get_author(self):
        return f'Author: {self.author}'


HP= Book('Harry Potter', 'J.K. Rowling')
PP=Book('Pride and Prejudice', 'Jane Austen ')
H= Book('Hamlet', 'William Shakespeare')
WP= Book('War and Peace', 'Leo Tolstoy')

print(WP.title)  #"Harry Potter"
print(WP.author) #"J.K. Rowling"
print(WP.get_title()) #"Title: Harry Potter"
print(WP.get_author()) #"Author: J.K. Rowling"



class Composer:
    count = 0
    def __init__ (self,name, dob, country):
        
        self.name = name
        self.dob = dob
        self.country = country
        Composer.count +=1

print(Composer.count) #0
c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
print(Composer.count) #1


c2 = Composer("Wolfgang Amadeus Mozart", 1756, "Austria")
c3 = Composer("Johannes Brahms", 1833, "Germany")
print(Composer.count) #3





class User:
    user_count = 0
    def __init__(self, username):
        self.username = username
        User.user_count +=1
        

u1 = User("johnsmith10")
print(User.user_count)  #1

u2 = User("marysue1989")
print(User.user_count) # 2

u3 = User("milan_rodrick")
print(User.user_count) #3


print(u1.username) #"johnsmith10"

print(u2.username) #"marysue1989"

print(u3.username) #"milan_rodrick"




