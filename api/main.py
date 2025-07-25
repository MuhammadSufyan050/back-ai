import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv

# Load your Gemini API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# FastAPI app setup
app = FastAPI()

# Allow frontend requests (adjust origin in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for incoming user request
class TravelRequest(BaseModel):
    destination: str
    duration: str
    budget: str
    travel_month: str

# Gemini LLM model
model = genai.GenerativeModel('gemini-1.5-flash')

@app.post("/generate-itinerary")
async def generate_itinerary(data: TravelRequest):
    prompt = f"""
    You are a travel agent. Create a personalized travel itinerary.
    Destination: {data.destination}
    Duration: {data.duration}
    Travel Month: {data.travel_month}
    Budget: {data.budget}
    
    Respond with:
    - Day-wise travel plan
    - Estimated flight and hotel costs
    - Top attractions and local tips
    """
    try:
        response = model.generate_content(prompt)
        return {"itinerary": response.text}
    except Exception as e:
        return {"error": str(e)}
























# import os
# from fastapi import FastAPI, Request
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# import google.generativeai as genai
# from dotenv import load_dotenv

# # Load your Gemini API key from .env
# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# # FastAPI app setup
# app = FastAPI

# # Allow Frontend Requests (adjust origin in production)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Pydantic model for incoming user request
# class TravelRequest(BaseModel):
#     destination: str
#     duration: str
#     budget: str
#     travel_month: str

# # Gemini LLM model
# model = genai.GenerativeModel('gemini-1.5-flash')

# @app.post("/generate-itinerary")
# async def generate_itinerary(data: TravelRequest):
#     prompt = f"""
#     You  are a travel agent. Create a personalized travel itinerary.
#     Destination: {data.destination}
#     Duration: {data.duration}
#     Travel Month: {data.travel_month}
#     Budget: {data.budget}

#     Respond with:
#     - Day-wise travel plan
#     - Estimated Flight and hotel costs
#     - Top attractions and local tips
#     """
#     try:
#         response = model.generate_content(prompt)
#         return {"itinerary": response.text}
#     except Exception as e:
#         return {"error": str(e)}
