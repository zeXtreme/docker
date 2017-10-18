import requests
import time
import os

hostname = os.environ.get('hostname')
password = os.environ.get('password')
myip = os.environ.get('myip')
url = 'https://' + hostname + ':' + password + '@dyn.dns.he.net/nic/update?hostname=' + hostname + ('' if myip == None else ('&myip=' + myip))
while True:
    print('GET:', url)
    r = requests.get(url)
    print(r.text)
    time.sleep(5 * 60)
