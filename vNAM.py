__author__ = 'astoklas'

import hashlib
import requests

nam_server = "10.19.0.102:80"
auth_url = "http://%s/auth/login.php?api=true" % nam_server

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    }

def encodeMD5(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()

def encodePassword(username=None, password=None, domain=None, nonce=None, pkey=None):
    if (nonce != None and len(nonce) > 0):
        return encodeMD5(domain+nonce+username+password)
    else:
        return None

print(auth_url)
response = requests.request("GET", auth_url, data=None, headers=headers, verify=False)
print(response.text)
print(encodePassword("admin","Qwertz1234","","aaaa"))



