import tkinter as tk
from tkinter import messagebox
import numpy as np

# Fungsi menghitung GAP
def calculate_gap(decision_matrix, ideal_profile):
    return decision_matrix - ideal_profile

# Fungsi menghitung skor total
def calculate_score(gap_matrix, weights):
    gap_scores = np.abs(gap_matrix)  # Nilai absolut dari GAP
    weighted_scores = gap_scores * weights  # Bobot dikalikan GAP
    total_scores = weighted_scores.sum(axis=1)  # Total skor tiap alternatif
    return total_scores

# Fungsi utama GUI
def pm_gui():
    root = tk.Tk()
    root.title("SPK - Profile Matching (PM)")
    root.geometry("700x500")

    # Judul
    tk.Label(root, text="SPK - Profile Matching (PM)", font=("Arial", 16, "bold")).pack(pady=10)

    # Input jumlah alternatif dan kriteria
    tk.Label(root, text="Masukkan Jumlah Alternatif:", font=("Arial", 12)).pack(pady=5)
    alt_count_entry = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
    alt_count_entry.pack()

    tk.Label(root, text="Masukkan Jumlah Kriteria:", font=("Arial", 12)).pack(pady=5)
    crit_count_entry = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
    crit_count_entry.pack()

    # Fungsi untuk melanjutkan ke input matriks
    def next_step():
        try:
            alt_count = int(alt_count_entry.get())
            crit_count = int(crit_count_entry.get())

            if alt_count <= 0 or crit_count <= 0:
                raise ValueError("Jumlah alternatif dan kriteria harus lebih dari 0.")

            # Window Input Data
            inputs_window = tk.Toplevel()
            inputs_window.title("Input Data Profile Matching")
            inputs_window.geometry("800x600")

            # Input Nama Alternatif
            tk.Label(inputs_window, text="Nama Alternatif:", font=("Arial", 12)).pack(pady=5)
            alt_entries = [tk.Entry(inputs_window, font=("Arial", 10), width=20) for _ in range(alt_count)]
            for entry in alt_entries:
                entry.pack()

            # Input Nama Kriteria
            tk.Label(inputs_window, text="Nama Kriteria:", font=("Arial", 12)).pack(pady=5)
            crit_entries = [tk.Entry(inputs_window, font=("Arial", 10), width=20) for _ in range(crit_count)]
            for entry in crit_entries:
                entry.pack()

            # Input Bobot Kriteria
            tk.Label(inputs_window, text="Bobot Kriteria (total 100%):", font=("Arial", 12)).pack(pady=5)
            weight_entries = [tk.Entry(inputs_window, font=("Arial", 10), width=10) for _ in range(crit_count)]
            for entry in weight_entries:
                entry.pack()

            # Input Profil Ideal
            tk.Label(inputs_window, text="Profil Ideal:", font=("Arial", 12)).pack(pady=5)
            ideal_entries = [tk.Entry(inputs_window, font=("Arial", 10), width=10) for _ in range(crit_count)]
            for entry in ideal_entries:
                entry.pack()

            # Matriks Keputusan
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

            # Fungsi menghitung hasil
            def calculate():
                try:
                    alternatives = [entry.get() for entry in alt_entries]
                    criteria = [entry.get() for entry in crit_entries]
                    weights = np.array([float(entry.get()) for entry in weight_entries]) / 100
                    ideal_profile = np.array([float(entry.get()) for entry in ideal_entries])

                    # Validasi jumlah bobot
                    if not np.isclose(weights.sum(), 1.0):
                        raise ValueError("Total bobot harus sama dengan 100%.")

                    decision_matrix = np.array([
                        [float(entry.get()) for entry in row]
                        for row in matrix_entries
                    ])

                    # Hitung GAP dan skor
                    gap_matrix = calculate_gap(decision_matrix, ideal_profile)
                    scores = calculate_score(gap_matrix, weights)

                    # Tampilkan hasil
                    results_window = tk.Toplevel()
                    results_window.title("Hasil Profile Matching")
                    results_window.geometry("500x400")

                    tk.Label(results_window, text="Hasil Skor Profile Matching", font=("Arial", 14, "bold")).pack(pady=10)
                    for alt, score in zip(alternatives, scores):
                        tk.Label(results_window, text=f"{alt}: {score:.4f}", font=("Arial", 12)).pack(pady=2)

                    # Alternatif terbaik
                    best_index = np.argmin(scores)
                    tk.Label(results_window, text=f"Alternatif Terbaik: {alternatives[best_index]}", 
                             font=("Arial", 12, "bold"), fg="green").pack(pady=10)

                except ValueError as e:
                    messagebox.showerror("Error", f"Input tidak valid: {e}")
                except Exception as e:
                    messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

            # Tombol untuk menghitung
            tk.Button(inputs_window, text="Hitung PM", font=("Arial", 12, "bold"), command=calculate).pack(pady=20)

        except ValueError as e:
            messagebox.showerror("Error", f"Input tidak valid: {e}")

    # Tombol lanjutkan
    tk.Button(root, text="Lanjutkan", font=("Arial", 12, "bold"), command=next_step).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    pm_gui()
