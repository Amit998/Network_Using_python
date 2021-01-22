charlist='abcdefghijklmnopqrstuvwxyz'
import zipfile
complete=['looo','help','lol']


# for current in range(4):
#     a=[i for i in charlist]
#     for x in range(current):
#         a=[y + i for i in charlist for y in a]
#     complete=complete + a

# print(complete)
z =zipfile.ZipFile('secret.zip')
name='secret.zip'

tries=0


for password in complete:
    try:
        # print(password)
        tries+=1
        z.setpassword(password.encode('ascii'))
        z.extract('secret.txt')
        print(f"Password was found It Was {password}")
        break
    except Exception as e:
        print(e)


