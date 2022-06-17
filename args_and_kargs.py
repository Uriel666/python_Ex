# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

def sum(*numbers):
    sum = 0
    numbers = list(numbers)
    numbers[0] = 0
    for argument in numbers:
        sum += argument

    return sum


print(sum(1,2,3,4,5))


# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):
    #print("Hello"+kwargs['first']+' '+kwargs['last'])

    print("Hello", end = " ")

    for key,value in kwargs.items():
        print(value,end = " ")


hello(first = "Bro",middle = "Dude" , last = "Code")