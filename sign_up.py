import customtkinter

def reg():
    print("Registered")

def signup_view(content_frame, clear_frame):
    from login import login_view
    clear_frame(content_frame)

    label_signup = customtkinter.CTkLabel(master=content_frame, width=120, height=32, text="Sign up", font=("Roboto", 24))
    label_signup.pack(pady=12, padx=10)

    firstname_signup = customtkinter.CTkEntry(master=content_frame, width=290, height=32, placeholder_text="First name")
    firstname_signup.pack(pady=12, padx=10)

    lastname_signup = customtkinter.CTkEntry(master=content_frame, width=290, height=32, placeholder_text="Last name")
    lastname_signup.pack(pady=12, padx=10)

    email_signup = customtkinter.CTkEntry(master=content_frame, width=290, height=32, placeholder_text="Email")
    email_signup.pack(pady=12, padx=10)

    oass_signup = customtkinter.CTkEntry(master=content_frame, width=290, height=32, placeholder_text="Password", show="*")
    oass_signup.pack(pady=12, padx=10)
    
    repeat_pass_login = customtkinter.CTkEntry(master=content_frame, width=290, height=32, placeholder_text="Repeat Password", show="*")
    repeat_pass_login.pack(pady=12, padx=10)

    button_signup = customtkinter.CTkButton(master=content_frame, width=290, height=32, text="Sign up", command=reg)
    button_signup.pack(pady=12, padx=10)

    login_label = customtkinter.CTkLabel(master=content_frame, text="Already a user? Login", cursor="hand2")
    login_label.bind("<Button-1>", lambda _: login_view(content_frame, clear_frame))
    login_label.pack(pady=12, padx=10)
