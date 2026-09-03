Machine Learning Classification Project

📌 Project Overview

This project is a Machine Learning classification project built using Python and Scikit-learn.

The project analyzes the given dataset, performs data preprocessing and exploratory data analysis, trains classification models, evaluates their performance, and deploys the best-performing model using a Flask web application.

🚀 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Flask
- Pickle
- Jupyter Notebook

📊 Machine Learning Workflow

1. Dataset Loading
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature and Target Selection
5. Data Preprocessing
6. Model Training
7. Logistic Regression
8. Decision Tree Classifier
9. Model Evaluation
10. Model Comparison
11. Best Model Selection
12. Model Saving using Pickle
13. Flask Web Application

🤖 Models Used

Logistic Regression

Used as the baseline classification model.

Decision Tree Classifier

Used to capture non-linear relationships in the dataset.

The models were compared using:

- Accuracy
- Precision
- Recall
- F1 Score

The model with the best F1 Score was selected as the final model.

🔢 Input Features

The application uses the following 10 features:

- Flength
- Fwidth
- Fsize
- Fconc
- Fconc1
- Fasym
- Fm3long
- Fm3trans
- Falpha
- Fdist

🌐 Flask Web Application

A Flask-based web application was created to allow users to enter the feature values and receive a machine learning prediction.

Run the Application

Install the required libraries:

pip install pandas numpy matplotlib seaborn scikit-learn flask

Run the Flask application:

python app.py

Open the application in your browser:

http://127.0.0.1:5000

📁 Project Structure

Machine-Learning-Project/
│
├── app.py
├── best_model.pkl
├── README.md
├── templates/
│   └── index.html
│
└── notebook/
    └── ML_Project.ipynb

📈 Model Evaluation

The trained models were evaluated using:

Accuracy: Overall percentage of correct predictions.

Precision: Measures how many predicted positive cases were actually positive.

Recall: Measures how many actual positive cases were correctly identified.

F1 Score: Harmonic mean of Precision and Recall.

🎯 Project Objective

The main objective of this project is to build an end-to-end Machine Learning classification system, from data preprocessing and model training to model deployment using Flask.

👨‍💻 Author

Yusufvali

⭐ Conclusion

This project demonstrates a complete Machine Learning workflow including data preprocessing, exploratory data analysis, classification model development, evaluation, model selection, and deployment using Flask.