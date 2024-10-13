first = int(input('Ввести число: '))
second = int(input('Ввести число: '))
third = int(input('Ввести число: '))

a = first
b = second
c = third

if a == b and b == c and c == a:
    print(3)
elif a == b or b == c or c == a:
    print(2)
else:
    print(0)