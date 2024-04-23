from flask import Flask, render_template, redirect, request, url_for, flash, send_file

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very secret key'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')


if __name__ == '__main__':
    app.run(port=5001, host='127.0.0.1', debug=True)
