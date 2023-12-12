import os
import shutil
import customtkinter 
from customtkinter import CTkCanvas
from tkinter import filedialog
from datetime import datetime
from PIL import Image, ImageTk

def home_view(content_frame, clear_frame, user_email):
    def home_button_event():
        select_frame_by_name("home")

    def acc_button_event():
        select_frame_by_name("acc")

    def select_frame_by_name(name):
        home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        acc_button.configure(fg_color=("gray75", "gray25") if name == "acc" else "transparent")

        if name == "home":
            home_frame.grid(row=0, column=1, sticky="nsew")
            acc_frame.grid_forget()
        elif name == "acc":
            acc_frame.grid(row=0, column=1, sticky="nsew")
            home_frame.grid_forget()

    clear_frame(content_frame)

    content_frame.grid_rowconfigure(0, weight=1)
    content_frame.grid_columnconfigure(1, weight=1)

    navigation_frame = customtkinter.CTkFrame(content_frame, corner_radius=0)
    navigation_frame.grid(row=0, column=0, sticky="nsew")
    navigation_frame.grid_rowconfigure(4, weight=1)

    navigation_frame_label = customtkinter.CTkLabel(navigation_frame, text="Food Recognition",
                                                    compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
    navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

    # Load images :
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icons")
    home_image = customtkinter.CTkImage(
        dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))

    home_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                        text="Home", fg_color="transparent", text_color=("gray10", "gray90"),
                                        hover_color=("gray70", "gray30"), image=home_image, anchor="w",
                                        command=home_button_event)
    home_button.grid(row=1, column=0, sticky="ew")

    acc_button = customtkinter.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                        text="My Account",fg_color="transparent", text_color=("gray10", "gray90"),
                                        hover_color=("gray70", "gray30"),image=home_image, anchor="w",
                                        command=acc_button_event)
    acc_button.grid(row=2, column=0, sticky="ew")

    #  Frames
    home_frame = customtkinter.CTkFrame(content_frame, corner_radius=0, fg_color="transparent")
    home_frame.grid_columnconfigure(0, weight=1)

    acc_frame = customtkinter.CTkFrame(content_frame, corner_radius=0, fg_color="transparent")
    acc_frame.grid_columnconfigure(0, weight=1)


    #  Home Frame
    def predict_action():
        pass

    def cancel_action():
        uploaded_image_canvas.grid_forget()
        predict_button.grid_forget()
        cancel_button.grid_forget()
        
        
    uploaded_image_canvas = CTkCanvas(master=home_frame)
    uploaded_file_info = None 

    predict_button = customtkinter.CTkButton(home_frame, text="Predict", height=50, width=100, command=predict_action)
    predict_button.grid(row=3, column=0, pady=(10, 0), padx=(200, 0))
    predict_button.grid_forget()

    cancel_button = customtkinter.CTkButton(home_frame, text="Cancel", height=50, width=100, command=cancel_action)
    cancel_button.grid(row=3, column=1, pady=(10, 0), padx=(0, 200))
    cancel_button.grid_forget()

    def upload_file():
        global uploaded_file_info

        file_path = filedialog.askopenfilename()

        if file_path:
            file_name = os.path.basename(file_path)
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            unique_file_name = f"{timestamp}_{file_name}"

            uploaded_file_info = {
                'file_path': file_path,
                'file_name': file_name,
                'unique_file_name': unique_file_name
            }

            upload_button_text = file_name
            upload_button.configure(text=upload_button_text)

        
    def submit_file():
        global uploaded_file_info, tk_image  
        
        if uploaded_file_info:
            images_folder = "images"
            if not os.path.exists(images_folder):
                os.makedirs(images_folder)

            destination_path = os.path.join(images_folder, uploaded_file_info['unique_file_name'])
            shutil.copyfile(uploaded_file_info['file_path'], destination_path)

            img = Image.open(destination_path)
            resized_img = img.resize((500, 400), Image.LANCZOS)  # Use the correct resampling filter
            tk_image = ImageTk.PhotoImage(resized_img)

            uploaded_image_canvas.configure(width=resized_img.width, height=resized_img.height)
            uploaded_image_canvas.create_image(0, 0, image=tk_image, anchor="nw")
            uploaded_image_canvas.grid(row=2, column=0, pady=10, padx=(240, 0))

            upload_button.configure(text="Upload File")
            predict_button.grid(row=4, column=0, pady=(10, 0), padx=(200, 0))
            cancel_button.grid(row=4, column=1, pady=(10, 0), padx=(0, 200))


    upload_button = customtkinter.CTkButton(home_frame, text="Upload File", height=50, width=300, 
                                            command=upload_file)
    upload_button.grid(row=1, column=0, pady=30, padx=(140, 0))  

    submit_button = customtkinter.CTkButton(home_frame, text="Submit", height=50, width=100, 
                                            command=submit_file)
    submit_button.grid(row=1, column=1, pady=0, padx=(10,140))

    # email_label = customtkinter.CTkLabel(home_frame, text=f"Logged in as: {user_email}")
    # email_label.grid(row=5, column=0, pady=10, padx=10)


    select_frame_by_name("home")
