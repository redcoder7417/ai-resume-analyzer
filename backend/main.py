from fastapi import FastAPI
from routes.resume_routes import router as resume_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(resume_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def root():
    return {"message": "AI Resume Analyzer Running"}