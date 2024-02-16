import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as integrate

from latex_figures import *

gen = np.random.default_rng(3)


def p(x):
    return np.sqrt(1 - x**2)


Z = np.pi / 2
width_support = 1 - 1

N = 10000
samples = np.zeros(N)
xt = 0.0
for i in range(len(samples)):
    xt_candidate = gen.uniform(-1, 1)
    if gen.uniform() < p(xt_candidate) / p(xt):
        xt = xt_candidate
    samples[i] = xt
burn_in = len(samples) // 10
samples = samples[burn_in:]


n_bins = 30
counts, bins = np.histogram(samples, bins=n_bins)
dx = 2 / n_bins
pmf = counts / sum(counts) / dx
midpoints = (bins[:-1] + bins[1:]) / 2


x_vals = np.linspace(-1, 1, 1000)
y_vals = p(x_vals)

plt.figure(figsize=(3, 1))
plt.plot(x_vals, y_vals / Z, 'r', label='P(x)')
plt.stairs(pmf, bins)
plt.tight_layout()
plt.savefig("../images/MH-half-circle.png", dpi=300)

true_probs = np.array([p(k) for k in midpoints])
Z_estimates = true_probs / pmf
print(f"{Z_estimates.mean()=:2.3f}, {Z=:2.3f}")


f = lambda x: x**2
E_f = integrate.quad(lambda x: f(x) * p(x) / Z, -1, 1)[0]

E_f_estimated = np.mean(f(samples))
print(f"{E_f_estimated=:2.3f}, {E_f=:2.3f}")
