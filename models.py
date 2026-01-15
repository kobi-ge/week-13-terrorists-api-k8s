from pydantic import BaseModel, Field, ValidationError

class Terrorist(BaseModel):
    name: str
    location: str
    danger_rate: int 
    model_config = {'extra': 'ignore'}


