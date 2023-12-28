from dotenv import load_dotenv
import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI

def get_model():
    load_dotenv()
    akey = os.getenv("GOOGLE_API_KEY")
    ##print('The key is ',akey)
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-pro')
    return model

def get_llm_model():
    load_dotenv()
    llm = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=os.getenv("GOOGLE_API_KEY"),temperature=0.2,convert_system_message_to_human=True)
    return llm