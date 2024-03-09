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

    request_line = data.decode().splitlines()[0]  # Get the request line
    path = request_line.split()[1]  # Extract the path from the request line

    resp_200 = "HTTP/1.1 200 OK\r\n\r\n"
    resp_404 = "HTTP/1.1 404 Not Found\r\n\r\n"
    print(path)
    if path == "/":
        response = resp_200  # Prepare the 200 OK response
    else:
        response = resp_404  # Prepare the 404 Not Found response

    connection.sendall(response.encode())  # Send the response


if __name__ == "__main__":
    main()
