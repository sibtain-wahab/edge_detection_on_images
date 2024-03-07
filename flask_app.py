import cv2
import os
from tempfile import mkdtemp

from flask import Flask, request, send_file

from edge_new import edge_detector

app = Flask(__name__)


@app.route('/edge', methods=['POST'])
def process_image():
    # Check if image uploaded
    if 'img' not in request.files:
        return "Image not found", 400

    file = request.files['img']

    if file.filename == '':
        return "No image selected", 404

    # Create temp directory and save image

    temp_dir = mkdtemp()
    image = file.filename
    # path = secure_filename(path)
    path = os.path.join(temp_dir, image)
    file.save(path)

    # Call function from custom module edge_new

    processed_image = edge_detector(path)

    # Save the processed image
    output_path = os.path.join(temp_dir, 'processed_img.jpg')
    cv2.imwrite(output_path, processed_image)

    return send_file(output_path, mimetype='image/jpeg', as_attachment=True, download_name='processed_img.jpg')


@app.route('/')
def status():
    return "The app is up and running. Go to /edge"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
