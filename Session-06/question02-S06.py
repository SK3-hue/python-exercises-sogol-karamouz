#question02-S06
inventory = {'apple': 20,'banana': 5,'orange': 0,'milk': 12,'bread': 0}

l =[i for i in inventory if inventory[i] <=0 ]

print(f'out of stock:\n{'\n'.join(f'{i}:{inventory[i]}'for i in l)}','\n')

l1 = [ i for i in inventory if inventory[i]>0]
print(f'Available:\n{'\n'.join(f'{i}:{inventory[i]}'for i in l1)}')

        
