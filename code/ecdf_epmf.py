# block modules
import matplotlib.pyplot as plt
import numpy as np
import scipy

# block modules

from latex_figures import *


# block ecdfdef
def ecdf(x):
    support, values = np.unique(x, return_counts=True)
    X = values.cumsum()
    return support, X / len(x)


# block ecdfdef

# block ecdfplot

X = np.array([2, 5, 2, 1, 9, 5, 5, 5])
x, F = ecdf(X)

fig, ax = plt.subplots(1, 1, figsize=(6, 3))

for i in range(len(x) - 1):
    ax.hlines(y=F[i], xmin=x[i], xmax=x[i + 1], color='k')
    ax.plot(x[i], F[i], 'o', c='k', mfc='k', ms=3)  # closed circles
    ax.plot(x[i + 1], F[i], 'o', c='k', mfc='white', ms=3)  # open circles

# left boundary
ax.hlines(y=0, xmin=x[0] - 1 / 2, xmax=x[0], color='k')
ax.plot(x[0], 0, 'o', c="k", mfc='white', ms=3)
# right boundary
ax.hlines(y=1, xmin=x[-1], xmax=x[-1] + 0.5, color='k')
ax.plot(x[-1], 1, 'o', c="k", mfc='k', ms=3)

ax.set_xlabel('$x$')
ax.set_ylabel('$F$')
ax.set_title('ecdf')

fig.tight_layout()
fig.savefig("../images/ecdf.png")
# block ecdfplot


# block epmf
def is_sorted_asc(arr):
    return np.all(arr[:-1] <= arr[1:])


def epmf(x, n=10):
    if not is_sorted_asc(x):
        x.sort()
    num = min(len(x), n + 1)
    v = x[np.linspace(0, len(x) - 1, num, dtype=int)]
    u = (v[1:] + v[:-1]) / 2
    delta = v[1:] - v[:-1]
    return u, 1 / num / delta


# block epmf


# block myepmf
gen = np.random.default_rng(3)

fig, [ax1, ax2] = plt.subplots(1, 2, figsize=(6, 3))

labda = 3
x, F = ecdf(gen.exponential(scale=1 / labda, size=10000))
u, f = epmf(x, n=30)
ax1.vlines(x=u, ymin=0, ymax=f, color='k', lw=0.2)
ax1.plot(u, f, 'ko', ms=2)
ax1.plot(x, labda * np.exp(-labda * x), color='k')
ax1.set_xlabel('x')
ax1.set_ylabel('epmf')
ax1.set_title('epmf exponential')

x, F = ecdf(gen.uniform(size=10000))
u, f = epmf(x, n=30)
ax2.vlines(x=u, ymin=0, ymax=f, color='k', lw=0.2)
ax2.plot(u, f, 'ko', ms=2)
ax2.plot(x, np.ones_like(x), color='k')
ax2.set_xlabel('x')
ax2.set_title('epmf uniform')

fig.tight_layout()
fig.savefig("../images/epmf.png")
# block myepmf


# block rho
def rho(x):
    return 1 / (1 + (x / sigma) ** 2)


def rho_p(x):  # derivative of rho
    return -2 * x * sigma**2 / (sigma**2 + x**2) ** 2


# block rho


# block radialG
rv = scipy.stats.expon()
N = 1000
x, F = ecdf(rv.rvs(size=N, random_state=gen))
sigma = 20 * np.diff(x).max()
# block radialG

# block radialmat
centers = x[::10]
G = rho(np.abs(x[:, None] - centers[None, :]))
a = np.linalg.lstsq(G, F, rcond=None)[0]  # rcond silences a warning

xi = np.linspace(x.min(), x.max(), 30)  # points to test the approximation
phi = rho(np.abs(xi[:, None] - centers[None, :])) @ a
phi_p = rho_p(xi[:, None] - centers[None, :]) @ a
# block radialmat

# block radialfig
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3))
ax1.plot(x, F, 'k-', linewidth=1, label="ecdf")
ax1.plot(xi, phi, 'ko', ms=2, label="fit")
ax1.legend()
ax2.plot(xi, rv.pdf(xi), 'k-', linewidth=1, label="pdf")
ax2.plot(xi, phi_p, 'k.', ms=3, label="fit")
ax2.vlines(xi, 0, phi_p, colors='k', linestyles='-', lw=1)
ax2.legend()
fig.tight_layout()
fig.savefig('../images/radial_epmf_expon.png')
# block radialfig
