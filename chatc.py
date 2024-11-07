# ================Import Modules===============#
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
gu = tk.Tk()
gu.title('CTS')
gu.geometry('200x170')
gu.resizable(False,False)
DARK_GREY = '#2F4550'
MEDIUM_GREY = '#424951'
OCEAN_BLUE = '#64A292'
WHITE = "white"
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)
setup_label = tk.Label(gu, text="Enter the server port", font=SMALL_FONT, bg=DARK_GREY, fg=WHITE)
setup_label.pack()

setup_textbox = tk.Entry(gu, font=FONT, bg=MEDIUM_GREY, fg=WHITE)
setup_textbox.pack()

setup_label2 = tk.Label(gu, text="Enter the server host", font=SMALL_FONT, bg=DARK_GREY, fg=WHITE)
setup_label2.pack()

setup_textbox2 = tk.Entry(gu, font=FONT, bg=MEDIUM_GREY, fg=WHITE)
setup_textbox2.pack()
def start():
    global setup_textbox,setup_textbox2,DARK_GREY,MEDIUM_GREY,OCEAN_BLUE,WHITE,FONT,BUTTON_FONT,SMALL_FONT
    # ================Host & Port===============#
    HOST = setup_textbox2.get()
    PORT = int(setup_textbox.get())
    # ===============Colors for GUI================#
    # Creating a socket object
    # AF_INET: we are going to use IPv4 addresses
    # SOCK_STREAM: we are using TCP packets for communication
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # ==============================Functions==============================#
    # ================Connect Server===============#
    def connect():
        # try except block
        try:
            client.connect((HOST, PORT))
            print("Successfully connected to server")
            add_message("[SERVER] Successfully connected to the server")
        except:
            messagebox.showerror("Unable to connect to server", f"Unable to connect to server {HOST} {PORT} because it might be not exist or full or maybe other reasons")
        username = username_textbox.get()
        if username != '':
            try:
                client.sendall(username.encode())
            except OSError:
                exit()
        else:
            messagebox.showerror("Invalid username", "Username cannot be empty")

        threading.Thread(target=listen_for_messages_from_server, args=(client,)).start()

        username_textbox.config(state=tk.DISABLED)
        username_button.config(state=tk.DISABLED)


    # ================ADD MESSAGE===============#
    def add_message(message):
        message_box.config(state=tk.NORMAL)
        message_box.insert(tk.END, message + '\n')
        message_box.config(state=tk.DISABLED)


    # ================Send Message===============#
    def send_message():
        message = message_textbox.get("1.0",tk.END)
        if message != '':
            try:
                client.sendall(message.encode())
            except (OSError,ConnectionResetError):
                pass
            message_textbox.delete("1.0", tk.END)
        else:
            messagebox.showerror("Empty message", "Message cannot be empty")


    # ================ TKINTER ===============#
    root = tk.Tk()
    root.geometry("600x600")
    root.title("Chat Application📶")
    root.resizable(False, False)

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=4)
    root.grid_rowconfigure(2, weight=1)

    top_frame = tk.Frame(root, width=600, height=100, bg=DARK_GREY)
    top_frame.grid(row=0, column=0, sticky=tk.NSEW)

    middle_frame = tk.Frame(root, width=600, height=400, bg=MEDIUM_GREY)
    middle_frame.grid(row=1, column=0, sticky=tk.NSEW)

    bottom_frame = tk.Frame(root, width=600, height=100, bg=DARK_GREY)
    bottom_frame.grid(row=2, column=0, sticky=tk.NSEW)

    username_label = tk.Label(top_frame, text="Enter username:", font=FONT, bg=DARK_GREY, fg=WHITE)
    username_label.pack(side=tk.LEFT, padx=10)

    username_textbox = tk.Entry(top_frame, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=23)
    username_textbox.pack(side=tk.LEFT)

    username_button = tk.Button(top_frame, text="Join", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=connect)
    username_button.pack(side=tk.LEFT, padx=15)

    message_textbox = tk.scrolledtext.ScrolledText(bottom_frame, font=FONT, bg=MEDIUM_GREY, fg=WHITE, width=36,height=5)
    message_textbox.pack(side=tk.LEFT, padx=10)

    message_button = tk.Button(bottom_frame, text="Send", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=send_message)
    message_button.pack(side=tk.LEFT, padx=10)

    message_box = scrolledtext.ScrolledText(middle_frame, font=SMALL_FONT, bg='gray', width=67, height=26.5)
    message_box.config(state=tk.DISABLED)
    message_box.pack(side=tk.TOP)

    # ================Listen for Incomming Message===============#
    """
    The incomming message is encoded in utf-8 , which we need to decode to print in the tkinter box.
    """


    def listen_for_messages_from_server(client):
        while 1:
            try:
                try:
                    message = client.recv(2048).decode('utf-8')
                    if message != '':
                        username = message.split("~")[0]
                        content = message.split('~')[1]
                        add_message(f"[{username}] {content}")

                    else:
                        messagebox.showerror("Error", "Message recevied from client is empty")
                except (ConnectionAbortedError,OSError):
                    exit()
            except ConnectionResetError:
                pass
    root.mainloop()

# ================ Main ===============#
setup_button = tk.Button(gu, text="go", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=start)
setup_button.pack()
def main():
    gu.mainloop()

if __name__ == '__main__':
    main()