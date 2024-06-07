from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()


    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please enter all details")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}" f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                email_entry.delete(0, END)
                website_entry.focus()

# copy password

def copy_password():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo(title="Copied", message="Password copied to clipboard")
    else:
        messagebox.showwarning(title="No Password", message="Please generate a password first")


# ---------------------------- UI SETUP ------------------------------- #

def on_enter(e):
    e.widget['background'] = '#add8e6'

def on_leave(e):
    e.widget['background'] = '#0078d7'

def show_add_tooltip(event=None):
    add_button_tooltip.config(text="Click to save the entered details")

def handle_enter(event, current_widget, next_widget):
    # Move to the next widget or trigger the function if it's the last
    current_widget.focus()
    if next_widget:
        next_widget.focus()
    return 'break'  # Prevent the default behavior

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg='#e0f7fa')  # Set a soft, light blue background color

style = ttk.Style()
style.theme_use('clam')  # Using 'clam' theme for a modern look

style.configure('TLabel',
                font=('Arial', 12, 'bold'),
                background='#e0f7fa',  # Match background color
                foreground='#333333')
style.configure('TEntry',
                padding='5 5 5 5',
                font=('Arial', 12),
                foreground='#333333',
                background='#ffffff')
style.configure('TButton',
                font=('Arial', 12, 'bold'),
                padding=5,
                background='#0078d7',
                foreground='white')
style.map('TButton',
          background=[('active', '#005fa3')])

# Canvas
canvas = Canvas(window, width=200, height=200, highlightthickness=0, bg='#e0f7fa')  # Match background color
logo_img = PhotoImage(file="logo.png")  # Update with your logo path
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, pady=20)

# Labels
website_label = ttk.Label(window, text="Website:")
website_label.grid(row=1, column=0, pady=5)
email_label = ttk.Label(window, text="Email/Username:")
email_label.grid(row=2, column=0, pady=5)
password_label = ttk.Label(window, text="Password:")
password_label.grid(row=3, column=0, pady=5)

# Entries
website_entry = ttk.Entry(window, width=60, style='TEntry')
website_entry.grid(row=1, column=1, columnspan=2, pady=5, padx=5, sticky="w")
website_entry.focus()

email_entry = ttk.Entry(window, width=60, style='TEntry')
email_entry.grid(row=2, column=1, columnspan=2, pady=5, padx=5, sticky="w")

password_entry = ttk.Entry(window, width=30, style='TEntry')
password_entry.grid(row=3, column=1, pady=5, padx=5, sticky="w")

copy_icon = PhotoImage(file="copy_icon.png")
small_copy_icon = copy_icon.subsample(0, 0)

# Buttons
generate_password_button = Button(window, text="Generate Password", command=generate_password, bg='#0078d7', fg='white', font=('Arial', 12, 'bold'))
generate_password_button.grid(row=3, column=2, pady=5, padx=5, sticky="w")
generate_password_button.bind("<Enter>", on_enter)
generate_password_button.bind("<Leave>", on_leave)

copy_password_button = Button(window, image=small_copy_icon, text=" Copy password", compound=LEFT, width=-18, command=copy_password, bg='#0078d7', fg='white', font=('Arial', 12, 'bold'))
copy_password_button.grid(row=4, column=1, pady=5, sticky="w")  # Removed padx=5
copy_password_button.bind("<Enter>", on_enter)
copy_password_button.bind("<Leave>", on_leave)

add_button = Button(window, text="Add", width=16, command=save, bg='#0078d7', fg='white', font=('Arial', 12, 'bold'))
add_button.grid(row=4, column=2, pady=10, sticky="w")
add_button.bind("<Enter>", show_add_tooltip)  # Bind Enter event to show tooltip
add_button.bind("<Leave>", lambda event: add_button_tooltip.config(text=""))  # Clear tooltip on Leave event

butto_quuit = Button(window,text="Quit",command=window.destroy)
butto_quuit.grid(row=4, column=3, pady=10, sticky="w")

add_button_tooltip = ttk.Label(window, background='#e0f7fa', font=('Arial', 10), anchor='w')
add_button_tooltip.grid(row=5, column=2, sticky="w")

# Bind Enter key to navigate
website_entry.bind("<Return>", lambda e: handle_enter(e, website_entry, email_entry))
email_entry.bind("<Return>", lambda e: handle_enter(e, email_entry, password_entry))
password_entry.bind("<Return>", lambda e: handle_enter(e, password_entry, add_button))

window.mainloop()