'''3 mesal Loop
2,3 --> for loop
2--> a ] adade farde byene 30 ta 50 ro print konid
     b ] adade farde beyne 30 ta 7000 ro beshmorid, begid chantas (print kone y adad -->beeg chanta)
    c]  adade zoje beyne 60 ta 120 ro joda konid tooye yek list bename zoj_list
        
'''
#A
i = 0
b =[i for i in range(30,50) if i % 2 != 0]
print(b)

#B
a =[i for i in range(30,7000) if i % 2 != 0]
print(f'sum of odd numbers: {len(a)}')

#c
Zoj_list = [i for i in range(59,121) if i % 2 == 0]
print(Zoj_list)


  
    
        