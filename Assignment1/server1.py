import socket

def start_server(host="0.0.0.0", port=5050):
    server_name = input("Enter your server name: ")
    server_number = int(input("Enter a server integer (1-100): "))

    if not (1 <= server_number <= 100):
        print("Invalid server number! Exiting...")
        return

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server '{server_name}' is running on {host}:{port}")

    while True:
        print("\nWaiting for a client to connect...")
        conn, addr = server_socket.accept()
        print(f"Connected to client at {addr}")

        data = conn.recv(1024).decode()
        if not data:
            conn.close()
            continue

        client_name, client_number_str = data.split("::")
        client_number = int(client_number_str)

        if not (1 <= client_number <= 100):
            print("Invalid number received from client. Shutting down server...")
            conn.close()
            server_socket.close()   
            return                  
        
        print(f"Client's Name:   {client_name}")
        print(f"Server's Name:   {server_name}")
        print(f"Client's Number: {client_number}")
        print(f"Server's Number: {server_number}")
        print(f"Sum:             {client_number + server_number}")

        response = f"{server_name}::{server_number}"
        conn.send(response.encode())
        conn.close()
        print("Connection closed.")

if __name__ == "__main__":
    start_server()
