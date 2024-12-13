import tkinter as tk
from tkinter import messagebox
import numpy as np

def calculate_wp(criteria, weights, decision_matrix):
    # Menghitung nilai preferensi WP
    weighted_matrix = np.power(decision_matrix, weights)
    scores = weighted_matrix.prod(axis=1)
    return scores / scores.sum()  # Normalisasi skor

def wp_gui():
    root = tk.Tk()
    root.title("SPK - Weighted Product (WP)")
    root.geometry("500x600")

    tk.Label(root, text="SPK - Weighted Product (WP)", font=("Arial", 14)).pack(pady=10)

    tk.Label(root, text="Jumlah Alternatif:").pack(pady=5)
    alt_count_entry = tk.Entry(root)
    alt_count_entry.pack()

    tk.Label(root, text="Jumlah Kriteria:").pack(pady=5)
    crit_count_entry = tk.Entry(root)
    crit_count_entry.pack()

    def next_step():
        try:
            alt_count = int(alt_count_entry.get())
            crit_count = int(crit_count_entry.get())

            if alt_count <= 0 or crit_count <= 0:
                raise ValueError("Jumlah alternatif dan kriteria harus lebih dari 0.")

            inputs_window = tk.Toplevel()
            inputs_window.title("Input WP")
            inputs_window.geometry("600x600")

            tk.Label(inputs_window, text="Nama Alternatif:").pack(pady=5)
            alt_entries = [tk.Entry(inputs_window) for _ in range(alt_count)]
            for entry in alt_entries:
                entry.pack()

            tk.Label(inputs_window, text="Bobot Kriteria (total 1):").pack(pady=5)
            weight_entries = [tk.Entry(inputs_window) for _ in range(crit_count)]
            for entry in weight_entries:
                entry.pack()

            tk.Label(inputs_window, text="Matriks Keputusan:").pack(pady=5)
            matrix_entries = []
            for i in range(alt_count):
                row_entries = []
                for j in range(crit_count):
                    entry = tk.Entry(inputs_window, width=10)
                    entry.pack(side=tk.LEFT, padx=5, pady=5)
                    row_entries.append(entry)
                matrix_entries.append(row_entries)
                tk.Label(inputs_window, text="").pack()

            def calculate():
                try:
                    alternatives = [entry.get() for entry in alt_entries]
                    weights = np.array([float(entry.get()) for entry in weight_entries])
                    decision_matrix = np.array([
                        [float(entry.get()) for entry in row]
                        for row in matrix_entries
                    ])

                    scores = calculate_wp(None, weights, decision_matrix)

                    results_window = tk.Toplevel()
                    results_window.title("Hasil WP")
                    results_window.geometry("400x300")
                    tk.Label(results_window, text="Skor Alternatif", font=("Arial", 14)).pack(pady=10)
                    for alt, score in zip(alternatives, scores):
                        tk.Label(results_window, text=f"{alt}: {score:.4f}").pack()

                except Exception as e:
                    messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

            tk.Button(inputs_window, text="Hitung WP", command=calculate).pack(pady=20)

        except ValueError as e:
            messagebox.showerror("Error", f"Input tidak valid: {e}")

    tk.Button(root, text="Lanjutkan", command=next_step).pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    wp_gui()
