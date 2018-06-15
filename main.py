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
		if option == "mask":
			#Mask case
			file = request.files['file']
			file2 = request.files['file2']

			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			filepath = (os.path.join('static/uploads', filename))
			filename2 = secure_filename(file2.filename)
			file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))
			filepath2 = (os.path.join('static/uploads', filename2))
			reader = os.system("python script.py "+option+" "+filename+" "+filename2)
			option = "Masque"
			filename_1, file_extension = filename.split(".")
			filename_1 += ".png"
			return render_template('upload_complete.html', file=filename_1, xred="", yred ="", operation= option, file2=filename2)

		elif option == "resize":
			#Resize case
			file = request.files['file']
			new_x = request.form['x_red']
			new_y = request.form['y_red']

			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			filepath = (os.path.join('static/uploads', filename))
			reader = os.system("python script.py "+option+" "+filename+" "+new_x+" "+new_y)
			option = "Resize"
			filename_1, file_extension = filename.split(".")
			filename_1 += ".png"
			return render_template('upload_complete.html', file=filename_1, xred=new_x, yred =new_y, operation= option, file2="")

		elif option == "accent":
			file = request.files['file']
			file2 = request.files['file2']
			new_x = request.form['x_red']
			new_y = request.form['y_red']

			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			filepath = (os.path.join('static/uploads', filename))
			filename2 = secure_filename(file2.filename)
			file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))
			filepath2 = (os.path.join('static/uploads', filename2))
			reader = os.system("python script.py "+option+" "+ filename+" "+filename2+" "+new_x+" "+new_y)
			option = "Accentuation"
			filename_1, file_extension = filename.split(".")
			return render_template('upload_complete.html', file=filename_1, xred=new_x, yred =new_y, operation= option, file2=filename2)
	return render_template('error.html')


@app.route("/")	
def index():
	return render_template('index.html')

@app.route("/index.html")	
def index2():
	return redirect("/")

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == '__main__':
	app.run(debug=True)