__author__ = 'astoklas'

import hashlib
import requests

def encodeMD5(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()

def encodePassword(username=None, password=None, domain=None, nonce=None, pkey=None):
    if (nonce != None and len(nonce) > 0):
        return encodeMD5(domain+nonce+username+password)
    else:
        return None

def loginNAM(nam_server, user, pwd):
    auth_url = "http://%s/auth/login.php?api=true" % nam_server
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
    }
    # get a session id and a nounce for login
    response = requests.request("GET", auth_url, data=None, headers=headers, verify=False)
    response.encoding = "utf-8"
    myvars = {}
    # parsing the return text ... for easy split replace \r\n with =
    s = response.text.replace("\n","=")
    s = s.split("=")
    # lets parse return values domina, nounce and others
    myvars[s[0].strip()] = s[1].strip()
    myvars[s[2].strip()] = s[3].strip()
    myvars[s[4].strip()] = s[5].strip()
    myvars[s[6].strip()] = s[7].strip()
    # encode pwd
    enc_pwd = encodePassword(user,pwd,myvars["domain"],myvars["nonce"])

    # build header
    headers_session = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'sessid': myvars["sessid"]
        }

    # login
    login_url = "http://%s/auth/authenicate.php?sessid=%s&username=%s&pwdigest=%s" % (nam_server,myvars["sessid"],user,enc_pwd)

    response = requests.request("GET", login_url, data=None, headers=headers_session, verify=False)
    if response.status_code == 200:
        return myvars["sessid"]
    else:
        return None

def logoutNAM(nam_server, sessid):
    logout_url = "http://%s/auth/logout.php" % nam_server
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'sessid': sessid
        }
    response = requests.request("GET", logout_url, data=None, headers=headers)

nam_server = "10.19.0.102:80"
user = "admin"
pwd = "Qwertz1234"
session = loginNAM(nam_server,user,pwd)
logoutNAM(nam_server,session)