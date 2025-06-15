import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import os

# 資料參數
n_particles = int(2e5)
n_steps = 1000 + 1
data_dir = os.getcwd() + "/particles_fmm"
bound = 1000

# 載入某一時間步的資料
def load_particles(step):
    filename = f"{data_dir}/double_plummer_2e5_step{step}.bin"
    data = np.fromfile(filename, dtype=np.float64).reshape(n_particles, 7)
    return data[:, 1], data[:, 2], data[:, 3]

# 圖表設定
fig = plt.figure(figsize=(16, 16), facecolor='black', dpi=150)
ax = fig.add_subplot(111, projection='3d', facecolor='black')

sc = ax.scatter([], [], [], s=0.3, color='yellow', alpha=0.8)

# 移除座標軸與標籤
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_axis_off()

# 設定邊界
ax.set_box_aspect([1, 1, 1])
ax.set_xlim(-bound, bound)
ax.set_ylim(-bound, bound)
ax.set_zlim(-bound, bound)

# 更新函數
def update(frame):
    x, y, z = load_particles(frame)
    sc._offsets3d = (x, y, z)
    time = frame*0.1/np.sqrt(1.25)
    ax.set_title(f"Time = {time:3.6f}"+" $t_\mathrm{dyn}$", color='white', fontsize=12)
    print(f'frame={frame}')
    return sc,

# 建立動畫
ani = FuncAnimation(fig, update, frames=n_steps, interval=100, blit=False)

# 儲存 GIF
ani.save(f"plummer_evolution_bound{bound}.gif", writer="pillow", fps=20, dpi=150)

print("GIF 已儲存為 plummer_evolution.gif")
