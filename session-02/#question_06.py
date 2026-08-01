#question_06.py
TP = float(input('enter your total purchase:'))

if TP > 1000000:
   price = TP*0.85
   print('price after 15% discount:',price)
elif 500000<=TP<=1000000:
    price = TP*0.9
    print('price after 10% discount:',price)
else: 
    print("No Discount")