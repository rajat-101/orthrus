import os, glob
import urllib.request
from flask import Flask, Blueprint, current_app, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

upload = Blueprint('upload', __name__)


ALLOWED_EXTENSIONS = set(['sol'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def clear_my_contracts():
	files = glob.glob('Orthrus/dataset/my_contracts/*')
	for f in files:
		os.remove(f)
	
clear_my_contracts()

@upload.route('/upload')
def upload_form():
	return render_template('upload.html')

@upload.route('/upload', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
			flash('File successfully uploaded')
			return redirect('/upload')
		else:
			flash('You can only upload Solidity files')
			return redirect(request.url)
