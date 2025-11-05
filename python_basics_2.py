# conditional {If ---- else}

x1 = int(input("Enter the value for x1: "))
x2 = int(input("Enter the value for x2: "))
x3 = int(input("Enter the value for x3: "))
print(f" The datatype if {x1} is {type(x1)}")

avg = (x1+x2+x3)/3
if avg > 90:
    print("A")
elif avg > 80:
    print("B")
elif avg > 70:
    print("C")
elif avg > 60:
    print("D")
elif avg >= 50:
    print("E")
else :
    print("FAIL")

l1 = [1,2,3,3,4,4,5,5]
for i in l1:
    print(i*i)

i = 1
while i <= 10:
    print(f"e{i} welcome to python")
    i += 1


for i in range(0,101,1):
    print(i)


# function
# def functionname(arg)
def squareval(x):
    return (x**3/(2*x))
ip1 = int(input("User1: "))
print(squareval(ip1))