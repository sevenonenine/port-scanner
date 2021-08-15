import sys
import socket
import pyfiglet

def printbanner():
    print(pyfiglet.figlet_format("PORT SCANNER"))

def printhelp():
    print("-"*50)
    print("")
    print("Usage: python " + sys.argv[0] + " [IP Address] <Port>")
    print("")

def scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((sys.argv[1],int(port)))
        if result == 0:
            print ("Port {} is open".format(port))
        s.close()
    except KeyboardInterrupt:
        print("\nExitting Program")
        sys.exit(0)
    except socket.gaierror:
        print("\nHostname could not be resolved")
        sys.exit()
    except socket.error:
        print("\nServer not responding")
        sys.exit()

def scanall():
    for port in range(1,65535):
        scan(port)
    sys.exit(0)

def main():
    printbanner()
    print("-"*50)
    if (len(sys.argv) < 2):
        printhelp()
        sys.exit(1)
    if (len(sys.argv) == 2):
            scanall()
            sys.exit(0)
    scan(sys.argv[2])
    sys.exit(0)

if __name__ == "__main__":
    main()
