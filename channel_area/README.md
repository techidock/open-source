# Channel Area Web Application

This is a simple Flask-based web application for calculating the cross-sectional area of water channels. Shapes are drawn as polygons that you can freely edit. The interface uses **Bootstrap-Flask** so it adapts well to mobile screens. If that package isn't installed, a minimal `bootstrap5/base.html` template included with the project prevents `TemplateNotFound` errors.

Each dimension field lets you choose units in metres, centimetres or millimetres.
All channel data is stored internally in millimetres so switching units only changes the way values are displayed.
Areas are reported in the selected units squared.
The **New Channel** button opens a dialog containing all the options for creating a shape and adjusting its dimensions. Water and silt heights are configured on the **Channel Calculations** page along with a unit selector. The shape is coloured transparent grey (40% opacity) above the water line and transparent blue below it. The **Channel Properties** tab lists the overall shape area, the water-filled area and the silt area. A transparent brown region illustrates any silt build up.

## Requirements

- Python 3.x
- Flask
- bootstrap-flask

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
Selecting **Circular Channel** creates a circle drawn with 36 points and a default diameter of 300&nbsp;mm. A *Diameter* field lets you set this size and you may adjust the number of points to change how smooth the circle appears. The circle's points are rounded to the nearest millimetre so its width and height always equal the chosen diameter.
Selecting **Rectangle Channel** lets you enter a width, height and corner radius. Each corner uses nine points, producing rounded edges while still forming a polygon. A units selector in the dialog defines the units for these values.
Selecting **Egg Shape Channel** combines two circles. Enter the diameters for the bottom and top circles and the distance between their centres. The circles share the same centre line so the shape is symmetrical. Straight sides join the far left and right points to create the egg-like outline.
The area updates automatically as you change the shape. Each point is shown as a
blue marker. Single-click a marker to select it. Double-clicking the selected
marker switches to move mode—the cursor becomes a move icon and you can drag the
point (it turns black while being edited). Double-clicking when **Add Points** is
active inserts a new vertex on the nearest edge. Choose the units (m, cm, or mm)
from the drop-down to have results shown in the chosen units squared. All shapes
are treated as polygons. A table beneath the canvas lists each vertex. Editing
the table keeps the coordinates inside the canvas and immediately redraws the
shape. Small red markers indicate the minimum and maximum points of the current
shape. Table numbers use three decimal places for metres, one for centimetres and
none for millimetres.

The right-hand **Properties** menu groups information into **Display**, **Channel** and **Edit Tools** tabs. Edit Mode and Add Points are toggled from the floating **Edit Tools** menu opened by the pencil icon in section 4 of the left toolbar. That floating panel also holds a **Delete Point** button, while **Undo** and **Redo** controls appear in section 1 of the bottom bar whenever the edit tool is active. Shape files are saved as SVG under `channel_area/shapes` and managed from the **Manage Shapes** dialog which lets you name, save and reload saved shapes. Use the **New Channel** dialog to choose a shape type when starting a drawing. The canvas size is configured from the **Setup** dialog, while units are selected on the **Display** tab.
The last design is automatically saved and restored the next time you open the page. When a saved shape is loaded, its canvas dimensions are also restored so the drawing matches the real-world scale it was saved with.

Double clicking when **Add Points** is active inserts a new vertex on the nearest edge. With the option off, a double click selects a point for editing instead.

The markers themselves can be hidden or shown with the **Show Vectors**
checkbox found on the **Display** tab of the Properties menu. This tab also lists **Show Bounding Box** and measurement options alongside the other display toggles.
Uploaded reference images appear with a dashed black outline so you can see their boundaries while positioning them. Use the image icon in section 5 of the left toolbar to open the **Image Tools** panel. The first button there uploads a file and additional controls let you move and scale the picture.
Section 6 hosts a canvas icon that opens the **Canvas Tools** panel. This floating menu matches the left bar width. Item 0 provides a canvas colour picker, items 1–3 are placeholder shape buttons, item 4 activates the tape‑measure tool and item 5 offers a **Copy to clipboard** button.

A button at the top left reveals a slide-out menu containing **New Channel**,
**Manage Shapes** and **Setup**. The menu automatically closes once you choose
an option.
The top navigation bar stretches across the entire page in black. A menu button appears in the left corner so you can open the slide out menu.
Along the left border runs a solid grey strip divided into ten equal squares
numbered **0** at the top down to **9**. This serves as the tool menu. The bar
can scroll if the window is short so every square remains accessible. The first
section (0) opens the **Projects** panel, section 4 shows a pencil icon for the
**Edit Tools** menu, section 5 opens the **Image Tools** panel, section 6 opens the **Canvas Tools** panel and section 8 toggles the **Channel Calculations** view.
Hovering over either icon simply reveals its menu, while clicking locks the panel open and shows a circular **X**. Selecting a tool also locks the panel. Only one menu can be locked at a time, so choosing another icon closes the previous menu. The active tool’s icon and its toolbar button both receive a blue outline.
Selecting the calculator icon switches to the Channel Calculations page. This view hides the canvas and shows the **Channel Properties** panel fixed on the right side so you can review dimensions while working through calculations. Enter the water height, silt height and height units here. A **Water Velocity** box lets you set the average flow speed in metres per second. The page includes a **Water Level to Area** table that computes evenly spaced depths with a Matplotlib chart above the table plotting area on the X‑axis versus water level on the Y‑axis. A **Copy Table** button copies the table as tab-separated text so you can paste it directly into a spreadsheet. The flow rate in cubic metres per second updates automatically from the current water area and velocity.
The Edit Tools menu slides 10 px to the right when opened. Position 0 offers **Select** with a cursor icon. Position 1 enables **Add Points** with an icon shaped like a green cross on a black circle the same size as the vector markers, and position 2 activates **Delete Point**. Double‑click a marker in delete mode to confirm via a small dialog near the cursor. The image panel provides an **Upload** button and a **Move Image** toggle. When this tool is active a slider titled **Image Scale** appears in section 2 of the bottom bar so you can resize the picture. The tape‑measure tool now resides in the **Canvas Tools** panel at position 4.
A **Properties** button sits in section **9** of the bottom toolbar. It opens another panel with tabs for display and channel information. Pinning is only available in landscape orientation so the panel stays beside the canvas. The Properties panel now includes separate **Vectors** and **Measurements** tabs where the vertex list and measurement table are shown.

The page shows light grey borders along the left, right and bottom edges. The left bar and a matching right bar are split into numbered tool sections. The bottom bar is divided into ten segments. Its final segment contains three smaller cells: the Properties button on the left, a Full Screen shortcut beside it and an empty spot on the right. The centre section holds a zoom slider flanked by minus and plus buttons. The first cell displays the currently selected tool. Any choice from the menus&mdash;including **Move Image** and **Measure**&mdash;updates this label. When the Edit tool is active a **Shape Scale** slider appears in the next cell so you can quickly resize the polygon.

Shapes are always positioned with their left edge along the bottom of the canvas. The canvas now fills the browser window and scroll bars are removed so the entire drawing stays visible. The available height is calculated between the top navigation bar and bottom toolbar so the drawing area makes full use of the space. Portrait mode shows the Properties panel below the canvas, while landscape mode allows the panel to be pinned on the right.
The canvas has no fixed width or height attributes, so it automatically grows or
shrinks to fit whatever space is available in the drawing area.
Edit Mode is off by default so the point markers remain hidden. When the edit tool is active the markers are forced visible even if the **Show Vectors** checkbox is off.

Use the **Water Height** and **Silt Height** boxes on the **Channel Calculations** page to draw blue and brown lines at the chosen levels. The resulting water and silt areas appear alongside the total area in the properties panel.
A **Height Units** dropdown on the same page lets you choose metres, centimetres or millimetres for these values.
The **Manage Shapes** dialog stores the water and silt heights along with the points when saving a design so it reloads exactly as drawn. All point coordinates are saved in millimetres regardless of the units currently displayed.
These levels are automatically restored when a shape is loaded.

A dashed orange rectangle indicates the shape's bounding box. Labels beside the rectangle show the current width and height in the chosen units and the same numbers appear on the **Channel** tab. The **Display** tab lets you toggle **Show Vectors**, **Show Bounding Box** and **Show Measurements**. Measurement mode is activated from the tape‑measure icon in the **Canvas Tools** panel so only one edit tool is active at a time. The **Channel** tab lists the maximum width and height along with the **Total Area**, **Water Area** and **Silt Area**.
Small orange markers appear at each corner of the bounding box along with a cross at its centre. The measurement tool snaps to these markers whenever the box is visible, making it easy to check overall dimensions.

The grid origin is the bottom left corner. Tick marks along the axes show the distance from the origin using a fixed spacing of **0.5&nbsp;metre** (50&nbsp;cm or 500&nbsp;mm). The current spacing is listed in the **Display Properties** panel along with the cursor coordinates. When editing a point you can drag it with the left mouse button and the marker follows the cursor until the button is released. When you hover over a marker or drag a point, the cursor becomes a blue crosshair to indicate the point is editable.
The axes rest slightly inside the canvas so the origin is about 20&nbsp;px from the top and sides and 40&nbsp;px from the bottom. This keeps the x‑axis visible above the bottom bar while still filling the drawing area.
 The **Display** tab controls the visibility of measurements. **Show Measurements** toggles all arrows and their table while the tape-measure tool starts drawing mode. Click once on the canvas to begin an arrow, move the mouse to see the distance and index numbers, then click again to fix it in place. The table lists each arrow with its distance, start and end coordinates and the vertex indexes if snapped. Every row provides a colour picker and a **Remove** button that confirms before deleting the row. Arrowheads turn black while being dragged and follow the cursor until released. Use **Clear All** to delete every measurement; a confirmation prompt prevents accidental clearing. Distances show three decimals in metres, one in centimetres and none in millimetres. Measurements are stored in millimetres alongside the channel points so resizing the canvas or switching units doesn't alter their real-world length.

 You can also set the real-world size represented by the canvas. The **Display** tab provides *Canvas Width* and *Canvas Height* inputs (default 4000&nbsp;mm wide by 3000&nbsp;mm high). These values define how many millimetres span the canvas and are saved with each shape so it reloads at the same scale. **Changing the canvas size does not modify the channel geometry or its total area**&mdash;only editing the points alters the shape itself. A **Shape Scale** field in the **Setup** dialog lets you enlarge or shrink the polygon about the bottom left. If scaling makes the shape exceed the canvas, the canvas size automatically expands to the next 500&nbsp;mm step up to a limit of 20&nbsp;m. The grid spacing remains fixed at 500&nbsp;mm (0.5&nbsp;m) regardless of the units so switching display units does not resize the grid. The current spacing appears in the **Display** tab. A zoom slider along the bottom border controls the magnification, replacing the old buttons on the canvas.

Resizing the browser window keeps the same drawing scale. The canvas width and height values update automatically so the channel remains the same size on screen. A 20 px margin surrounds the top and sides with a 40 px margin at the bottom so points near the borders are easier to edit.

