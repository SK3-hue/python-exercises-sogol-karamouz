#Exercise 01- S 04
import random 
c = random.randint(1,50)

while True:
   a = int(input('enter number:  '))
   if a < c :
       print('enter bigger number')
   elif a > c:
       print('enter smaller number')
   elif a ==c:
       print('Congratulation!')
       break