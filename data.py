import datetime
import os
import socket, sys, time
from tqdm import tqdm
import requests
from colorama import Fore, Style
import threading
import dns.resolver
from queue import Queue
queue = Queue()
open_ports = []



def style(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)


def style_print(s):
    for c  in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.001)


class scanTools:

    def __init__(self, target):
        self.target = target

    def portScan(self):
        global target, scanning
        if self.target.startswith("https://"):
            self.target = self.target[8:]
            try:
                target = socket.gethostbyname(self.target)
                pass
            except socket.gaierror as x:
                style(f'{Fore.RED}Host not found!\n')
                print(x)
                exit()

        elif self.target.startswith('http://'):
            self.target = self.target[7:]
            try:
                target = socket.gethostbyname(self.target)
                pass
            except socket.gaierror as r:
                style(f'{Fore.RED}Host not found!\n')
                print(r)
                exit()

        elif self.target.startswith("www"):
            try:
                target = socket.gethostbyname(self.target)
                pass
            except socket.gaierror as e:
                style(f"{Fore.RED}Host not found!\n")
                print(e)
                exit()

        else:
            try:
                target = socket.gethostbyname(self.target)
                pass
            except socket.gaierror:
                style(f"{Fore.RED}Host not found!\n")
                exit()

        style_print(f"{Fore.RED}=" * 47)
        a = "="
        style(f'\n{Fore.YELLOW}{Style.BRIGHT}STATUS{Style.NORMAL}  : {Fore.CYAN}Scanning Target : {Fore.LIGHTGREEN_EX}{target}\n{Fore.YELLOW}{Style.BRIGHT}STATUS{Style.NORMAL}  : {Fore.CYAN}Started scan at : {Fore.LIGHTGREEN_EX}{str(datetime.datetime.now())}\n')
        style_print(f"{Fore.RED}{a*47}\n")
        style(f"{Fore.YELLOW}{Style.BRIGHT}WARNING{Style.NORMAL}  : {Fore.CYAN}{Style.BRIGHT}SPEED DEPENDS ON YOUR CPU POWER{Style.NORMAL}{Fore.RESET}\n")
        style_print(f"{Fore.RED}{a * 47}\n")
        # scanning here
        def pscan(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((target, port))
                socket.setdefaulttimeout(0.5)
                return True
            except:
                return False

        def fill_queue(port_list):
            for port in port_list:
                queue.put(port)

        def worker():
            while not queue.empty():
                port = queue.get()
                if pscan(port):
                    print(f'{Fore.YELLOW}--> {Fore.GREEN}Port{Style.BRIGHT} {port}{Style.NORMAL} is open')
                    open_ports.append(port)
        port_list = range(1, 1024)
        fill_queue(port_list)

        thread_list = []

        for t in range(600):
            thread = threading.Thread(target=worker)
            thread_list.append(thread)

        for thread in thread_list:
            thread.start()

        for thread in thread_list:
            thread.join()

        print(f'{Fore.YELLOW}Open ports are : {Fore.CYAN}{Style.BRIGHT}{open_ports}\n')
class subdomain:
    def __init__(self, domain):
        self.domain = domain
    def subScan(self):
        a = '='
        b = '_'
        style_print(f'{Fore.RED}{a*47}\n')
        style(f'{Fore.GREEN}Initialising subnet scan for {self.domain} . . .\n')
        file = open('./src/git_src/x12/subd.txt', 'r')
        content = file.read()
        subdomain_list = content.splitlines()
        success_list = []
        print(f'{Fore.WHITE}{Style.BRIGHT}{a * 47}\n')
        print(F'{Style.NORMAL}{Fore.YELLOW}PLEASE WAIT WHILE SCANNING\n')
        print(Fore.WHITE+Style.BRIGHT)
        for subdomain in tqdm(subdomain_list):
            url1 = f'https://{subdomain}.{self.domain}'
            try:
                a = "="
                requests.get(url1, timeout=0.5)
                # print(f'{Fore.GREEN}{Style.BRIGHT}Subdomain found : {url1}{Style.NORMAL}')
                # print(f'{Fore.WHITE}{Style.BRIGHT}{a*47}\n')
                success_list.append(url1)
            except requests.ReadTimeout:
                pass
            except requests.ConnectionError:
                pass
        if len(success_list) == 0:
            style(f'\n{Fore.RED}No subdomains found for {self.domain}!\n')
            pass
        else:
            print(f'\n{Fore.GREEN}{Style.NORMAL}------ Subnets for {self.domain} ------\n')
            for i in range(0, len(success_list)):
                print(Fore.YELLOW + '[*] ' + Fore.RESET + Style.BRIGHT + success_list[i])
                pass
        print("\n")
