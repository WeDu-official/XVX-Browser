import socket
import threading
HOST = socket.gethostbyname(socket.gethostname())   # Use same IPV4 adress  # You can use any port between 0 to 65535
LISTENER_LIMIT = 2
MAX_CLIENTS = 2
active_clients = []
active_clients2 = []
# Function to listen for upcoming messages from a client
def listen_for_messages(client, username):
    while 1:
        try:
            message = client.recv(2048).decode('utf-8')
            if message != '':

                final_msg = username + '~' + message
                send_messages_to_all(final_msg)

            else:
                print(f"The message send from client {username} is empty")
        except (ConnectionResetError,ConnectionAbortedError):
            pass

# Function to send message to a single client
def send_message_to_client(client, message):
    try:
        client.sendall(message.encode())
    except ConnectionResetError:
        pass

# Function to send any new message to all the clients that
# are currently connected to this server
def send_messages_to_all(message):
    for user in active_clients:
        send_message_to_client(user[1], message)

def dead():
    if len(active_clients2) >= MAX_CLIENTS:
        return True
    else:
        print(len(active_clients2),MAX_CLIENTS)
        return False
# Function to handle client
def client_handler(client):
    # Server will listen for client message that will
    # Contain the username
    while 1:

        username = client.recv(2048).decode('utf-8')
        if len(active_clients2) == MAX_CLIENTS:
            exit()
        if username != '':
            active_clients2.append(username)
            active_clients.append((username, client))
            prompt_message = "SERVER~" + f"{username} added to the chat"
            send_messages_to_all(prompt_message)
            break
        else:
            print("Client username is empty")

    threading.Thread(target=listen_for_messages, args=(client, username,)).start()


# Main function
def main(PORT):
    # Creating the socket class object
    # AF_INET: we are going to use IPv4 addresses
    # SOCK_STREAM: we are using TCP packets for communication
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Creating a try catch block
    try:

        print(f"Trying to bind to HOST: {HOST} and PORT: {PORT}")
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST} {PORT}")
    except:
        print(f"Unable to bind to host {HOST} and port {PORT}")
        return  # Exit the program if binding fails
    # Set server limit
    try:
        server.listen(LISTENER_LIMIT)
    except OSError as e:
        print(f"Error during listen: {e}")
        return  # Exit the program if listen fails
    # This while loop will keep listening to client connections
    while 1:
        print(active_clients2)
        if len(active_clients2) >= MAX_CLIENTS:
            print(f'{len(active_clients2),MAX_CLIENTS}')
            if len(active_clients2) == MAX_CLIENTS:
                break
            print("Server is full. Rejecting additional connections.")
            client, address = server.accept()
            client.sendall("Server is full.".encode())
            client.close()
        else:
            client, address = server.accept()
            print(f"Successfully connected to client {address[0]} {address[1]}")
            threading.Thread(target=client_handler, args=(client,)).start()
if __name__ == '__main__':
    with open('port.txt','r') as x:
        data = int(x.read())
    main(data)