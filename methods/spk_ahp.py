import tkinter as tk
from tkinter import messagebox
import numpy as np

# Fungsi perhitungan AHP
def calculate_ahp(pairwise_matrix):
    # Normalisasi matriks perbandingan berpasangan
    normalized_matrix = pairwise_matrix / pairwise_matrix.sum(axis=0)
    priority_vector = normalized_matrix.mean(axis=1)
    return priority_vector

# Fungsi utama GUI AHP
def ahp_gui():
    root = tk.Tk()
    root.title("SPK - Analytic Hierarchy Process (AHP)")
    root.geometry("600x400")

    # Judul
    tk.Label(root, text="SPK - Analytic Hierarchy Process (AHP)", font=("Arial", 16, "bold")).pack(pady=10)

    # Input jumlah kriteria
    tk.Label(root, text="Masukkan Jumlah Kriteria:", font=("Arial", 12)).pack(pady=5)
    crit_count_entry = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
    crit_count_entry.pack()

    def next_step():
        try:
            crit_count = int(crit_count_entry.get())
            if crit_count <= 0:
                raise ValueError("Jumlah kriteria harus lebih dari 0.")

            # Window untuk input matriks perbandingan berpasangan
            inputs_window = tk.Toplevel()
            inputs_window.title("Input Matriks Perbandingan Berpasangan")
            inputs_window.geometry(f"{crit_count * 100 + 150}x{crit_count * 50 + 200}")

            tk.Label(inputs_window, text="Masukkan Matriks Perbandingan Berpasangan", font=("Arial", 14)).pack(pady=10)

            # Input matriks dalam bentuk tabel
            matrix_frame = tk.Frame(inputs_window)
            matrix_frame.pack()

            matrix_entries = []
            for i in range(crit_count):
                row_entries = []
                for j in range(crit_count):
                    # Entry input dengan default diagonal bernilai 1
                    entry = tk.Entry(matrix_frame, width=10, font=("Arial", 10), justify="center")
                    entry.grid(row=i, column=j, padx=5, pady=5)
                    if i == j:
                        entry.insert(0, "1")
                    row_entries.append(entry)
                matrix_entries.append(row_entries)

            # Fungsi perhitungan AHP
            def calculate():
                try:
                    # Ambil data input matriks
                    pairwise_matrix = np.array([
                        [float(entry.get()) for entry in row]
                        for row in matrix_entries
                    ])

                    # Validasi matriks persegi
                    if pairwise_matrix.shape[0] != pairwise_matrix.shape[1]:
                        raise ValueError("Matriks harus berbentuk persegi (NxN).")

                    # Validasi nilai diagonal harus 1
                    for i in range(crit_count):
                        if pairwise_matrix[i, i] != 1:
                            raise ValueError("Nilai diagonal utama matriks harus 1.")

                    # Validasi simetri jika matriks bersifat konsisten
                    for i in range(crit_count):
                        for j in range(crit_count):
                            if pairwise_matrix[i, j] != 0 and pairwise_matrix[j, i] != 0:
                                if not np.isclose(pairwise_matrix[i, j] * pairwise_matrix[j, i], 1.0):
                                    raise ValueError("Matriks tidak konsisten, nilai tidak simetris.")

                    # Lakukan perhitungan AHP
                    priority_vector = calculate_ahp(pairwise_matrix)

                    # Tampilkan hasil
                    results_window = tk.Toplevel()
                    results_window.title("Hasil AHP")
                    results_window.geometry("400x300")
                    tk.Label(results_window, text="Prioritas Kriteria", font=("Arial", 14, "bold")).pack(pady=10)

                    for i, val in enumerate(priority_vector):
                        tk.Label(results_window, text=f"Kriteria {i+1}: {val:.4f}", font=("Arial", 12)).pack(pady=2)

                except ValueError as e:
                    messagebox.showerror("Error", f"Input tidak valid: {e}")
                except Exception as e:
                    messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

            # Tombol untuk menghitung
            tk.Button(inputs_window, text="Hitung AHP", font=("Arial", 12, "bold"), command=calculate).pack(pady=10)

        except ValueError as e:
            messagebox.showerror("Error", f"Input tidak valid: {e}")

    # Tombol untuk melanjutkan ke input matriks
    tk.Button(root, text="Lanjutkan", font=("Arial", 12, "bold"), command=next_step).pack(pady=20)

    root.mainloop()

# Menjalankan program
if __name__ == "__main__":
    ahp_gui()
