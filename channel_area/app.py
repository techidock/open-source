from flask import Flask, render_template, request, jsonify
import os
import json

app = Flask(__name__)
SHAPE_DIR = os.path.join(os.path.dirname(__file__), 'shapes')
os.makedirs(SHAPE_DIR, exist_ok=True)

@app.route('/', methods=['GET'])
def index():
    """Serve the main page."""
    return render_template('index.html')


@app.route('/save_shape', methods=['POST'])
def save_shape():
    data = request.get_json(force=True)
    name = data.get('name')
    points = data.get('points', [])
    silt_height = data.get('siltHeight', 0)
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
        json.dump({'points': points, 'siltHeight': silt_height}, f)
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
    files = [f[:-5] for f in os.listdir(SHAPE_DIR) if f.endswith('.json') and not f.startswith('_last')]
    return jsonify({'shapes': files})

if __name__ == '__main__':
    app.run(debug=True)
