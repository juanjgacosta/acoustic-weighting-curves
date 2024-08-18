import json
import numpy as np
import matplotlib.pyplot as plt

# Load the JSON file
with open("frequencies.json", "r") as file:
    json_data = json.load(file)

central_frequencies = np.array(json_data["central_frequencies"])
a_weighting_curve = np.array(json_data["a_weighting_curve"])
c_weighting_curve = np.array(json_data["c_weighting_curve"])

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(central_frequencies, a_weighting_curve, marker="o", linestyle="-", color="b")

# Setting the scale of x-axis to log
plt.xscale("log")

# Labeling axes
plt.xlabel("Central Frequencies (Hz)")
plt.ylabel("A-Weighting Curve (dB)")

# Title and grid
plt.title("Central Frequencies vs. A-Weighting Curve")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

# Save the plot to a file
plt.savefig("a_weighting_curve.png")

# Display the plot
plt.show()
