# question02-S03.py

h1 = int(input('enter your 1st height:   '))
max = h1 
for i in range (10):
    h2 = int(input('enter your new height:   '))
    if h2>max:
        max = h2
        print(f'new record: {max}\n')
    
        
        
    else:
        print('already recorded\n')
   
print(f'maximum record:{max}')        
        
        
    
        
        