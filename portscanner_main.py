import socket
import time

from scans import tcp_scan
from scans import udp_scan

#Scanning a range of ports of a host on a network

#Creating socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPV4, TCP connection.
byte_message = bytes("Hello, World!", "utf-8") #MUDP message 
opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP connection


target = input('What do you want to scan?: ')
target_ip = socket.gethostbyname(target)

print("Which protocol to scan?")
print("1 : TCP")
print("2 : UDP")

protocol_type = input("")

port_range = input('How many ports do you want to scan?:') #maybe make a max range so that it is up to 1024 ports 
 
#Need to ask here if user wants to scan using TCP or UDP

print('Starting scan on host:', target_ip)


if protocol_type == '1':
    start = time.time()

    for port in range(port_range):
        tcp_scan(s, target_ip, port)

    end = time.time()
    print(f'Time taken {end-start:.2f} seconds')

elif protocol_type == '2':
    start = time.time()

    for port in range(port_range):
        udp_scan(opened_socket, byte_message,target_ip,port)

    end = time.time()
print(f'Time taken {end-start:.2f} seconds')



