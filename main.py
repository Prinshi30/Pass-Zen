
try:
    from tkinter import *
except ImportError:
    from Tkinter import *
import time
from pwgenfunc import RandPass
import pyperclip

# Function to generate a password and update the UI
def pwGenerator(size=8):
    data = RandPass(size)
    new_password = data[0]
    pw_strength = data[1]
    pw_color = data[2]

    # Update the password entry field and label with the new password and its strength
    PASSWORD.set(new_password)
    label_strength.configure(foreground="white", background=pw_color, text=pw_strength, font=('Segoe UI', 10, 'bold'), bd=10, height=1, width=10)
    
    # Copy the new password to the clipboard
    gui.clipboard_clear()
    gui.clipboard_append(new_password)
    gui.update()
    time.sleep(0.02)
    gui.update()

# Main window setup
gui = Tk()
gui.title("Password Generator")
gui.config(bg='#1A1A1A')
width = 600
height = 342
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
gui.geometry(f"{width}x{height}+{int(x)}+{int(y)}")

# Variables
PASSWORD = StringVar()
PW_SIZE = IntVar()
PW_SIZE.set(8)  # Default password size

# Frame setup
Top = Frame(gui, width=width, bg='#1A1A1A')
Top.pack(side=TOP)

Form = Frame(gui, width=width, bg="#1A1A1A")
Form.pack(side=TOP)

Bot = Frame(gui, width=width)
Bot.pack(side=BOTTOM)

# UI Elements
label_password = Label(Form, font=('Segoe UI', 18), text="Password", foreground="white", background="#1A1A1A", bd=10)
label_password.grid(row=0, pady=10)

label_strength = Label(Form, font=('Segoe UI', 10, 'bold'), foreground="white", background="white", text="Weak", bd=10, height=1, width=10)
label_strength.grid(row=0, column=3, pady=10, padx=10)

label_pw_size = Label(Form, font=('Segoe UI', 18), text="Size", foreground="white", background="#1A1A1A", bd=10)
label_pw_size.grid(row=2, pady=10)

label_instructions = Label(Bot, width=width, font=('Segoe UI', 12, 'bold'), text="Password Generated to your Clipboard!", foreground="white", background="#1A1A1A", bd=1, relief=SOLID)
label_instructions.pack(fill=X)

# Widgets
password = Entry(Form, textvariable=PASSWORD, font=(18), width=24)
password.grid(row=0, column=1, columnspan=2)

pw_size = Scale(Form, from_=8, to=24, length=200, width=24, sliderlength=14, orient=HORIZONTAL, variable=PW_SIZE, foreground="white", background="#1A1A1A", font=(16))
pw_size.grid(row=2, column=1, columnspan=2)

# Function to copy the generated password to the clipboard
def Copy_password():
    pyperclip.copy(PASSWORD.get())

# Buttons
Button(Top, text='COPY TO CLIPBOARD', foreground="white", background="#1A1A1A", command=Copy_password).pack(pady=5)

btn_generate = Button(Form, text="Generate Now", width=20, command=lambda: pwGenerator(PW_SIZE.get()))
btn_generate.grid(row=4, column=1, columnspan=2)

# Run the main event loop
gui.resizable(False, False)
gui.mainloop()


