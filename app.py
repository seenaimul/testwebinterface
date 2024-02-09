# app.py
from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import os
import cv2

app = Flask(__name__)

# Folder to store uploaded images
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the 'uploads' directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# ... (rest of your code remains the same)


# Route to handle image upload
@app.route('/upload', methods=['POST'])
def upload():
    if 'files[]' not in request.files:
        return 'No file part'

    files = request.files.getlist('files[]')

    # Save each uploaded file
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    return redirect(url_for('index'))

# Helper function to check if the file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png'}

# Route to handle ROI selection for a specific image
@app.route('/select_roi/<image_name>', methods=['GET'])
def select_roi(image_name):
    # Get the path to the uploaded image
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_name)

    # Load the reference image
    image = cv2.imread(image_path)

    # Select ROI using cv2.selectROI()
    roi = cv2.selectROI(image)

    # Crop the selected ROI from the image
    roi_cropped = image[int(roi[1]):int(roi[1] + roi[3]), int(roi[0]):int(roi[0] + roi[2])]

    # Save the cropped ROI as a new image
    roi_filename = f"roi_{image_name}"
    roi_path = os.path.join(app.config['UPLOAD_FOLDER'], roi_filename)
    cv2.imwrite(roi_path, roi_cropped)

    # Get ROI coordinates
    roi_coordinates = {
        'x': int(roi[0]),
        'y': int(roi[1]),
        'width': int(roi[2]),
        'height': int(roi[3])
    }

    return jsonify(roi_coordinates)

# Other routes and logic...

@app.route('/')
def index():
    # Ensure the 'uploads' directory exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Get the list of uploaded images in the 'uploads' folder
    uploaded_images = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if allowed_file(f)]

    return render_template('index.html', uploaded_images=uploaded_images)

# Other routes and logic...

if __name__ == '__main__':
    app.run(debug=True)
