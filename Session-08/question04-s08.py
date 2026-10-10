#question04-S089
values=[]
duplicated_words=0
position=[]

def get_values():
    global duplicated_words
    rangee = int(input('Homw many items you want to add?  '))

   
    for i in range (rangee) :
        b = input('enetr :').strip().casefold()
        
        if b == "":
            print('not valid')
            continue
            
        elif b in values:
            duplicated_words+=1

            print(f'{b} already exists')
            position = values.index(b)+1
            print(f'{b}--> duplicated word in position {position}\n')
            
            
        else:
            values.append(b)
            print(f'{b}-->New value added\n')
            
    return values,duplicated_words,position


def add_unique():
    global duplicated_words
    position=[]

    new_input = input('Enter new input: ')
    new_input = new_input.casefold()

    
    if new_input == "":
        print('not valid')
        return None,None
    
    if new_input in values:
        duplicated_words+=1
        print(f'{new_input} already exists')
        position = values.index(new_input)+1
        print(f'{new_input} duplicated input in position {position}\n')

        
        
    else:
        values.append(new_input)
        print(f'{new_input}-->New input added\n')
            
    
  
    return new_input,position    
            
def process_values():
    unuique_words = len(values)

    
    return unuique_words, duplicated_words
            
    
def show_report():
  get_values()
  add_unique()
  unuique_words,duplicated_words=process_values()
  print('Final Report:\n========================')
  print(f'Unique List: {values}')
  print(f'Number of unique values: {unuique_words}')
  print(f'Number of duplicate values: {duplicated_words}')
 
  print("\nPositions:")
  for i, value in enumerate(values, start=1):
        print(f"{value} --> Position: {i}")

   

show_report()   
    

           
            

