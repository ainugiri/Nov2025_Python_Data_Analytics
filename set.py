s1 = {'a825662','Giri','Giri','giri','a825662','a825662','a843122'}
print(s1)
# print(s1[1]) error, not able to access with index, unordered

for items in s1:
    print(items)

s1.add('a825663')
s1.add('a825663')
s1.add('a825663')
s1.add('a825663')
s1.add('a825663')
print(s1)

python = {'e12','e11','e10','e9'}
sql = {'e1','e3','e11','e10'}
js = {'e1','e12','e10','e5'}

print(f"Python or SQL Developer {python.union(sql)}")
print(f"Both Python and SQL Developer {python.intersection(sql)}")
print(f"Python alone, not sql {python-sql-js}")
print(f"SQL alone, not Python {sql-python}")