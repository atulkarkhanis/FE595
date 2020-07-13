import requests
status_code = requests.get('http://www.google.com', timeout = None)
print(status_code)
print(status_code.headers)



