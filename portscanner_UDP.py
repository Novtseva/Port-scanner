
#What if you want to test a UDP package? If a UDP port answers us within a maximum time of 12 seconds, we consider it to be open, otherwise, we consider it closed.

import socket
import time
byte_message = bytes("Hello, World!", "utf-8") #MUDP message 
opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP connection


target = input('What do you want to scan?: ')
target_ip = socket.gethostbyname(target)
port_range = input('How many ports do you want to scan?:') #maybe make a max limit for 1024 ports

#Need to ask here if user wants to scan using TCP or UDP

print('Starting scan on host:', target_ip)

def send_data(port):
    try:
        socket.settimeout(12) #12 second timout to receive an answer package from server
        opened_socket.sendto(byte_message, (target_ip, port))
        return True 
    except: #If socket has not received an answer (or has gotten an ICMP packet which we cannot detect)
         return False

start = time.time()

for port in range(port_range):
    if send_data(port):
        print(f'Message could be sent to port {port}')
    else:
        print(f'Message could NOT be sent to port {port}')

end = time.time()
print(f'Time taken {end-start:.2f} seconds')


