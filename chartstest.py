import customtkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import json
import requests


def charts(predicted):
    # food_data = {
    #     "items": [
    #         {
    #             "name": "carrot",
    #             "calories": 34.0,
    #             "serving_size_g": 100.0,
    #             "fat_total_g": 0.2,
    #             "fat_saturated_g": 0.0,
    #             "protein_g": 0.8,
    #             "sodium_mg": 57,
    #             "potassium_mg": 30,
    #             "cholesterol_mg": 0,
    #             "carbohydrates_total_g": 8.3,
    #             "fiber_g": 3.0,
    #             "sugar_g": 3.4,
    #         }
    #     ]
    # }

    api_url = "https://api.calorieninjas.com/v1/nutrition?query="
    query = f"100g {predicted}"
    response = requests.get(
        api_url + query, headers={"X-Api-Key": "your calorieninjas api here"}
    )
    if response.status_code == requests.codes.ok:
        print(response.text)
        food_data = json.loads(response.text)
    else:
        print("Error:", response.status_code, response.text)
    dark_bg = "#1E1E1E"
    dark_text = "#CCCCCC"
    tk.set_appearance_mode("dark")
    window = tk.CTk()
    window.title("Nutrition Data")
    
    window.configure(bg=dark_bg)
    header_frame = tk.CTkFrame(window, bg_color=dark_bg)
    header_frame.pack(expand=False, fill=tk.BOTH)

    food_name_label = tk.CTkLabel(
        header_frame,
        text=food_data["items"][0]["name"],
        font=("Helvetica", 38),
        bg_color=dark_bg,
        fg_color=dark_bg,
    )
    food_name_label.pack(pady=20, padx=0)

    frame = tk.CTkFrame(window, bg_color=dark_bg)
    frame.pack(expand=True, fill=tk.BOTH)

    # Create Pie Chart
    fig_pie = Figure(figsize=(5, 5), dpi=100, facecolor=dark_bg)
    ax_pie = fig_pie.add_subplot(111)
    wedges, texts, autotexts = ax_pie.pie(
        [
            food_data["items"][0]["fat_total_g"],
            food_data["items"][0]["protein_g"],
            food_data["items"][0]["carbohydrates_total_g"],
        ],
        labels=["Fat", "Protein", "Carbohydrates"],
        autopct="%1.1f%%",
        startangle=90,
    )
    for text in texts:
        text.set_color(dark_text)
    ax_pie.set_title("Nutrient Distribution", color=dark_text)

    # Create Radar Chart
    fig_radar = Figure(figsize=(5, 5), dpi=100, facecolor=dark_bg)
    ax_radar = fig_radar.add_subplot(111, polar=True)
    categories = list(food_data["items"][0].keys())[3:]
    values = [food_data["items"][0][category] for category in categories]
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]
    ax_radar.fill(angles, values, color="b", alpha=0.25)
    ax_radar.set_yticklabels([])
    ax_radar.set_xticks(angles[:-1])
    ax_radar.set_xticklabels(categories, color=dark_text)
    ax_radar.set_title("Nutrient Values", color=dark_text)

    canvas_pie = FigureCanvasTkAgg(fig_pie, master=frame)
    canvas_pie.draw()
    canvas_pie.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    canvas_radar = FigureCanvasTkAgg(fig_radar, master=frame)
    canvas_radar.draw()
    canvas_radar.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    window.mainloop()
