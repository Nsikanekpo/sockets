from socket import *

def createServer():
    # Create a socket and set options to reuse the address
    serversocket = socket(AF_INET, SOCK_STREAM)
    serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # Allow port reuse
    
    try:
        serversocket.bind(('localhost', 9000))  # Bind to localhost on port 9000
        serversocket.listen(5)
        print('Server is listening on port 9000...')

        while True:
            # Accept incoming connections
            clientsocket, address = serversocket.accept()
            print(f"Connection established with {address}")

            try:
                # Receive data from client
                rd = clientsocket.recv(5000).decode()
                print(f"Received from client: {rd}")

                # Send a response back to the client
                data = "HTTP/1.1 200 OK\r\n"
                data += "Content-Type: text/html; charset=utf-8\r\n"
                data += "\r\n"
                data += "<html><body>Hello World</body></html>\r\n\r\n"
                clientsocket.sendall(data.encode())
                print("Response sent to client")

            except Exception as e:
                print(f"Error during connection handling: {e}")
            finally:
                # Close the client connection
                clientsocket.close()
                print("Client connection closed")

    except KeyboardInterrupt:
        print("\nShutting down the server...")
    except Exception as exc:
        print(f"Server Error: {exc}")
    finally:
        # Always close the server socket
        serversocket.close()
        print("Server socket closed.")

createServer()

