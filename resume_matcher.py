from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def match_resumes(job_description, resume_text):
    jd_embedding = model.encode(job_description, convert_to_tensor=True)
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(jd_embedding, resume_embedding).item()
    return similarity
