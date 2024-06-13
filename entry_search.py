from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class EntrySearch:
    def __init__(self, window):
        self.window = window

    def decrypt_password(self, encrypted_password, shift=3):
        decrypted_password = []
        for char in encrypted_password:
            decrypted_char = chr((ord(char) - shift - 32) % 95 + 32)
            decrypted_password.append(decrypted_char)
        return ''.join(decrypted_password)

    def open_search_window(self):
        search_window = Toplevel(self.window)
        search_window.title("Search Entry")
        search_window.config(padx=50, pady=50, bg='#abcdef')  # Change the background color of the search window

        def handle_enter(event, current_widget, next_widget):
            # Move to the next widget or trigger the function if it's the last
            current_widget.focus()
            if next_widget:
                next_widget.focus()
            return 'break'  # Prevent the default behavior

        def search():

            search_term_website = search_entry_website.get().lower()
            search_term_email = search_entry_email.get().lower()
            if search_term_website and search_term_email:
                with open("data.txt", "r") as data_file:
                    for line in data_file:
                        website, email, password = line.strip().split(" | ")
                        if search_term_website == website.lower() and search_term_email == email.lower():
                            messagebox.showinfo(title="Search Result",
                                                message=f"Website: {website}\nEmail: {email}\nPassword: {self.decrypt_password(password, 3)}")
                            clear_entries()

                            return
                    messagebox.showinfo(title="Search Result", message="No matching entry found.")
                    clear_entries()
            else:
                messagebox.showwarning(title="Error", message="Please enter all the details.")
                if search_term_website:
                    search_entry_email.focus()
                else:
                    search_entry_website.focus()

        def clear_entries():
            search_entry_website.delete(0, END)
            search_entry_email.delete(0, END)
            search_entry_website.focus()

        search_label_website = ttk.Label(search_window, text="Website:")
        search_label_website.grid(row=0, column=0, pady=5)

        search_entry_website = ttk.Entry(search_window, width=30, style='TEntry')
        search_entry_website.grid(row=0, column=1, pady=5, padx=5, sticky="w")
        search_entry_website.focus()

        search_label_email = ttk.Label(search_window, text="Email:")
        search_label_email.grid(row=1, column=0, pady=5)

        search_entry_email = ttk.Entry(search_window, width=30, style='TEntry')
        search_entry_email.grid(row=1, column=1, pady=5, padx=5, sticky="w")

        search_button = Button(search_window, text="Search", command=search)
        search_button.grid(row=2, column=1, pady=5, sticky="w")

        back_button = Button(search_window, text="Back", command=search_window.destroy)
        back_button.grid(row=3, column=1, pady=10)

        # Bind Enter key to navigate
        search_entry_website.bind("<Return>", lambda e: handle_enter(e, search_entry_website, search_entry_email))
        search_entry_email.bind("<Return>", lambda e: handle_enter(e, search_entry_email, search_button))
