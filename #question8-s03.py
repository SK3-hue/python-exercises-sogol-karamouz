#question8-s03.py
b = int(input('enter balance: '))
w = int(input('withdrawal amount:  '))

if w >0 and w<b:
    print('withdrawal is being done...')
elif w>0 and w>b:
    print('Balance is not enough!')
else:
    print('error!')