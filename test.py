import os
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=['POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		new_x = request.form['x_red']
		new_y = request.form['y_red']
		option = request.form['operation']

		if(option == 'mask'):
			#Cas mask
			option = "Masque"
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			filepath = (os.path.join('static/uploads', filename))
			file2 = request.files['file2']
			filename2 = secure_filename(file2.filename)
			file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))
			filepath2 = (os.path.join('static/uploads', filename2))
			#os.system("python script.py "+filename +" "+new_x +" "+ new_y)
			return render_template('upload_complete.html', file=filename, xred=new_x, yred =new_y, operation= option, file2=filename2)
		else:
			#Cas resize
			option = "Resize"
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			filepath = (os.path.join('static/uploads', filename))
			#os.system("python script.py "+filename +" "+new_x +" "+ new_y)
			return render_template('upload_complete.html', file=filename, xred=new_x, yred =new_y, operation= option, file2="")
	return render_template('error.html')

@app.route("/")	
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)