sales = (('Ali', 'Laptop', 1200),('Sara', 'Phone', 800),('Ali', 'Phone', 800),\
         ('Reza', 'Laptop', 1200),('Sara', 'Laptop', 1200),('Ali', 'Mouse', 50))
    
names = set(i[0] for i in sales)

for name in names:
    total=[]
    s = sum([i[2] for i in sales if i[0]==name])
    total.append((name,s))
    print(f'Customer perchase: {total}\n')

for i in total:
    x = max([i[1]]for i in total)
print(f'Max purchase: {name,x}\n')
      

b = [i[1]for i in sales ]
for i in b:
    if b.count(i) >1:
     print(f'Best selling products: {i}\n')
     break 
 
c = [ i[1] for i in sales]
for i in set(c):
 print(f'product sales:{i}-->{c.count(i)}\n')
 
total_sales = [i[2] for i in sales]
total_sales = sum(total_sales) 
print(f'Total sales: {total_sales} $')