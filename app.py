from flask import Flask, render_template
from livereload import Server

# livereload-2.4.0

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    # return "cc"
    return render_template('mm.html')

@app.route('/bart')
def use_jinja():
    return render_template('mm.html')



if __name__ == '__main__':
    # server = Server(app.wsgi_app)
    # server.serve(port=5000)
    app.run()
  