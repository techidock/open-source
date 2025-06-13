from flask import Flask, render_template, request
import math

app = Flask(__name__)

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
        elif shape == 'river':
            width = float(request.form.get('width', 0))
            depth = float(request.form.get('depth', 0))
            area = width * depth
        elif shape == 'vduct':
            base = float(request.form.get('base', 0))
            depth = float(request.form.get('depth', 0))
            area = 0.5 * base * depth
    else:
        units = 'm'
    return render_template('index.html', area=area, shape=shape, units=units)

if __name__ == '__main__':
    app.run(debug=True)
