#exercise04-S04.py
list=[]
while True:
    a = int(input('enter a number...'))
    if a != 0:
        list.append(a)
        continue
    elif a == 0:
        result = sum(list)
        print(result)
        break
    else:
        print('invalid!')
