import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# 画像サイズ
size = 500
radius = size // 2

# HSV色空間で色相を角度に対応させる
hsv_image = np.ones((size, size, 3))  # 初期値を白にする

for y in range(size):
    for x in range(size):
        dx = x - radius
        dy = y - radius
        dist = np.sqrt(dx**2 + dy**2)
        if dist <= radius:
            hue = (np.arctan2(dy, dx) / (2 * np.pi) + 0.5) % 1.0  # 角度から色相に変換
            hsv_image[y, x] = mcolors.hsv_to_rgb([hue, 1, 1])  # HSV -> RGB 変換
        else:
            hsv_image[y, x] = [1, 1, 1]  # 円の外側を白にする

# 画像を描画
fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(hsv_image, extent=[-1, 1, -1, 1])
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)
plt.show()
