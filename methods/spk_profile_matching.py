import numpy as np

def input_pm_data():
    print("Masukkan jumlah alternatif:")
    m = int(input("Jumlah alternatif: "))
    alternatives = [input(f"Nama alternatif {i+1}: ") for i in range(m)]

    print("Masukkan jumlah kriteria:")
    n = int(input("Jumlah kriteria: "))
    criteria = [input(f"Nama kriteria {i+1}: ") for i in range(n)]

    print("Masukkan bobot masing-masing kriteria (dalam persentase, total 100%):")
    weights = np.array([float(input(f"Bobot {criteria[i]}: ")) for i in range(n)])

    print("Masukkan profil ideal:")
    ideal_profile = np.array([float(input(f"Profil ideal untuk {criteria[i]}: ")) for i in range(n)])

    print("Masukkan matriks keputusan:")
    decision_matrix = []
    for i in range(m):
        print(f"Alternatif {alternatives[i]}:")
        decision_matrix.append([float(input(f"Nilai {criteria[j]}: ")) for j in range(n)])

    return alternatives, criteria, weights, ideal_profile, np.array(decision_matrix)

def calculate_gap(decision_matrix, ideal_profile):
    return decision_matrix - ideal_profile

def calculate_score(gap_matrix, weights):
    gap_scores = np.abs(gap_matrix)  # Absolute gap values
    weighted_scores = gap_scores * weights
    total_scores = weighted_scores.sum(axis=1)
    return total_scores

def main():
    print("### Profile Matching (PM) ###")
    alternatives, criteria, weights, ideal_profile, decision_matrix = input_pm_data()

    print("\nMatriks Keputusan:")
    print(decision_matrix)

    print("\nProfil Ideal:")
    print(ideal_profile)

    gap_matrix = calculate_gap(decision_matrix, ideal_profile)
    print("\nMatriks Gap:")
    print(gap_matrix)

    scores = calculate_score(gap_matrix, weights)

    print("\nHasil Skor Profile Matching:")
    for alt, score in zip(alternatives, scores):
        print(f"{alt}: {score:.4f}")

    print("\nAlternatif Terbaik:")
    best_index = np.argmin(scores)  # Lower score indicates better match
    print(f"{alternatives[best_index]} dengan skor {scores[best_index]:.4f}")

if __name__ == "__main__":
    main()
