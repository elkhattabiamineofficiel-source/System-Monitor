import psutil
import platform
import datetime
import os
from tkinter import *
from tkinter import ttk

# === Fenster erstellen ===
root = Tk()
root.title("System Monitor")
root.geometry("500x400")
root.config(bg="#f4f4f4")

# === Systeminformationen ===
uname = platform.uname()
Label(root, text=f"System: {uname.system} {uname.release}", font=("Arial", 11), bg="#f4f4f4").pack(pady=5)
Label(root, text=f"Computername: {uname.node}", font=("Arial", 11), bg="#f4f4f4").pack(pady=2)
Label(root, text=f"CPU: {uname.processor}", font=("Arial", 11), bg="#f4f4f4").pack(pady=2)

# === CPU & RAM ===
cpu_label = Label(root, text="", font=("Arial", 12, "bold"), bg="#f4f4f4")
cpu_label.pack(pady=10)
ram_label = Label(root, text="", font=("Arial", 12, "bold"), bg="#f4f4f4")
ram_label.pack(pady=10)

# === Festplatte ===
disk_label = Label(root, text="", font=("Arial", 11), bg="#f4f4f4")
disk_label.pack(pady=5)

# === Netzwerk ===
net_label = Label(root, text="", font=("Arial", 11), bg="#f4f4f4")
net_label.pack(pady=5)

# === Funktion zur Aktualisierung der Werte ===
def update_info():
    # CPU-Auslastung
    cpu = psutil.cpu_percent(interval=1)
    cpu_label.config(text=f"CPU-Auslastung: {cpu}%")

    # RAM-Auslastung
    memory = psutil.virtual_memory()
    ram_label.config(text=f"RAM: {memory.percent}% verwendet ({round(memory.used / (1024 ** 3), 1)} GB von {round(memory.total / (1024 ** 3), 1)} GB)")

    # Festplattenspeicher
    disk = psutil.disk_usage('/')
    disk_label.config(text=f"Festplatte: {round(disk.used / (1024 ** 3), 1)} GB von {round(disk.total / (1024 ** 3), 1)} GB belegt ({disk.percent}%)")

    # Netzwerk
    net_io = psutil.net_io_counters()
    net_label.config(text=f"Gesendete Daten: {round(net_io.bytes_sent / (1024 ** 2), 2)} MB | Empfangene Daten: {round(net_io.bytes_recv / (1024 ** 2), 2)} MB")

    root.after(2000, update_info)  # alle 2 Sekunden aktualisieren

update_info()

# === App starten ===
root.mainloop()
