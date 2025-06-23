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
regular polygon is positioned at the bottom left of the canvas. You can then click to
edit the points. You can clear the shape using the *Clear Polygon Channel* button.
Selecting **Circular Channel** creates a circle drawn with 36 points and a default diameter of 1000&nbsp;mm. A *Diameter* field lets you set this size and you may adjust the number of points to change how smooth the circle appears. The circle's points are rounded to the nearest millimetre so its width and height always equal the chosen diameter.
The area updates automatically as you change the shape. Each point is shown as a
blue marker. Double‑click a marker to drag it to a new location; it turns black
while being edited. Choose the units (m, cm, or mm) from the drop‑down to have results shown in the chosen units squared. All shapes are treated as polygons. A table beneath the canvas lists each vertex. Editing the table keeps the coordinates inside the canvas and immediately redraws the shape. Small red markers indicate the minimum and maximum points of the current shape. Table numbers use three decimal places for metres, one for centimetres and none for millimetres.

An **Edit Mode** checkbox controls whether shapes can be modified with the
mouse or table. Use **Undo** and **Redo** to step through previous edits. Shape
files are saved as SVG under `channel_area/shapes` and managed from the
**Manage Shapes** dialog which lets you name, save and reload saved shapes.
Use the **New Channel** dialog to choose a shape type when starting a drawing.
The canvas size is configured from the **Setup** dialog, while display units are selected in the **Display Settings** panel.
The last design is automatically saved and restored the next time you open the page.

An **Add Points** checkbox lets you insert new vector points with a double
click. The point is placed on the edge closest to where you clicked so the
polygon updates naturally. When the option is disabled, a double click selects a
point for editing instead.

The markers themselves can be hidden or shown with the **Show Vectors**
checkbox found in the **Display Settings** section of the sidebar. This
panel also contains the **Edit Mode** and **Show Bounding Box** options.

A simple menu at the top of the page provides quick access to the **New
Channel** and **Manage Shapes** dialogs, and the application now uses a basic
stylesheet for clearer layout.

Shapes are always positioned with their left edge along the bottom of the canvas.

Use the **Water Height** box below the canvas to draw a blue line at the chosen level and see the water area. The line spans only the width of the current shape. The resulting water area is listed in the **Channel Properties** panel.
Use the **Silt Height** box to show sediment build-up. The brown region up to this line is counted separately so you can see the silt area alongside the water area; this value is also displayed in **Channel Properties**.
A **Height Units** dropdown lets you show these heights in metres, centimetres or millimetres independently of the shape units.
The **Manage Shapes** dialog stores the water and silt heights along with the points when saving a design so it reloads exactly as drawn. All point coordinates are saved in millimetres regardless of the units currently displayed.

A dashed orange rectangle indicates the shape's bounding box. Labels beside the rectangle show the current width and height in the chosen units and the same numbers appear in the **Display Properties** panel to the right of the canvas. A **Show Bounding Box** checkbox lets you hide or reveal this rectangle and its labels.
The sidebar also provides a **Display Settings** section to toggle **Edit Mode**, **Show Vectors**, **Show Bounding Box** and **Enable Measurements**.
Below this menu, the **Channel Properties** panel lists the maximum width and height along with the **Total Area**, **Water Area** and **Silt Area**.

The grid origin is the bottom left corner. Tick marks along the axes show the distance from the origin using a fixed spacing of **0.5&nbsp;metre** (50&nbsp;cm or 500&nbsp;mm). The current spacing is listed in the **Display Properties** panel along with the cursor coordinates. When editing a point you can drag it with the left mouse button and the marker follows the cursor until the button is released. When you hover over a marker or drag a point, the cursor becomes a blue crosshair to indicate the point is editable.
A small margin on the left and bottom edges keeps the axes slightly inside the canvas so points near the origin are easier to manipulate.
The **Display Settings** panel includes an **Enable Measurements** option. Click once on the canvas to start an arrow, move the mouse to see the length, then click again to fix it in place. Arrowheads are drawn at both ends and can be dragged to adjust the measurement. When an arrowhead is selected it turns black and follows the cursor until released. Use **Clear** to remove the arrow. Distances show three decimals in metres, one in centimetres and none in millimetres.

You can also set the real-world size represented by the canvas. The **Display Settings** panel now contains *Canvas Width* and *Canvas Height* inputs (default 4000&nbsp;mm each). These values define how many millimetres span the canvas and are saved with each shape so it reloads at the same scale. A **Shape Scale** field in the **Setup** dialog lets you enlarge or shrink the polygon about the bottom left. If scaling makes the shape exceed the canvas, the canvas size automatically expands to the next 500&nbsp;mm step up to a limit of 20&nbsp;m. The grid spacing remains fixed at 500&nbsp;mm (0.5&nbsp;m) regardless of the units so switching display units does not resize the grid. The current spacing appears in the **Display Properties** panel.
