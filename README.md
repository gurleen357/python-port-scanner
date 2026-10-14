# python-port-scanner
## Overview
A simple Python port scanner that checks for open TCP ports on a target IPv4 address. This tool uses Python’s built‑in socket module to attempt connections across the well‑known port range (1–1024) and reports which ports are open. It’s lightweight, beginner‑friendly, and ideal for learning networking and cybersecurity fundamentals.


## 🚀 Features
- Scans ports 1-1024
- Uses TTCP connect scanning
- Fast scanning with a 0.5 second timeout
- Clean, readable output
- Fully commented code
- No external libraries required


## 🔍How It Works
The scanner:
1. Prompts the user for a target IP  
2. Loops through ports 1-1024  
3. Creates a TCP IPv4 socket
4. Attempts a connection using connect_ex()
5. Prints ports that return a successful connection
6. Closes the socket before scanning the next port
This is known as a TCP Connect Scan, a simple and reliable scanning method.

## 🖥️ Usage
- Run the script
- Enter the target IP
- Wait for output

## 📂 Code Overview
The script uses:
- socket.AF_INET → IPv4
- socket.SOCK_STREAM → TCP
- settimeout() → prevents slow scans
- connect_ex() → safe connection attempts
The code is fully commented so as to explain each step clearly.


## 🔧 Future Improvements
- Scan all 65,535 ports
- Detect service names (HTTP,FTP,etc.)
- Save results to a file
- Add colour coded output
  
## 📸 Screenshots
<img width="518" height="486" alt="Screenshot 2026-10-14 132833" src="https://github.com/user-attachments/assets/8527bfa6-c04c-4e57-b952-2f80c40aa0f7" />


## 🎯 What I Learned
This project helped me to understand some concepts in networking and Python:
- How TCP ports work and why devices expose certain services
- The difference between open, closed, and filtered ports
- How to use Pythons 'socket' library to create network connections
- How 'connect_ex()' safely checks whether a port is open
- Why timeouts are important to prevent scans from freezing
This project strengthened my understanding of basic cybersecurity techniques and gave me hands on experience with network scanning.




