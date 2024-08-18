import numpy as np
import matplotlib.pyplot as plt
import os


def plot_all_weighting_curves(
    _central_frequencies, _weighting_curve_1, _weighting_curve_2, _weighting_curve_3
):
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(
        _central_frequencies,
        _weighting_curve_1,
        linestyle="-",
        color="b",
        label="A-Weighting Curve",
    )

    plt.plot(
        _central_frequencies,
        _weighting_curve_2,
        linestyle="-",
        color="r",
        label="C-Weighting Curve",
    )

    plt.plot(
    _central_frequencies,
    _weighting_curve_3,
    linestyle="-",
    color="g",
    label="Z-Weighting Curve",
    )

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
    plt.title(" Weighting Curves", fontsize=14)
    plt.grid(True, which="both", linestyle="--", linewidth=1.0)

    # Add a legend
    plt.legend()

    # Adjust layout to prevent cutting off the labels
    plt.tight_layout()

    # Ensure the 'figures' directory exists
    os.makedirs("figures", exist_ok=True)

    # Save the plot to a file
    plt.savefig(os.path.join("figures", "weighting_curves.png"))

    # Display the plot
    plt.show()
