# password begirid bayad bish az 8 karakter bashe tarkibi az adad o caps o lower
 #case bashe 
 
 
while True:
    a = input('enter your password:...')
    
    if len(a)>8 and any(i.isdigit()for i in a) and any(i.isupper()for i in a) and\
        any(i.isalpha()for i in a ) and any(i.islower() for i in a):
            print('confirmed')
            break
    else:
        print('enter correct password')