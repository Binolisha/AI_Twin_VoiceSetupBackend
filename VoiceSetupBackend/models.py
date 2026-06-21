from pydantic import BaseModel


class VoiceSelection(BaseModel):
    voice: str
    language: str
    
class PremiumUser(BaseModel):
    username: str
    premium: bool
    

