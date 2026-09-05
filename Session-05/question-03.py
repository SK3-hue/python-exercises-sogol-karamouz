#Q3-S05
a = (input('enter a string:  '))

l = [ i for i in a if i.isalpha()]
ll =len(l)
print(f'letters:{ll}')


d = [i for i in a if i.isdigit()]
dd = len(d)
print(f'digits:{dd}')

u = [i for i in a if i.isupper()]
uu=len(u)
print(f'upprecase:{uu}')

w = [i for i in a if i.islower()]
ww = len(w)
print(f'lowercase:{ww}')

s = [i for i in a if i==" "]
ss =len(s)
print(f'space:{ss}')

c = [i for i in a if i in"!@#$%^&*"]
cc =len(c)
print(f'special characters:{cc}')

        


