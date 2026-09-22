# 🔎 TCP Port Scanner

A simple, concurrent **TCP Port Scanner** built with Python as part of the **Syntecxhub Cyber Security Internship – Week 1, Project 1**.

The project demonstrates socket programming, TCP connection testing, concurrent scanning with threads, port-range selection, timeout handling, exception handling, and readable command-line output.

## 📌 Project Overview

The scanner checks TCP ports on a host and reports whether each tested port is:

- **OPEN** — a TCP connection was successfully established
- **CLOSED** — the connection was refused
- **TIMEOUT** — the connection attempt exceeded the configured timeout
- **ERROR** — an unexpected error occurred

## ✨ Features

- Scan a hostname or IP address
- Scan a single port or a configurable port range
- Concurrent TCP scanning using `ThreadPoolExecutor`
- Configurable timeout
- Configurable number of worker threads
- Open, closed, and timeout status reporting
- Hostname-to-IP resolution
- Exception handling
- Response-time measurement
- Clean command-line output
- No external Python dependencies

## 🛠️ Technologies

- Python 3
- TCP/IP
- Socket Programming

## ⚙️ Requirements

Python 3.8+ is recommended.

Check your installation:

```bash
python --version
```

No third-party packages are required.

# 🔎 Python Port Scanner

A simple Python-based **TCP port scanner** that checks whether selected ports on a target IP address are open or closed.

This project is designed for learning the fundamentals of:

- IP addresses
- TCP and UDP
- Ports
- Sockets
- TCP connection scanning
- Exception handling
- `try`, `except`, and `finally`
- Port scanning
- Multithreading
- Network security basics

> **Important:** Only scan systems, networks, and devices that you own or have explicit permission to test.

---

# 📌 1. What Is Port Scanning?

A computer connected to a network can provide different services.

For example:

| Port | Common Service   |
| ---: | ---------------- |
|   21 | FTP              |
|   22 | SSH              |
|   23 | Telnet           |
|   25 | SMTP             |
|   53 | DNS              |
|   80 | HTTP             |
|  443 | HTTPS            |
| 3306 | MySQL            |
| 3389 | RDP              |
| 8080 | Alternative HTTP |

A **port scanner** checks ports on a target computer and determines whether they are accepting connections.

For example:

```text
Target: 192.168.1.10

22    → OPEN
80    → OPEN
443   → CLOSED
3306  → CLOSED
```

This can help a system administrator understand which network services are exposed.

---

# 🌐 2. What Is an IP Address?

An IP address identifies a device on a network.

Example:

```text
192.168.1.10
```

This is an IPv4 address.

Another example is:

```text
127.0.0.1
```

`127.0.0.1` is the **localhost** address.

It means:

> "This computer."

You can therefore test your scanner against:

```text
127.0.0.1
```

without scanning another machine.

---

# 🔢 3. What Is a Port?

A port is a numerical endpoint used by network applications.

Port numbers range from:

```text
0 – 65535
```

For example:

```text
192.168.1.10:80
```

means:

```text
IP address = 192.168.1.10
Port       = 80
```

The IP address identifies the device, while the port identifies a network service or application on that device.

Think of it like this:

```text
IP address = Building address
Port       = Door number
```

---

# 🚚 4. TCP vs UDP

There are two major transport-layer protocols commonly encountered when discussing port scanning:

## TCP

TCP stands for:

**Transmission Control Protocol**

TCP is connection-oriented.

Before communicating, TCP establishes a connection between the two endpoints.

Simplified:

```text
Client
   |
   | ---- Connection request ---->
   |
Server
   |
   | <---- Connection response ----
   |
Connection established
```

Examples of services commonly using TCP include:

- HTTP
- HTTPS
- SSH
- FTP
- SMTP

Our current scanner uses **TCP**.

---

# 📡 5. UDP

UDP stands for:

**User Datagram Protocol**

UDP is connectionless.

There is no TCP-style connection establishment before sending data.

UDP is commonly used for services such as:

- DNS
- DHCP
- NTP
- Streaming
- VoIP

UDP scanning is different from TCP scanning because simply failing to establish a TCP connection does not tell us whether a UDP service exists.

Therefore, the code in this project should be described as a:

> **TCP Connect Port Scanner**

not a UDP scanner.

---

# 🔌 6. What Is a Socket?

Python provides the `socket` module for network communication.

We create a socket with:

```python
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

There are two important parts here.

### `AF_INET`

This means we are using:

```text
IPv4
```

### `SOCK_STREAM`

This represents a stream socket, normally used with:

```text
TCP
```

Therefore:

```python
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

means:

> Create an IPv4 TCP socket.

---

# 🧑‍💻 7. Basic Scanner Code

```python
import socket

target = "127.0.0.1"
ports = [22, 80, 443, 8080]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    try:
        s.connect((target, port))
        print(f"Port {port} is OPEN")

    except:
        print(f"Port {port} is CLOSED")

    finally:
        s.close()
```

---

# 📖 8. Line-by-Line Explanation

## Line 1

```python
import socket
```

Imports Python's built-in `socket` module.

This gives us functions and classes for network communication.

---

## Line 2

```python
target = "127.0.0.1"
```

Defines the target IP address.

Here:

```text
127.0.0.1
```

means the local computer.

You could use an authorized test machine's IP address instead.

Example:

```python
target = "192.168.1.10"
```

---

## Line 3

```python
ports = [22, 80, 443, 8080]
```

Creates a list of ports to scan.

The scanner will check:

```text
22
80
443
8080
```

You can add other ports to the list.

Example:

```python
ports = [22, 25, 53, 80, 443, 3306]
```

---

# 🔁 9. The `for` Loop

```python
for port in ports:
```

This goes through every port in the list.

For example:

```text
First → 22
Second → 80
Third → 443
Fourth → 8080
```

The scanner processes each port one at a time.

---

# 🔌 10. Creating the Socket

```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

Creates a new TCP socket.

The components are:

```text
AF_INET
   ↓
IPv4

SOCK_STREAM
   ↓
TCP
```

So the scanner is preparing to make a TCP connection.

---

# ⏱️ 11. Setting a Timeout

```python
s.settimeout(1)
```

Sets the connection timeout to:

```text
1 second
```

If the connection doesn't complete within that time, Python raises an exception.

Without a timeout, a scanner could potentially wait too long on an unreachable or filtered port.

---

# 🧪 12. The `try` Block

```python
try:
    s.connect((target, port))
    print(f"Port {port} is OPEN")
```

This is the main connection attempt.

The important line is:

```python
s.connect((target, port))
```

For example:

```python
s.connect(("127.0.0.1", 80))
```

means:

> Try to establish a TCP connection to port 80 on 127.0.0.1.

If the connection succeeds:

```text
Port 80 is OPEN
```

is printed.

---

# ❌ 13. The `except` Block

```python
except:
    print(f"Port {port} is CLOSED")
```

If the connection raises an exception, the code enters the `except` block.

The simple scanner treats that as:

```text
CLOSED
```

However, technically this is an important limitation.

A failed TCP connection can also happen because of:

- Firewall filtering
- Network problems
- Host unreachable
- Timeout
- Connection refusal
- Other socket errors

Therefore, in a more accurate scanner, it is better to distinguish between:

```text
OPEN
CLOSED
FILTERED
TIMEOUT
ERROR
```

The simple version uses `CLOSED` as an easy beginner-friendly result.

---

# 🧹 14. The `finally` Block

```python
finally:
    s.close()
```

This is one of the most important parts of the program.

`finally` executes whether:

```text
try succeeds
```

or:

```text
try fails
```

Therefore the socket gets closed in both situations.

For example:

```python
try:
    s.connect((target, port))

except:
    print("Connection failed")

finally:
    s.close()
```

The purpose is to prevent unnecessary open sockets and clean up the network resource.

---

# 🧠 15. Why Use `try`, `except`, and `finally`?

Without exception handling, a connection failure could stop the program.

Example:

```python
s.connect((target, port))
```

If the connection fails, Python may raise an exception.

With:

```python
try:
    ...
except:
    ...
finally:
    ...
```

we can:

1. Attempt the connection.
2. Handle the failure.
3. Close the socket.
4. Continue scanning the next port.

This makes the program more reliable.

---

# 🧵 16. What Is Threading?

Our current scanner checks ports sequentially.

For example:

```text
Port 22
   ↓
wait
   ↓
Port 80
   ↓
wait
   ↓
Port 443
   ↓
wait
```

If every connection takes some time to timeout, scanning many ports can become slow.

**Threading** allows multiple port checks to happen concurrently.

Conceptually:

```text
Main Program
     |
     +---- Thread 1 → Port 22
     |
     +---- Thread 2 → Port 80
     |
     +---- Thread 3 → Port 443
     |
     +---- Thread 4 → Port 8080
```

Instead of waiting for each port sequentially, multiple network operations can be in progress at the same time.

---

# ⚡ 17. Why Use Threads in Port Scanning?

The major benefit is **speed**.

Without threading:

```text
Port 1 → wait
Port 2 → wait
Port 3 → wait
Port 4 → wait
```

With threading:

```text
Port 1 ──┐
Port 2 ──┤
Port 3 ──┤ → processed concurrently
Port 4 ──┘
```

This is especially useful when:

- Scanning many ports
- Network latency is significant
- Many ports are filtered
- Connection attempts have timeouts

---

# 🧵 18. Simple Threaded Version

A beginner-friendly version can use Python's `threading` module:

```python
import socket
import threading

target = "127.0.0.1"
ports = [22, 80, 443, 8080]

def scan_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    try:
        s.connect((target, port))
        print(f"Port {port} is OPEN")

    except:
        print(f"Port {port} is CLOSED")

    finally:
        s.close()


threads = []

for port in ports:
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("Scan complete.")
```

---

# 🔍 19. Threaded Code Explanation

## Import threading

```python
import threading
```

Imports Python's threading functionality.

---

## Create a function

```python
def scan_port(port):
```

This function contains the scanning logic for one port.

---

## Create a thread

```python
thread = threading.Thread(
    target=scan_port,
    args=(port,)
)
```

This creates a thread that will execute:

```python
scan_port(port)
```

---

## Start the thread

```python
thread.start()
```

Starts the thread.

---

## Store the thread

```python
threads.append(thread)
```

Stores the thread in a list.

This lets us wait for all threads later.

---

# ⏳ 20. What Does `join()` Do?

```python
thread.join()
```

`join()` tells the main program:

> Wait until this thread finishes.

The program therefore doesn't print:

```text
Scan complete.
```

until the scanning threads have finished.

---

# 🚀 21. Sequential vs Threaded Scanner

### Sequential

```text
Port 22
   ↓
Port 80
   ↓
Port 443
   ↓
Port 8080
```

Only one connection attempt is handled at a time.

### Threaded

```text
Port 22    ──┐
Port 80    ──┤
Port 443   ──┤
Port 8080  ──┘
```

Multiple connection attempts can be active concurrently.

This can significantly reduce scanning time for larger port lists.

---

# ⚠️ 22. Threading Has a Cost

More threads aren't automatically better.

Creating too many threads can cause:

- High resource usage
- Network congestion
- Large numbers of simultaneous connections
- Unstable behavior
- Excessive load on the target

For larger scanners, a **thread pool** is generally preferable to creating an unlimited number of threads.

---

# 🔐 23. Why Is Port Scanning Useful?

Port scanning has legitimate uses in:

### System Administration

An administrator can check which services are exposed on their servers.

### Network Troubleshooting

A port scan can help determine whether a service is reachable.

### Security Auditing

Security teams can identify unexpectedly exposed services.

For example:

```text
Expected:
22 SSH
80 HTTP
443 HTTPS

Unexpected:
3306 MySQL
```

An administrator can investigate why the database service is exposed.

### Learning Networking

Port scanning is a useful project for learning:

- TCP
- IP networking
- Sockets
- Exceptions
- Timeouts
- Concurrency
- Network security

---

# 🛡️ 24. What Does an Open Port Mean?

An open port generally means that something on the target is accepting connections on that port.

For example:

```text
443 OPEN
```

could indicate that an HTTPS service is listening.

It does **not automatically mean the system is vulnerable**.

An open port simply tells you that a service may be reachable.

Further investigation would be required to understand the service and its security configuration.

---

# 🚫 25. What Does a Closed Port Mean?

A closed TCP port generally means that the target responded but isn't accepting connections on that port.

For example:

```text
Port 9999 CLOSED
```

This doesn't necessarily mean that the entire machine is unreachable.

Other ports may still be open.

---

# 🔥 26. What About Firewalls?

A firewall can affect scanning results.

For example:

```text
Scanner
   |
   | TCP connection
   ↓
Firewall
   X
Server
```

The firewall may silently drop packets.

The scanner might experience a timeout instead of receiving a normal connection refusal.

Therefore:

```text
Connection failed ≠ definitely closed
```

This is why professional scanners distinguish between different states.

---

# 🧪 27. Limitations of This Beginner Scanner

This project intentionally keeps the logic simple.

It does not currently provide:

- UDP scanning
- Service/version detection
- OS detection
- SYN scanning
- Banner grabbing
- IPv6 support
- Advanced firewall detection
- Rate limiting
- Thread pools
- Detailed error classification

It is primarily a learning project for TCP sockets.

---

# 📚 28. Important Networking Concepts Learned

By completing this project, you learn the relationship between:

```text
IP Address
     ↓
Device
     ↓
Port
     ↓
TCP/UDP
     ↓
Network Service
```

For example:

```text
192.168.1.10:443
       │       │
       │       └── Port
       │
       └── IP address
```

TCP is the transport protocol used by the scanner.

---

# 🧩 29. Project Flow

The complete program works approximately like this:

```text
Start
  ↓
Select target IP
  ↓
Select ports
  ↓
Create TCP socket
  ↓
Set timeout
  ↓
Try connection
  ↓
 ┌───────────────┐
 │               │
Success        Exception
 │               │
 ↓               ↓
OPEN           CLOSED*
 │               │
 └───────┬───────┘
         ↓
    Close socket
         ↓
    Next port
         ↓
       Finish
```

`CLOSED*` is a simplified result in this beginner implementation. A failed connection can have several causes.

---

# 🛠️ 30. Possible Future Improvements

Once the basic scanner works, you can improve it by adding:

### 1. User input

Allow the user to enter:

```text
Target IP
Start port
End port
```

### 2. Threading

Scan multiple ports concurrently.

### 3. Thread pool

Control the maximum number of concurrent scans.

### 4. Better exception handling

Instead of:

```python
except:
```

use specific exceptions such as:

```python
except socket.timeout:
```

and:

```python
except socket.error:
```

### 5. UDP support

Create a separate UDP scanner.

### 6. Service identification

After finding an open port, identify the service where appropriate.

### 7. Results

Save results to:

```text
scan_results.txt
```

or:

```text
scan_results.csv
```

---

# 📦 31. Requirements

Python 3 is sufficient.

The basic scanner uses:

```python
import socket
```

and the threaded version uses:

```python
import threading
```

Both are part of Python's standard library.

No external packages are required.

---

# ▶️ 32. Running the Scanner

Save the file as:

```text
port_scanner.py
```

Run:

```bash
python port_scanner.py
```

For Windows, you can also use:

```bash
py port_scanner.py
```

---

# 🧪 33. Safe Testing

For learning, start with your own computer:

```python
target = "127.0.0.1"
```

You can also scan devices in a network you administer, provided you have authorization.

Avoid scanning systems you don't own or don't have permission to test.

---

# 🎯 34. What This Project Teaches

This small project introduces several important programming and networking concepts:

```text
Python
  │
  ├── Variables
  ├── Lists
  ├── Loops
  ├── Functions
  ├── Exceptions
  ├── try / except / finally
  ├── Sockets
  └── Threading

Networking
  │
  ├── IP addresses
  ├── Ports
  ├── TCP
  ├── UDP concepts
  ├── Timeouts
  └── Network services
```

---

# 📌 Summary

A port scanner tests whether network ports accept connections.

The basic scanner uses:

```python
socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
```

which creates an IPv4 TCP socket.

The scanner then:

```text
1. Selects a target
2. Selects ports
3. Creates a socket
4. Sets a timeout
5. Attempts a TCP connection
6. Reports the result
7. Closes the socket
8. Moves to the next port
```

Exception handling prevents one failed connection from stopping the entire scan.

The `finally` block ensures that:

```python
s.close()
```

runs regardless of whether the connection succeeds or fails.

Threading can then be introduced to allow multiple port checks to happen concurrently, making larger authorized scans considerably faster.

This project is a good starting point for learning **Python networking and basic network-security concepts**.
