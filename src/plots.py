import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd


z_cols = [
    "mental_health_z",
    "digital_discipline_z",
    "financial_security_z",
    "physical_health_z",
    "academic_performance_z"
]


figures_folder = Path(__file__).resolve().parent.parent / "outputs" / "figures"
figures_folder.mkdir(parents=True, exist_ok=True)


def plot_correlations(output_path):
    corr_file = Path(__file__).resolve().parent.parent / "outputs" / "domain_correlations.csv"
    correlations = pd.read_csv(corr_file, index_col=0).squeeze("columns").sort_values()
    
    fig, ax = plt.subplots(figsize=(8,4))
    
    y_positions = range(len(correlations))
    bars = ax.barh(y_positions, correlations.values, height=0.7, color='skyblue', edgecolor='navy')
    ax.set_yticks(y_positions)

    formatted_labels = [
        label.replace("_z", "").replace("_", " ").title()
        for label in correlations.index
    ]

    ax.set_yticklabels(formatted_labels)    
    ax.set_xlim(-0.35, 1.0)

    ax.set_title("Domain Correlations")
    ax.set_xlabel("Correlation with GPA (score out of 1)")
    ax.set_ylabel("Domain")
    ax.bar_label(bars, fmt='%.3f', padding=4)
    ax.axvline(0, color='black', linewidth=0.8, linestyle='--')
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    pass


if __name__ == '__main__':

    out_path = figures_folder / "correlations_chart.png"
    plot_correlations(out_path)