

def square(numero):
    return numero ** 2

numeri = [1,2,3,4,5]

squared = map(square,numeri)
print(list(squared))