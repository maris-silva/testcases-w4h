import csv

# Função para calcular o número de formas de alcançar o topo usando a fórmula de Fibonacci
def calcular_maneiras(n):
    """
    Retorna o número de maneiras que Aria pode alcançar o degrau n.
    Baseado na lógica da sequência de Fibonacci.
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    # Usando uma abordagem iterativa para evitar recursão
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

# Gerar 200 test cases
test_cases = []
for i in range(1, 31):  # Limite máximo do problema é 30
    saida_esperada = calcular_maneiras(i)
    test_cases.append((i, saida_esperada))

# Nome do arquivo CSV
csv_file_path = "test_cases_aria.csv"

# Criar o arquivo CSV
with open(csv_file_path, mode="w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    # Escrever cabeçalho
    csv_writer.writerow(["N", "Saida Esperada"])
    # Adicionar test cases
    for case in test_cases:
        csv_writer.writerow(case)

print(f"Arquivo CSV com test cases criado com sucesso: {csv_file_path}")
