__author__ = 'astoklas'

import hashlib

def encodeMD5(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()

def encodePassword(username=None, password=None, domain=None, nonce=None, pkey=None):
    if (nonce != None and len(nonce) > 0):
        return encodeMD5(domain+nonce+username+password)
    else:
        return None

print(encodePassword(b"admin",b"admin",b"",b"aaaa"))



