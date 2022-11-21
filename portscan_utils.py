import socket

def getServiceName(port, protocol):
    """
    Returns the common service name on given port number
    """
    try:
        name = socket.getservbyport(int(port), protocol)
    except:
        return 'unknown'
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
        print("Port: ", port, "Service: ", n)

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
        #print ("Received message:", data)
    except ConnectionResetError:
         print("Closed UDP port:", port)
    except TimeoutError:
          print("No data received from UDP port:", port, "before timeout:",timeout)