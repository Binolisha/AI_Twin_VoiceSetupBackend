from fastapi import APIRouter
from models import VoiceSelection
from services import save_settings, load_settings
from voice_data import VOICES, LANGUAGES
from voice_model import clone_voice_xtts

router = APIRouter()


@router.get("/voices")
def get_all_voices():
    return VOICES



@router.get("/voice/sample/{voice_id}")
def play_sample(voice_id: int):

    for voice in VOICES:

        if voice["id"] == voice_id:

            return {
                "voice": voice["name"],
                "sample_url": voice["sample"]
            }

    return {"error": "Voice not found"}

@router.get("/languages")
def get_languages():
    return LANGUAGES

@router.post("/voice/select")
def select_voice(selection: VoiceSelection):

    # validate voice exists
    voice_exists = any(v["name"] == selection.voice for v in VOICES)

    # validate language exists
    language_exists = any(l["name"] == selection.language for l in LANGUAGES)

    if not voice_exists:
        return {"success": False, "message": "Invalid voice selected"}

    if not language_exists:
        return {"success": False, "message": "Invalid language selected"}

    save_settings(selection.dict())

    return {
        "success": True,
        "message": "Voice and language selected successfully",
        "data": selection
    }


@router.post("/voice/select")
def select_voice(selection: VoiceSelection):

    save_settings(selection.dict())

    return {
        "success": True,
        "message": "Voice selected successfully",
        "data": selection
    }
@router.get("/voice-clone/status")
def clone_status():

    return {
        "premium": False,
        "message": "Upgrade to Premium to use Voice Cloning"
    }

@router.get("/voice/current")
def current_voice():

    return load_settings()

