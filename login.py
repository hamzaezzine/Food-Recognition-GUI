from CTkMessagebox import CTkMessagebox
import customtkinter
import re 
from database import Database

direction_db = "users.db"  
db = Database(direction_db)

email_login = None
pass_login = None

def login():
    email_value = email_login.get()
    password_value = pass_login.get()
        
    if not email_value or not password_value:
        CTkMessagebox(title="Error", message="Please enter both email and password", icon="cancel")
        return
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email_value):
        CTkMessagebox(title="Error", message="Invalid email format", icon="cancel")
        return

    if len(password_value) < 6:
        CTkMessagebox(title="Error", message="Password must be at least 6 characters long", icon="cancel")
        return
    
    user = db.get_user(email_value)

    if user and user[0][4] == password_value: 
        CTkMessagebox(title="Success", message="Login successful!", icon="info")
        print(f"Email: {email_value}\nPassword: {password_value}")

        email_login.delete(0, 'end')
        pass_login.delete(0, 'end')
    else:
        CTkMessagebox(title="Error", message="Invalid email or password", icon="cancel")


def login_view(content_frame, clear_frame):
    from sign_up import signup_view
    clear_frame(content_frame)

    global email_login, pass_login  
    
    label_login = customtkinter.CTkLabel(master=content_frame, width=120, height=32, text="Login", font=("Roboto", 24))
    label_login.pack(pady=30, padx=10)
    
    email_login = customtkinter.CTkEntry(master=content_frame, width=290, height=32, placeholder_text="Email")
    email_login.pack(pady=12, padx=10)

    pass_login = customtkinter.CTkEntry(master=content_frame, width=290, height=32, placeholder_text="Password", show="*")
    pass_login.pack(pady=12, padx=10)

    button_login = customtkinter.CTkButton(master=content_frame, width=290, height=32, text="Login", command=login)
    button_login.pack(pady=12, padx=10)

    register_label = customtkinter.CTkLabel(master=content_frame, text="Not a member? Sign up", cursor="hand2")
    register_label.bind("<Button-1>", lambda _: signup_view(content_frame, clear_frame))
    register_label.pack(pady=14, padx=10)
