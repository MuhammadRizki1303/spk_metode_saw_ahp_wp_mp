import tkinter as tk
from tkinter import messagebox
import numpy as np

def calculate_saw(criteria, weights, decision_matrix):
    # Normalisasi matriks
    normalized_matrix = decision_matrix / decision_matrix.sum(axis=0)

    # Mengalikan dengan bobot
    weighted_matrix = normalized_matrix * weights

    # Menghitung skor total
    scores = weighted_matrix.sum(axis=1)

    return scores

def show_results(alternatives, scores):
    # Menampilkan hasil
    results_window = tk.Toplevel()
    results_window.title("Hasil SPK - SAW")
    results_window.geometry("400x300")

    tk.Label(results_window, text="Hasil Perhitungan SAW", font=("Arial", 14)).pack(pady=10)
    for i, (alt, score) in enumerate(zip(alternatives, scores)):
        tk.Label(results_window, text=f"{alt}: {score:.4f}").pack()

    best_alt = alternatives[np.argmax(scores)]
    tk.Label(results_window, text=f"Alternatif Terbaik: {best_alt}", font=("Arial", 12, "bold")).pack(pady=10)

def saw_gui():
    # Membuat jendela utama
    root = tk.Tk()
    root.title("SPK - Simple Additive Weighting (SAW)")
    root.geometry("500x600")

    tk.Label(root, text="SPK - Simple Additive Weighting (SAW)", font=("Arial", 14)).pack(pady=10)

    # Input jumlah alternatif dan kriteria
    tk.Label(root, text="Jumlah Alternatif:").pack(pady=5)
    alt_count_entry = tk.Entry(root)
    alt_count_entry.pack()

    tk.Label(root, text="Jumlah Kriteria:").pack(pady=5)
    crit_count_entry = tk.Entry(root)
    crit_count_entry.pack()

    def next_step():
        try:
            # Mendapatkan jumlah alternatif dan kriteria
            alt_count = int(alt_count_entry.get())
            crit_count = int(crit_count_entry.get())

            if alt_count <= 0 or crit_count <= 0:
                raise ValueError("Jumlah alternatif dan kriteria harus lebih dari 0.")

            # Masukkan nama alternatif dan kriteria
            inputs_window = tk.Toplevel()
            inputs_window.title("Input Alternatif dan Kriteria")
            inputs_window.geometry("600x600")

            tk.Label(inputs_window, text="Nama Alternatif:").pack(pady=5)
            alt_entries = []
            for i in range(alt_count):
                entry = tk.Entry(inputs_window)
                entry.pack()
                alt_entries.append(entry)

            tk.Label(inputs_window, text="Nama Kriteria:").pack(pady=5)
            crit_entries = []
            for i in range(crit_count):
                entry = tk.Entry(inputs_window)
                entry.pack()
                crit_entries.append(entry)

            tk.Label(inputs_window, text="Bobot Kriteria (dalam %, total harus 100%):").pack(pady=5)
            weight_entries = []
            for i in range(crit_count):
                entry = tk.Entry(inputs_window)
                entry.pack()
                weight_entries.append(entry)

            tk.Label(inputs_window, text="Matriks Keputusan:").pack(pady=5)
            matrix_entries = []
            for i in range(alt_count):
                row_entries = []
                for j in range(crit_count):
                    entry = tk.Entry(inputs_window, width=10)
                    entry.pack(side=tk.LEFT, padx=5, pady=5)
                    row_entries.append(entry)
                matrix_entries.append(row_entries)
                tk.Label(inputs_window, text="").pack()  # Pindah ke baris berikutnya

            def calculate():
                try:
                    # Ambil nama alternatif dan kriteria
                    alternatives = [entry.get().strip() for entry in alt_entries]
                    criteria = [entry.get().strip() for entry in crit_entries]
                    weights = np.array([float(entry.get().strip()) for entry in weight_entries]) / 100

                    # Validasi apakah bobot total 100%
                    if not np.isclose(weights.sum(), 1.0):
                        raise ValueError("Total bobot kriteria harus 100%.")

                    # Ambil matriks keputusan
                    decision_matrix = np.array([
                        [float(entry.get().strip()) for entry in row]
                        for row in matrix_entries
                    ])

                    # Pastikan tidak ada input kosong
                    if any(entry.get().strip() == '' for row in matrix_entries for entry in row):
                        raise ValueError("Semua kolom matriks keputusan harus diisi.")

                    # Lakukan perhitungan SAW
                    scores = calculate_saw(criteria, weights, decision_matrix)

                    # Tampilkan hasil
                    show_results(alternatives, scores)

                except ValueError as e:
                    messagebox.showerror("Error", f"Terjadi kesalahan: {e}")
                except Exception as e:
                    messagebox.showerror("Error", f"Terjadi kesalahan yang tidak terduga: {e}")

            tk.Button(inputs_window, text="Hitung SAW", command=calculate).pack(pady=20)

        except ValueError as e:
            messagebox.showerror("Error", f"Input tidak valid: {e}")

    tk.Button(root, text="Lanjutkan", command=next_step).pack(pady=20)
    root.mainloop()

if __name__ == "__main__":
    saw_gui()