# TO install
#  pip install numpy
# include<stdio.h>
# l1 = [1,2,3,4,5]
# print(type(l1))


import numpy as np
arr1 = np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))

list1 = [1,1.5, 'Python', False]
arr2 = np.array([1,1.5, 'Python', False])
x = float(arr2[1]) + 10
list1[1] = x
arr2[1] = x
print(x)
print(list1)
print(arr2)
print(type(list1))
print(type(arr2))
list2 = [11,12,13,14,15]
print()
arr3 = np.array([11,12,13,14,15])
# list2 = list2 + 5
# print(list2)
arr3 = arr3[1] + 5
print(arr3)

arr4 = np.array([1,1.1,2.0,3.14,100])
print(arr4)
arr4 = arr4 * 3.14
print(arr4)

# int and float -> float
# str + other -> str
print(arr4.dtype)
print(type(list1))
print(type(list1[3]))


arr5 = np.zeros(8)
print(arr5)
arr5 = np.ones(8)
print(arr5)
arr5 = np.arange(1001,1011)
print(arr5)

tdimarr = np.array([[1,2,3],[11,22,33]])
print(tdimarr)

a1 = np.array([11,22,33])
print(a1.max())
print(a1.min())
print(a1.sum())
print(a1.mean())

l1 = [11,101,121,21,201,221,31,301,331]
a1 = np.array(l1)
print(l1)
print(a1)
firstfour = a1[:4]
print(firstfour)

lastfour = a1[-4:]
print(lastfour)

midthree = a1[3:6]
print(midthree)

rev_a1 = a1[::-1]
print(a1)
print(rev_a1)

every2element = a1[::2]
print(every2element)




every2element = a1[1:6:2]
print(every2element)

ar1 = np.array([1,2,3,4,5,6,7,8,9])
ar2 = ar1.reshape(3,3)
print(ar1)
print(ar2)


ar1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
ar2 = ar1.reshape(3, -1)
print(ar1)
print(ar2)

ar3 = ar2.reshape(-1)
print(ar3)

ar2_T = ar2.T
print(ar2_T)



ar1 = np.array([1,2,3,4,5,6,7,8,9])
ar2 = ar1.reshape(3,3)
print(ar2)
ar3 = ar2.T
print(ar3)


i1 = np.array([19,21,33])
i2 = np.array([32,22,13])
print(i1)
print(i2)
print("add = :",i1 + i2)
print("sub = :",i1 - i2)
print("mul = :",i1 * i2)
print("div = :",i1 / i2)


print(ar2)
print(ar3)
print("add = :",ar2 + ar3)
print("sub = :",ar2 - ar3)
print("mul = :",ar2 * ar3)
print("div = :",ar2 / ar3)

print(ar2*ar3)
# matrix mul .dot
print(ar2.dot(ar3))

ar4 = ar2.dot(ar3)
print(ar4[:,0:2])
print(ar4[:,1:])

ar4 = ar2.dot(ar3)
print(ar4[0:2,:])
print(ar4[1:,:])

print(ar4[1:,1:])
print(ar4)
print(np.where(ar4 > 50, "Yes","No"))

ar5 = ar4.reshape(-1)
print(ar5)
print(np.sort(ar5))
# np.array
# np.zeros
# np.ones
# np.arange
# np.dtype
# reshape, -1, T
# .dot()
# check where