import numpy as np

def input_wp_data():
    print("Masukkan jumlah alternatif:")
    m = int(input("Jumlah alternatif: "))
    alternatives = [input(f"Nama alternatif {i+1}: ") for i in range(m)]

    print("Masukkan jumlah kriteria:")
    n = int(input("Jumlah kriteria: "))
    criteria = [input(f"Nama kriteria {i+1}: ") for i in range(n)]

    print("Masukkan bobot masing-masing kriteria (dalam persentase, total 100%):")
    weights = np.array([float(input(f"Bobot {criteria[i]}: ")) for i in range(n)])

    print("Masukkan jenis kriteria (1 untuk Benefit, 0 untuk Cost):")
    types = np.array([int(input(f"Jenis {criteria[i]} (1=Benefit, 0=Cost): ")) for i in range(n)])

    print("Masukkan matriks keputusan:")
    decision_matrix = []
    for i in range(m):
        print(f"Alternatif {alternatives[i]}:")
        decision_matrix.append([float(input(f"Nilai {criteria[j]}: ")) for j in range(n)])

    return alternatives, criteria, weights, types, np.array(decision_matrix)

def normalize_weights(weights):
    return weights / weights.sum()

def calculate_wp_score(decision_matrix, weights, types):
    normalized_weights = normalize_weights(weights)
    for j, t in enumerate(types):
        if t == 0:  # Cost
            decision_matrix[:, j] = 1 / decision_matrix[:, j]
    
    scores = np.prod(decision_matrix ** normalized_weights, axis=1)
    return scores

def main():
    print("### Weighted Product (WP) ###")
    alternatives, criteria, weights, types, decision_matrix = input_wp_data()

    print("\nMatriks Keputusan:")
    print(decision_matrix)

    print("\nBobot Kriteria:")
    print(weights)

    scores = calculate_wp_score(decision_matrix, weights, types)

    print("\nHasil Skor WP:")
    for alt, score in zip(alternatives, scores):
        print(f"{alt}: {score:.4f}")

    print("\nAlternatif Terbaik:")
    best_index = np.argmax(scores)
    print(f"{alternatives[best_index]} dengan skor {scores[best_index]:.4f}")

if __name__ == "__main__":
    main()
