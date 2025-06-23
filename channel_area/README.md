# Channel Area Web Application

This is a simple Flask-based web application for calculating the cross-sectional area of water channels. Shapes are drawn as polygons that you can freely edit.

Each dimension field lets you choose units in metres, centimetres or millimetres.
All channel data is stored internally in millimetres so switching units only changes the way values are displayed.
Areas are reported in the selected units squared.
The **New Channel** button opens a dialog containing all the options for creating a shape and adjusting its dimensions. An additional **Water Height** box sits beneath the canvas where you can specify how full the channel is, from 0 up to the maximum height of the selected shape. The height inputs show the current units next to the edit boxes. The shape is coloured grey above the water line and blue below it. Both the overall shape area and the water-filled area are displayed beneath the canvas. A **Silt Height** box lets you define how much sediment fills the bottom of the channel; this region is shown in brown and its area is also reported.

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
Selecting **Circular Channel** creates a circle drawn with 30 points and a default diameter of 1000&nbsp;mm. A *Diameter* field lets you set this size and you may adjust the number of points to change how smooth the circle appears.
The area updates automatically as you change the shape. Each point is shown as a
blue marker. Double‑click a marker to drag it to a new location; it turns black
while being edited. Choose the units (m, cm, or mm) from the drop‑down to have results shown in the chosen units squared. All shapes are treated as polygons. A table beneath the canvas lists each vertex. Editing the table keeps the coordinates inside the canvas and immediately redraws the shape. Small red markers indicate
the minimum and maximum points of the current shape.

An **Edit** checkbox controls whether shapes can be modified with the
mouse or table. Use **Undo** and **Redo** to step through previous edits. Shape
files are saved as SVG under `channel_area/shapes` and managed from the
**Manage Shapes** dialog which lets you name, save and reload saved shapes.
Use the **New Channel** dialog to choose a shape type when starting a drawing.
Display units and the canvas size are configured from the **Setup** dialog.
The last design is automatically saved and restored the next time you open the page.

An **Add Points** checkbox lets you insert new vector points with a double
click. The point is placed on the edge closest to where you clicked so the
polygon updates naturally. When the option is disabled, a double click selects a
point for editing instead.

A simple menu at the top of the page provides quick access to the **New
Channel** and **Manage Shapes** dialogs, and the application now uses a basic
stylesheet for clearer layout.

Two buttons under the canvas let you rotate the shape while keeping it anchored
at the bottom centre. Use **One Point Down** to place a single vertex on the baseline or **Two Points Down** to place a flat edge along the baseline. Shapes are automatically repositioned so their bounding box stays centred at the bottom of the canvas after every edit.

Use the **Water Height** box below the canvas to draw a blue line at the chosen level and see the water area. The line spans only the width of the current shape.
Use the **Silt Height** box to show sediment build-up. The brown region up to this line is counted separately so you can see the silt area alongside the water area.
A **Height Units** dropdown lets you show these heights in metres, centimetres or millimetres independently of the shape units.
The **Manage Shapes** dialog stores the silt height along with the points and orientation when saving a design so it reloads exactly as drawn. All point coordinates are saved in millimetres regardless of the units currently displayed.

A dashed orange rectangle indicates the shape's bounding box so you can see its maximum width and height. These values are listed below the canvas.

The grid origin is the bottom left corner. A label beneath the canvas shows the current cursor coordinates in this system. When editing a point you can drag it with the left mouse button and the marker follows the cursor until the button is released. When you hover over a marker or drag a point, the cursor becomes a blue crosshair to indicate the point is editable.
The **Tools** menu includes an **Enable Measurements** option. Click once on the canvas to start an arrow, move the mouse to see the length, then click again to fix it in place. Arrowheads are drawn at both ends and can be dragged to adjust the measurement. When an arrowhead is selected it turns black and follows the cursor until released. Use **Clear** to remove the arrow.

You can also set the real-world size represented by the canvas. The **Setup** dialog provides *Draw Width* and *Draw Height* fields which default to 4000&nbsp;mm by 4000&nbsp;mm along with a units selector. These values define how many millimetres span the canvas and all width, height and area readouts scale accordingly. Changing the draw size no longer alters the channel itself—only the scale used for measurements and labels. The grid spacing is always shown in millimetres so switching display units does not resize the grid.
