#question04-S06
employees = {'E01':{"name": "Ali","age": 28,"salary": 3000},\
             "E02": {"name": "Sara","age": 32,"salary": 4500},\
                 "E03": {"name": "Reza","age": 25,"salary": 2800}}
max_salary = max([ i['salary'] for i in employees.values()])

for i in employees.items():
    if i[1]['salary'] == max_salary:
        a = i[1]["name"]
        
print(f"Maximum salary --> {a}:{max_salary}\n")
    
average = sum([i['salary'] for i in employees.values()])/len(employees)
print (f"Average salary : {average:.2f}\n")

for i in employees.values():
    if i['salary']>3000:
        print(f"More than 3k salary -->{i['name']}:{i['salary']}\n")
    
    
m = min([i['salary'] for i in employees.values()])
print(f'Minimum salary -->{i['name']}:{i['salary']}')


