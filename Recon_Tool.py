import os
import socket
import time
import requests

def cont():
    resp = input("\033[90mDo you want to continue[y/n]: \033[00m")
    if resp == 'y':
        welcome()
    else:
        print("\033[33m[*]Exitting...\033[00m")
        exit(0)
def first():
        print("\033[35m[+]Installing required tools\033[00m")
        time.sleep(5)
        os.system("sudo apt install httrack; sudo apt install whois; sudo apt install nslookup;git clone https://github.com/m4ll0k/Infoga.git infoga;cd infoga;sudo python setup.py install;sudo apt install sublist3r")
def whois(ip):
    print("\033[35m[+]Performing whois...\033[00m")
    time.sleep(5)
    os.system("whois {}".format(ip))
def dnslookup(ip):
    print("\033[35m[+]Getting Name server records...\033[00m")
    time.sleep(5)
    os.system("nslookup -type=ns {}".format(ip))
    print("\033[35m[+]Getting mx records...\033[00m")
    time.sleep(5)
    os.system("nslookup -type=mx {}".format(ip))
    print("\033[35m[+]Getting 'A' records...\033[00m")
    time.sleep(5)
    os.system("nslookup -type=a {}".format(ip))
    print("\033[35m[+]Getting 'SOA' records...\033[00m")
    os.system("nslookup -type=soa {}".format(ip))
def iploc(ip):
    print("\033[35m[+]Locating Target...\033[00m")
    time.sleep(5)
    req = 'https://ipinfo.io/'+ip+'/json'
    iploc = requests.get(req)
    print(iploc.text)
def webclone(web):
    name = input('\033[92mEnter website name:\033[00m')
    os.system("mkdir {}".format(name))
    os.system("httrack {} -W -O {} -%v".format(web,name))
    print("\033[35m[+]Cloned in {} directory...\033[00m".format(name))

def revip(ip):
    req = 'https://api.hackertarget.com/reverseiplookup/?q='+ip
    revip = requests.get(req)
    print("\033[35m[+]Perfroming Reverse IP lookup on Target\033[00m")
    time.sleep(5)
    print(revip.text)
    
def hostfind(ip):
    req = 'https://api.hackertarget.com/hostsearch/?q='+ip
    hostfind = requests.get(req)
    print("\033[35m[+]Finding Host of Target...\033[00m")
    time.sleep(5)
    print(hostfind.text)
def email(web):
    print("\033[35m[+]Gathering Email info...(using infoga)\033[00m")
    os.system("python3 infoga/infoga.py --domain {} --source all --breach --v 2".format(web))

def sublist3r(web):
    print("\033[35m[+]Gathering Subdomains...(using sublist3r)\033[00m")
    print("\033[35m[+]Saving the results to {}.result file\033[00m".format(web))
    os.system("sublist3r -d {}  -t 10 -o {}.result".format(web,web))


def revdns(ip):
    print("\033[35m[+]Performing Reverse DNS Lookup\033[00m")
    req='https://api.hackertarget.com/reversedns/?q='+ip
    revdns = requests.get(req)
    time.sleep(5)
    print(revdns.text)

def quickscan(ip):
    print("\033[35m[+]Performing Quick port scan\033[00m")
    req='https://api.hackertarget.com/nmap/?q='+ip
    quickscan= requests.get(req)
    time.sleep(5)
    print(quickscan.text)







def welcome():
    os.system("clear")
    print("""\33[93m 
#####**Recon Tool**#####
#####**************#####
### By ~ d4rkn1gh7 #####
#####**************#####
 \033[00m""")
    r = input('\033[90mIs this the first time you are using?[y/n]: \033[00m')
    if r == 'y':
        first()
    opt = input('\033[92mEnter Website or IP[W/I]: \033[00m')
    if opt.upper() == 'W':
        web = input('\033[92mEnter website :\033[00m')
        ip = socket.gethostbyname(web)
        print("\033[35m[+]Target's ip is {}\033[00m".format(ip))
    else:
        ip = input('\033[92mEnter IP address:\033[00m')
    print("""\033[96m
        [1]Whois Lookup   [5]Reverse IP lookup             [9] Reverse DNS Lookup
        [2]DNS Lookup     [6]Host Finder                   [10] Quick port scan
        [3]IPLocator      [7]Email Gatherer(using infoga)  [11] Quit Program
        [4]Website Cloner [8]Subdomain Gathering                        \033[00m""")
    option = str(input("\033[92mEnter your option:\033[00m"))
    if option == '1':
        whois(ip)
    elif option == '2':
        dnslookup(ip)
    elif option == '3':
        iploc(ip)
    elif option == '4':
        webclone(web)
    elif option == '5':
        revip(ip)
    elif option == '6':
        hostfind(ip)
    elif option == '7':
        email(web)
    elif option == '8':
        sublist3r(web)
    elif option == '9':
        revdns(ip)
    elif option == '10':
        quickscan(ip)
    elif option == '11':
        print("\033[33m[*]Exitting...\033[00m")
        exit(0)        
    cont()



welcome()
