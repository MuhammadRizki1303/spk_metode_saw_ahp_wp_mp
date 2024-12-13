import numpy as np

def input_criteria():
    print("Masukkan jumlah kriteria:")
    n = int(input("Jumlah kriteria: "))
    criteria = [input(f"Nama kriteria {i+1}: ") for i in range(n)]

    print("Masukkan matriks perbandingan berpasangan:")
    pairwise_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            elif i < j:
                value = float(input(f"Nilai perbandingan {criteria[i]} vs {criteria[j]}: "))
                row.append(value)
            else:
                row.append(1 / pairwise_matrix[j][i])
        pairwise_matrix.append(row)

    return criteria, np.array(pairwise_matrix)

def calculate_weights(pairwise_matrix):
    eig_values, eig_vectors = np.linalg.eig(pairwise_matrix)
    max_index = np.argmax(eig_values)
    principal_eig_vector = eig_vectors[:, max_index].real
    weights = principal_eig_vector / principal_eig_vector.sum()
    return weights

def calculate_consistency(pairwise_matrix, weights):
    n = pairwise_matrix.shape[0]
    lambda_max = (pairwise_matrix @ weights).sum() / weights.sum()
    ci = (lambda_max - n) / (n - 1)
    ri_values = {1: 0.00, 2: 0.00, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
    ri = ri_values.get(n, 1.49)
    cr = ci / ri if ri != 0 else 0
    return cr

def main():
    print("### Analytic Hierarchy Process (AHP) ###")
    criteria, pairwise_matrix = input_criteria()

    print("\nMatriks Perbandingan Berpasangan:")
    print(pairwise_matrix)

    weights = calculate_weights(pairwise_matrix)
    print("\nBobot Kriteria:")
    for crit, weight in zip(criteria, weights):
        print(f"{crit}: {weight:.4f}")

    cr = calculate_consistency(pairwise_matrix, weights)
    print(f"\nRasio Konsistensi (CR): {cr:.4f}")
    if cr < 0.1:
        print("Konsistensi diterima.")
    else:
        print("Konsistensi tidak diterima. Silakan revisi matriks perbandingan.")

if __name__ == "__main__":
    main()
