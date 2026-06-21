import edge_tts
import asyncio
import uuid
import os

VOICE_MAP = {
    "male": "en-US-GuyNeural",
    "female": "en-US-JennyNeural"
}

async def _generate(text, voice, output_path):
    communicate = edge_tts.Communicate(text=text, voice=voice)
    await communicate.save(output_path)

async def clone_voice_xtts(audio_path: str, text: str):

    output_filename = f"{uuid.uuid4()}.wav"
    output_path = os.path.join("cloned", output_filename)

     # default to female voice (you can change later using UI)
    voice = VOICE_MAP["female"]

    await _generate(text, voice, output_path)

    return output_path
