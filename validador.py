import numpy as np
from scipy.interpolate import CubicSpline

# Função para calcular as splines cúbicas naturais
def calculate_cubic_splines(x, y):
    cs = CubicSpline(x, y, bc_type='natural')
    return cs

# Função para calcular si(z) e si(x) para um conjunto de pontos igualmente espaçados
def calculate_spline_values(cs, z, m):
    x_values = np.linspace(cs.x[0], cs.x[-1], m)
    si_z = cs(z)
    si_x_values = cs(x_values)
    return si_z, x_values, si_x_values

# Função principal
def main():
    # Leitura dos dados de entrada
    n = int(input("Digite a quantidade de pontos: "))
    x_values = list(map(float, input("Digite os valores de x separados por espaço: ").split()))
    y_values = list(map(float, input("Digite os valores de y separados por espaço: ").split()))
    z = float(input("Digite o valor de z: "))
    m = int(input("Digite a quantidade de pontos para cálculo de si(x): "))

    # Verificação do número de pontos
    if n != len(x_values) or n != len(y_values):
        print("Erro: O número de pontos informado não coincide com a entrada.")
        return

    # Cálculo das splines cúbicas naturais
    cs = calculate_cubic_splines(x_values, y_values)

    # Cálculo de si(z) e si(x) para o conjunto de pontos
    si_z, x_values, si_x_values = calculate_spline_values(cs, z, m)

    # Exibição dos resultados
    print(f"\nValor de z: {z}, si(z): {si_z}\n")
    for x, si_x in zip(x_values, si_x_values):
        print(f"x: {x}, si(x): {si_x}")

    # Salvar os pontos em um arquivo grafico.txt se desejar
    with open("grafico.txt", "w") as file:
        file.write("x\tsi(x)\n")
        for x, si_x in zip(x_values, si_x_values):
            file.write(f"{x}\t{si_x}\n")

if __name__ == "__main__":
    main()
