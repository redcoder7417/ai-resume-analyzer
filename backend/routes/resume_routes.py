from fastapi import APIRouter, UploadFile, File, Form
from utils.file_handler import extract_text
from services.parser import parse_resume
from services.matcher import match_resume
from services.ai_agent import generate_suggestions
from services.agent import run_agent
from config.db import resumes_collection
from services.chat_agent import chat_with_agent
from fastapi import UploadFile, File, Form
from services.job_recommender import recommend_jobs

router = APIRouter()


@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...), user_id: str = Form(...)):
    text = extract_text(file)
    parsed_data = parse_resume(text)

    # store in DB
    resumes_collection.insert_one({
        "user_id": user_id,
        "filename": file.filename,
        "parsed_data": parsed_data,
        "text": text
    })

    return {
        "message": "Resume stored successfully",
        "parsed_data": parsed_data
    }


@router.post("/match")
async def match(file: UploadFile = File(...), job_description: str = Form(...)):
    resume_text = extract_text(file)
    result = match_resume(resume_text, job_description)

    return result


@router.post("/suggest")
async def suggest(file: UploadFile = File(...), job_description: str = Form(...)):
    resume_text = extract_text(file)

    suggestions = generate_suggestions(resume_text, job_description)

    return {
        "suggestions": suggestions
    }
    
    
    
@router.post("/agent")
async def agent(
    file: UploadFile = File(...),
    job_description: str = Form(...),
    user_goal: str = Form(None)
):
    resume_text = extract_text(file)

    result = run_agent(resume_text, job_description, user_goal)

    return result


@router.post("/chat")
async def chat(
    user_id: str = Form(...),
    message: str = Form(...),
    job_description: str = Form(None),
    file: UploadFile = File(None)
):
    resume_text = ""

    if file:
        resume_text = extract_text(file)

    response = chat_with_agent(user_id, message, resume_text, job_description)

    return {
        "reply": response
    }

@router.post("/recommend-jobs")
async def recommend_jobs_api(file: UploadFile = File(...)):
    resume_text = extract_text(file)

    jobs = recommend_jobs(resume_text)

    return {
        "recommended_jobs": jobs
    }
