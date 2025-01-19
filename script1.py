import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

lg_h_steps = np.array([
    1.342422681, 0.643452676, -0.055517328, -0.754487332, -1.453457337,
    -2.152427341, -2.851397345, -3.55036735, -4.249337354, -4.948307358,
    -5.647277363
])

lg_phi_steps = np.array([
    0.679694742, -1.529237417, -1.049192782, -2.344104658, -3.891105058,
    -5.938958998, -5.409661053, -5.387725199, -5.386871176, -5.386838689,
    -5.386834032
])

linear_mask_steps = (lg_h_steps >= -1.5) & (lg_h_steps <= 0)
lg_h_linear_steps = lg_h_steps[linear_mask_steps]
lg_phi_linear_steps = lg_phi_steps[linear_mask_steps]

# Линейная регрессия на линейном участке
slope_steps, intercept_steps, r_value_steps, p_value_steps, std_err_steps = linregress(lg_h_linear_steps, lg_phi_linear_steps)

# Параметры наклона и пересечения
p_order_steps = slope_steps  # порядок малости
lg_C_steps = intercept_steps  # log(C)
C_steps = 10 ** lg_C_steps  # константа погрешности

# Построение графика
plt.figure(figsize=(10, 6))
plt.scatter(lg_h_steps, lg_phi_steps, label="Original Data", color='blue')
plt.plot(lg_h_linear_steps, slope_steps * lg_h_linear_steps + intercept_steps, color='red', label=f"Linear Fit (p={p_order_steps:.2f})")
plt.axvline(-7, color='gray', linestyle='--', label="End of linear region")
plt.axvline(-3, color='gray', linestyle='--', label="Start of linear region")
plt.title("Log-Log Graph for φ(h) vs h (Steps Data)")
plt.xlabel("lg(h)")
plt.ylabel("lg(φ(h))")
plt.legend()
plt.grid(True)
plt.show()

print(f"Порядок малости p: {p_order_steps}")
print(f"log(C): {lg_C_steps}")
print(f"Константа C: {C_steps}")
