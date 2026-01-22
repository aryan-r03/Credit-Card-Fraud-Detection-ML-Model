# Setup Guide - Fraud Detection Application

## Step-by-Step Installation Guide

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Web browser

---

## File Organization

Your project should be organized exactly as follows:

```
fraud_detection_app/
│
├── app.py                          # Main Flask application (run this file)
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── .gitignore                      # Git ignore rules
│
├── config/                         # Configuration package
│   ├── __init__.py                # Makes config a Python package
│   └── config.py                  # Application settings and constants
│
├── models/                         # Machine learning models package
│   ├── __init__.py                # Makes models a Python package
│   └── fraud_detector.py          # FraudDetector class with ML logic
│
├── utils/                          # Utility functions package
│   ├── __init__.py                # Makes utils a Python package
│   └── data_generator.py          # Sample data generation
│
├── templates/                      # HTML templates (Flask requirement)
│   └── index.html                 # Main web page
│
└── static/                         # Static files (Flask requirement)
    ├── css/
    │   └── style.css              # Stylesheet
    └── js/
        └── app.js                 # Frontend JavaScript
```

---

## Installation Steps

### 1. Create Project Directory

```bash
# Create main directory
mkdir fraud_detection_app
cd fraud_detection_app
```

### 2. Create All Subdirectories

```bash
# On Windows (Command Prompt)
mkdir config models utils templates static\css static\js

# On macOS/Linux (Terminal)
mkdir -p config models utils templates static/css static/js
```

### 3. Create All Files

Create each file in its proper location as shown in the file structure above. 

**Important:** Make sure to create the `__init__.py` files in:
- `config/`
- `models/`
- `utils/`

These files make Python treat the directories as packages.

### 4. Create Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt after activation.

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- Flask-CORS (cross-origin resource sharing)
- pandas (data manipulation)
- numpy (numerical computing)
- scikit-learn (machine learning)

---

## Running the Application

### First Time Setup

1. **Navigate to project directory:**
   ```bash
   cd fraud_detection_app
   ```

2. **Activate virtual environment:**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

### What Happens on First Run

1. The system checks for a saved model file (`fraud_model.pkl`)
2. If not found, it checks for `creditcard.csv`
3. If the dataset is not found, it generates sample data
4. The model is trained and saved
5. The web server starts

### Expected Output

```
CREDIT CARD FRAUD DETECTION

⚠️  'creditcard.csv' not found!
Creating sample dataset...

Dataset:
  Fraudulent: 50 (1.00%)
  Legitimate: 4,950 (99.00%)

Training on 4,000 samples...

Results:
  Accuracy:  99.40%
  Precision: 60.00%
  Recall:    30.00%
  F1 Score:  40.00%

✓ Model saved!
============================================================

============================================================
CREDIT CARD FRAUD DETECTION SYSTEM
============================================================

🚀 Starting server...
📱 Open: http://127.0.0.1:5000

💡 Dataset: creditcard.csv
   Download: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

============================================================
```

---

## Accessing the Application

1. Open your web browser
2. Navigate to: `http://127.0.0.1:5000`
3. You should see the fraud detection interface

---

## Testing the Application

### Quick Test

1. Click "Load Fraud Example" - Should predict FRAUD
2. Click "Load Legit Example" - Should predict LEGITIMATE
3. Click "Clear Form" to reset

### Manual Test

1. Enter values for Time and Amount
2. (Optional) Expand "Advanced Features" to enter V1-V28 values
3. Click "Analyze Transaction"
4. View the prediction results

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution:** Activate virtual environment and install dependencies
```bash
# Activate venv first
pip install -r requirements.txt
```

### Issue: "ModuleNotFoundError: No module named 'config'"
**Solution:** Make sure you're running from the project root and `__init__.py` files exist
```bash
# Check you're in the right directory
pwd  # Should show .../fraud_detection_app

# Verify __init__.py files exist
ls config/__init__.py
ls models/__init__.py
ls utils/__init__.py
```

### Issue: Port 5000 already in use
**Solution:** Change port in `config/config.py`
```python
PORT = 5001  # Or any available port
```

### Issue: Template not found
**Solution:** Ensure `templates/` directory exists in project root with `index.html`

### Issue: Static files not loading (no styling)
**Solution:** Ensure `static/css/style.css` and `static/js/app.js` exist

---

## Optional: Using Real Dataset

For production-quality results:

1. Download from Kaggle: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
2. Place `creditcard.csv` in the project root directory
3. Delete `fraud_model.pkl` (if it exists)
4. Restart the application - it will retrain with real data

---

## Stopping the Application

Press `Ctrl+C` in the terminal to stop the Flask server.

---

## Deactivating Virtual Environment

```bash
deactivate
```

---

## Next Steps

- Customize settings in `config/config.py`
- Modify styling in `static/css/style.css`
- Enhance frontend in `static/js/app.js`
- Add new features to the model in `models/fraud_detector.py`

---

## File Sequence Summary

**Create in this order:**

1. **Root level:**
   - `requirements.txt`
   - `.gitignore`
   - `README.md`

2. **Config package:**
   - `config/__init__.py`
   - `config/config.py`

3. **Utils package:**
   - `utils/__init__.py`
   - `utils/data_generator.py`

4. **Models package:**
   - `models/__init__.py`
   - `models/fraud_detector.py`

5. **Templates:**
   - `templates/index.html`

6. **Static files:**
   - `static/css/style.css`
   - `static/js/app.js`

7. **Main application:**
   - `app.py` (run this to start the server)
