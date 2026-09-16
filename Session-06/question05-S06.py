#question05-S06

students = students = {
'Ali': [18, 17, 20],
'Sara': [15, 19, 18],
'Reza': [12, 14, 10],
'Mina': [20, 20, 19] }

for i in students:
    avg = sum(students[i])/len(students[i])
    print(f"{i},{avg: .2f}")
    a = max(students[i])
    print(f'highest score:{a}')
    
    if avg >=15 : 
        print('Status: Passed\n')
    else:
        print("Status: Failed\n")
        
        
best = max({avg})
print(f"The best average: {i}-->{best:.2f}")
