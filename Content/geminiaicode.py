import io
import json
import requests  # Import the requests library
import os
from fastapi.security import OAuth2PasswordRequestForm
from Content import schemas,models,database,hashing, token, oauth2
from sqlalchemy.orm import Session 
import google.generativeai as genai
from fastapi import Depends, FastAPI, HTTPException,Query, UploadFile, File,status

get_db = database.get_db

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello User"}
genai.configure(api_key="Your API Key")

@app.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    if not hashing.Hash.verify(user.password, form_data.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")

    access_token = token.create_access_token(data={"sub": user.email})
    
    return {"access_token": access_token, "token_type": "bearer"}

async def get_gemini_ai_output( file: UploadFile):
    base_url = "http://localhost:8001"
    endpoint = "/extract_text/"

    try:
        files = {'file': (file.filename, file.file, file.content_type)}

        response = requests.post(url=f"{base_url}{endpoint}", files=files)
        if response.status_code == 200:
            details = response.json()
            return details
        else:
            raise HTTPException(status_code=response.status_code, detail=f"Request failed with status code {response.status_code}: {response.text}")

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Request error: {str(e)}")

@app.post("/Resume_Analysis")
async def resume(position:str=Query(...) , file: UploadFile = File(...),current_user: schemas.User = Depends(oauth2.get_current_user)):
    try:
        details = await get_gemini_ai_output(file)
        genai.configure(api_key="Your API Key")
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Resume: {details['text']} based on this resume,find everything in the resume and based on this you analyse and give your coments on this resume as a Hiring Manager of a big company and after anysing this resume you have to give a verdict that for the {position} position this resume is selected or rejected so putput should be strictly in format MY COMMENTS: and then your comments and then VERDICT: and then your verdict and cant you give ans in a format where there can't be any /n ir something like that so that i can give it as my api response please seperate the verdict and if possible return answer in json format")
        return response.text
    except HTTPException as e:
        return e
