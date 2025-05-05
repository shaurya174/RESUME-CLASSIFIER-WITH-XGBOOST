import streamlit as st
import string
import nltk
import re
import joblib
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('wordnet')
def clean_text1(test_str):
    test_str = test_str.lower()
    ref1_str = ""
    for i in test_str:
        if(i not in string.punctuation):
            ref1_str+=i
    ref2_str = ""
    for j in ref1_str:
        if(j not in string.digits):
            ref2_str+=j
    return ref2_str
banned = nltk.corpus.stopwords.words('english')
def clean_text3(test_str):
    final_lst = []
    myy = re.split(r'\s+',test_str)
    for j in myy:
        if j not in banned:
            final_lst.append(j)
    return ' '.join(final_lst)
def clean_text4(test_str):
    lemmatizer = WordNetLemmatizer()
    words = nltk.word_tokenize(test_str)
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(lemmatized_words)
st.set_page_config(page_title="Resume Classifier", layout="centered")
st.markdown(
    """
    <style>
    /* Make title bold and centered */
    .main h1 {
        text-align: center;
        font-weight: 800;
        color: #2E86C1;
    }

    /* Background color and padding for the main container */
    .reportview-container {
        background-color: #F4F6F7;
        padding: 2rem;
    }

    /* Custom font for the whole app */
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        color: #333333;
    }

    /* Style the file uploader and buttons */
    .stButton>button {
        background-color: #2E86C1;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.5em 1em;
    }

    .stFileUploader {
        border: 2px dashed #2E86C1;
        background-color: #D6EAF8;
        border-radius: 10px;
        padding: 1em;
    }

    /* Style prediction text */
    .prediction {
        background-color: #D1F2EB;
        padding: 1em;
        border-radius: 10px;
        font-weight: bold;
        color: #1A5276;
        margin-top: 1em;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("📄 Resume Classifier App")
st.write("Upload a resume and let the model predict the most suitable job role!")
import joblib

tf_object = joblib.load('Models/tf_object.pkl')
idf_object = joblib.load('Models/idf_object.pkl')
xgb_model = joblib.load('Models/xgboost_model.pkl')
uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])
if uploaded_file is not None:
    import fitz  # PyMuPDF
    
    # Read and extract text
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()

    st.subheader("Extracted Text")
    st.write(text)

    # Now apply your clean_text functions here:
    cleaned_text = clean_text1(text)
    cleaned_text = clean_text3(cleaned_text)
    cleaned_text = clean_text4(cleaned_text)

    st.subheader("Cleaned Text")
    st.write(cleaned_text)
#Vectorize
    resume_tf =  tf_object.transform([cleaned_text])
    resume_tfidf = idf_object.transform(resume_tf)
    predicted_role = xgb_model.predict(resume_tfidf)[0]
    st.subheader("Predicted Job Role")
    st.success(predicted_role)
    role_keywords = {
        'HR': "recruitment employee relations payroll benefits talent acquisition training compliance",
        'DESIGNER': "graphic design photoshop illustrator creativity branding layout typography",
        'INFORMATION-TECHNOLOGY': "software development programming databases networks troubleshooting cybersecurity",
        'TEACHER': "lesson planning classroom management curriculum development student assessment pedagogy",
        'ADVOCATE': "legal advice litigation contracts court representation legal research case management",
        'BUSINESS-DEVELOPMENT': "sales strategy partnerships market expansion lead generation client acquisition",
        'HEALTHCARE': "patient care diagnosis treatment medical terminology clinical support healthcare services",
        'FITNESS': "personal training workout plans nutrition physical health exercise coaching strength",
        'AGRICULTURE': "farming crop production irrigation soil management pest control harvesting",
        'BPO': "call center customer service communication data entry process outsourcing support",
        'SALES': "sales targets customer relationship CRM lead conversion cold calling negotiation",
        'CONSULTANT': "strategy analysis business solutions client management project execution problem solving",
        'DIGITAL-MEDIA': "social media marketing content creation SEO analytics branding engagement",
        'AUTOMOBILE': "vehicle maintenance automotive engineering repair diagnostics manufacturing mechanics",
        'CHEF': "cooking recipes food preparation kitchen management menu planning ingredients",
        'FINANCE': "financial analysis budgeting accounting investment risk management auditing",
        'APPAREL': "fashion clothing textiles garment design merchandising production trends",
        'ENGINEERING': "mechanical electrical civil CAD systems design problem solving development",
        'ACCOUNTANT': "balance sheet taxation auditing bookkeeping financial reporting ledger entries",
        'CONSTRUCTION': "site management blueprints structural engineering safety equipment planning labor",
        'PUBLIC-RELATIONS': "media communication brand image press releases crisis management campaigns",
        'BANKING': "loans credit analysis customer service transactions investment banking regulations",
        'ARTS': "painting sculpture performing arts creativity exhibitions visual storytelling",
        'AVIATION': "flight operations aircraft maintenance aviation safety airport customer service"
    }
# Assuming you have a dictionary called role_keywords
    st.subheader("Suggested Keywords for Role")

# Join keywords into a single comma-separated string
    if predicted_role in role_keywords:
        my_str = role_keywords[predicted_role]
        my_str=my_str.capitalize()
        st.write(my_str)
    else:
        st.write("No keyword suggestions available.")
