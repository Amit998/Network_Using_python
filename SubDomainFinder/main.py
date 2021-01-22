import requests
import os

domain='hackthissite.org'
# domain='amazon.com'

# print(os.getcwd())
file=open('db/subdomains.txt','r')

content=file.read()
subdomains=content.splitlines()

for subdomain in subdomains:
    url=f'http://{subdomain}.{domain}'
    try:
        requests.get(url)
    except Exception as e :
        # print(e)
        pass
    else:
        print("Discoverd Subdomain",url)