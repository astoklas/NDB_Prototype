__author__ = 'astoklas'

# This is only a quick hack to start interacting with a NAM module
# No error handling included
# responses from NAM are not being parsed

# todo: error handling
# todo: parse xml response
# todo: cleanup code
# todo: proper parsing of login function
# todo: implement non-local users authentication password encoding

import hashlib
import requests

DEBUG = True

def debug(string):
    if DEBUG:
        print(string)

def encodeMD5(string):
    debug("encodeMD5")
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()

def encodePassword(username=None, password=None, domain=None, nonce=None, pkey=None):
    if (nonce != None and len(nonce) > 0):
        debug("Encode Password for local authentication")
        return encodeMD5(domain+nonce+username+password)
    else:
        debug("Not Implemented: authentication for non local users")
        return None

def loginNAM(nam_server, user, pwd):
    debug("Login NAM")
    auth_url = "http://%s/auth/login.php?api=true" % nam_server
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
    }
    # get a session id and a nounce for login
    debug("auth-url"+auth_url)
    response = requests.request("GET", auth_url, data=None, headers=headers, verify=False)
    response.encoding = "utf-8"
    debug("Return Values from NAM")
    debug(response.text)
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
    print(response.cookies)
    sess = response.cookies
    print(myvars["sessid"])
    # build header
    headers_session = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        }

    # login
    login_url = "http://%s/auth/authenicate.php?sessid=%s&username=%s&pwdigest=%s" % (nam_server,myvars["sessid"],user,enc_pwd)
    debug("Login URL:"+login_url)
    debug("Session Coookie")
    debug(sess)
    response = requests.request("GET", login_url, data=None, headers=headers_session, verify=False, cookies=sess)
    if response.status_code == 200:
        return sess
    else:
        return None

def logoutNAM(nam_server, sessid):
    debug("Logout NAM")
    logout_url = "http://%s/auth/logout.php" % nam_server
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        }
    response = requests.request("GET", logout_url, data=None, headers=headers, cookies=sessid)

def createCapture(nam_server, sessid, captureName="rest", sliceSize="500"):
    debug("Create Capture")
    url = "http://%s/nbi/nbi-capture/session" % (nam_server)
    headers = {
        'cache-control': "no-cache",
        }
    data = """
<capture>
  <session>
    <name>%s</name>
    <trafficSource>1</trafficSource>
    <dataPorts>
      <dataPort>DATA PORT 1</dataPort>
    </dataPorts>
    <sliceSize>%s</sliceSize>
    <state>0</state>
    <buffer>
      <bufferSize>30</bufferSize>
      <wrapMode>0</wrapMode>
    </buffer>
    <filters>
      <filterId>1</filterId>
    </filters>
  </session>
</capture>
""" % (captureName,sliceSize)

    debug("XML to create capture")
    debug(data)
    debug("Create Capture url"+url)
    debug("SessionID"+sessid)
    response = requests.request("POST", url, data=data, headers=headers, cookies=sessid)
    print(response.status_code)
    print(response.text)

def startCapture():
    return None

def stopCapture():
    return None

def deleteCapture(captureID):
    url = "/nbi/nbi-capture/session/id/%s" % captureID
    return None

nam_server = "10.19.0.102:80"
user = "rest"
pwd = "rest"
session = loginNAM(nam_server,user,pwd)
createCapture(nam_server,session,"myCapture","500")
print("Session")
print(session)