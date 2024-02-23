# from flask import Flask, request, render_template, redirect, url_for, send_from_directory

# app = Flask(__name__)

# app.config['IMAGE_DIRECTORY'] = 'E:/python/images'

# @app.route('/')
# def index():
#     return render_template('home.html')

# @app.route('/display_image', methods=['POST'])
# def display_image():
#     if request.method == 'POST':
#         image_url = request.form['image_url']
#         # Assuming you have validated the URL here
#         return redirect(url_for('show_image', filename=image_url))
#     return redirect(url_for('index'))

# @app.route('/show_image/<filename>')
# def show_image(filename):
#     # For security reasons, you should validate the filename to ensure it's safe
#     return render_template('next_page.html', image_url=url_for('uploaded_image', filename=filename))

# @app.route('/uploads/<filename>')
# def uploaded_image(filename):
#     return send_from_directory(app.config['IMAGE_DIRECTORY'], filename)

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/display_image', methods=['POST'])
def display_image():
    if 'image_file' in request.files:
        image_file = request.files['image_file']
        if image_file.filename != '':
            filename = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
            image_file.save(filename)
            return redirect(url_for('show_image', filename=image_file.filename))
    return redirect(url_for('index'))

@app.route('/show_image/<filename>')
def show_image(filename):
    return render_template('next_page.html', image_url=url_for('uploaded_image', filename=filename))

@app.route('/uploads/<filename>')
def uploaded_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
