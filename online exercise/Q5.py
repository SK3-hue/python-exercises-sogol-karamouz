
    
Q = input('Hi,do you want to buy? yes/no...')
Q = Q.casefold().strip()
cart = []
if Q == 'yes':
   product = input('product:')
   cart.append(product)
   print(f'CART:{cart}')
   while True:
    a = input('do u want anything else: ')
    a = a.casefold().strip()
    if a == 'yes':
        print('add product:')
        product1 = input('product:')
        cart.append(product1)
        print(f'CART:{cart}')        
    elif a =='no':
        print(f'Your cart:{cart}\nbye!')
        break 
    else:
        print('only yes/no')
        continue
elif Q == 'no':    
 print('Thanks for visiting us!')    
  
else:
    print('only yes/no!')
    