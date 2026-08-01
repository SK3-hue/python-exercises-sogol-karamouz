#question_08.py
T = int(input('enter a time: '))

if 0<=T<12:
    print('Morning')
elif 12<=T<17:
    print('Noon')
elif 17<=T<20:
    print('Evening')
elif 20<=T<=23:
    print('Night')
else:
    print('invalid operation')