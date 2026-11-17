# Computer Science for Physics and Chemistry (CSPC)

## PW1 — Radioactive Decay Simulation
* **Lab A (`decay.py`, `speed.py`, `test_decay.py`):** Implemented stochastic and vectorized radioactive decay simulations ($N(t) = N_0 e^{-\lambda t}$), benchmarked execution speed, and verified accuracy with `pytest`.
* **Lab B (`plot.py`, `Snakefile`):** Visualized simulated vs. observed decay data (`figure.png`, `test.png`) and automated the workflow using Snakemake.

---

## PW2 — Lab A: Motion from Tracking Data (`analysis.py`)
* **Mean Acceleration:** -8.5797 m/s² (close to theoretical $-9.81\text{ m/s}^2$).
* **Why acceleration is noisy:** Differentiation compares adjacent data points, which amplifies small measurement noise in position once for velocity and twice for acceleration (standard deviation: 28.7161 m/s²).
* **Integration result:** Integrating acceleration back to position cancels out random noise through summation, recovering the original position within 0.7846 meters.

---

## PW2 — Lab B: Optimization & Chemical Applications
* **Warmup (`warmup.py`):** On the convex function $f(x)$, Gradient Descent, Newton, and SLSQP all converge to $x = 3.0$. On the non-convex function $g(x)$, starting from $x_0 = 0.0$ causes Newton's method to converge to a local maximum ($x \approx 0.170$, $g''(x) < 0$), whereas Gradient Descent and SLSQP find the global minimum ($x \approx -1.301$). Starting from $x_0 = 2.0$ traps Gradient Descent and Newton in a local minimum ($x \approx 1.131$, $g''(x) > 0$), while SLSQP still reaches the global minimum.
* **Chemical Kinetics (`kinetics.py`):** Minimizing the sum of squared residuals with SLSQP yields a fitted rate constant $k \approx 0.2818$.
* **Chemical Equilibrium (`equilibrium.py`):** Newton's method converged to $x \approx 1.3944$ (non-physical root exceeding initial reactant), while SLSQP found the physical equilibrium at $x \approx 0.7795$ ($0.22\text{ mol } H_2$, $0.22\text{ mol } I_2$, and $1.56\text{ mol } HI$).
* **Titration Curve (`titration.py`):** Using numerical differentiation ($dpH/dV$), the steepest slope identifies the equivalence point at $V \approx 50.00\text{ mL}$.
