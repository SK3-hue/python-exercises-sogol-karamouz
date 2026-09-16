#question01-S06.py
products = {'laptop': 1200,'phone': 800,'tablet': 500,\
            'headphone': 150,'mouse': 50}

most_expensive = max(products,key=products.get)
print(f'Most expensive product:\n {most_expensive} -->\
      {products[most_expensive]}\n')

cheapest = min(products, key=products.get)
print(f'Cheapest product: \n {cheapest} -->{products[cheapest]}\n')

average = sum(products.values())/len(products)
print(f'Average price : {average}\n')

print("Product price >500 :")

for i in products:  
    if products[i] > 500:
        
       print(f'{i}={products[i]}')
        
total = sum(products.values())
print(f'\n Total values: {total}')