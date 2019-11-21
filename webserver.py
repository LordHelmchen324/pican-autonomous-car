from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('pican_main.html')

@app.route('/keydown/<key>', methods=['POST'])
def keydown(key):
    print('DATA: {}'.format(key))
    return ('', 204)

@app.route('/keyup/<key>', methods=['POST'])
def keyup(key):
    print('DATA: {}'.format(key))
    return ('', 204)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
