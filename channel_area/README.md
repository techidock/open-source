# Channel Area Web Application

This is a simple Flask-based web application for calculating the cross-sectional area of different water channel shapes:

- **Pipe**: circular cross-section, area = π * radius²
- **River**: rectangular cross-section, area = width * depth
- **V Duct**: triangular cross-section, area = 0.5 * base * depth
- **Polygon**: free-form shape drawn by clicking points on the canvas

## Requirements

- Python 3.x
- Flask

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Running the App

```bash
python app.py
```

Then open your browser at [http://localhost:5000](http://localhost:5000).
Use the form to pick a shape and adjust dimensions. Each shape comes with a
default size when selected and is rendered as a polygon on a grid. The canvas
shows grid lines with **x** and **y** axes for reference. Select **Polygon** to
set a number of points (minimum three) and click to place each vertex; the
coordinates are listed below the canvas. You can clear the shape using the
*Clear Polygon* button. The area updates automatically as you change the shape.
Each point is shown as a blue marker. Double‑click a marker to drag it to a
new location; it turns black while being edited.
