import tkinter as tk
import methods.spk_saw as spk_saw
import methods.spk_ahp as spk_ahp
import methods.spk_wp as spk_wp
import methods.spk_profile_matching as spk_pm

def main_menu():
    root = tk.Tk()
    root.title("Sistem Pendukung Keputusan (SPK)")
    root.geometry("400x300")

    tk.Label(root, text="Sistem Pendukung Keputusan (SPK)", font=("Arial", 16)).pack(pady=20)

    tk.Button(root, text="Metode SAW", width=20, command=spk_saw.saw_gui).pack(pady=10)
    tk.Button(root, text="Metode AHP", width=20, command=spk_ahp.ahp_gui).pack(pady=10)
    tk.Button(root, text="Metode WP", width=20, command=spk_wp.wp_gui).pack(pady=10)
    tk.Button(root, text="Metode Profile Matching", width=20, command=spk_pm.pm_gui).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_menu()
