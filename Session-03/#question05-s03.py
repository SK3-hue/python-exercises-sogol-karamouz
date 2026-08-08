#question05-s03.py
for i in range (5):

 num1=int(input('enter number1:  '))
 num2=int(input('enter number2:  '))
 op = input('* + / -:')
 
 if op == '*' :
     
     print( num2*num1) 
 elif op == '/':
     print(num1/num2)
 elif op == '+':
     print(num1+num2)
 elif op == '-':
     print(num1-num2)
     
 else:
     print('invalide input!')
