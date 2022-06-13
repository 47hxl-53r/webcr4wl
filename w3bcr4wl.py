print("Starting...")
import os
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
    for c  in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.001)


def banner():
    os.system("clear")
    style_print(f'''{Fore.YELLOW}
██╗    ██╗██████╗ ██████╗          ██████╗██████╗ ██╗  ██╗██╗    ██╗ ██╗
██║    ██║╚════██╗██╔══██╗        ██╔════╝██╔══██╗██║  ██║██║    ██║███║
██║ █╗ ██║ █████╔╝██████╔╝        ██║     ██████╔╝███████║██║ █╗ ██║╚██║
██║███╗██║ ╚═══██╗██╔══██╗        ██║     ██╔══██╗╚════██║██║███╗██║ ██║
╚███╔███╔╝██████╔╝██████╔╝███████╗╚██████╗██║  ██║     ██║╚███╔███╔╝ ██║
 ╚══╝╚══╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝     ╚═╝ ╚══╝╚══╝  ╚═╝
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
{Fore.RED}[{Fore.WHITE}{Style.BRIGHT}4{Style.NORMAL}{Fore.RED}] {Fore.RESET}->{Fore.YELLOW} Subdomain finder    
''')


    def shell():
        choice = input(f"{Fore.RESET}>> ")
        if choice == "1":
            f = open('./src/lol_src/mc_donalds/wordlist.txt', 'r')
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
            elif raw_url.startswith("http://") and raw_url.endswith("/"):
                pass
            elif raw_url.startswith("https://") == False and raw_url.endswith("/"):
                raw_url = f'https://{raw_url}'
            elif raw_url.startswith("https://") and raw_url.endswith("/"):
                pass
            elif raw_url.startswith('www') or raw_url.startswith('https://') == False and raw_url.endswith(
                    '/') == False:

                raw_url = f'https://{raw_url}/'
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


        elif choice == "2":
            def shellcode():
                website = input(f"{Fore.YELLOW}Enter website : {Fore.RESET}")
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
                        back = input(f"{Fore.WHITE}Enter 1 to go back : ")
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
            ascii_banner = pyfiglet.figlet_format("p0rt_sc4n")
            style_print(ascii_banner)
            style_print(f"{Fore.RED}=" * 50)
            target = input(f"\n{Fore.RED}[{Fore.RESET}+{Fore.RED}] {Fore.YELLOW}Target website/IP : {Fore.RESET}")
            scanner = scanTools(target)
            scanner.portScan()
            def goback():
                back = input(f'{Fore.RESET}Enter 1 to go back : {Style.NORMAL}')
                if back == "1":
                    os.system("clear")
                    menu()
                else:
                    style(f'{Fore.RED}Invalid choice!\n')
                    goback()
            goback()
        elif choice == "4":
            domain = input("Enter the Domain : ")
            subscanner = subdomains(domain)
            subscanner.subdomainScanner()
        else:
            print(f"{Fore.RED}Invalid choice")
            shell()
    shell()


menu()
