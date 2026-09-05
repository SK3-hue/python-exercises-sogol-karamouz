while True:

  a = input('enter your password:   ')
  if len(a)>8 and any(x.isalpha() for x in a) and any(x.isdigit() for x in a)\
      and any(x.isupper() for x in a) and any(x.islower() for x in a) \
          and any(x in "@#$%^&*" for x in a):
              print('password is confirmed')
              break
  
  elif len(a)<8:
      print('Password must contain at least 8 characters')
  elif not any(x.isdigit() for x in a ):
      print('password must contain digits')
  elif not any(x.isalpha() for x in a ):
      print('password must contain alphabet')
  elif not any(x.isupper() for x in a ):
      print('password must contain uppercase')
  elif not any(x.islower() for x in a ):
      print('password must contain lowercase')
  elif not any(x in "@#$%^&*" for x in a):
      print('password must contain special caracters')
      
  else:
      print('invalid password')