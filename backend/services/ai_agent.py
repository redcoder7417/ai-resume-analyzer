import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"


def generate_suggestions(resume_text, job_description):
    prompt = f"""
    You are an expert career coach.

    Analyze this resume and job description.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Give:
    1. Missing skills
    2. Improvements
    3. Better rewritten experience
    """

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(
            f"{URL}?key={API_KEY}",
            headers=headers,
            json=data
        )

        result = response.json()

        return result["candidates"][0]["content"]["parts"][0]["text"]

    except Exception as e:
        return f"Error: {str(e)}"