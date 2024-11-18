nombre = (1,2,3,4,5)
x=0
while True:
    x = int(input("donnez un numero: "))
    if x != 0:
        break

multiple = tuple(x*i for i in nombre)
print(multiple)
pair = tuple(i for i in multiple if i%2==0)
impair = tuple(i for i in multiple if i%2!=0)
print(pair)
print(impair)