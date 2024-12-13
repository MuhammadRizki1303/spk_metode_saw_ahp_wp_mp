import tkinter as tk
from tkinter import messagebox
import numpy as np

def calculate_ahp(pairwise_matrix, criteria_weights):
    # Normalisasi matriks perbandingan berpasangan
    normalized_matrix = pairwise_matrix / pairwise_matrix.sum(axis=0)
    priority_vector = normalized_matrix.mean(axis=1)
    return priority_vector

def ahp_gui():
    root = tk.Tk()
    root.title("SPK - Analytic Hierarchy Process (AHP)")
    root.geometry("600x600")

    tk.Label(root, text="SPK - Analytic Hierarchy Process (AHP)", font=("Arial", 14)).pack(pady=10)

    tk.Label(root, text="Jumlah Kriteria:").pack(pady=5)
    crit_count_entry = tk.Entry(root)
    crit_count_entry.pack()

    def next_step():
        try:
            crit_count = int(crit_count_entry.get())
            if crit_count <= 0:
                raise ValueError("Jumlah kriteria harus lebih dari 0.")

            inputs_window = tk.Toplevel()
            inputs_window.title("Input Matriks Perbandingan Berpasangan")
            inputs_window.geometry("600x600")

            tk.Label(inputs_window, text="Masukkan Matriks Perbandingan Berpasangan:").pack(pady=5)

            matrix_entries = []
            for i in range(crit_count):
                row_entries = []
                for j in range(crit_count):
                    entry = tk.Entry(inputs_window, width=10)
                    entry.pack(side=tk.LEFT, padx=5, pady=5)
                    row_entries.append(entry)
                matrix_entries.append(row_entries)
                tk.Label(inputs_window, text="").pack()  # Pindah ke baris berikutnya

            def calculate():
                try:
                    # Ambil matriks perbandingan berpasangan
                    pairwise_matrix = np.array([
                        [float(entry.get()) for entry in row]
                        for row in matrix_entries
                    ])

                    # Validasi matriks
                    if pairwise_matrix.shape[0] != pairwise_matrix.shape[1]:
                        raise ValueError("Matriks harus berbentuk persegi.")

                    # Lakukan perhitungan AHP
                    priority_vector = calculate_ahp(pairwise_matrix, None)

                    # Tampilkan hasil
                    results_window = tk.Toplevel()
                    results_window.title("Hasil AHP")
                    results_window.geometry("400x300")
                    tk.Label(results_window, text="Prioritas Kriteria", font=("Arial", 14)).pack(pady=10)
                    for i, val in enumerate(priority_vector):
                        tk.Label(results_window, text=f"Kriteria {i+1}: {val:.4f}").pack()

                except Exception as e:
                    messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

            tk.Button(inputs_window, text="Hitung AHP", command=calculate).pack(pady=20)

        except ValueError as e:
            messagebox.showerror("Error", f"Input tidak valid: {e}")

    tk.Button(root, text="Lanjutkan", command=next_step).pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    ahp_gui()
