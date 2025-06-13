from flask import Flask, render_template, request, jsonify
import math
import os
import json

app = Flask(__name__)
SHAPE_DIR = os.path.join(os.path.dirname(__file__), 'shapes')
os.makedirs(SHAPE_DIR, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    area = None
    shape = None
    if request.method == 'POST':
        shape = request.form.get('shape')
        units = request.form.get('units', 'm')
        if shape == 'circular':
            radius = float(request.form.get('radius', 0))
            area = math.pi * radius ** 2
        elif shape == 'rectangle':
            width = float(request.form.get('width', 0))
            depth = float(request.form.get('depth', 0))
            area = width * depth
    else:
        units = 'm'
    return render_template('index.html', area=area, shape=shape, units=units)


@app.route('/save_shape', methods=['POST'])
def save_shape():
    data = request.get_json(force=True)
    name = data.get('name')
    points = data.get('points', [])
    if not name or not points:
        return jsonify({'status': 'error', 'message': 'invalid data'}), 400
    svg_path = os.path.join(SHAPE_DIR, f'{name}.svg')
    json_path = os.path.join(SHAPE_DIR, f'{name}.json')
    pts = ' '.join(f"{p['x']},{p['y']}" for p in points)
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" '
        'width="500" height="375">'
        f'<polygon points="{pts}" fill="#99ccff" stroke="#000" />'
        '</svg>'
    )
    with open(svg_path, 'w') as f:
        f.write(svg)
    with open(json_path, 'w') as f:
        json.dump({'points': points}, f)
    return jsonify({'status': 'ok'})


@app.route('/load_shape/<name>')
def load_shape(name):
    json_path = os.path.join(SHAPE_DIR, f'{name}.json')
    if not os.path.exists(json_path):
        return jsonify({'status': 'error', 'message': 'not found'}), 404
    with open(json_path) as f:
        data = json.load(f)
    return jsonify(data)


@app.route('/list_shapes')
def list_shapes():
    files = [f[:-5] for f in os.listdir(SHAPE_DIR) if f.endswith('.json')]
    return jsonify({'shapes': files})

if __name__ == '__main__':
    app.run(debug=True)
