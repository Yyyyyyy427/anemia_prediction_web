# Anemia Prediction Web

This is a Flask-based web application for predicting anemia using a trained machine learning model.

## Features
- Predict anemia status using a trained TensorFlow model (`anemia_model.h5`).
- Easy-to-use web interface for image upload and prediction.
- RESTful API endpoint (`/predict`) for programmatic access.

## Folder Structure
anemia_prediction_web/ ├── app.py # Main Flask application ├── generate_model.py # Script to generate and train the machine learning model ├── anemia_model_files/ # Folder containing the trained model │ └── anemia_model.h5 # Pre-trained model file ├── requirements.txt # Python dependencies

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git (for cloning the repository)

### Clone the Repository
```bash
git clone https://github.com/Yyyyyyy427/anemia_prediction_web.git
cd anemia_prediction_web
Install Dependencies
Use pip to install all required dependencies:

bash
pip install -r requirements.txt
Running the Application
Start the Flask server:
python app.py
Open your browser and navigate to:
http://127.0.0.1:5000/
Use the /predict endpoint for predictions:

Upload an image via the web interface.
Or use a tool like Postman or curl to send a POST request.
API Usage
Endpoint: /predict
Method: POST

Description: Accepts an image file for anemia prediction.

Request:

image (form-data): Upload an image for prediction.
Response:
{
  "result": "Anemic"  // or "Not Anemic"
}
Example using curl:
curl -X POST -F "image=@path_to_image.jpg" http://127.0.0.1:5000/predict
Deployment
You can deploy this project on platforms like Render.

Steps to Deploy on Render
Push your repository to GitHub.
Connect your GitHub repository to Render.
Use the following build and start commands:
Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app
Access your web service at the provided Render URL.
Credits
Developed by: Yyyyyyy427
Model Training: TensorFlow and Keras
License
This project is licensed under the MIT License. See the LICENSE file for details.
