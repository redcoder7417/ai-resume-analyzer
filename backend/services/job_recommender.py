from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

# predefined job roles (we can expand later)
JOB_ROLES = [
    "Backend Developer",
    "Frontend Developer",
    "Full Stack Developer",
    "Data Scientist",
    "Machine Learning Engineer",
    "AI Engineer",
    "Software Engineer",
    "DevOps Engineer"
]


def recommend_jobs(resume_text):
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)

    results = []

    for job in JOB_ROLES:
        job_embedding = model.encode(job, convert_to_tensor=True)
        score = util.cos_sim(resume_embedding, job_embedding)

        results.append({
            "job_role": job,
            "score": round(float(score[0][0]) * 100, 2)
        })

    # sort by score
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return results