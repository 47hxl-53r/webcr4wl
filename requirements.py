import os, time
print("PLEASE WAIT WHILE DOWNLOADING THE REQUIREMENTS...\n")

# REQUESTS
os.system('clear')
print("Installing requests")
os.system('pip install requests')

# COLORAMA
os.system('clear')
print("Installing colorama")
os.system("pip install colorama")

# DNSPYTHON
os.system('clear')
print('Installing dnspython')
os.system('pip install dnspython')

# PYFIGLET
os.system('clear')
print('Installing pyfiglet')
os.system('pip install pyfiglet')

#TQDM
os.system('clear')
print('Installing additional packages...')
os.system('pip install tqdm')

# SELF-KILLING
os.system('clear')
os.system('THIS FILE IS GOING TO SELF DELETE IN 3 SECONDS...')
time.sleep(2)
os.system('clear')
os.system('rm -rf requirements.py')