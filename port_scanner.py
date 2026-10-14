import socket  #Import the socket module to create network connections

target = input("Enter target IP: ")  #Ask the user to type the target IP address and store it in the variable called 'target'

print(f"Scanning {target}...\n")  #Print a message showing which IP address is being scanned

for port in range(1, 1025):  #The variable 'port' is a loop variable that takes each port number from 1 to 1024. Well-known ports (1-1024) are scanned as this is where common services usually run
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Creates a socket using IPv4(AF_INET) and TCP(SOCK_STREAM) to attempt a connection
    s.settimeout(0.5)  #This sets a timeout of 0.5s for the socket connection so the scan doesn't hang on ports that are slow or unresponsive
    result = s.connect_ex((target, port))  #Try connecting to the target IP on this port
    if result == 0:  #If the result returns as 0. Any other number is returned if the port is closed, filtered or blocked.
        print(f"Port {port} is open") #This message is output showing the port number that is open
    s.close()  #Close the socket to free resources before going on to scan the next port

