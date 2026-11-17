import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

# --- PART 2: Mövqedən sürət və təcilə keçid ---
data = np.loadtxt("freefall.csv", skiprows=1)
t = data[:, 0]
y = data[:, 1]

v = np.gradient(y, t)
a = np.gradient(v, t)

print(f"Mean acceleration: {np.mean(a):.4f} m/s^2")

# --- PART 3: Səs-küy (Noise) problemi ---
print(f"Acceleration std: {np.std(a):.4f} m/s^2")

# --- PART 4: Geri inteqrasiya ---
v_rec = cumulative_trapezoid(a, t, initial=0) + v[0]
y_rec = cumulative_trapezoid(v_rec, t, initial=0) + y[0]

max_diff = np.max(np.abs(y - y_rec))
print(f"Max position difference after integration: {max_diff:.4f} m")

# --- PART 5: Qrafiklərin çəkilməsi (motion.png) ---
fig, axs = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

axs[0].plot(t, y, label="Position (y)")
axs[0].set_ylabel("Position (m)")
axs[0].legend()

axs[1].plot(t, v, color="orange", label="Velocity (v)")
axs[1].set_ylabel("Velocity (m/s)")
axs[1].legend()

axs[2].plot(t, a, color="green", label="Acceleration (a)")
axs[2].axhline(-9.81, color="red", linestyle="--", label="Expected g (-9.81 m/s²)")
axs[2].set_ylabel("Acceleration (m/s²)")
axs[2].set_xlabel("Time (s)")
axs[2].legend()

plt.tight_layout()
plt.savefig("motion.png")
plt.close()

# --- BONUS: 2D Traektoriya (Vaxt qalarsa) ---
try:
    traj = np.loadtxt("trajectory.csv", delimiter=",", skiprows=1)
    t_2d, x_2d, y_2d = traj[:, 0], traj[:, 1], traj[:, 2]
    
    vx = np.gradient(x_2d, t_2d)
    vy = np.gradient(y_2d, t_2d)
    speed = np.sqrt(vx**2 + vy**2)
    
    fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
    ax1.plot(x_2d, y_2d)
    ax1.set_title("2D Path (x vs y)")
    ax1.set_xlabel("x (m)")
    ax1.set_ylabel("y (m)")
    
    ax2.plot(t_2d, speed, color="purple")
    ax2.set_title("Speed over Time")
    ax2.set_xlabel("Time (s)")
    ax2.set_ylabel("Speed (m/s)")
    
    plt.tight_layout()
    plt.savefig("trajectory_plot.png")
    plt.close()
except Exception as e:
    print("Bonus skipped or file missing:", e)