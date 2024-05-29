'''def greet():
    print("Hello,World")
greet()
def greet(name):
    print("Hello ,",name)
greet("Alice")


def add_numbers(x,y):
    return x+y
result=add_numbers(3,5)
print(result)


#parameter passing
def greet(name,age):
    print(f"Hello, {name}! you are {age} years old.")
greet(age=30,name="Alice")


#default
def greet(name="world"):
    print(f"hello,{name}!")
greet()
greet("bob")   


def greet(*names):
    for name in names:
        print(f"Hello, {name}!")
        print(type(names))
greet("Alice","Bob","Charlice")


def greet(**kwargs):
    print(type(kwargs))
    for key,value in kwargs. items():
        print(f"{key}:{value}")
        
greet(name="Alice,",age=30)


def greet(name,*names,age=30,**kwargs):
    print(f"Hello, {name}! you are {age} years old.")
    print(type(name),type(names),type(age),type(kwargs))
    for n in names:
        print(f"Hello,{n}!")
    for key,value in kwargs. items():
        print(f"{key}:{value}")
greet("Alice","Bob","Charlice",age=30,city="New York",Country="USA")


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
num=5
print("Factorial of",num,"is",factorial(num))'''


fibonacci=lambda n: n if n<=1 else fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(5))

