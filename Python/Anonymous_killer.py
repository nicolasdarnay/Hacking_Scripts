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
    ftp.connect(port=port)
    ftp.login(user=usr,passwd=passwd) 
    print('[+] ~ Anonymous login allowed')
    return anonymous_login(target,port)

def anonymous_login(target,port):
    '''This function should allow user to get a ftp shell'''#function help

    print(f'[~] ~ Trying to connect {target}')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Doesn't work. Learning how to use socket lib
    sock.connect((target,port))
    print('[+] ~ Done, have fun')

#Code
target = input(f'Enter remote host: ') #Remote host (ftp server)
port = int(input(f'Enter remote port: ')) #Port 21 by default
user = 'anonymous' #User to login
password = 'pwnd' #Password to login

try: #Try to connect
    anonymous_try(target,user,password,port)
except: 
    print("[-] ~ Anonymous login disallowed or couldn't connect")