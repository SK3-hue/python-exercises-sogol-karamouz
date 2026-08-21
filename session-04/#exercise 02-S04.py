#exercise02-S04.py
import random
while True:

 start  = input('start/exit?')
 
 if start == 'start':
  c = random.choice(['sang','kaghaz', 'gheichi'])
  q  = input('choose: sang, kaghaz, gheici...:')
  if (q =='sang' and c =='sang'or q =='kaghaz' and c =='kaghaz' 
                or q =='gheichi' and c=='gheichi'):
                print('win-win')
  elif (q == 'sang' and c=='kaghaz' or q == 'kaghaz'and c=='gheichi'
                or q == 'gheichi'and c== 'sang'):
           print('PC won!')
  elif (q == 'kaghaz' and c=='sang' or q == 'gheichi'and c=='kaghaz'
                or q == 'sang'and c== 'gheichi'):
           print('User won!')
  else:
      print('enter valid input')
 elif start == 'exit':
        print('bye')
        break
 
 