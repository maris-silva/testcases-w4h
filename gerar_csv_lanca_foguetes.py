import csv

# Lista de test cases
test_cases = [
    (5, [50, 40, 30, 20, 10], 25, 30),
    (4, [20, 15, 10, 5], 21, -1),
    (6, [11, 9, 7, 5, 3, 1], 6, 7),
    (7, [700, 600, 500, 400, 300, 200, 100], 350, 400),
    (3, [20, 10, 5], 10, 10),
    (5, [50, 40, 30, 20, 10], 5, 10),  # H menor que todas as alturas
    (4, [20, 15, 10, 5], 25, -1),     # H maior que todas as alturas
    (1, [10], 10, 10),                # Apenas um elemento
    (6, [50, 40, 40, 30, 20, 10], 40, 40),  # Múltiplos elementos repetidos
]

# Nome do arquivo CSV
csv_file_path = "test_cases_lanca_foguetes.csv"

# Criando o arquivo CSV
with open(csv_file_path, mode="w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    # Escrevendo o cabeçalho
    csv_writer.writerow(["N", "Alturas", "H", "Saida Esperada"])
    # Escrevendo os test cases
    for case in test_cases:
        csv_writer.writerow(case)

print(f"Arquivo CSV criado com sucesso: {csv_file_path}")
