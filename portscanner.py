import argparse
import socket

from portscan_utils import (
    tcp_scanner,
    udp_scanner
)

def scan_port_range(
    host,
    port_range,
    socket_type, 
):
    """
    Scn
    """
    ip = socket.gethostbyname(host)
    print(f"Scanning {socket_type} port range {port_range} on host {host} ({ip})")
    print("")

    for port in range(*port_range):
        if socket_type == 'tcp':
            tcp_scanner(host, port)
        elif socket_type == 'udp':
            udp_scanner(host, port)
        else:
            raise ValueError(f"Socket type {socket_type} not supported")

    print(f"--------------")
    print(f"Scan complete!")

def extract_port_range(s):
    ports = s.split("-")
    return int(ports[0]), int(ports[1])
    
if __name__ == "__main__":
    # Define command-line arguments
    parser = argparse.ArgumentParser(
                    prog = 'Portscanner',
                    description = 'Basic port scanner for TCP and UDP on a single host',
    )
    parser.add_argument('host', metavar='host', type=str,
                        help='Name or IP address of the host to scan')

    parser.add_argument('-p', dest='port_range', type=str, required=True,
                        help='port range separated by dash (i.e. "0-100")')
    parser.add_argument('-s', dest='socket_type', type=str, required=True,
                        help='One "tcp" or "udp"')

    # Parse arguments 
    args = parser.parse_args()
    
    port_range = extract_port_range(args.port_range)

    scan_port_range(
        args.host, 
        port_range=port_range, 
        socket_type=args.socket_type
    )