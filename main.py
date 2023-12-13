import customtkinter
from login import login_view
from home import home_view
from database import Database

direction_db = "users.db"  
db = Database(direction_db)

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

rt = customtkinter.CTk()
rt.geometry("1000x550")
rt.title("Food Recognition")

content_frame = customtkinter.CTkFrame(rt)
content_frame.pack(fill='both', expand=True)

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

login_view(content_frame, clear_frame, db)

rt.mainloop()
