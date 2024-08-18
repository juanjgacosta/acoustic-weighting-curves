import json
import numpy as np
from plot_weighting_curve import plot_weighting_curve
from plot_all_weighting_curves import plot_all_weighting_curves

with open("frequencies.json", "r") as file:
    json_data = json.load(file)

central_frequencies = np.array(json_data["central_frequencies"])
a_weighting_curve = np.array(json_data["a_weighting_curve"])
c_weighting_curve = np.array(json_data["c_weighting_curve"])
z_weighting_curve = np.array(json_data["z_weighting_curve"])

plot_weighting_curve(central_frequencies, a_weighting_curve, "a_weighting")
plot_weighting_curve(central_frequencies, c_weighting_curve, "c_weighting")
plot_all_weighting_curves(
    central_frequencies, a_weighting_curve, c_weighting_curve, z_weighting_curve
)
