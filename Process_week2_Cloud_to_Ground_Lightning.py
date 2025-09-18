
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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



import numpy as np

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

    # Prepare all dots: each lightning stroke is a dot
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
        [1, 1, 0.5, 0.8],    # yellow
    ]
    dot_idx = 0
    for ring in range(rings):
        radius = 20 + ring * 8 + 3 * np.random.rand()
        for i in range(dots_per_ring[ring]):
            angle = 2 * np.pi * i / dots_per_ring[ring] + np.random.normal(0, 0.05)
            dots_theta.append(angle)
            dots_r.append(radius + np.random.normal(0, 1.5))
            x = (radius + np.random.normal(0, 1.5)) * np.cos(angle)
            y = (radius + np.random.normal(0, 1.5)) * np.sin(angle)
            dots_x.append(x)
            dots_y.append(y)
            month_idx = dot_month_map[len(colors)] if len(colors) < len(dot_month_map) else 0
            colors.append(lightning_colors[month_idx % len(lightning_colors)])
            dot_idx += 1



    # Animation: reveal dots one by one
    # Make animation faster by skipping frames
    dots_per_frame = 10  # You can adjust this value for even faster animation
    frames = range(0, len(dots_theta), dots_per_frame)
    scatter = ax.scatter([], [], s=18, color=[], alpha=0.8, zorder=2)
    month_text = ax.text(0, 80, '', ha='center', va='top', fontsize=14, color='white',
                        bbox=dict(facecolor='black', alpha=0.7, boxstyle='round,pad=0.4'))

    def init():
        scatter.set_offsets(np.empty((0, 2)))
        scatter.set_color([])
        month_text.set_text('')
        return scatter, month_text

    def update(frame):
        # Reveal multiple dots per frame
        # Use cartesian coordinates for regular axes
        x = dots_x[:frame+1]
        y = dots_y[:frame+1]
        c = colors[:frame+1]
        coords = np.column_stack([x, y])
        scatter.set_offsets(coords)
        scatter.set_color(c)
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
                                  blit=True, interval=0, repeat=True)
    plt.tight_layout()
    plt.show()




def main():
    animate_flower()

if __name__ == "__main__":
    main()
