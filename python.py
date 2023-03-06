print('Ali')
if 'Ali' == 'Ali':
    print("two Ali")


myArray = list([1,2,3,4,5])
print(myArray)
for i in myArray:
    print(i)

san = 1
san2 = 1
san3 = str(san2)
san4 = str(san)
print(san is san2)

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
        
print(fibonacci(3))

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b