import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static\\uploads')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		x_red = request.form['x_red']
		y_red = request.form['y_red']
		print(file)
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		os.system("python script.py "+filename)
		filepath = (os.path.join('static\\uploads', filename))
		return render_template('upload_complete.html', file=filepath, xred=x_red, yred =y_red)
	return render_template('error.html')

@app.route("/")
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)