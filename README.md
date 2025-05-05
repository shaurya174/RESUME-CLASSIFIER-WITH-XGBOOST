# 🤖 Resume Classifier Web App

A machine learning-powered web app that predicts the most suitable job role based on a candidate's resume. Upload a PDF resume, and the app classifies it into roles like HR, IT, Finance, Engineer, etc., and even suggests relevant keywords.

## 🚀 Features

- Extracts and cleans resume text
- Classifies resumes into 20+ job roles
- Suggests keywords relevant to the predicted role
- User-friendly Streamlit web interface

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- XGBoost
- NLTK
- PyMuPDF (PDF text extraction)
- TF-IDF Vectorization

## 📁 Project Structure
📂 Resume-Classifier/
├── app.py # Streamlit web app
├── Models/
│ ├── tf_object.pkl # Fitted TF vectorizer
│ ├── idf_object.pkl # Fitted TF-IDF transformer
│ └── xgboost_model.pkl # Trained XGBoost classifier
├── resume_classifier.ipynb # Jupyter Notebook (EDA + Model training)
├── requirements.txt # Python dependencies
└── README.md # This file
 


## 🧠 Model Training Summary

- Used TF-IDF for feature extraction
- Tested multiple models: Naive Bayes, Random Forest, XGBoost
- Final model: **XGBoost Classifier**
- Achieved **~93% accuracy** on test data

## 🌐 How to Run the App

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/resume-classifier.git
   cd resume-classifier
2. Install Dependancies
    pip install -r requirements.txt
3. Run The Streamlit App
    streamlit run app.py
4. Open your browser and upload a PDF resume to see predictions.

✨ Example Roles
. HR

. Designer

. IT

. Teacher

. Advocate

. Engineer

. Sales

. Consultant

. Chef

. Aviation

And many more...

📌 Notes
1) Resume must be in PDF format
##DEPLOYEMENT

3) Internet not required after model and vectorizer are loaded

4) Works locally and can be deployed to Hugging Face Spaces / Streamlit Cloud

📄 License
This project is open source and available under the MIT License.

##DEPLOYMENT
1)Streamlit Cloud -> https://resume-classifier-with-xgboost-fuaelejvgoczklbrebeqhs.streamlit.app/ 
2) Render -> https://resume-classifier-with-xgboost.onrender.com
