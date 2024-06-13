from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import pyperclip
from entry_saver import EntrySaver
from password_generator import PasswordGenerator
from entry_search import EntrySearch
from entry_delete import EntryDelete


# copy password

def copy_password():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo(title="Copied", message="Password copied to clipboard")
    else:
        messagebox.showwarning(title="No Password", message="Please generate a password first")


# ---------------------------- UI SETUP ------------------------------- #

def handle_enter(event, current_widget, next_widget):
    # Move to the next widget or trigger the function if it's the last
    current_widget.focus()
    if next_widget:
        next_widget.focus()
    return 'break'  # Prevent the default behavior
def on_enter(e):
    e.widget['background'] = '#add8e6'

def on_leave(e):
    e.widget['background'] = '#0078d7'

def on_enter1(e):
    e.widget['background'] ='#bfbfbf'

def on_leave1(e):
    e.widget['background'] ='#cc3333'


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
email_label = ttk.Label(window, text="Email:")
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

password_generator = PasswordGenerator(password_entry)
# Buttons
generate_password_button = Button(window, text="Generate Password", command=password_generator.gen_password, bg='#0078d7', fg='white', font=('Arial', 12, 'bold'))
generate_password_button.grid(row=3, column=2, pady=5, padx=5, sticky="w")
generate_password_button.bind("<Enter>", on_enter)
generate_password_button.bind("<Leave>", on_leave)

copy_password_button = Button(window, image=small_copy_icon, text=" Copy password", compound=LEFT, width=-18, command=copy_password, bg='#0078d7', fg='white', font=('Arial', 12, 'bold'))
copy_password_button.grid(row=4, column=1, pady=5, sticky="w")  # Removed padx=5
copy_password_button.bind("<Enter>", on_enter)
copy_password_button.bind("<Leave>", on_leave)

password_saver = EntrySaver(website_entry, email_entry, password_entry)

add_button = Button(window, text="Add", width=16, command=password_saver.save, bg='#0078d7', fg='white', font=('Arial', 12, 'bold'))
add_button.grid(row=4, column=2, pady=10, sticky="w")
add_button.bind("<Enter>", show_add_tooltip)  # Bind Enter event to show tooltip
add_button.bind("<Leave>", lambda event: add_button_tooltip.config(text=""))  # Clear tooltip on Leave event

button_quit = Button(window,text="Quit",command=window.destroy,  font=('Arial', 14, 'bold'), bg='#cc3333', fg='white')
button_quit.grid(row=4, column=3, pady=10, sticky="w")
button_quit.bind("<Enter>", on_enter1)
button_quit.bind("<Leave>", on_leave1)

add_button_tooltip = ttk.Label(window, background='#e0f7fa', font=('Arial', 10), anchor='w')
add_button_tooltip.grid(row=5, column=2, sticky="w")

website_entry.bind("<Return>", lambda e: handle_enter(e, website_entry, email_entry))
email_entry.bind("<Return>", lambda e: handle_enter(e, email_entry, password_entry))
password_entry.bind("<Return>", lambda e: handle_enter(e, password_entry, add_button))



# search button
entry_search = EntrySearch(window)
search_button = Button(window, text="Search Entry", command=entry_search.open_search_window, font=('Arial', 14, 'bold'), bg='#cc3333', fg='white', padx=20)
search_button.grid(row=6, column=0, columnspan=2, pady=30)
search_button.bind("<Enter>", on_enter1)
search_button.bind("<Leave>", on_leave1)



entry_delete = EntryDelete(window)
# Create Delete Entry button in the main window
delete_button = Button(window, text="Delete Entry", command=entry_delete.delete_search_window, font=('Arial', 14, 'bold'), bg='#cc3333', fg='white', padx=20)
delete_button.grid(row=6, column=2, columnspan=2, pady=30)
delete_button.bind("<Enter>", on_enter1)
delete_button.bind("<Leave>", on_leave1)


window.mainloop()