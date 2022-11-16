def tcp_scan(socket, target_ip, port):
    def port_scan(port):
        try:
            socket.connect((target_ip, port))
            return True
        except:
            return False

    if port_scan(port):
        print(f'port {port} is open')
    else:
        print(f'port {port} is closed')


def udp_scan(socket, byte_message,target_ip,port):
    def send_data(port):
        try:
            socket.settimeout(12) #12 second timout to receive an answer package from server
            socket.sendto(byte_message, (target_ip, port))
            return True 
        except: #If socket has not received an answer (or has gotten an ICMP packet which we cannot detect)
            return False

    if send_data(port):
        print(f'Message could be sent to port {port}')
    else:
        print(f'Message could NOT be sent to port {port}')
