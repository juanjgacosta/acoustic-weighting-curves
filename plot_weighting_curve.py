import numpy as np
import matplotlib.pyplot as plt
import os


def plot_weighting_curve(_central_frequencies, _weighting_curve, _curve_name):
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(_central_frequencies, _weighting_curve, linestyle="-", color="b")

    # Setting the scale of x-axis to log
    plt.xscale("log")

    # Set the ticks and labels for the x-axis
    plt.xticks(
        _central_frequencies,
        labels=[f"{freq:.0f}" for freq in _central_frequencies],
        rotation=90,
        fontsize=10,
    )

    # Labeling axes
    plt.xlabel("Band centre Frequency (Hz)", fontsize=12)
    plt.ylabel("Weighting Correction (dB)", fontsize=12)

    # Title and grid
    plt.title(f"{_curve_name.replace('_', ' ').capitalize()} Curve", fontsize=14)
    plt.grid(True, which="both", linestyle="--", linewidth=1.0)

    # Adjust layout to prevent cutting off the labels
    plt.tight_layout()

    # Ensure the 'figures' directory exists
    os.makedirs("figures", exist_ok=True)

    # Save the plot to a file
    plt.savefig(os.path.join("figures", f"{_curve_name}_curve.png"))

    # Display the plot
    plt.show()
