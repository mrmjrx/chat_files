""""
Main script for the server side of that app
"""

import socket
import threading

HEADER = 64  # Number of bytes for initial contact with client
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())  # Gets IP address
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
MESSAGE_SPLIT_CHARS = "&<>&"
SUCCESS_PHRASE = "OK"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

messages = []
display_names = []


def padd_msg_bytes(msg: str, pad_len: int):
    global FORMAT
    if FORMAT:
        if type(msg) != bytes:
            msg = msg.encode(FORMAT)
    msg += b' ' * (pad_len - len(msg))
    return msg


def get_structured_message(str_message: str):
    """Returns formatted messages the client will be able to understand"""
    message = str_message.encode(FORMAT)  # Encodes the message
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)  # Encodes the message providing length
    send_length += b' ' * (HEADER - len(send_length))  # Pads the message so the client can receive it
    return message, send_length


def handle_client(conn: socket.socket, addr):
    """Thread that handles each individual client"""
    try:  # Wrapped in a try-catch so that if the client suddenly disconnects, the server doesn't crash
        global messages

        status = ""
        while status != SUCCESS_PHRASE:  # While the setting of the display name is not successful
            display_name_req = conn.recv(HEADER).decode(FORMAT).strip()  # Formats length of display name
            if display_name_req:  # First message is blank, so check to see if there is any content
                status = SUCCESS_PHRASE if display_name_req not in display_names else "Name already taken."
                conn.send(padd_msg_bytes(status, HEADER))  # Send the formatted message of the status to the client
        display_name = display_name_req

        messages.append(f"[SERVER] {display_name} ({addr[0]}:{addr[1]}) connected.")
        print(messages[-1])

        connected = True
        while connected:
                msg_length = conn.recv(HEADER).decode(FORMAT)  # Receive message length message
                msg_length = int(msg_length)
                if msg_length == 0:  # If the length is 0, this is a request for messages sent from other clients
                    messages_formatted = MESSAGE_SPLIT_CHARS.join(messages)  # Convert list to string
                    message, send_length = get_structured_message(messages_formatted)  # Formats string
                    conn.send(send_length)
                    conn.send(message)
                else:
                    msg = conn.recv(msg_length).decode(FORMAT)  # Receive entire message
                    if msg == DISCONNECT_MESSAGE:
                        connected = False
                    messages.append(f"[{display_name}] {msg}")  # Add message to list
                    print(messages[-1])

    except ConnectionResetError:
        connected = False

    print(f"[SERVER] {display_name} disconnected.")
    conn.close()



def start():
    """Function that listens for new connections, and creates threads for each client connecting"""
    server.listen()  # Listen for incoming connections
    print(f"[SERVER] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()  # Wait until new connection opens, then gather this information
        thread = threading.Thread(target=handle_client, args=(conn, addr))  # Start thread that will handle the client
        thread.start()
        print(f"[INFO] Number of active connections: {threading.active_count() - 1}")


print("[SERVER] Server is starting...")
start()
