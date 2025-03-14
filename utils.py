import PyPDF2
import docx
from io import BytesIO
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_from_file(uploaded_file):
    file_name = uploaded_file.name.lower()
    if file_name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)
    elif file_name.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)
    else:
        return ""

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_docx(file):
    doc = docx.Document(BytesIO(file.read()))
    return "\n".join([para.text for para in doc.paragraphs])

def match_resume_to_job(resume_text, job_description):
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume_text, job_description])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    score_percent = round(score * 100, 2)

    feedback = "Great alignment!" if score_percent >= 70 else "Good start, but you can improve alignment by including more relevant skills and experiences."

    return score_percent, feedback
