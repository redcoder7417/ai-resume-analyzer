from sentence_transformers import SentenceTransformer, util

# load model once (important for performance)
model = SentenceTransformer('all-MiniLM-L6-v2')


def calculate_similarity(resume_text, job_description):
    emb1 = model.encode(resume_text, convert_to_tensor=True)
    emb2 = model.encode(job_description, convert_to_tensor=True)

    score = util.cos_sim(emb1, emb2)

    return float(score[0][0])


def match_resume(resume_text, job_description):
    similarity_score = calculate_similarity(resume_text, job_description)

    return {
        "match_score": round(similarity_score * 100, 2)
    }