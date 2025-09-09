import socket

def start_client(server_ip="127.0.0.1", port=5050):
    client_name = input("Enter your name: ")

    client_number = int(input("Enter an integer (1-100): "))

    if not (1 <= client_number <= 100):
        print("Number out of range! Closing client.")
        return

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))
    print(f"Connected to server at {server_ip}:{port}")

    message = f"{client_name}::{client_number}"
    client_socket.send(message.encode())

    data = client_socket.recv(1024).decode()
    server_name, server_number_str = data.split("::")
    server_number = int(server_number_str)

    print("\n--- Communication Summary ---")
    print(f"Client's Name:   {client_name}")
    print(f"Server's Name:   {server_name}")
    print(f"Client's Number: {client_number}")
    print(f"Server's Number: {server_number}")
    print(f"Sum:             {client_number + server_number}")

    client_socket.close()
    print("Connection closed.")


if __name__ == "__main__":
    start_client()
