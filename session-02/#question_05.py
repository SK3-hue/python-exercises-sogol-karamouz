#question_05.py
Q = float(input('enter the distance(KM):'))
cost = 20000 
if 0< Q <= 2 :
  
    print('final cost:',cost,'Toman')
    
elif Q>2:
    km = Q-2
    cost = cost+km*5000
    print('final cost:',cost,'Toman')
     
    
else:
    print('no cost')