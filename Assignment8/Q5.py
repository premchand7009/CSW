import numpy as np

sugar = np.array([85, 110, 145, 95, 130, 160, 100, 139, 75, 180])
print("Blood sugar levels:", sugar)

classification = np.empty(sugar.shape, dtype=object)

normal_mask = sugar < 100
prediabetic_mask = (sugar >= 100) & (sugar <= 139)
diabetic_mask = sugar >= 140

classification[normal_mask] = "Normal"
classification[prediabetic_mask] = "Pre-Diabetic"
classification[diabetic_mask] = "Diabetic"

print("Patient classification:", classification)
