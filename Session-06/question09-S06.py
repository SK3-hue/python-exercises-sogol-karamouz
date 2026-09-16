#question09-S06

products = {
'P01': ('Laptop', 1200, 5),
'P02': ('Phone', 800, 0),
'P03': ('Tablet', 500, 12),
'P04': ('Mouse', 50, 25),
'P05': ('Keyboard', 100, 0)
}

product_name = [i[0] for i in products.values()]
print(f'Products_name: {product_name}')

Available = [(i[0],i[2]) for i in products.values() if i[2]>0]
unavailable = [(i[0],i[2]) for i in products.values() if i[2]==0]
d = dict(Available)
d1=dict(unavailable)
print(f'Available products: {dict(d)}')
print(f'Unavailable products: {dict(d1)}')

Total = [(i[0],i[1]*i[2]) for i in products.values()]
for i in Total:
     print(f'Total stock values: {i[0],i[1]}')
     
print(f'Max Stock value : {max(Total)}')

tsv = sum([(i[1]*i[2]) for i in products.values()])

print(f'Total stock value: {tsv}')