import numpy as np
import glob

def calculate_spline_coefficients(x, y):
    n = len(x)
    h = np.diff(x)
    delta_y = np.diff(y)

    # Construção da matriz A e vetor b
    A = np.zeros((n, n))
    b = np.zeros(n)
    A[0, 0] = 1
    A[-1, -1] = 1

    for i in range(1, n - 1):
        A[i, i - 1] = h[i - 1]
        A[i, i + 1] = h[i]
        A[i, i] = 2 * (h[i - 1] + h[i])
        b[i] = 3 * (delta_y[i] / h[i] - delta_y[i - 1] / h[i - 1])

    # Solução do sistema linear
    c = np.linalg.solve(A, b)

    # Cálculo dos coeficientes b, d
    b = np.zeros(n - 1)
    d = np.zeros(n - 1)

    for i in range(n - 1):
        b[i] = (delta_y[i] / h[i]) - (h[i] / 3) * (2 * c[i] + c[i + 1])
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])

    return b, c, d

# Função para calcular si(x) para um conjunto de pontos igualmente espaçados
def calculate_spline_at_x(x, y, m):
    b, c, d = calculate_spline_coefficients(x, y)
    n = len(x)
    x_values = np.linspace(x[0], x[-1], m)
    spline_values = []

    for z in x_values:
        for i in range(n - 1):
            if x[i] <= z <= x[i + 1]:
                h = z - x[i]
                result = y[i] + b[i] * h + c[i] * h**2 + d[i] * h**3
                spline_values.append(result)
                break

    return x_values, spline_values

def main():
    source_option = input("Deseja ler as entradas da pasta input? (s/n): ").lower()

    if source_option == 's':
        input_files = glob.glob("input/*.txt")

        if not input_files:
            print("Nenhum arquivo de entrada encontrado na pasta input.")
            return

        for input_file in input_files:
            process_input(input_file)
    elif source_option == 'n':
        process_input()
    else:
        print("Opção inválida. Use 's' para ler da pasta input ou 'n' para entrada pelo console.")

def process_input(input_file=None):
    if input_file:
        with open(input_file, "r") as file:
            lines = file.readlines()
    else:
        n = int(input("Digite a quantidade de pontos: "))
        x_values = list(map(float, input("Digite os valores de x separados por espaço: ").split()))
        y_values = list(map(float, input("Digite os valores de y separados por espaço: ").split()))
        z = float(input("Digite o valor de z: "))
        m = int(input("Digite a quantidade de pontos para cálculo de si(x): "))

        if n != len(x_values) or n != len(y_values):
            print("Erro: O número de pontos informado não coincide com a entrada.")
            return

        lines = [str(n)] + [f"{val:.6f}" for val in x_values] + [f"{val:.6f}" for val in y_values] + [f"{z:.6f}", str(m)]

    n = int(lines[0].strip())
    x_values = list(map(float, lines[1].split()))
    y_values = list(map(float, lines[2].split()))
    z = float(lines[3])
    m = int(lines[4])

    if n != len(x_values) or n != len(y_values):
        print(f"Erro: O número de pontos informado não coincide com a entrada no arquivo {input_file}.")
        return

    x_values, si_x_values = calculate_spline_at_x(x_values, y_values, m)

    output_file = "grafico.txt" if input_file is None else input_file.replace("input/", "output/").replace(".txt", "_grafico.txt")

    with open(output_file, "w") as file:
        file.write("x\tsi(x)\n")
        for x, si_x in zip(x_values, si_x_values):
            file.write(f"{x:.6f}\t{si_x:.6f}\n")

    print(f"Resultados salvos em {output_file}")

if __name__ == "__main__":
    main()
