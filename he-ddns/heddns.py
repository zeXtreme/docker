import urllib
import time
import os

hostname = os.environ.get('hostname')
password = os.environ.get('password')
myip = os.environ.get('myip')
url = 'https://' + hostname + ':' + password + '@dyn.dns.he.net/nic/update?hostname=' + hostname + ('' if myip == None else ('&myip=' + myip))
print('GET:', url)
while True:
    r = urllib.urlopen(url)
    print(r.read())
    time.sleep(5 * 60)