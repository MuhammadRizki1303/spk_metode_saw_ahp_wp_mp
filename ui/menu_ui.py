import tkinter as tk
from tkinter import messagebox
import os

def open_saw():
    os.system("python methods/spk_saw.py")

def open_ahp():
    os.system("python methods/spk_ahp.py")

def open_wp():
    os.system("python methods/spk_wp.py")

def open_profile_matching():
    os.system("python methods/spk_profile_matching.py")

# Membuat GUI untuk Menu SPK
def main_menu():
    root = tk.Tk()
    root.title("Sistem Pengambilan Keputusan")
    root.geometry("400x300")

    label_title = tk.Label(root, text="Pilih Metode Pengambilan Keputusan", font=("Arial", 14))
    label_title.pack(pady=20)

    # Tombol Metode
    btn_saw = tk.Button(root, text="Simple Additive Weighting (SAW)", width=30, command=open_saw)
    btn_saw.pack(pady=5)

    btn_ahp = tk.Button(root, text="Analytic Hierarchy Process (AHP)", width=30, command=open_ahp)
    btn_ahp.pack(pady=5)

    btn_wp = tk.Button(root, text="Weighted Product (WP)", width=30, command=open_wp)
    btn_wp.pack(pady=5)

    btn_pm = tk.Button(root, text="Profile Matching", width=30, command=open_profile_matching)
    btn_pm.pack(pady=5)

    # Menutup aplikasi
    btn_exit = tk.Button(root, text="Keluar", width=30, command=root.quit)
    btn_exit.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main_menu()
