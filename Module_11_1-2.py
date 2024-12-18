import requests


response = requests.get('https://api.github.com')
answ = response.status_code
print (answ)
if response:
    print('Success!')
else:
    print('An error has occurred.')
cont = response.content
print (cont)
jsn = response.json()
print(jsn)
hdrs = response.headers
print(hdrs)
