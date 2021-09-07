import requests

response = requests.get('https://raw.githubusercontent.com/jackie0608/404lab1/main/print.py)
print (response.status_code)
print (response.content)
