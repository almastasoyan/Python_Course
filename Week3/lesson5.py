user_name=input("Write your name")

if user_name == "Mubashir":
    print("Hello my love" )

elif user_name != "Mubashir":
    print("Hello" ,user_name)



a = 1
b = 9
z = (a == 10 or b == 10) or (a + b == 10)
print (z)



x = 5
y = x%5 == 0
print(y)



x = "ABC"
y = "DE"
z = len(x) == len(y)
print(z)



x = "Hello_Teacher"
y = len(x)%2==0
print(y)


x = "Matt"
y = 3
if (isinstance(x,str)):
    print(x * y) 

else:
    print("Not A String")