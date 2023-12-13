import customtkinter
from CTkMessagebox import CTkMessagebox
import re
import hashlib

firstname_signup = None
lastname_signup = None
email_signup = None
pass_signup = None
repeat_pass_signup = None

def Clear():
    firstname_signup.delete(0, 'end')
    lastname_signup.delete(0, 'end')
    email_signup.delete(0, 'end')
    pass_signup.delete(0, 'end')
    repeat_pass_signup.delete(0, 'end')

def reg(db):
    firstname_value = firstname_signup.get()
    lastname_value = lastname_signup.get()
    email_value = email_signup.get()
    pass_value = pass_signup.get()
    repeat_pass_value = repeat_pass_signup.get()
    
    if not firstname_value or not lastname_value or not email_value or not pass_value or not repeat_pass_value:
        CTkMessagebox(title="Error", message="Please fill in all fields", icon="cancel")
        return
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email_value):
        CTkMessagebox(title="Error", message="Invalid email format", icon="cancel")
        return
    
    if len(pass_value) < 6:
        CTkMessagebox(title="Error", message="Password must be at least 6 characters long", icon="cancel")
        return
    
    if pass_value != repeat_pass_value:
        CTkMessagebox(title="Error", message="Passwords do not match", icon="cancel")
        return
    
    existing_user = db.get_user(email_value)
    if existing_user:
        CTkMessagebox(title="Error", message="Email is already registered", icon="cancel")
        return
    else:
        db.insert(firstname_value, lastname_value, email_value, hashlib.md5(pass_value.encode()).hexdigest())
        CTkMessagebox(title="check", message="User successfully registered!", icon="check")
        Clear()


def signup_view(content_frame, clear_frame, db):
    from login import login_view
    clear_frame(content_frame)
    
    global firstname_signup, lastname_signup, email_signup, pass_signup, repeat_pass_signup

    label_signup = customtkinter.CTkLabel(master=content_frame, width=120, height=32, text="Sign up", font=("Roboto", 24))
    label_signup.pack(pady=12, padx=10)

    firstname_signup = customtkinter.CTkEntry(master=content_frame, width=290, height=32, placeholder_text="First name")
    firstname_signup.pack(pady=12, padx=10)

    lastname_signup = customtkinter.CTkEntry(master=content_frame, width=290, height=32, placeholder_text="Last name")
    lastname_signup.pack(pady=12, padx=10)

    email_signup = customtkinter.CTkEntry(master=content_frame, width=290, height=32, placeholder_text="Email")
    email_signup.pack(pady=12, padx=10)

    pass_signup = customtkinter.CTkEntry(master=content_frame, width=290, height=32, placeholder_text="Password", show="*")
    pass_signup.pack(pady=12, padx=10)
    
    repeat_pass_signup = customtkinter.CTkEntry(master=content_frame, width=290, height=32, placeholder_text="Repeat Password", show="*")
    repeat_pass_signup.pack(pady=12, padx=10)

    button_signup = customtkinter.CTkButton(master=content_frame, width=290, height=32, text="Sign up", command=lambda: reg(db))
    button_signup.pack(pady=12, padx=10)

    login_label = customtkinter.CTkLabel(master=content_frame, text="Already a user? Login", cursor="hand2")
    login_label.bind("<Button-1>", lambda _: login_view(content_frame, clear_frame, db))
    login_label.pack(pady=12, padx=10)
