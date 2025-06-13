# Channel Area Web Application

This is a simple Flask-based web application for calculating the cross-sectional area of different water channel shapes:

- **Pipe**: circular cross-section, area = π * radius²
- **River**: rectangular cross-section, area = width * depth
- **V Duct**: triangular cross-section, area = 0.5 * base * depth

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
Use the form to pick a shape and adjust dimensions either by typing or by
dragging on the canvas. The area updates automatically as you change the
shape.
