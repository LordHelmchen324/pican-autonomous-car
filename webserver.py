from flask import Flask, render_template, request
app = Flask(__name__)

from car import Car
pican = Car()

@app.route('/')
def root():
    return render_template('pican_main.html')

@app.route('/keydown/<key>', methods=['POST'])
def keydown(key):
    if key == 'a':
        pican.left()
    elif key == 'd':
        pican.right()
    elif key == 'w':
        pican.forwards()
    elif key == 's':
        pican.backwards()
    return ('', 204)

@app.route('/keyup/<key>', methods=['POST'])
def keyup(key):
    if key == 'a':
        pican.straight()
    elif key == 'd':
        pican.straight()
    elif key == 'w':
        pican.stop()
    elif key == 's':
        pican.stop()
    return ('', 204)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
