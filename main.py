import tkinter as tk
from tkinter import messagebox
import os
from dotenv import find_dotenv, load_dotenv
from controller import HomeStatus

load_dotenv(find_dotenv())

API_KEY = os.environ["API_KEY"]

homestatus = HomeStatus(API_KEY)

def get_sensor_temperature():
    status = homestatus.get()
    temp_set = status["temp"]

    return temp_set

def set_temperature():
    if not temperature_entry.get():
        messagebox.showinfo("Błąd", "Podaj temperature")

    else:
        temperature = temperature_entry.get()

        if int(temperature) > 30:
            messagebox.showinfo("Błąd", "Ustawiona temperatura nie może przekraczać 30 stopni C")
        elif int(temperature) < 18:
            messagebox.showinfo("Błąd", "Ustawiona temperatura nie może być mniejsza niż 18 stopni C")
        else:
            homestatus.update_temp_setting(temperature)
            current_temperature_label.config(text=f"Ustawiona temperatura: {temperature}°C")

def update_sensor_temperature():
    sensor_temperature = get_sensor_temperature()
    sensor_temperature_label.config(text=f"Temperatura sensora: {sensor_temperature}°C")
    root.after(5000, update_sensor_temperature)

def toggle_light():
    if light_state.get() == 0:
        light_button.config(text="Włącz światło")
    else:
        light_button.config(text="Wyłącz światło")
    light_state.set(1 - light_state.get())
    homestatus.update_light(1 - light_state.get())

root = tk.Tk()
root.title("Kontroler systemy Smart Home")
root.geometry("400x300")

#temperatura
temperature_label = tk.Label(root, text="Ustaw temperature (°C):", font=("Helvetica", 14))
temperature_label.pack()
temperature_entry = tk.Entry(root, font=("Helvetica", 14))
temperature_entry.pack()
set_temperature_button = tk.Button(root, text="Ustaw", command=set_temperature, font=("Helvetica", 12))
set_temperature_button.pack()
current_temperature_label = tk.Label(root, text="Ustaw temperature: --°C", font=("Helvetica", 14))
current_temperature_label.pack()

#sensor
sensor_temperature_label = tk.Label(root, text="Temperatura sensora: --°C", font=("Helvetica", 14))
sensor_temperature_label.pack()
update_sensor_temperature()

#światło
light_state = tk.IntVar()
light_button = tk.Button(root, text="Włącz światło", command=toggle_light, font=("Helvetica", 12))
light_button.pack()

root.mainloop()