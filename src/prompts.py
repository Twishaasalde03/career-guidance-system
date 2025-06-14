from langchain.prompts import PromptTemplate

class CareerPrompts:
    @staticmethod
    def get_preference_extraction_prompt():
        template = """
You are a career counselor AI. Extract the user's career preferences from the following conversation.
Focus on identifying:
1. Interests and hobbies
2. Skills and strengths
3. Values (work-life balance, helping others, financial success, creativity, etc.)
4. Preferred work environment (team vs individual, office vs remote, structured vs flexible)
5. Personality traits
6. Education level or willingness to pursue education

Conversation: {conversation}

Please extract the preferences in the following JSON format:
{{
    "interests": [list of interests],
    "skills": [list of skills],
    "values": [list of values],
    "work_environment": "description of preferred work environment",
    "personality_traits": [list of personality traits],
    "education_level": "current or preferred education level",
    "confidence_score": "score from 0-10 indicating how confident you are about these preferences"
}}

If information is missing or unclear, set the confidence_score lower and indicate what information is needed.
"""
        return PromptTemplate(template=template, input_variables=["conversation"])

    @staticmethod
    def get_clarification_prompt():
        template = """
Based on the extracted preferences, you need more information to provide accurate career recommendations.

Current preferences: {preferences}
Missing information: {missing_info}

Generate 2-3 thoughtful clarifying questions that would help you better understand the user's career preferences. 
Make the questions conversational and engaging, not like a survey.

Focus on the most important missing information that would significantly impact career recommendations.

Questions:
"""
        return PromptTemplate(template=template, input_variables=["preferences", "missing_info"])

    @staticmethod
    def get_recommendation_prompt():
        template = """
You are a career counselor providing personalized career recommendations.

User Preferences:
{user_preferences}

Matched Career Paths:
{matched_careers}

Generate a comprehensive career recommendation response that includes:
1. A brief summary of the user's key strengths and interests
2. Top 3 recommended career paths with explanations for why they're good matches
3. For each recommendation, include:
   - Why it matches their preferences
   - Key skills they should develop
   - Next steps to pursue this path
4. Additional career paths to consider
5. General advice for career development

Make the response encouraging, specific, and actionable. Use a conversational tone.
"""
        return PromptTemplate(template=template, input_variables=["user_preferences", "matched_careers"])

# Fallback prompts for different scenarios
FALLBACK_PROMPTS = {
    "insufficient_info": """
I'd love to help you explore career options! To give you the best recommendations, I need to learn more about you. Could you tell me about:

1. What activities or subjects genuinely interest you or make you lose track of time?
2. What are you naturally good at, or what do others often ask for your help with?
3. What's important to you in a career - creativity, helping others, financial stability, work-life balance, or something else?

Feel free to share as much or as little as you'd like about any of these areas!
    """,
    
    "vague_interests": """
It sounds like you have some interests, but I'd love to dig deeper! When you mention [INTEREST], what specifically draws you to it? 

For example:
- Is it the problem-solving aspect?
- The creative expression?
- The opportunity to help others?
- The technical challenges?
- Something else entirely?

Understanding the 'why' behind your interests helps me suggest careers that would truly fulfill you.
    """,
    
    "conflicting_preferences": """
I notice you've mentioned some different interests and preferences. That's totally normal - most people are multi-faceted! 

To help me understand your priorities better:
- Which of these interests energizes you most?
- If you had to choose, would you prefer [OPTION A] or [OPTION B]?
- Are there ways you see these different interests potentially combining in a career?

There might be careers that blend multiple interests, so don't worry about having varied preferences!
    """
}