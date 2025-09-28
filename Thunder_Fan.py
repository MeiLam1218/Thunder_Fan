# Copy of Cloud_to_Ground_Lightning.py for process week 4

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Lightning stroke data: years 2005–2025, 12 months per year (Jan–Dec)
# Data format: {year: [Jan, Feb, ..., Dec]}
lightning_data = {
    2005: [None, None, None, None, None, 7638, 19659, 13911, 886, 773, 0, 0],
    2006: [0, 1, 7, 3600, 2099, 16333, 5606, 17132, 2192, 1, 573, 0],
    2007: [0, 0, 0, 2688, 6647, 12789, 325, 8813, 832, 0, 0, 0],
    2008: [0, 0, 16, 220, 6338, 14970, 13652, 103, 6512, 205, 23, 0],
    2009: [0, 0, 2442, 1075, 1291, 9205, 1456, 5967, 11369, 0, 0, 0],
    2010: [0, 140, 0, 43, 11454, 820, 7885, 7794, 35961, 24, 0, 0],
    2011: [0, 0, 0, 1405, 1811, 1615, 1477, 3618, 1221, 3, 0, 0],
    2012: [0, 0, 0, 15196, 9661, 1332, 12597, 2568, 2714, 0, 241, 0],
    2013: [0, 0, 3377, 2043, 19116, 3968, 1673, 6406, 745, 0, 0, 0],
    2014: [0, 0, 12401, 2853, 17141, 5291, 9608, 8931, 3319, 2990, 0, 0],
    2015: [0, 1, 0, 1, 13483, 1609, 7001, 14135, 1626, 573, 0, 0],
    2016: [56, 0, 341, 2439, 3035, 2209, 15449, 15480, 1276, 731, 0, 0],
    2017: [0, 33, 17, 4342, 2093, 7273, 4706, 7907, 5761, 196, 0, 0],
    2018: [0, 0, 57, 272, 924, 4712, 2789, 17233, 2176, 2, 0, 0],
    2019: [0, 151, 172, 15332, 3946, 13414, 8996, 12395, 806, 2714, 0, 0],
    2020: [89, 332, 107, 4, 8058, 31355, 669, 1728, 24168, 417, 0, 0],
    2021: [0, 0, 1, 0, 1754, 9078, 13397, 6807, 7452, 465, 0, 0],
    2022: [0, 0, 109, 0, 1230, 9122, 6615, 5741, 3570, 7, 0, 0],
    2023: [0, 0, 1241, 4699, 4561, 21033, 3352, 6554, 1336, 105, 0, 0],
    2024: [0, 0, 0, 17031, 4714, 7507, 3904, 7077, 4728, 1, 0, 0],
    2025: [0, 0, 89, 186, 175, 1320, 18518, 28901, None, None, None, None],
}

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
years = sorted(lightning_data.keys())

def animate_flower():
    fig = plt.figure(figsize=(5, 5))
    fig.patch.set_facecolor('black')
    ax = plt.subplot(111)
    ax.set_aspect('equal')  # Make the plot area a perfect circle
    ax.set_facecolor('black')
    ax.set_xticks([])
    ax.set_yticklabels([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(False)
    ax.set_frame_on(False)
    ax.set_xlim(-70, 70)
    ax.set_ylim(-70, 70)

    # Each dot represents 10 lightning strokes
    strokes_per_dot = 10
    counts = [c if c is not None else 0 for c in lightning_data[2023]]
    month_dot_counts = [max(1, c // strokes_per_dot) for c in counts]
    total_dots = sum(month_dot_counts)
    rings = 6
    dots_per_ring = [total_dots // rings] * rings
    for i in range(total_dots % rings):
        dots_per_ring[i] += 1

    dots_theta = []
    dots_r = []
    dots_x = []
    dots_y = []
    colors = []
    dot_month_map = []
    for m, count in enumerate(month_dot_counts):
        dot_month_map.extend([m]*count)

    # Calculate size scale for each month based on lightning strokes
    counts = [c if c is not None else 0 for c in lightning_data[2023]]
    min_strokes = min([c for c in counts if c > 0])
    max_strokes = max(counts)
    month_size_scale = [0.5 + 1.5 * ((c - min_strokes) / (max_strokes - min_strokes) if max_strokes > min_strokes else 1) for c in counts]

    lightning_colors = [
        [1, 1, 1, 0.9],      # white
        [0.5, 0.7, 1, 0.8],  # blue
        [0.7, 0.5, 1, 0.8],  # violet
        [1, 1, 0.3, 0.8],    # yellow
        [0.8, 0.9, 1, 0.8],  # pale blue
        [0.9, 0.8, 1, 0.8],  # pale violet
        [1, 0.95, 0.7, 0.8], # pale yellow
        [0.7, 0.8, 1, 0.8],  # blue-violet
        [1, 1, 0.8, 0.8],    # soft white
        [0.6, 0.7, 1, 0.8],  # blue
        [0.8, 0.7, 1, 0.8],  # violet
    ]
    dots_per_frame = 4  # Reveal 4 dots per frame for even faster animation
    dot_idx = 0
    # Multi-lobed flower petal pattern: r = base_radius * (1 + petal_depth * sin(lobes * theta))
    lobes = 7  # Number of petals (unique look)
    petal_depth = 0.6  # How deep the lobes are (0-1)
    base_radius = 40
    # Use a spiral (phyllotaxis) pattern to minimize overlap
    golden_angle = np.pi * (3 - np.sqrt(5))  # ~137.5 degrees
    for i in range(len(dot_month_map)):
        angle = i * golden_angle
        r = 15 + 55 * np.sqrt(i / len(dot_month_map))  # Spiral out from center
        # Optionally, add flower petal modulation
        r_mod = base_radius * (1 + petal_depth * np.sin(lobes * angle))
        r = (r + r_mod) / 2
        x = r * np.cos(angle)
        y = r * np.sin(angle)
        dots_theta.append(angle)
        dots_r.append(r)
        dots_x.append(x)
        dots_y.append(y)
        month_idx = dot_month_map[i]
        colors.append(lightning_colors[month_idx % len(lightning_colors)])
        dot_idx += 1

    frames = range(0, len(dots_theta), dots_per_frame)
    min_size, max_size = 0.5, 40
    scatter = ax.scatter([], [], s=[], color=[], alpha=0.8, zorder=2)
    month_text = ax.text(0, 80, '', ha='center', va='top', fontsize=14, color='white',
                        bbox=dict(facecolor='black', alpha=0.7, boxstyle='round,pad=0.4'))

    def init():
        scatter.set_offsets(np.empty((0, 2)))
        scatter.set_color([])
        month_text.set_text('')
        return scatter, month_text

    def update(frame):
        # Reveal multiple dots per frame
        n = frame + 1
        # Petal bloom: scale radius outward as animation progresses
        bloom = min(1.0, frame / (len(dots_x) * 0.6))  # 0 to 1, controls bloom speed
        x = np.array(dots_x[:n]) * bloom
        y = np.array(dots_y[:n]) * bloom
        # Pulse effect: modulate alpha for all dots
        pulse = 0.5 + 0.5 * np.sin(frame * 0.15)
        c = []
        for i, base_col in enumerate(colors[:n]):
            # Animate alpha for all dots, stronger for the newest dot
            alpha = base_col[3] * (0.7 + 0.3 * np.sin(frame * 0.15 + i))
            if i == n - 1:
                alpha = 1.0  # newest dot is always fully visible
            c.append([base_col[0], base_col[1], base_col[2], alpha])
        # Animate only the newest dot from small to large
        s = []
        for i in range(n):
            month_idx = dot_month_map[i]
            scale = month_size_scale[month_idx]
            if i == n - 1 and frame > 0:
                s.append(min_size * scale)
            else:
                s.append(max_size * scale)

        # Rotating effect
        angle = np.deg2rad(frame * 1.0)  # 1 degree per frame (slightly faster rotation)
        cos_a, sin_a = np.cos(angle), np.sin(angle)
        x_rot = x * cos_a - y * sin_a
        y_rot = x * sin_a + y * cos_a
        coords = np.column_stack([x_rot, y_rot])
        scatter.set_offsets(coords)
        scatter.set_color(c)
        scatter.set_sizes(s)
        # Show current month and dot count at the top
        if frame < len(dot_month_map):
            current_month_idx = dot_month_map[frame]
            current_month = months[current_month_idx]
            current_count = month_dot_counts[current_month_idx]
            month_text.set_text(f"{current_month}: {current_count} dots")
        else:
            month_text.set_text('')
        return scatter, month_text

    ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init,
                                  blit=True, interval=5, repeat=True)
    plt.tight_layout()
    plt.show()

def main():
    animate_flower()

if __name__ == "__main__":
    main()