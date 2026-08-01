#question_02.py
num = input("enter your phone number:  ")

if len(num) == 11:
    print(num[1:4])
else:
    print('Your number should contain 11 digits.')
    