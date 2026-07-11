x = 10

y = x

print("Before changing x:")
print("x =", x)
print("y =", y)

x = 20

print("\nAfter changing x:")
print("x =", x)
print("y =", y)

x = 10
y = x

print(id(x))
print(id(y))


# -----------------
x = 100
y = x
z = y

x = 500

print(x)
print(y)
print(z)

# ------------------------
a = 5
b = a
c = b

b = 10

print(a)
print(b)
print(c)
