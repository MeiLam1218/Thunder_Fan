# Thunder_Fan

## Thunder_Fan.py Overview

`Thunder_Fan.py` is a Python script that visualizes Hong Kong Observatory lightning data as a dynamic flower animation.

**Features:**
- Multi-lobed flower petal pattern using a spiral (phyllotaxis) layout to minimize overlap
- Petal bloom effect: petals grow outward from the center as the animation progresses
- Dots represent lightning strokes, with size and color mapped to monthly data
- Rotating and pulse effects for visual interest
- Data for 2023 is used by default, but the script supports other years

**What was used:**
- Python 3.x
- matplotlib (for plotting and animation)
- numpy (for calculations)

**What was done:**
- Implemented spiral pattern for dot placement
- Added petal bloom animation effect
- Mapped dot size and color to monthly lightning data
- Enabled saving animation as GIF/MP4 if GUI display is not available
- Provided troubleshooting for display issues (Tkinter, backend selection)

**How to run:**
1. Make sure you have Python 3.x, matplotlib, and numpy installed.
2. Run the script:
   ```
   python Thunder_Fan.py
   ```
3. If GUI windows do not display, the script can be modified to save the animation as a GIF or MP4 file for viewing in any media player.

---
