# 🤖 Resume Classifier & Semantic Resume Matching

A machine learning application that analyzes PDF resumes, predicts the most suitable job-role category, and performs relevance matching between resumes and job requirements.

The project combines **NLP, TF-IDF, XGBoost, Sentence Transformers, cosine similarity, and keyword-based matching** with a Streamlit interface.

## 🚀 Features

* Extracts resume text from PDF files using **PyMuPDF**
* Performs NLP preprocessing including:

  * Lowercasing
  * Punctuation removal
  * Digit removal
  * Stopword removal
  * Lemmatization
* Classifies resumes into **24 job-role categories**
* Uses **TF-IDF** for textual feature representation
* Evaluates multiple machine learning models including:

  * Multinomial Naive Bayes
  * Random Forest
  * XGBoost
* Performs **semantic resume-job matching** using Sentence Transformer embeddings
* Calculates **cosine similarity** to measure resume-job relevance
* Performs **keyword-based relevance matching**
* Ranks resumes based on semantic and keyword relevance
* Provides a Streamlit web interface for resume classification
* Supports local experimentation through Jupyter notebooks

## 🛠️ Tech Stack

### Machine Learning & NLP

* Python
* Scikit-learn
* XGBoost
* NLTK
* TF-IDF
* Sentence Transformers
* Cosine Similarity

### Data & Visualization

* Pandas
* NumPy
* Matplotlib
* Seaborn

### Application

* Streamlit
* PyMuPDF
* Joblib

## 📁 Project Structure

```text
RESUME-CLASSIFIER-WITH-XGBOOST/
│
├── app/
│   └── app.py
│
├── DATA/
│   ├── Resume.csv
│   ├── extractor.py
│   ├── combined_resume_ranking.csv
│   ├── embedding_resume_ranking.csv
│   └── keyword_resume_ranking.csv
│
├── Models/
│   ├── tf_object.pkl
│   ├── idf_object.pkl
│   └── xgboost_model.pkl
│
├── Notebooks/
│   ├── Resume_Classifier.ipynb
│   └── Resume_Matching_and_Embedding_Ranking.ipynb
│
├── requirements.txt
└── README.md
```

## 🧠 Machine Learning Pipeline

### Resume Classification

```text
PDF Resume
    ↓
PyMuPDF
    ↓
Text Extraction
    ↓
NLP Preprocessing
    ↓
TF-IDF
    ↓
XGBoost
    ↓
Predicted Job Role
```

The classifier was trained using resume text represented through TF-IDF features.

### Resume Matching & Relevance Ranking

A separate matching pipeline uses dense semantic embeddings:

```text
Resume
   ↓
Sentence Transformer
   ↓
Resume Embedding
                 ┐
                 │ Cosine Similarity
                 │
Job Description ─┘
   ↓
Job Embedding
   ↓
Semantic Relevance Score
```

A second keyword-based matching method checks the presence of predefined role-related keywords.

The project therefore supports two complementary relevance signals:

* **Semantic relevance** using embeddings
* **Keyword relevance** using predefined role keywords

These scores can be combined to rank resumes for a job requirement.

## 📊 Model Evaluation

Multiple classification approaches were explored during development:

* Multinomial Naive Bayes
* Random Forest
* XGBoost
* TensorFlow-based neural network

The project reports approximately **79% classification accuracy** for the XGBoost-based classification experiment.

Evaluation includes:

* Accuracy
* Precision
* Recall
* F1-score
* Classification report
* Confusion matrix

## 🎯 Supported Job Categories

The dataset contains 24 categories:

```text
ACCOUNTANT
ADVOCATE
AGRICULTURE
APPAREL
ARTS
AUTOMOBILE
AVIATION
BANKING
BPO
BUSINESS-DEVELOPMENT
CHEF
CONSTRUCTION
CONSULTANT
DESIGNER
DIGITAL-MEDIA
ENGINEERING
FINANCE
FITNESS
HEALTHCARE
HR
INFORMATION-TECHNOLOGY
PUBLIC-RELATIONS
SALES
TEACHER
```

## 🌐 Streamlit Application

The Streamlit application allows a user to:

1. Upload a PDF resume
2. Extract its text
3. View the processed text
4. Predict the most suitable job role
5. View role-specific keyword suggestions
6. Enter a job description for relevance matching
7. View semantic and keyword-based relevance scores

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/shaurya174/RESUME-CLASSIFIER-WITH-XGBOOST.git
cd RESUME-CLASSIFIER-WITH-XGBOOST
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app/app.py
```

Then open the local URL shown by Streamlit in your browser.

## 📓 Notebooks

### `Resume_Classifier.ipynb`

Contains the original:

* Dataset analysis
* PDF text extraction
* NLP preprocessing
* EDA
* TF-IDF feature extraction
* Model experimentation
* Classification evaluation
* Role-based similarity analysis

### `Resume_Matching_and_Embedding_Ranking.ipynb`

Adds:

* Sentence Transformer embeddings
* Semantic resume-job similarity
* Cosine similarity scoring
* Keyword-based relevance scoring
* Candidate ranking
* Combined relevance scoring

## 📌 Notes

* Resume input should be in **PDF format** for the Streamlit application.
* The classifier and matching system are separate components.
* TF-IDF + XGBoost is used for **job-role classification**.
* Embeddings + cosine similarity are used for **semantic resume-job matching**.
* Keyword matching provides an additional relevance signal.
* The embedding-based matching component requires the Sentence Transformers dependency and model availability.

## 🌐 Deployment

The Streamlit application is deployed at:

https://resume-classifier-with-xgboost-fuaelejvgoczklbrebeqhs.streamlit.app/

## 📄 License

This project is open source and available under the MIT License.

