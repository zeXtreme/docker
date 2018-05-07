import urllib
import ssl
import time
import os

not_verify = ssl._create_unverified_context()
hostname = os.environ.get('hostname')
password = os.environ.get('password')
myip = os.environ.get('myip')
url = 'https://' + hostname + ':' + password + '@dyn.dns.he.net/nic/update?hostname=' + hostname + ('' if myip == None else ('&myip=' + myip))
print('GET:', url)
while True:
    try:
        r = urllib.urlopen(url, context=not_verify)
        print(r.read())
    except Exception:
        print('something error')
    finally:
        time.sleep(5 * 60)
