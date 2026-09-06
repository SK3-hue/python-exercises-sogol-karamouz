#question-10.py

a = input('enter text1: ').split()
b = input('enter text2: ').split()


c= [i for i in a if i in b]
print(f'Common words: \n{' \n'.join(c)}')
