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
    else if key == 'd':
        pican.right()
    else if key == 'w':
        pican.forward()
    else if key == 's':
        pican.backward()
    return ('', 204)

@app.route('/keyup/<key>', methods=['POST'])
def keyup(key):
    if key == 'a':
        pican.straight()
    else if key == 'd':
        pican.straight()
    else if key == 'w':
        pican.stop()
    else if key == 's':
        pican.stop()
    return ('', 204)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
