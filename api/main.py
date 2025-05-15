from fastapi import FastAPI
from api.models import SpamRequest, SpamResponse
from api.ml_filter import is_spam_ml
from api.llm_filter import is_spam_llm

app = FastAPI(title="Anti-Spam API")

@app.post("/check", response_model=SpamResponse)
async def check_spam(req: SpamRequest):
    ml_result = is_spam_ml(req.text)
    llm_result = is_spam_llm(req.text)
    return SpamResponse(text=req.text, ml_result=ml_result, llm_result=llm_result)
