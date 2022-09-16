from ftplib import FTP
from socket import *
import os

print('''
           __                  __        __  
 /\  |\ | /  \ |\ | \ /  |\/| /  \ |  | /__` 
/~~\ | \| \__/ | \|  |   |  | \__/ \__/ .__/ 
                                             
                  ___  __                    
|__/ | |    |    |__  |__)                   
|  \ | |___ |___ |___ |  \                   
                                             
                                             ''') #Banner
#Functions
def anonymous_try(target,usr,passwd,port):
    '''This function try to connect with anonymous credentials'''#function help

    ftp = FTP(host=target)
    ftp.connect(port=port)
    ftp.login(user=usr,passwd=passwd)
    print('[+] ~ Anonymous login allowed')
    print('[+] ~ Banner detected:')
    banner = ftp.getwelcome()
    print(banner)
    return sanitized(banner)

def sanitized(banner):
    salida = banner.split(" ")
    salida2 = salida[1].strip("()")
    salida3 = salida[2].strip("()")
    sanitized = salida2+' '+salida3
    print(sanitized)
    
    return search_exp(sanitized)

def search_exp(sanitized):
    os.system(f"searchsploit {sanitized}")

#Code
if os.system('find /usr/bin/searchsploit >/dev/null 2>&1') == 0:
    target = input(f'Enter remote host: ') #Remote host (ftp server)
    port = int(input(f'Enter remote port: ')) #Port 21 by default
    user = 'anonymous' #User to login
    password = 'pwnd' #Password to login

    try: #Try to connect
        anonymous_try(target,user,password,port)
    except: 
        print("[-] ~ Anonymous login disallowed or couldn't connect")
    
else:
    print("[-] ~ Searchsploit not installed... bye")