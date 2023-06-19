from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
from markupsafe import escape

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == 'POST':
        files = request.files.getlist('file')
        for file in files:
            file = escape(file.filename)
            with Image.open(file) as f:
                f.save(app.root_path + '/iconos/' + file.split('.')[0] + "ICO.ico", format="ICO")
    return redirect(url_for('index'))
