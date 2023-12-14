
import matplotlib.pyplot as plt
import glob
import os

def plot_from_file(file_path, output_folder):
    """
    Read points from a file and generate a plot.

    Parameters:
    - file_path (str): Path to the file containing points.
    - output_folder (str): Path to the output folder for saving plots.

    Returns:
    - None
    """
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    # Read points from the file, ignoring the first line (header)
    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]

    x_values = []
    si_x_values = []

    for line in lines:
        x, si_x = map(float, line.strip().split('\t'))
        x_values.append(x)
        si_x_values.append(si_x)

    # Generate the plot
    plt.plot(x_values, si_x_values, label='Interpolation')
    plt.scatter(x_values, si_x_values, color='red', marker='o', label='Data Points')
    plt.xlabel('x')
    plt.ylabel('si(x)')
    plt.title('Spline Interpolation')
    plt.legend()
    plt.grid(True)

    # Save the plot to the output folder
    plot_name = os.path.splitext(os.path.basename(file_path))[0] + '_plot.png'
    output_path = os.path.join(output_folder, plot_name)
    plt.savefig(output_path)
    plt.close()

def generate_plots():
    """
    Generate plots for all files in the output folder.

    Parameters:
    - None

    Returns:
    - None
    """
    output_folder = 'plots'
    os.makedirs(output_folder, exist_ok=True)

    output_files = glob.glob('output/*.txt')

    for file_path in output_files:
        plot_from_file(file_path, output_folder)

if __name__ == "__main__":
    generate_plots()
