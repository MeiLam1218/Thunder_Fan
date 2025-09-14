# Cloud-to-Ground Lightning Strokes Visualization

An interactive web-based visualization that transforms monthly cloud-to-ground lightning stroke data from Hong Kong Territory into an abstract animated experience.

## Features

- **Abstract Animation**: Lightning strokes are visualized as dynamic, animated lightning bolts with particle effects
- **Monthly Data Progression**: Automatically cycles through 12 months of lightning stroke data
- **Intensity-Based Visualization**: Different colors represent different lightning stroke intensities:
  - Yellow: Low intensity (1-50 strokes)
  - Orange: Medium intensity (51-200 strokes) 
  - Red: High intensity (201+ strokes)
- **Interactive Controls**: Play, pause, reset, and speed control for the animation
- **Responsive Design**: Works on desktop and mobile devices

## How to Use

1. Open `index.html` in a web browser
2. Click "Play" to start the animation
3. Use the speed slider to adjust animation speed (0.1x to 3x)
4. Watch as lightning strikes animate based on historical Hong Kong data
5. Monitor the info panel for current month, stroke count, and intensity level

## Data Source

The visualization uses sample monthly lightning stroke data representative of Hong Kong's seasonal weather patterns, with higher activity during summer months (June-September) when thunderstorms are more frequent.

## Technology Stack

- **HTML5 Canvas**: For rendering lightning animations
- **Vanilla JavaScript**: Animation engine and data visualization logic
- **CSS3**: Styling and responsive design with gradient backgrounds and effects

## File Structure

- `index.html` - Main webpage structure
- `style.css` - Styling and visual effects
- `script.js` - Lightning visualization engine and animation logic
- `README.md` - Project documentation

## Lightning Animation Details

The visualization creates realistic lightning effects by:
- Generating jagged lightning bolt paths with random segments
- Adding particle effects at strike points
- Implementing opacity fade-out for natural dissipation
- Creating screen flash effects during high-intensity strikes
- Using color coding to represent different intensity levels

This abstract representation transforms raw meteorological data into an engaging visual experience that helps viewers understand Hong Kong's lightning patterns throughout the year.