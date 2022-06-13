import datetime
import socket, sys, time
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

        style_print(f"{Fore.RED}=" * 50)
        a = "="
        style(f'\n{Fore.YELLOW}{Style.BRIGHT}STATUS{Style.NORMAL}  : {Fore.CYAN}Scanning Target : {Fore.LIGHTGREEN_EX}{target}\n{Fore.YELLOW}{Style.BRIGHT}STATUS{Style.NORMAL}  : {Fore.CYAN}Started scan at : {Fore.LIGHTGREEN_EX}{str(datetime.datetime.now())}\n')
        style_print(f"{Fore.RED}{a*50}\n")
        style(f"{Fore.YELLOW}{Style.BRIGHT}WARNING{Style.NORMAL}  : {Fore.CYAN}{Style.BRIGHT}SPEED DEPENDS ON YOUR CPU POWER{Style.NORMAL}{Fore.RESET}\n")
        style_print(f"{Fore.RED}{a * 50}\n")
        # scanning here
        def pscan(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((target, port))
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

        thread_list     = []

        for t in range(600):
            thread = threading.Thread(target=worker)
            thread_list.append(thread)

        for thread in thread_list:
            thread.start()

        for thread in thread_list:
            thread.join()

        print(f'{Fore.YELLOW}Open ports are : {Fore.CYAN}{Style.BRIGHT}{open_ports}\n')
class subdomains:
    def __init__(self, domain):
        self.domain = domain
    def subdomainScanner(self):
        try:
            ip_value = dns.resolver.resolve(self.domain, "A")
            if ip_value:
                print("SUBDOMAIN FOUND!")
        except dns.resolver.NXDOMAIN:
            print("Subdomain not found!")
            quit()



