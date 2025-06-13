# Channel Area Web Application

This is a simple Flask-based web application for calculating the cross-sectional area of different water channel shapes:

- **Circular Channel**: circular cross-section, area = π * radius²
- **Rectangle Channel**: rectangular cross-section, area = width * depth
- **Polygon Channel**: free-form shape drawn by clicking points on the canvas

Each dimension field lets you choose units in metres, centimetres or millimetres.
Areas are reported in the selected units squared. The circular channel also
allows editing the number of points used to draw the circle (default is 25).
Rectangular channels are centred at the bottom of the canvas and always use four
points. The **New Channel** button opens a dialog containing all the options for
creating a shape and adjusting its dimensions. An additional **Water Height**
box sits beneath the canvas where you can specify how full the channel is, from
0 up to the maximum height of the selected shape. The shape is coloured grey
above the water line and blue below it. Both the overall shape area and the
water-filled area are displayed beneath the canvas.

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
shows grid lines with **x** and **y** axes for reference. Select **Polygon Channel** to
set a number of points (minimum three). When the value changes, a default
regular polygon is centred at the bottom of the canvas. You can then click to
edit the points. You can clear the shape using the *Clear Polygon Channel* button.
The area updates automatically as you change the shape. Each point is shown as a
blue marker. Double‑click a marker to drag it to a new location; it turns black
while being edited. Choose the units (m, cm, or mm) from the drop‑down to have
results displayed in the same units squared. All shapes are treated as polygons:
the circular channel defaults to 25 points and the rectangle uses four. A table
beneath the canvas lists each vertex. Editing the table keeps the coordinates
inside the canvas and immediately redraws the shape. Small red markers indicate
the minimum and maximum points of the current shape.

A **Allow Scaling** checkbox controls whether shapes can be edited with the
mouse or table. Use **Undo** and **Redo** to step through previous edits. Shape
files are saved as SVG under `channel_area/shapes` and managed from the
**Manage Shapes** dialog which lets you name, save and reload saved shapes. Use
the **New Channel** dialog to choose a shape type, units and dimensions when
starting a drawing.

An **Add Points** checkbox lets you insert new vector points with a double
click. The point is placed on the edge closest to where you clicked so the
polygon updates naturally. When the option is disabled, a double click selects a
point for editing instead.

A simple menu at the top of the page provides quick access to the **New
Channel** and **Manage Shapes** dialogs, and the application now uses a basic
stylesheet for clearer layout.

Two buttons under the canvas let you rotate the shape while keeping it anchored at the bottom centre. Use **One Point Down** to place a single vertex on the baseline or **Two Points Down** to place a flat edge along the baseline.

Use the **Water Height** box below the canvas to draw a blue line at the chosen level and see the water area. The line spans only the width of the current shape.

A dashed orange rectangle indicates the shape's bounding box so you can see its maximum width and height. These values are listed below the canvas.

The grid origin is the bottom left corner. A label beneath the canvas shows the current cursor coordinates in this system. When editing a point you can drag it with the left mouse button and the marker follows the cursor until the button is released.
