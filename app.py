"""
Fraud Detection Web Application
Flask backend for credit card fraud detection system
"""
import os
import warnings
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

from config import Config
from models import FraudDetector

# Suppress warnings
warnings.filterwarnings('ignore')

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize fraud detector
detector = FraudDetector()

# Load or train model on startup
if os.path.exists(Config.MODEL_PATH):
    try:
        print("Loading saved model...")
        detector.load()
        print("✓ Model loaded!\n")
    except Exception as e:
        print(f"Error loading model: {e}")
        print("Retraining model...")
        detector.train()
else:
    print("No saved model found. Training new model...")
    detector.train()


@app.route('/')
def home():
    """Render the main application page"""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """
    API endpoint for fraud prediction
    
    Expected JSON format:
    {
        "features": {
            "Time": 0,
            "Amount": 100.0,
            "V1": 0.0,
            ...
            "V28": 0.0
        }
    }
    
    Returns:
    {
        "success": true,
        "result": {
            "is_fraud": 0,
            "result": "LEGITIMATE",
            "fraud_probability": 5.23,
            "legitimate_probability": 94.77,
            "risk_level": "Low Risk"
        }
    }
    """
    try:
        data = request.get_json()
        features = data.get('features', {})
        
        # Predict using the model
        result = detector.predict(features)
        
        return jsonify({
            'success': True,
            'result': result
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': detector.model is not None
    })


if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("CREDIT CARD FRAUD DETECTION SYSTEM")
    print("=" * 60)
    print("\n🚀 Starting server...")
    print(f"📱 Open: http://{Config.HOST}:{Config.PORT}")
    print("\n💡 Dataset: creditcard.csv")
    print("   Download: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud")
    print("\n" + "=" * 60 + "\n")
    
    app.run(
        debug=Config.DEBUG,
        host=Config.HOST,
        port=Config.PORT
    )
