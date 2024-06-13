# Password Manager Application

This is a simple password manager application developed using Python and Tkinter. It provides a user-friendly interface for generating strong passwords, securely storing website credentials, and copying passwords to the clipboard.

## Description

The Password Manager application is designed to offer a convenient solution for managing passwords. With the increasing number of online accounts and the importance of strong, unique passwords, this application aims to simplify the process of password management. It allows users to generate complex passwords, store them securely, and access them when needed.

## Features

- **Generate Password:** Automatically generates a strong password using a combination of letters, numbers, and symbols.

- **Secure Storage:** Users can store their website, email, and password details securely within the application. This feature helps users manage multiple accounts without the risk of forgetting their login details.

- **Save Entry:** Stores website, email, and encrypted password information securely in a text file (`data.txt`).

- **Clipboard Functionality:** The application provides a convenient clipboard functionality that allows users to copy passwords with a single click. This feature makes it easy to paste passwords directly into login forms, enhancing user experience and efficiency.

- **Search Entry:** Allows users to search for saved entries based on website or email.

- **Delete Entry:** Provides functionality to delete saved entries from the password manager.


## Tech Stack

- Python
- tkinter (GUI library)
- cryptography (for password encryption)
- Random Module
- Pypercli (for copying passwords to clipboard)

## 3. Using the Application

### Generate Password

1. Open the Password Manager application.
2. Click on the **"Generate Password"** button.
3. A new, strong password will be generated and displayed in the password field.

### Copy Password

1. After generating or entering a password, click on the **"Copy Password"** button.
2. The password will be copied to the clipboard.
3. You can now paste the copied password into login forms or other secure locations.

### Save Entry

1. Enter the details of the website, email, and password in their respective fields.
2. Click on the **"Add"** button to save the entry.
3. The details will be saved securely in the `data.txt` file located in the project directory.

### Search Entry

1. Click on the **"Search Entry"** button.
2. A new window will appear.
3. Enter the website and email you want to search for and click **"Search"**.
4. The application will display matching entries from the `data.txt` file.

### Delete Entry

1. Click on the **"Delete Entry"** button.
2. A new window will appear.
3. Enter the website and email for the entry you want to delete and click **"Delete"**.
4. The application will remove the matching entry from the `data.txt` file.

### Quitting the Application

- Click on the **"Quit"** button to close the application.


