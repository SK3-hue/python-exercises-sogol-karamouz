#question02-S07
def process_order(customer, *products, **options):
    

    discount = options.get('discount',0)
    tax = options.get('tax',0)
    shipping = options.get('shipping',0)
    prices ={"Laptop":1000000,"Mouse":500000,"Keyboard":200000}
    total =0
    print(f'Customer:{customer}')
    print(f'products:{products}')
    
    for product in products:
        price = prices[product]
        total+=price
    price_ad= total-(total*discount/100)
    tax = price_ad*tax/100
    final_price=price_ad+tax+shipping
    
    print(f'Total_cost:{total}')
    print(f'discount:{(total*discount/100)}')
    print(f'tax:{tax}')
    print(f'shipping:{shipping}')
    print(f'final_price:{final_price}')
        
process_order("Ali","Laptop","Mouse","Keyboard",discount=10,tax=9,shipping=200000)
      








