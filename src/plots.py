import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd
import numpy as np
from data_loader import load_the_data


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


def mental_health_scatter_plot(output_path):
    df = load_the_data().sample(n=2500, random_state=42)
    stress_levels = df["stress"]
    gpa = df["gpa"]
    m, c = np.polyfit(stress_levels, gpa, 1)
    trendline = m*stress_levels + c
    plt.scatter(stress_levels, gpa, color='red', s=1, label='Data Points')
    plt.plot(stress_levels, trendline, color='red', linestyle='--', linewidth=2, label=f'OLS Trendline (y = {m:.2f}x + {abs(c):.2f})')
    plt.xlabel("Stress Levels (From 0 to 10)")
    plt.ylabel("GPA (From 0 to 2)")
    plt.title("Stress Levels vs. GPA")
    plt.legend()
    
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    pass



if __name__ == '__main__':

    out_path1 = figures_folder / "correlations_chart.png"
    plot_correlations(out_path1)
    out_path2 = figures_folder / "stress_gpa_scatter_plot.png"
    mental_health_scatter_plot(out_path2)