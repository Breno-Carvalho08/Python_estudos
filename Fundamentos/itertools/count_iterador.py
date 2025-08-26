from itertools import count

#count é um iterador sem fim

c1 = count(start=8, step=8)

print(next(c1)) 
print(next(c1)) 
print(c1.__iter__)