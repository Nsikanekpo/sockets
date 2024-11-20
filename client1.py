import socket

def create_client():
    try:
        # Create a socket
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.settimeout(10)  # Set timeout to avoid hanging indefinitely

        # Connect to the server at localhost:9000
        mysock.connect(('127.0.0.1', 9000))
        print("Connected to server")

        # Send the HTTP GET request
        cmd = 'GET / HTTP/1.0\r\n\r\n'.encode()
        mysock.send(cmd)

        # Receive and print the server's response
        data = ""
        while True:
            chunk = mysock.recv(512)
            if len(chunk) < 1:
                break
            data += chunk.decode()

        print("Received data from server:")
        print(data)

    except socket.timeout:
        print("Error: The connection timed out.")
    except ConnectionRefusedError:
        print("Error: Unable to connect to the server. Is it running?")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        # Ensure the socket is closed properly
        mysock.close()
        print("\nSocket closed.")

create_client()

