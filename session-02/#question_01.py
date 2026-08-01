#question_01.py
Q = input('enter your name: ')
ID = int(input('enter your id number: '))
print(f"{Q}{ID}")
num = int(str(ID)[-10:])
print(num)