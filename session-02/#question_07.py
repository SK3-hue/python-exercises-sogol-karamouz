#question_07.py
a = input("enter your account number:  ")
x = a[:4]
p = '6214'
s = '6037'
if x == p:
    print('Saman Bank')
elif x == s:
    print('Saderat Bank')
else:
    print('invalid bank account')