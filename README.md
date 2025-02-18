# adey-fraud-detection-system
   Real-Time Fraud Detection for E-commerce and Banking

A machine learning pipeline for detecting fraudulent transactions, featuring geolocation analysis, model explainability (SHAP/LIME), Flask/Docker deployment, and a Dash dashboard.

##  Overview
This project addresses fraud detection in two domains:
1. **E-commerce Transactions** (`Fraud_Data.csv`): Analyzes user behavior, device/IP data, and transaction patterns.
2. **Bank Credit Transactions** (`creditcard.csv`): Uses anonymized PCA features for fraud prediction.

Key components:
- Data preprocessing & geolocation mapping
- ML/DL model training (Logistic Regression, Random Forest, LSTM, etc.)
- Model explainability with SHAP and LIME
- Real-time API using Flask and Docker
- Interactive dashboard with Dash

##  Features
- **Geolocation Analysis**: Maps IP addresses to countries for fraud pattern detection.
- **Multiple Models**: Traditional ML and deep learning (CNN, RNN, LSTM) implementations.
- **MLOps Pipeline**: Experiment tracking with MLflow, Dockerized deployment.
- **Explainability**: SHAP summary plots and LIME explanations for model transparency.
- **Real-Time API**: Flask endpoints for fraud prediction.
- **Dashboard**: Visualizes fraud trends, geolocation hotspots, and device/browser analysis.

