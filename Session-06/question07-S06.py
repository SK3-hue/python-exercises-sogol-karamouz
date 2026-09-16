#question07-S06

orders = [('Ali', 'Laptop'),('Sara', 'Phone'),('Ali', 'Phone'),\
          ('Reza', 'Laptop'),('Sara', 'Laptop'),('Ali', 'Tablet'),\
              ('Reza', 'Phone')]

dic = {}
for i in orders :
    if i[0] not in dic :
       dic[i[0]]=[]
    dic[i[0]].append(i[1])
        
print(dic)






