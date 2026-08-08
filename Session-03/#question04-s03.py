#question04-s03.py
a = input('enter your str:')
print(len(a))
if len(a)%2==0:
    print(a[:(len(a)//2)])
else:
    print(a[(len(a)//2):])