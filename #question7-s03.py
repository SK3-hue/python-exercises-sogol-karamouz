#question7-s03.py
colors = []

for i in range (3):
    c = input('enter color:  ')
    colors.append(c)
print(f'{colors}')
    
if colors[0] == colors [1] == colors[2]:
    
    print('3 colors are the same')
    
elif colors[0]==colors[1] or colors[0]==colors[2] or colors[1]==colors[2]:
    print('2colors are the same')
else:
    print('all different')
        
        
        
        
