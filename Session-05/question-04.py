#Q4-S05
a = input('enetr a string: ').split()
b = [i for i in a if a.count(i)>1]
l = max(a, key=a.count)
print(f' most repeated word: {l}, {(a.count(l))}')