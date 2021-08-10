"""
Main script of handling the client-side of the chat app
"""

import socket
import threading
from time import sleep
from client_ui_styling import style_text_browser

HEADER = 64
PORT = 5050
SERVER = input("Enter the IP of the server: ")
if SERVER == "":
    SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
MESSAGE_SPLIT_CHARS = "&<>&"
UPDATE_FREQ = 5
SUCCESS_PHRASE = "OK"

client: socket.socket = None
messages = []
messages_formatted = ""
connected = None
display_name: str = ""


def padd_msg_bytes(msg: str, pad_len: int):
    global FORMAT
    if FORMAT:
        if type(msg) != bytes:
            msg = msg.encode(FORMAT)
    msg += b' ' * (pad_len - len(msg))
    return msg


def get_structured_message(str_message: str):
    """Returns 2 formatted messages that can be sent to the server"""
    message = str_message.encode(FORMAT)  # Encodes message
    send_length = padd_msg_bytes(msg=str(len(message)).encode(FORMAT), pad_len=HEADER)
    # Formats and pads the length message, so server can receive it
    return message, send_length


def start():  # Takes in the ClientMainWindow so that it can be interacted with
    """Thread that handles the input in the console"""
    global client, connected, display_name

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Sets up the connection object
    try:
        client.connect(ADDR)  # Connects to the domain
    except ConnectionRefusedError:
        print("Error: could not connect to server")
        quit()
    except TimeoutError:
        print("Error: the request to connect to the server timed out")
        quit()

    try:   # Wrapped in a try-catch so that, should the server close, the client doesn't produce an error code
        display_name_status = ""
        while display_name_status != SUCCESS_PHRASE:
            requested_display_name = input("Enter your display name: ")
            if requested_display_name:  # If requested_display_name is NOT empty
                client.send(padd_msg_bytes(requested_display_name, HEADER))  # Sends to the server the display name

                display_name_status = client.recv(HEADER).decode(FORMAT).strip()  # Receives the response to the
                # display name assignment (server-side)

                if display_name_status != SUCCESS_PHRASE:
                    print(f"Error: {display_name_status}")

        display_name = requested_display_name  # Set globally here so that it can be accessed by the UI

        messages.append("You have successfully connected")

        connected = True

        update_message_thread = threading.Thread(target=update_messages)
        update_message_thread.start()

    except ConnectionResetError:
        connected = False
        print("Error: server closed")
        quit()


def update_messages():
    """Thread that handles the receiving of messages from the server"""
    try:
        global connected, messages, messages_formatted
        while connected:
            send_length, message = get_structured_message("")  # Gets the formatted message of no text, which is
            # considered by the server to be a request for up to date messages
            client.send(send_length)
            client.send(message)
            msg_length = client.recv(HEADER).decode(FORMAT)  # Receives the length of the message list
            messages_raw = client.recv(int(msg_length)).decode(FORMAT)  # Receives the message list
            messages += [n for n in messages_raw.split(MESSAGE_SPLIT_CHARS) if n not in messages]  # Splits received
            # list and adds new messages to global list
            messages_formatted = style_text_browser(messages)  # Formatted for the PyQt TextBrowser

            sleep(1 / UPDATE_FREQ)  # Waits for frequency
    except ConnectionResetError:
        connected = False
        print("Error: server closed")
        quit()


def send_message(str_message: str):
    """Sends a single message to the server"""
    global connected

    if str_message == "":
        print("[CLIENT ERROR] Message must be entered")  # If nothing is entered, tell the user
    elif str_message.replace(MESSAGE_SPLIT_CHARS, "") != str_message:
        print("[CLIENT ERROR] Message contains forbidden characters")  # If the split character is used,
        # tell the user
    else:
        message, send_length = get_structured_message(str_message)

        client.send(send_length)
        client.send(message)

        if str_message == DISCONNECT_MESSAGE:
            connected = False


if __name__ == '__main__':
    start()

