a = [1,2,3,4,5,6,7,8,9]
b = []

for i in a:
	b.append(i**2)

print(a)
print(b)

#list comprehension

x = [1,2,3,4,5,6,7,8,9]
y = [i**2 for i in x]
z = [i for i in x if i%2==1]

print("\n") #quebra de linha

print("Usando list comprehension")
print(x)
print(y)

print("\n") #quebra de linha

print("Usando list comprehension exemplo 2 - usando apenas números ímpares")
print(z)