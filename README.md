# Edge Detector openCV Flask

## Description
This project is a web application built with Flask that takes image input from the user, detects edges in the image, and overlays the edges on the original image, and converts it into JSON format.

OpenCV edge detection has been used for edge detection.

## Features

Upload an image file.
Apply edge detection using openCV.
Download the JSON serialized file of processed image with highlighted edges.

## Requirements

    Python 3.11.5
    Flask
    OpenCV

Check requirements.txt file for rest of the requirements.
    

## Installation:
Open terminal, and go to your destination directory.

    cd path/to/the/folder

Replace path/to/the/folder with your directory path e.g ~/Projects/edge

Clone this git by copying the following in your terminal.

    git clone https://github.com/sibtain-wahab/edge_detection_on_images.git

Create a virtual environment in conda

    conda create -n edge_env python=3.11
    
Replace edge_env with your custom virtual envname. Python 3.11 is required.

Check if pip is installed.

    pip --version
    
Install the required libraries:

    pip install -r requirements.txt

## Running the application

Navigate to the project directory in your terminal.
Run the following command:

    flask_app.py
    
This will start the Flask development server and the application should be accessible at http://localhost:3000/ by default (port might vary if you change the code at app.run(port = 3000)).

## Usage

Open the application in your web browser.
    
    http://localhost:3000
    
For edge detection functionality, go to:

    http://localhost:3000/edge 
    
Click "Choose File" and select an image from your local machine. Supported formats include common image types (JPG, PNG etc.).
Click "Upload Image". The edge detection algorithm will be applied to your image.
Click "Download" to save the JSON file of the processed image with edges highlighted.

Note: You can customize the edge detection algorithm used in the code by modifying the edge_detector function in edge_new.py script.

## Contributing

Feel free to fork this repository and contribute to improve the application.

## Contact

For any questions or feedback, feel free to reach out to me at linkedin.com/in/sibtain-wahab
