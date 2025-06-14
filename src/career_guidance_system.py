import json
from src.career_paths import load_career_paths_from_file
from src.conversation_manager import extract_preferences, generate_recommendations
from config.config import config

career_paths = load_career_paths_from_file(config.settings["database"]["career_paths_file"])

def get_matching_careers(preferences: dict) -> list:
    matches = []

    for career in career_paths:
        match_score = 0
        for skill in preferences.get("skills", []):
            if skill.lower() in map(str.lower, career.required_skills):
                match_score += 1

        if match_score >= config.settings["system"]["confidence_threshold"]:
            matches.append((career, match_score))

    matches.sort(key=lambda x: x[1], reverse=True)
    return [match[0] for match in matches[:config.settings["system"]["max_career_matches"]]]

def run_conversation(conversation: str) -> str:
    raw_preferences = extract_preferences(conversation)

    try:
        preferences = json.loads(raw_preferences)
    except json.JSONDecodeError:
        return "⚠️ Failed to parse preferences from LLM. Try again with more specific input."

    matched_careers = get_matching_careers(preferences)
    response = generate_recommendations(preferences, [c.to_dict() for c in matched_careers])
    return response
