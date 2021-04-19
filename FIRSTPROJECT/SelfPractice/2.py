x ="I can do this how ever i want to"

temp =x.split()
y=[]
for i in temp:
    y.append(i[::-1])
print(' '.join(y))
#temp = ' '.join(temp)

#print(temp)



# def flip(x):
#     return x[::-1]

# def mainn(y):
#     t=[]
#     for i in y:
#         temp = y
#         save= flip(temp)

#         t.append(save)
#         return t



# print(mainn(y))


# def fuc(t):
#     return re=t[::-1]

# def MainFunc(x):
#     y=x.split()
#     for i in y:
#         temp[i]=fun(y)
#     return y.join()

# print(MainFunc(x))


class GeekforGeeks:
  
    # default constructor
    def __init__(self):
        self.geek = "GeekforGeeks"
  
    # a method for printing data members
    def print_Geek(self):
        print(self.geek)
  
  
# creating object of the class
obj = GeekforGeeks()
  
# calling the instance method using the object obj
obj.print_Geek()