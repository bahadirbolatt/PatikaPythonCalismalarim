# 1-10 arası sayıların karesinden bir liste oluşturalım.
"""
squares = []
for i in range(1,11):
    squares.append(i*i)
    print(squares)
    if i == 4:
        break
"""
# Bunu "list compression" ile de yapabiliriz.
"""
squares = [i * i for i in range(1,11)]
print(squares)

# başka bir örneğe bakalım.

squares =[i + 5 for i in range(1,11)]
print(s)
"""
# fonksiyon ile listcomph birlikte kullanımı
from re import X

x = 2
def cube(x):
    return x * x * x
cubes = [cube(x) for i in range (1,11)]
print(x)
