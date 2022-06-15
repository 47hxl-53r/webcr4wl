print("Starting...")
import os
if os.path.isfile('requirements.py'):
    print("You need to run 'python3 requirements.py' before running this script")
    exit()
else:
    pass
import importlib.util
import time, sys
import pyfiglet, requests, dns.resolver
from colorama import Fore
from data import *
dirs = []
def style(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
def style_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.001)
def banner():
    os.system("clear")
    style_print(f'''{Fore.YELLOW}{Style.NORMAL}

░█░█░▀▀█░█▀▄░░░░░█▀▀░█▀▄░█░█░█░█░█░░
░█▄█░░▀▄░█▀▄░░░░░█░░░█▀▄░░▀█░█▄█░█░░
░▀░▀░▀▀░░▀▀░░▀▀▀░▀▀▀░▀░▀░░░▀░▀░▀░▀▀▀

{Fore.RED}==============================================================
{Fore.WHITE}{Style.BRIGHT}||{Style.NORMAL}{Fore.YELLOW} Coded by {Style.BRIGHT}47hx1-53r{Style.NORMAL}
{Fore.WHITE}{Style.BRIGHT}||{Style.NORMAL}{Fore.YELLOW} Automated enumeration script
{Fore.RED}==============================================================
''')
def menu():
    banner()
    print(f'''
{Fore.RED}[{Fore.WHITE}{Style.BRIGHT}1{Style.NORMAL}{Fore.RED}] {Fore.RESET}->{Fore.YELLOW} Directory enumeration
{Fore.RED}[{Fore.WHITE}{Style.BRIGHT}2{Style.NORMAL}{Fore.RED}] {Fore.RESET}->{Fore.YELLOW} IP finder
{Fore.RED}[{Fore.WHITE}{Style.BRIGHT}3{Style.NORMAL}{Fore.RED}] {Fore.RESET}->{Fore.YELLOW} Port scanner    
{Fore.RED}[{Fore.WHITE}{Style.BRIGHT}4{Style.NORMAL}{Fore.RED}] {Fore.RESET}->{Fore.YELLOW} Subdomain scanner    
{Fore.RED}[{Fore.WHITE}{Style.BRIGHT}5{Style.NORMAL}{Fore.RED}] {Fore.RESET}->{Fore.YELLOW} Update script    
{Fore.RED}[{Fore.WHITE}{Style.BRIGHT}6{Style.NORMAL}{Fore.RED}] {Fore.RESET}->{Fore.YELLOW} Exit    
''')
    def shell():
        global choice, f, target
        try:
            choice = input(f"{Fore.RESET}>> ")
        except KeyboardInterrupt:
            print(f'{Fore.RED}\nGoodbye!')
            exit()
        if choice == "1":
            try:
                f = open('./src/lol_src/mc_donalds/wordlist.txt', 'r')
            except FileNotFoundError:
                print(f'{Fore.RED}\nWordlist.txt not found!')
            for l in f:
                l = l.split()
                for w in l:
                    dirs.append(w)
            raw_url = input("Enter the URL :  ")
            style(f'{Fore.CYAN}{len(dirs)} directories Loaded...\n')
            os.system('clear')
            style(f"{Fore.YELLOW}Bruteforce initialising...\n")
            if raw_url.startswith('www') and not raw_url.endswith('/'):
                raw_url = 'https://' + raw_url + '/'
                pass
            elif raw_url.startswith("http://") and raw_url.endswith("/"):
                pass
            elif raw_url.startswith("https://") is False and raw_url.endswith("/"):
                raw_url = f'https://{raw_url}'
                pass
            elif raw_url.startswith("https://") and raw_url.endswith("/"):
                pass
            elif raw_url.startswith('www') or raw_url.startswith('https://') is False and raw_url.endswith(
                    '/') == False:
                raw_url = f'https://{raw_url}/'
                pass
            else:
                raw_url = raw_url + '/'
                print(raw_url)
            for dirr in dirs:
                try:
                    response = requests.get(f'{raw_url + dirr}')
                    if response.status_code == 404:
                        print(
                            f'{Fore.RED}Trying /{dirr} {Fore.WHITE}|{Fore.RED} {response.status_code}\n{Fore.WHITE}{Style.BRIGHT}__________________________________{Style.NORMAL}')
                    elif response.status_code == 200:
                        print(
                            f'{Fore.GREEN}Found /{dirr} {Fore.WHITE}|{Fore.GREEN} {response.status_code}\n{Fore.WHITE}{Style.BRIGHT}__________________________________{Style.NORMAL}')
                    elif response.status_code == 403:
                        print(
                            f'{Fore.YELLOW}Forbidden /{dirr} {Fore.WHITE}|{Fore.YELLOW} {response.status_code}\n{Fore.WHITE}{Style.BRIGHT}__________________________________{Style.NORMAL}')
                        continue
                except ConnectionError:
                    print(f'{Fore.RED}Host unreachable!\n')
                    exit()
            def goback():
                global gobackk
                try:
                    gobackk = input(f'{Fore.WHITE}{Style.NORMAL}Enter 1 to go back : ')
                except KeyboardInterrupt:
                    print(f'{Fore.RED}\nGoodbye!')
                    exit()
                if gobackk == "1":
                    menu()
                else:
                    print(f'{Fore.RED}\nInvalid option!')
                    goback()
        elif choice == "2":
            def shellcode():
                try:
                    website = input(f"{Fore.YELLOW}Enter website : {Fore.RESET}")
                except KeyboardInterrupt:
                    print(f'{Fore.RED}\nGoodbye!')
                    exit()
                if website.startswith("https://"):
                    website = website[8:]
                    pass
                elif website.startswith("http://"):
                    website = website[7:]
                    pass
                try:
                    ip = socket.gethostbyname(website)
                    style(f'{Fore.YELLOW}IP  : {Fore.CYAN}{ip}\n')
                    def backer():
                        global back, website
                        try:
                            back = input(f"{Fore.WHITE}Enter 1 to go back : ")
                        except KeyboardInterrupt:
                            print(f'{Fore.RED}\nGoodbye!')
                            exit()
                        if back == "1":
                            os.system('clear')
                            menu()
                        else:
                            style(f"{Fore.RED}Invalid option!\n")
                            backer()
                    backer()
                except:
                    print(f"\n{Fore.RED}ERROR OCCURRED")
                    exit()
            shellcode()
        elif choice == "3":
            os.system('clear')
            print(f'{Fore.YELLOW}')
            ascii_banner = '''

░█▀█░▄▀▄░█▀▄░▀█▀░░░░░█▀▀░█▀▀░█░█░█▀█
░█▀▀░█/█░█▀▄░░█░░░░░░▀▀█░█░░░░▀█░█░█
░▀░░░░▀░░▀░▀░░▀░░▀▀▀░▀▀▀░▀▀▀░░░▀░▀░▀

'''
            style_print(ascii_banner)
            style_print(f"{Fore.RED}=" * 47)
            try:
                target = input(f"\n{Fore.RED}[{Fore.RESET}+{Fore.RED}] {Fore.YELLOW}Target website/IP : {Fore.RESET}")
            except KeyboardInterrupt:
                print(f'{Fore.RED}\nGoodbye!')
                exit()
            scanner = scanTools(target)
            scanner.portScan()
            def goback():
                global backie
                try:
                    backie = input(f'{Fore.RESET}Enter 1 to go back : {Style.NORMAL}')
                except KeyboardInterrupt:
                    print(f'{Fore.RED}\nGoodbye!')
                    exit()
                if backie == "1":
                    os.system("clear")
                    menu()
                else:
                    style(f'{Fore.RED}Invalid choice!\n')
                    goback()
            goback()
        elif choice == "4":
            os.system('clear')
            a = '='
            banner = f'''{Fore.YELLOW}
░█▀▀░█░█░█▀▄░░░░░█▀▄░▄▀▄░█▄█░█░█░▀█▀░█▀█
░▀▀█░█░█░█▀▄░░░░░█░█░█/█░█░█░░▀█░░█░░█░█
░▀▀▀░▀▀▀░▀▀░░▀▀▀░▀▀░░░▀░░▀░▀░░░▀░▀▀▀░▀░▀

{Fore.WHITE}{Style.BRIGHT}--> {Fore.YELLOW}P0w3rful subn3t sc4nner{Style.NORMAL}          
'''
            style_print(banner)
            style_print(f'{Fore.RED}{a*47}\n\n')
            def subnets():
                domain = input(f"{Fore.RESET}{Style.BRIGHT}[+] Domain : {Style.NORMAL}")
                instance = subdomain(domain)
                instance.subScan()
                def goback():
                    global shellback
                    try:
                        shellback = input(f'{Fore.YELLOW}{Style.NORMAL}Enter 1 to go back : ')
                    except KeyboardInterrupt:
                        print(f'{Fore.RED}\nGoodbye!')
                        exit()
                    if shellback == "1":
                        menu()
                    else:
                        print(f'{Fore.RED}Invalid option!')
                        goback()
                goback()
            subnets()
        elif choice == "5":
            os.system('clear')
            print(f'{Fore.BLUE}CHECKING FOR UPDATES . . .')
            print(f'{Fore.WHITE}{Style.BRIGHT}')
            for i in tqdm(range(10)):
                time.sleep(0.5)
            print(f"\n{Fore.GREEN}{Style.NORMAL}Already latest version")
            def gobacks():
                global shellbacks
                try:
                    shellbacks = input(f'{Fore.RESET}{Style.NORMAL}Enter 1 to go back : ')
                except KeyboardInterrupt:
                    print(f'{Fore.RED}\nGoodbye!')
                    exit()
                if shellbacks == "1":
                    menu()
                else:
                    print(f'{Fore.RED}Invalid option!')
                    gobacks()
            gobacks()
        elif choice == "6":
            print("Goodbye!")
            exit()
        else:
            print(f"{Fore.RED}Invalid choice")
            shell()
    shell()
menu()