t1 = ("apple","abc", "bcd","abc")
print(t1)
print(type(t1))
print(t1[1])
# t1[1] = "Giri"
print(t1)

templist = list(t1)
templist[1] = "Giri Prasad P"
l1 = tuple(templist)
print(l1)

t2 = ("A","B","C")
t3 = t1 + t2
print(t3)

t4 = t3 * 2
print(t4)

templist = list(t3)
templist.remove('abc')
templist.remove('abc')
t3 = tuple(templist)
print(t3)

del t3
# print(t3)