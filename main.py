import json
from tkinter import *
from tkinter import messagebox


def search():
    website_output = website_input.get()
    try:
        with open("passwords.json", "r") as data_file:
            data = json.load(data_file)
    except:
        messagebox.showwarning(message="No data in password list. Add a record")
    else:
        if website_output in data:
            email = data[website_output]['email']
            password = data[website_output]['password']
            messagebox.showinfo(title=website_output, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showwarning(message="There is no such website in the list")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    from random import shuffle, randint, choice
    import pyperclip
    password_input.delete(0, "end")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    website_output = website_input.get()
    password_output = password_input.get()
    email_output = email_input.get()
    new_data = {
        website_output: {
            "email": email_output,
            "password": password_output
        }
    }

    if len(password_output) < 1 or len(website_output) < 1 or len(email_output) < 1:
        messagebox.showwarning(message="Please, fill in all the fields")
    else:
        is_ok = messagebox.askokcancel(title=website_output, message=f"Email: {email_output}\nPassword: {password_output}")
        if is_ok:
            try:
                with open('passwords.json', 'r') as data_file_2:
                    # Loading the JSON file
                    json_data = json.load(data_file_2)
            except:
                with open('passwords.json', 'w') as data_file_4:
                    # Adding the updated data
                    json.dump(new_data, data_file_4, indent=4)
            else:
                json_data.update(new_data)
                with open('passwords.json', 'w') as data_file_3:
                    # Adding the updated data
                    json.dump(json_data, data_file_3, indent=4)
            finally:
                website_input.delete(0, "end")
                password_input.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_input = Entry()
website_input.grid(column=1, row=1)
website_input.focus()
email_input = Entry()
email_input.grid(column=1, row=2)
email_input.insert(0, "Email@email.com")
password_input = Entry()
password_input.grid(column=1, row=3)

# Buttons
search_btn = Button(text="Search", command=search, width=8)
search_btn.grid(column=2, row=1)
gen_password = Button(text="Generate", command=generate, width=8)
gen_password.grid(column=2, row=3)
add_button = Button(text="Add", width=25, command=add)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

