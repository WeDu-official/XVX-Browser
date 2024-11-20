import subprocess
import tkinter as tk
gu = tk.Tk()
gu.title('MAS')
gu.geometry('200x100')
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
def ch():
    with open('port.txt','w') as x:
        x.write(setup_textbox.get())
    subprocess.Popen('python chats.py')
setup_button = tk.Button(gu, text="make", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=ch)
setup_button.pack()
gu.mainloop()