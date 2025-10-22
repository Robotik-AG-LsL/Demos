import socket

ARDUINO_IP = "192.168.178.28"  # Arduino IP
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((ARDUINO_IP, PORT))
    print(f"Connected to Arduino at {ARDUINO_IP}:{PORT}")

    # Send data
    message = "Hello from Raspberry Pi\n"
    s.sendall(message.encode())
    print("Sent:", message.strip())

    # Receive echo (or response)
    data = s.recv(1024)  # Wait for reply (blocking)
    print("Received:", data.decode().strip())


    while True:
        msg = input("Send to Arduino: ")
        s.sendall((msg + "\n").encode())
        data = s.recv(1024)
        print("Arduino replied:", data.decode().strip())
