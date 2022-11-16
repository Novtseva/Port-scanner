import socket
import time

#Scanning a range of ports of a host on a network


#Creating socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPV4, TCP connection.


target = input('What do you want to scan?: ')
target_ip = socket.gethostbyname(target)
port_range = input('How many ports do you want to scan?:') #maybe make a max range so that it is up to 1024 ports 
 
#Need to ask here if user wants to scan using TCP or UDP

print('Starting scan on host:', target_ip)

 
def port_scan(port):
    try:
        s.connect((target_ip, port))
        return True
    except:
        return False

start = time.time()

for port in range(port_range):
    if port_scan(port):
        print(f'port {port} is open')
    else:
        print(f'port {port} is closed')

end = time.time()
print(f'Time taken {end-start:.2f} seconds')


