# Program Sistem Pendukung Keputusan (SPK) Metode SAW

# 1. Identifikasi Alternatif dan Kriteria
def input_data():
    print("Masukkan jumlah alternatif:")
    alternatives = [input(f"Nama alternatif {i+1}: ") for i in range(int(input()))]

    print("Masukkan jumlah kriteria:")
    criteria = [input(f"Nama kriteria {i+1}: ") for i in range(int(input()))]

    print("Masukkan bobot untuk masing-masing kriteria (total harus 1):")
    weights = [float(input(f"Bobot kriteria {criteria[i]}: ")) for i in range(len(criteria))]

    print("Masukkan tipe kriteria (benefit atau cost):")
    criteria_type = [input(f"Tipe kriteria {criteria[i]}: ") for i in range(len(criteria))]

    print("Masukkan matriks keputusan:")
    decision_matrix = []
    for i in range(len(alternatives)):
        print(f"Nilai untuk alternatif {alternatives[i]}:")
        decision_matrix.append([float(input(f"{criteria[j]}: ")) for j in range(len(criteria))])

    return alternatives, criteria, weights, criteria_type, decision_matrix

# 2. Normalisasi Matriks Keputusan
def normalize_matrix(decision_matrix, criteria_type):
    normalized_matrix = []
    for j in range(len(criteria_type)):
        column = [decision_matrix[i][j] for i in range(len(decision_matrix))]
        if criteria_type[j] == "benefit":
            max_value = max(column)
            normalized_column = [x / max_value for x in column]
        elif criteria_type[j] == "cost":
            min_value = min(column)
            normalized_column = [min_value / x for x in column]
        normalized_matrix.append(normalized_column)

    # Transpose matriks normalisasi untuk kemudahan perhitungan
    return list(zip(*normalized_matrix))

# 3. Menghitung Skor Akhir
def calculate_scores(normalized_matrix, weights, alternatives):
    final_scores = []
    for i, alt in enumerate(alternatives):
        score = sum(normalized_matrix[i][j] * weights[j] for j in range(len(weights)))
        final_scores.append((alt, score))

    # Sorting berdasarkan skor
    final_scores.sort(key=lambda x: x[1], reverse=True)
    return final_scores

# 4. Menampilkan Hasil Akhir
def display_results(final_scores):
    print("\nHasil Penilaian Menggunakan Metode SAW:")
    print("Alternatif | Skor Akhir")
    print("-----------------------")
    for alt, score in final_scores:
        print(f"{alt:<11} | {score:.4f}")

# Fungsi Utama
def main():
    print("### Sistem Pendukung Keputusan - Metode SAW ###")
    print("Langkah 1: Identifikasi Alternatif dan Kriteria")
    alternatives, criteria, weights, criteria_type, decision_matrix = input_data()

    print("\nLangkah 2: Normalisasi Matriks Keputusan")
    normalized_matrix = normalize_matrix(decision_matrix, criteria_type)
    print("Matriks Normalisasi:")
    for row in normalized_matrix:
        print(row)

    print("\nLangkah 3: Menghitung Skor Akhir")
    final_scores = calculate_scores(normalized_matrix, weights, alternatives)

    print("\nLangkah 4: Menampilkan Hasil Akhir")
    display_results(final_scores)

if __name__ == "__main__":
    main()
