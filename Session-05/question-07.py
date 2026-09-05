#Q7-S05.py
a = input('enter: ')

b=""
for i in a:
    if i not in b:
        print(i,a.count(i),sep='', end='')
        b+=i
        