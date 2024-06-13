from tkinter import messagebox
from tkinter import *

class EntrySaver:

    def __init__(self, website_entry, email_entry, password_entry):
        self.website_entry = website_entry
        self.email_entry = email_entry
        self.password_entry = password_entry

    def encrypt_password(self, password, shift=3):
        encrypted_password = []
        for char in password:
            encrypted_char = chr((ord(char) + shift - 32) % 95 + 32)  # Shift characters in printable ASCII range (32-126)
            encrypted_password.append(encrypted_char)
        return ''.join(encrypted_password)

    def save(self):

        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if len(website) == 0 or len(email) == 0 or len(password) == 0:
            self.messagebox.showerror(title="Error", message="Please enter all details")
        else:
            with open("data.txt", "r") as data_file:
                for line in data_file:
                    existing_website, existing_email, _ = line.strip().split(" | ")
                    if website.lower() == existing_website.lower() and email.lower() == existing_email.lower():
                        messagebox.showwarning(title="Existing Entry", message=f"You have already used this website ({existing_website}) and email ({existing_email}) combination.")
                        break
                else:
                    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}" f"\nPassword: {password} \nIs it ok to save?")

                    if is_ok:
                        with open("data.txt", "a") as data_file:
                            data_file.write(f"{website} | {email} | {self.encrypt_password(password, 3)}\n")
                            self.website_entry.delete(0, END)
                            self.password_entry.delete(0, END)
                            self.email_entry.delete(0, END)
                            self.website_entry.focus()
