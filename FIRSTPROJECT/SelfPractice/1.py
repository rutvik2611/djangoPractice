def hello_decorator(func):
    def inner1():
        print("Hello, this is before function execution")

        func()

        print("This is after function execution")
    
    return inner1    
@hello_decorator
def function_to_be_used():
    print("This is inside the function !!")

function_to_be_used()
#COnstuctor
class GeekforGeeks:
  
    # default constructor
    def __init__(self):
        self.geek = "GeekforGeeks"
  
    # a method for printing data members
    def print_Geek(self):
        print(self.geek)
obj = GeekforGeeks()
obj.print_Geek()
x = lambda a : a + 10
print(x(5))

#tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
#sets
thisset = {"apple", "banana", "cherry", "apple"}
#list
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#dict
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
