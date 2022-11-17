import socket

def getServiceName(port, proto):
    try:
        name = socket.getservbyport(int(port), proto)
    except:
        return None
    return name


def tcp_scanner(host, port):
    """
    TCP Scanner function that prints if the port is open
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    n = getServiceName(port,'tcp')

    if s.connect_ex((host, port)):
        pass
    else:
        print("Port:",port,"Service:",n)

    s.close()

   

def udp_scanner(host, port, timeout=10):
    """
    UDP Scanner function that prints if the port is open
    """
    s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s1.settimeout(timeout)
    msg = bytes("Hello, World!", "utf-8")
    
    try:
        s1.sendto(msg, (host, port))
        data, addr = s1.recvfrom(4096)
        print("Reply received from UDP port:",port)
        print ("Received message:", data)
    except ConnectionResetError:
         print("Closed UDP port:", port)
    except TimeoutError:
          print("No data received from UDP port:", port, "before timeout:",timeout)


def find_port_range(
    port_range=(0,1025), 
    host='45.33.32.156', 
    socket_type='tcp', 
):

    for port in range(*port_range):
        if socket_type == 'tcp':
            tcp_scanner(host, port)
        elif socket_type == 'udp':
            udp_scanner(host,port)
        else:
            raise ValueError(f"Socket type {socket_type} not supported")


if __name__ == "__main__":
    find_port_range()
