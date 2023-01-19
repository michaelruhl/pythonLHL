# password = 'password'
# attempt = input("Enter a password-> ")


# if password != attempt:
#     print('WRONG')
# else:
#     print('right!!!!')


choosepw = input("Choose a password-> ")
enterpw = input("Enter the password-> ")

if choosepw != enterpw:
    print('WRONG')
elif len(enterpw) <= 8:
    print('password too short')
else:
    print('right!!!!')