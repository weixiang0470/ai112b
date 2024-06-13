import os                                                                                                                                                                                                       
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
load_dotenv(Path(".env"))
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")
# api = {
#     "OPENAI_API_KEY":OPENAI_API_KEY,
#     "SERPAPI_API_KEY":SERPAPI_API_KEY,
#     "GROQ_API_KEY":GROQ_API_KEY}