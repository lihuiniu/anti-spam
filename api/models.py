from pydantic import BaseModel

class SpamRequest(BaseModel):
    text: str

class SpamResponse(BaseModel):
    text: str
    ml_result: bool
    llm_result: bool
