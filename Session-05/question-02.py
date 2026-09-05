#Q2-S05
s = list((input('enter a word: ')))

for i in s[:]:
    if s.count(i)>1:
        index = s.index(i)
        second= s.index(i,index+1)
        
        s.pop(second)

print(''.join(s))
        