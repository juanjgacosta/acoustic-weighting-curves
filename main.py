import json
import numpy as np

# Load the JSON file
with open("frequencies.json", "r") as file:
    json_data = json.load(file)

central_frequencies = np.array(json_data["central_frequencies"])
a_weighting_curve = np.array(json_data["a_weighting_curve"])
c_weighting_curve = np.array(json_data["c_weighting_curve"])
print(c_weighting_curve)
