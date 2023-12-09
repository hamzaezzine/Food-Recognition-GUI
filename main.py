import customtkinter
from login import login_view

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

rt = customtkinter.CTk()
rt.geometry("900x450")

content_frame = customtkinter.CTkFrame(rt)
content_frame.pack(fill='both', expand=True)

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

login_view(content_frame, clear_frame)

rt.mainloop()
