import tkinter as tk
from tkinter import messagebox
import numpy as np

# Fungsi menghitung nilai preferensi Weighted Product
def calculate_wp(weights, decision_matrix):
    # Menghitung matriks yang telah diberi bobot
    weighted_matrix = np.power(decision_matrix, weights)
    scores = weighted_matrix.prod(axis=1)  # Menghitung produk dari setiap baris
    return scores / scores.sum()  # Normalisasi skor agar totalnya 1

# Fungsi utama GUI
def wp_gui():
    root = tk.Tk()
    root.title("SPK - Weighted Product (WP)")
    root.geometry("600x500")

    # Judul Aplikasi
    tk.Label(root, text="SPK - Weighted Product (WP)", font=("Arial", 16, "bold")).pack(pady=10)

    # Input jumlah alternatif dan kriteria
    tk.Label(root, text="Jumlah Alternatif:", font=("Arial", 12)).pack(pady=5)
    alt_count_entry = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
    alt_count_entry.pack()

    tk.Label(root, text="Jumlah Kriteria:", font=("Arial", 12)).pack(pady=5)
    crit_count_entry = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
    crit_count_entry.pack()

    # Fungsi untuk lanjut ke input data
    def next_step():
        try:
            alt_count = int(alt_count_entry.get())
            crit_count = int(crit_count_entry.get())

            if alt_count <= 0 or crit_count <= 0:
                raise ValueError("Jumlah alternatif dan kriteria harus lebih dari 0.")

            # Window untuk input data
            inputs_window = tk.Toplevel()
            inputs_window.title("Input Data Weighted Product")
            inputs_window.geometry("700x700")

            # Input Nama Alternatif
            tk.Label(inputs_window, text="Nama Alternatif:", font=("Arial", 12)).pack(pady=5)
            alt_entries = [tk.Entry(inputs_window, font=("Arial", 10), width=20) for _ in range(alt_count)]
            for entry in alt_entries:
                entry.pack()

            # Input Bobot Kriteria
            tk.Label(inputs_window, text="Bobot Kriteria (Total = 1):", font=("Arial", 12)).pack(pady=5)
            weight_entries = [tk.Entry(inputs_window, font=("Arial", 10), width=10) for _ in range(crit_count)]
            for entry in weight_entries:
                entry.pack()

            # Input Matriks Keputusan
            tk.Label(inputs_window, text="Matriks Keputusan:", font=("Arial", 12)).pack(pady=5)
            matrix_frame = tk.Frame(inputs_window)
            matrix_frame.pack()

            matrix_entries = []
            for i in range(alt_count):
                row_entries = []
                for j in range(crit_count):
                    entry = tk.Entry(matrix_frame, width=10, font=("Arial", 10), justify="center")
                    entry.grid(row=i, column=j, padx=5, pady=5)
                    row_entries.append(entry)
                matrix_entries.append(row_entries)

            # Fungsi untuk menghitung Weighted Product
            def calculate():
                try:
                    alternatives = [entry.get() for entry in alt_entries]
                    weights = np.array([float(entry.get()) for entry in weight_entries])

                    # Validasi total bobot
                    if not np.isclose(weights.sum(), 1.0):
                        raise ValueError("Total bobot harus sama dengan 1.")

                    decision_matrix = np.array([
                        [float(entry.get()) for entry in row]
                        for row in matrix_entries
                    ])

                    # Hitung nilai WP
                    scores = calculate_wp(weights, decision_matrix)

                    # Tampilkan hasil
                    results_window = tk.Toplevel()
                    results_window.title("Hasil Weighted Product")
                    results_window.geometry("500x400")

                    tk.Label(results_window, text="Skor Alternatif", font=("Arial", 14, "bold")).pack(pady=10)
                    for alt, score in zip(alternatives, scores):
                        tk.Label(results_window, text=f"{alt}: {score:.4f}", font=("Arial", 12)).pack(pady=2)

                    # Alternatif terbaik
                    best_index = np.argmax(scores)
                    tk.Label(results_window, text=f"Alternatif Terbaik: {alternatives[best_index]}",
                             font=("Arial", 12, "bold"), fg="green").pack(pady=10)

                except ValueError as e:
                    messagebox.showerror("Error", f"Input tidak valid: {e}")
                except Exception as e:
                    messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

            # Tombol untuk menghitung
            tk.Button(inputs_window, text="Hitung WP", font=("Arial", 12, "bold"), command=calculate).pack(pady=20)

        except ValueError as e:
            messagebox.showerror("Error", f"Input tidak valid: {e}")

    # Tombol Lanjutkan
    tk.Button(root, text="Lanjutkan", font=("Arial", 12, "bold"), command=next_step).pack(pady=20)

    root.mainloop()

# Jalankan aplikasi
if __name__ == "__main__":
    wp_gui()
