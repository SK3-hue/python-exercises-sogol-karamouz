#question03-S08

transaction_file = 'C:/Users/Asus/Documents/Programming/Programming/Py Fanavari/Session-08/transaction.txt'

with open (transaction_file, 'r') as file:
    file = [i.strip() for i in file.readlines()]
   
def calculate_balance():
    balance={}
    for i in file : 
        name, transaction,amount = i.split(',')
        amount=int(amount)
        if name not in balance :
            balance[name]=0
            
        if transaction == "deposit":
            balance[name]+=amount
        elif transaction == "withdraw":
            balance[name]-=amount
            
        
    return balance
            
    
    
    
    
def total_deposit():
    deposit ={}
    for i in file : 
        name, transaction,amount = i.split(',')
        amount=int(amount)
        if name not in deposit:
            deposit[name]=0
            
        if transaction =="deposit":
            deposit[name]+=amount
    return deposit
        
    
def total_withdrawals():
    w={}
    for i in file :
        name, transaction,amount = i.split(',')
        amount=int(amount)
        if name not in w:
            w[name]=0
            
        if transaction =="withdraw":
            w[name]+=amount
    return w
        
    
def find_invalid_transactions():
    balance = calculate_balance()
    invalid={}
    for name, amount in balance.items():
        if amount<0:
            invalid[name]=amount
    return invalid
   


def generate_report():
    balance = calculate_balance()
    deposit= total_deposit()
    w = total_withdrawals()
    invalid = find_invalid_transactions()
    print('Final Report: .....')
    
    
    print(f'Total Balance : {balance}')
    print(f'Total deposit: {deposit}')
    print(f'Total withdrawal : {w}')
    print(f'{invalid} : invalid transaction!')    
    for name in sorted (balance):
        print(f'\n{name}')
        print(f'Deposit: {deposit[name]}')
        print(f'Withdraw: {w[name]}')
        print(f'balance: {balance[name]}\n---------------')
    


calculate_balance()
total_deposit()
total_withdrawals()
find_invalid_transactions()
generate_report()
    
    