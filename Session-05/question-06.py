#Q6-S05.py
x = input('enter: ').split()
l = ['hack','fraud', 'scam', 'password', 'attack']

for i in x :
    if i in l :
        print(i,x.count(i))
       
