#question08-S06
users = [
('Ali', 25, 'Python'),
('Sara', 30, 'Java'),
('Reza', 22, 'Python'),
('Mina', 28, 'C++'),
('John', 35, 'Python'),
('David', 30, 'Java')
]


d = {language:[i[0]for i in users if i[2]==language] for language in set(i[2] \
                                                        for i in users)}

print(d,'\n')

avg_age = sum( i[1] for i in users)/len(users)
print(f'average age is : {avg_age:.2f}\n')

oldest = max(i[1] for i in users)
print(f'The oldest person is : {oldest} y/o\n')

most_user= max(d.keys())

print(f'Language with most users: {most_user}\n')

print(f'languages: {set(d.keys())}')