from langchain_core.prompts import PromptTemplate
from langchain_community.llms import OpenAI
from config.config import config
from src.prompts import CareerPrompts

llm = OpenAI(api_key=config.openai_api_key)

def extract_preferences(conversation: str) -> str:
    prompt = CareerPrompts.get_preference_extraction_prompt()
    full_prompt = prompt.format(conversation=conversation)
    response = llm.invoke(full_prompt)
    return response

def generate_recommendations(user_preferences: dict, matched_careers: list) -> str:
    prompt = CareerPrompts.get_recommendation_prompt()
    return llm.invoke(prompt.format(user_preferences=user_preferences, matched_careers=matched_careers))
