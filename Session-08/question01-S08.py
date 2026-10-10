#question01-S08
user_text= 'C:/Users/Asus/Documents/Programming/Programming/Py Fanavari/Session-08/user.txt'
print('initial text:\n---------')
with open(user_text,'r') as text_file:
    text1 = text_file.read()
print(text1)
def add_user():

   while True:
    new_user = input('add new user (name: user_id: status):')
    new_user=new_user.casefold()

    with open ( user_text,"r") as text:
        text1 = text.read()
        
    if new_user+'\n' not in text1:
        with open ( user_text,"a") as text:
            text.write(new_user+'\n')
        print(f'{new_user} added')
        return new_user
   
    elif new_user+'\n' in text1:
        print(f'{new_user} already exsist')
   
    else:
        print('not found')
        return None
    

     
     
def find_user():
    with open (user_text,"r") as text:
        text1 = text.read().casefold()
           
    while True:
        
        name = input('enetr your name: ')
        name = name.casefold()
        
        
        if name in text1:
            print(f'{name} found') 
            return name
        
        else:
            print('user not found')
            return None
                 
def delet_user():
    with open(user_text,'r') as text:
        text2 = text.readlines()
        
    query = input('what word to delet?')
    
    for line in text2:
        if query.casefold() in line.casefold():
            text2.remove(line)
    print(f'{query} removed\n')
                    
    with open(user_text,'w') as text:
      text.writelines(text2)
    return query     
        
    print(f'{query} not found\n')
    
    
def generate_report():
    print('Generating Report...\n___________________________')
    active = 0 
    blocked = 0 
    with open ("user.txt","r") as file:
         text_file = file.readlines()
         
    for line in text_file:
        name, user_id, status = line.strip().split(",")

        if status =="active":
            active+=1
        elif status=="blocked":
            blocked+=1
    print(f'Active accounts: {active}')
    print(f'Blocked accounts: {blocked}\n')
    
    print('final text:\n -------------')

    with open(user_text,'r') as text_final:
        textf = text_final.read()
    print(textf)


    

    
    
    
add_user()
find_user()
delet_user()
generate_report()


       
    
    