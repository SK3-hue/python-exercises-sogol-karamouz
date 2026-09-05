#question-08.py
a = input('enter a text: ')
b = len(a)
print(f'Total characters: {b}')
c = a.split()
c = [i for i in c if not i.isdigit()]
print(f'Total words:{len(c)}')
d = a.replace(' ','')
d = [i for i in d if not i.isdigit()]
print(f'Total Letters:{len(d)}')

e = sum(i.isdigit() for i in a)
print(f'Total digits:{e}')

u = sum(i.isupper() for i in a )
print(f'Total uppercase:{u}')

l = sum(i.islower() for i in a )
print(f'Total lowercase:{l}')

w = max(c, key=len)
print(f'Longest word:{w}')

s = min(c,key=len)
print(f'Shortest word:{s}')

m = max(d, key= d.count)
print(f'Most repeated character: {m}')

z = max(c, key=c.count)
print(f'Most repeated word: {z}')
