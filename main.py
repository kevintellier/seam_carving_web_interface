import os
import sys
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')

filename = ""
filename2 = ""
new_x = 0
new_y = 0
option = ""


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['POST'])
def upload_file():
	if request.method == 'POST':
		option = request.form['operation']
		print(option, file=sys.stderr)

		if option == "mask":
			#Mask case
			option = "Masque"
			file = request.files['file']
			file2 = request.files['file2']

			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			filepath = (os.path.join('static/uploads', filename))
			filename2 = secure_filename(file2.filename)
			file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))
			filepath2 = (os.path.join('static/uploads', filename2))
			reader = os.system("python script.py")
			#print(reader, file=sys.stderr)
			return render_template('upload_complete.html', file=filename, xred="", yred ="", operation= option, file2=filename2)

		elif option == "resize":
			#Resize case
			option = "Resize"
			file = request.files['file']
			new_x = request.form['x_red']
			new_y = request.form['y_red']

			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			filepath = (os.path.join('static/uploads', filename))
			reader = os.system("python script.py "+filename +" resize " + new_x + " " + new_y)
			return render_template('upload_complete.html', file=filename, xred=new_x, yred =new_y, operation= option, file2="")

		elif option == "accent":
			option = "Accentuation"
			file = request.files['file']
			new_x = request.form['x_red']
			new_y = request.form['y_red']

			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			filepath = (os.path.join('static/uploads', filename))
			reader = os.system("python script.py "+filename +" accent " + new_x + " " + new_y)
			return render_template('upload_complete.html', file=filename, xred=new_x, yred =new_y, operation= option, file2="")
	return render_template('error.html')


@app.route("/")	
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)