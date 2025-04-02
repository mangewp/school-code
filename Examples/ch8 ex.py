print("one")
print("two")
print("three")

print("one", end= " ")
print("two", end= " ")
print("three")
print()
list = ["one", "two", "three"]
print(list)
for n in list:
    print(n)
print()

for n in list:
    print(n, end=" ")
    print('-', end="")