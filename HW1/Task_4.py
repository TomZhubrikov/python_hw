# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

print('Enter size of chocolate (m x n)')
m = int(input('m = '))
n = int(input('n = '))
print('Enter the number of slices (k)')
k = int(input('k = '))
if (k % n == 0 or k % m == 0) and k < m * n:
    print('yes')
else:
    print('no')
