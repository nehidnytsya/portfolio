from flask import Flask
from flask import request
from flask import render_template
from flask import abort, redirect, url_for, make_response
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
 return app.send_static_file('about.html')
@app.route('/contact')
def contact():
 return app.send_static_file('contact.html')
@app.route('/gallery')
def gallery():
 return render_template('gallery.html')
if __name__ == '__main__':
    app.run(debug=True)