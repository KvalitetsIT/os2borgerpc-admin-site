import sys
import re
import socket
import netifaces
from socket import AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_BROADCAST

MESSAGE = "Hello"
REPLY_MESSAGE = "BibOS-server:"
PORT = 42420


def find_gateway(timeout=1):
    result = None

    for if_name in netifaces.interfaces():
        if if_name.startswith('eth'):
            interface = netifaces.ifaddresses(if_name)
            broadcast_addr = interface[netifaces.AF_INET][0]['broadcast']
            try:
                sock = socket.socket(AF_INET, SOCK_DGRAM)
                sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
                sock.sendto(MESSAGE, (broadcast_addr, PORT))
                sock.settimeout(timeout)
                data, addr = sock.recvfrom(1024)
                m = re.match("^" + REPLY_MESSAGE + "(.+)", data)
                if m is not None:
                    result = m.group(1)
            except Exception as inst:
                #sys.stderr.write("Exception: " + str(inst) + "\n")
                return None
        if result is not None:
            break

    return result

if(__name__ == '__main__'):
    s = find_gateway()
    if s is not None:
        print s