from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import router
from voice_model import clone_voice_xtts
from fastapi import UploadFile, File, Form
from fastapi.responses import FileResponse
import shutil
import uuid
import os

app = FastAPI(title="AI Twin Backend")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

app.include_router(router)

@app.post("/voice-clone")
async def clone_voice(
    audio: UploadFile = File(...),
    text: str = Form(...),
    language: str = Form("English"),
    premium: bool = Form(False)
):
    
    if not premium:
        return {
            "success": False,
            "message": "Voice cloning is available only for Premium users."
        }

    filename = str(uuid.uuid4()) + ".wav"

    upload_path = os.path.join("uploads", filename)

    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)
        
    cloned_file = await clone_voice_xtts(upload_path, text, language)

    return {
        "success": True,
        "message": "Voice uploaded successfully.",
        "uploaded_file": upload_path,
        "generated_audio": cloned_file
    }
