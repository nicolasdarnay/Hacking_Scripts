from ftplib import FTP
from socket import *

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
    ftp.login(user=usr,passwd=passwd) 
    print('[+] ~ Anonymous login allowed')
    return anonymous_login(target,port)

def anonymous_login(target,port):
    '''This function should allow user to get a ftp shell'''#function help

    print('[~] ~ Trying to connect')
    sock = socket(family=AF_INET) #Doesn't work. Learning how to use socket lib
    sock.connect(target,port)
    print('[~] ~ Trying to connect')
    print('[+] ~ Done have fun')

#Code
target = input(f'Enter remote host: ') #Remote host (ftp server)
port = 21 #Port 21 by default
user = 'anonymous' #User to login
password = 'pwnd' #Password to login

try: #Try to connect
    anonymous_try(target,user,password,port)
except: 
    print("[-] ~ Anonymous login disallowed or couldn't connect")