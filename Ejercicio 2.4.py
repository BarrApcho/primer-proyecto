a=b=c=1
print(a,b,c)
b=2
print(a,b,c)

x=y=[7,8,9]
x=[13,8,9]
print(y)

x=[1,2,[3,4,5],6,7]
print (x[2])
print (x[2][1])

def my_function():
    a=5
    b=10
    return a+b
print(my_function())

a=reversed('Hola Mundo')

a = [1, 2, 3]
b = ['a', 1, 'python', (1, 2), [1, 2]]
b[2] = 'something else' # allowed

i='2'
if isinstance(i, int):
    i+=1
elif isinstance(i, str):
    i=int(i)
    i+=1
print(i)

