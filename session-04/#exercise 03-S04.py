#exercise03-S04.py
while True:
    
 pw = input('enter your password: ')


 if len(pw)== 8 and pw[0:4].isalpha() and pw[4:8].isdigit():
    print('Valid password')
    break
 else:
     print('Invalid password!')
     
    