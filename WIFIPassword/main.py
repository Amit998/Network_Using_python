import subprocess


data=subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')


# print(data)
wifis=[line.split(':')[1][1:-1] for line in data if 'All User Profile' in line]

# netsh wlan show profile Redmi key=clear
for wifi in wifis:
   
    result=subprocess.check_output(['netsh','wlan','show','profile',wifi,'key=clear']).decode('utf-8').split('\n')
    newData=[line.split(':')[1][:-1] for line in result if 'Key Content' in line]
    try:
        print(f'wifi  {wifi} password is {newData[0]}')
    except IndexError:
        print(f'wifi {wifi} Cannot Be Read')

# print(wifis)