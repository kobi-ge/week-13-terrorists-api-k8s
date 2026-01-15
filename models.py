from pydantic import BaseModel, Field, ValidationError

class Terrorist(BaseModel):
    name: str
    danger_rate: int 
    location: str





