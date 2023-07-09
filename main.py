import requests
import colorama, os, time
from threading import Thread
from colorama import Fore
from pystyle import Colors, Colorate
from pystyle import Write, Colors
from pystyle import Center

os.system("mode 149,30 && title Ngl Spammer - Make By Dekregenxyz - Contact > t.me/Notthatregenxy")
print(Colorate.Horizontal(Colors.yellow_to_red, '''
888b    |       / 888       ,d88~~\                                                                  
|Y88b   | e88~88e 888       8888    888-~88e    /~~~8e  888-~88e-~88e 888-~88e-~88e  e88~~8e  888-~\ 
| Y88b  | 888 888 888       `Y88b   888  888b       88b 888  888  888 888  888  888 d888  88b 888    [+] Fast Spam
|  Y88b | "88_88" 888        `Y88b, 888  8888  e88~-888 888  888  888 888  888  888 8888__888 888    [+] ProxyLess
|   Y88b|  /      888          8888 888  888P C888  888 888  888  888 888  888  888 Y888    , 888    
|    Y888 Cb      888       \__88P' 888-_88"   "88_-888 888  888  888 888  888  888  "88___/  888    
           Y8""8D                   888                                                              All Coded By Dekregenxyz''', 1))

def spammer(link, ms):
    nax = os.path.basename(link)
    ss = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,th;q=0.8",
    "Content-Length": "103",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "_ga=GA1.1.1680072718.1688839648; __stripe_mid=ba6404fb-2fd3-4ee5-97a1-6fc7946d59117ae008; __stripe_sid=b5d53d4c-d1c7-46e3-a20c-2fc89a64625ba310fe; mp_e8e1a30fe6d7dacfa1353b45d6093a00_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18936afeff13ec-01c9e03b950d89-26031d51-1fa400-18936afeff13ec%22%2C%22%24device_id%22%3A%20%2218936afeff13ec-01c9e03b950d89-26031d51-1fa400-18936afeff13ec%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fl.instagram.com%2F%22%2C%22%24initial_referring_domain%22%3A%20%22l.instagram.com%22%7D; _ga_5DV1ZR5ZHG=GS1.1.1688881867.2.1.1688881881.0.0.0",
    "Origin": "https://ngl.link",
    "Referer": f"https://ngl.link/{nax}",
    "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
    }

    cc = {
        "username": nax,
        "question": "fsdkofskdofskdofkosdofk",
        "deviceId": "2a64b14e-75ae-4ef3-acb5-c87adaa0a753",
        "gameSlug": None,
        "referrer": None,
    }


    r = requests.post('https://ngl.link/api/submit', headers=ss, data=cc, timeout=1)
    try:
        if r.status_code == 200:
            print(Center.XCenter(f"{Fore.LIGHTBLACK_EX}[{Fore.GREEN}+{Fore.LIGHTBLACK_EX}] Send {ms} to {link}"))
        else:
            if "Just a moment" or "<!DOCTYPE html>" in str(r.text):
                print(Center.XCenter(f"{Fore.LIGHTBLACK_EX}[{Fore.RED}+{Fore.LIGHTBLACK_EX}] ERROR : {r.status_code}"))
    except:time.sleep(10); pass

link = Write.Input("Ngl Link -> ", Colors.red_to_purple, interval=0.0025)
name = Write.Input("Message -> ", Colors.red_to_purple, interval=0.0025)
amount = Write.Input("Amount -> ", Colors.red_to_purple, interval=0.0025)
for i in range(int(amount)):
    Thread(target=spammer,args=[link, name]).start()
    #spammer("https://ngl.link/regenxxy.png", "x")