import socket

target = input("Target IP/hostname: ")
start = int(input("Start port: "))
end = int(input("End port: "))

print(f"\nScanning {target}...\n")

for port in range(start, end + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    try:
        s.connect((target, port))
        print(f"Port {port} is OPEN")

    except:
        print(f"Port {port} is CLOSED")

    finally:
        s.close()

print("\nScan complete.")