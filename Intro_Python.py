print("Welcome")

# data types -> dynamic binding -> mentioning not required, w.r.t data -> assigns the datatype
# int x = 10;
# datatype variablename = value
# variablename = value
# w.r.t value -> int / float / complex / boolean / str 

x = 100
print(x)
# numerical value without any single / double quotation - if it is not decimal -> int else float
print(type(x))

x1 = 10
print(f"The value of x1 is {x1} and its datatype is {type(x1)}")
x1 = 10.0
print(f"The value of x1 is {x1} and its datatype is {type(x1)}")
x1 = 1 + 4j
print(f"The value of x1 is {x1} and its datatype is {type(x1)}")

x1 = "100"
print(f"The value of x1 is {x1} and its datatype is {type(x1)}")

x1 = "()"
print(f"The value of x1 is {x1} and its datatype is {type(x1)}")

x1 = "True"
print(f"The value of x1 is {x1} and its datatype is {type(x1)}")

x1 = True
print(f"The value of x1 is {x1} and its datatype is {type(x1)}")


x1 = False
print(f"The value of x1 is {x1} and its datatype is {type(x1)}")

pi = ['iPhone', 'iPad', 'Tomato']

print(f"List of purchased items are {pi}")
# access with index
print(f"The second item in the purchased list is  {pi[1]}")

pi[1] = "Dell Laptop"
print(f"The second item in the purchased list is  {pi[1]}")

print(f"The updated list is {pi}")
pi.append("Keyboard")
print(f"The updated list is {pi}")
pi.insert(1, "TV")
print(f"The updated list is {pi}")
pi.append("iPhone")
print(f"The updated list is {pi}")
# pi.remove("iPhone") # first occ
# pi.pop(2) remove by index
# pi.pop() # remove at the end
# pi.clear() # remove all
# del pi
print(f"The updated list is {pi}")
