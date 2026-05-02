from services.parser import parse_resume
from services.matcher import match_resume
from services.ai_agent import generate_suggestions


def run_agent(resume_text, job_description, user_goal=None):
    # Step 1: Parse resume
    parsed = parse_resume(resume_text)

    # Step 2: Match score
    match = match_resume(resume_text, job_description)

    # Step 3: AI suggestions
    suggestions = generate_suggestions(resume_text, job_description)

    # Step 4: Build structured response
    response = {
        "goal": user_goal,
        "candidate_name": parsed.get("name"),
        "skills": parsed.get("skills"),
        "match_score": match.get("match_score"),
        "analysis": {
            "strengths": parsed.get("skills"),
            "improvements": suggestions
        }
    }

    return response