import tkinter as tk
from tkinter import messagebox
import numpy as np

# Fungsi perhitungan SAW
def calculate_saw(criteria, weights, decision_matrix):
    # Normalisasi matriks
    normalized_matrix = decision_matrix / decision_matrix.sum(axis=0)
    
    # Mengalikan dengan bobot
    weighted_matrix = normalized_matrix * weights
    
    # Menghitung skor total
    scores = weighted_matrix.sum(axis=1)
    return scores

# Menampilkan hasil SAW
def show_results(alternatives, scores):
    results_window = tk.Toplevel()
    results_window.title("Hasil SPK - SAW")
    results_window.geometry("400x300")

    tk.Label(results_window, text="Hasil Perhitungan SAW", font=("Arial", 14)).pack(pady=10)
    for alt, score in zip(alternatives, scores):
        tk.Label(results_window, text=f"{alt}: {score:.4f}").pack()

    best_alt = alternatives[np.argmax(scores)]
    tk.Label(results_window, text=f"Alternatif Terbaik: {best_alt}", font=("Arial", 12, "bold")).pack(pady=10)

# Tampilan utama GUI
def saw_gui():
    root = tk.Tk()
    root.title("SPK - Simple Additive Weighting (SAW)")
    root.geometry("600x400")

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
            # Ambil jumlah alternatif dan kriteria
            alt_count = int(alt_count_entry.get())
            crit_count = int(crit_count_entry.get())

            if alt_count <= 0 or crit_count <= 0:
                raise ValueError("Jumlah alternatif dan kriteria harus lebih dari 0.")

            # Window input alternatif, kriteria, bobot, dan matriks
            inputs_window = tk.Toplevel()
            inputs_window.title("Input Data SAW")
            inputs_window.geometry("800x600")

            # Input Nama Alternatif
            tk.Label(inputs_window, text="Nama Alternatif:", font=("Arial", 12, "bold")).pack(pady=5)
            alt_entries = []
            for i in range(alt_count):
                frame = tk.Frame(inputs_window)
                frame.pack()
                tk.Label(frame, text=f"Alternatif {i+1}:", width=15, anchor="w").pack(side=tk.LEFT)
                entry = tk.Entry(frame, width=20)
                entry.pack(side=tk.LEFT)
                alt_entries.append(entry)

            # Input Nama Kriteria
            tk.Label(inputs_window, text="Nama Kriteria:", font=("Arial", 12, "bold")).pack(pady=5)
            crit_entries = []
            for i in range(crit_count):
                frame = tk.Frame(inputs_window)
                frame.pack()
                tk.Label(frame, text=f"Kriteria {i+1}:", width=15, anchor="w").pack(side=tk.LEFT)
                entry = tk.Entry(frame, width=20)
                entry.pack(side=tk.LEFT)
                crit_entries.append(entry)

            # Input Bobot Kriteria
            tk.Label(inputs_window, text="Bobot Kriteria (dalam %, total harus 100%):", font=("Arial", 12, "bold")).pack(pady=5)
            weight_entries = []
            for i in range(crit_count):
                frame = tk.Frame(inputs_window)
                frame.pack()
                tk.Label(frame, text=f"Bobot Kriteria {i+1}:", width=15, anchor="w").pack(side=tk.LEFT)
                entry = tk.Entry(frame, width=10)
                entry.pack(side=tk.LEFT)
                weight_entries.append(entry)

            # Input Matriks Keputusan (Tabel)
            tk.Label(inputs_window, text="Matriks Keputusan:", font=("Arial", 12, "bold")).pack(pady=5)
            matrix_frame = tk.Frame(inputs_window)
            matrix_frame.pack()

            # Header Kriteria
            tk.Label(matrix_frame, text="Alternatif / Kriteria", width=15, borderwidth=1, relief="solid", bg="lightgray").grid(row=0, column=0, padx=2, pady=2)
            for j in range(crit_count):
                tk.Label(matrix_frame, text=f"Kriteria {j+1}", width=12, borderwidth=1, relief="solid", bg="lightblue").grid(row=0, column=j+1, padx=2, pady=2)

            # Input Nilai Matriks
            matrix_entries = []
            for i in range(alt_count):
                tk.Label(matrix_frame, text=f"Alternatif {i+1}", width=15, borderwidth=1, relief="solid", bg="lightgreen").grid(row=i+1, column=0, padx=2, pady=2)
                row_entries = []
                for j in range(crit_count):
                    entry = tk.Entry(matrix_frame, width=12, borderwidth=1, relief="solid", justify="center")
                    entry.grid(row=i+1, column=j+1, padx=2, pady=2)
                    row_entries.append(entry)
                matrix_entries.append(row_entries)

            # Fungsi Hitung SAW
            def calculate():
                try:
                    # Ambil data input
                    alternatives = [entry.get().strip() for entry in alt_entries]
                    criteria = [entry.get().strip() for entry in crit_entries]
                    weights = np.array([float(entry.get().strip()) for entry in weight_entries]) / 100

                    # Validasi total bobot
                    if not np.isclose(weights.sum(), 1.0):
                        raise ValueError("Total bobot kriteria harus 100%.")

                    # Ambil matriks keputusan
                    decision_matrix = np.array([
                        [float(entry.get().strip()) for entry in row]
                        for row in matrix_entries
                    ])

                    # Perhitungan SAW
                    scores = calculate_saw(criteria, weights, decision_matrix)

                    # Tampilkan hasil
                    show_results(alternatives, scores)

                except ValueError as e:
                    messagebox.showerror("Error", f"Input tidak valid: {e}")
                except Exception as e:
                    messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

            tk.Button(inputs_window, text="Hitung SAW", command=calculate).pack(pady=20)

        except ValueError as e:
            messagebox.showerror("Error", f"Input tidak valid: {e}")

    tk.Button(root, text="Lanjutkan", command=next_step).pack(pady=20)
    root.mainloop()

# Menjalankan Program
if __name__ == "__main__":
    saw_gui()
