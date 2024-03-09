import socket


def main():
    print("Logs from your program will appear here!")

    addr = "localhost"
    port = 4221
    server_socket = socket.create_server((addr, port), reuse_port=True)
    connection, address = server_socket.accept()  # Accept a TCP connection
    print(f"Connection established with {address}")

    data = connection.recv(4096)  # Read data from the connection
    print(f"Received data: {data}")

    response = "HTTP/1.1 200 OK\r\n\r\n"  # Prepare the HTTP response
    connection.sendall(response.encode())  # Send the response
    connection.close()  # Close the connection


if __name__ == "__main__":
    main()
