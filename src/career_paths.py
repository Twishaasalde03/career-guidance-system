from dataclasses import dataclass
from typing import List
import json

@dataclass
class CareerPath:
    name: str
    category: str
    description: str
    required_skills: List[str]
    personality_traits: List[str]
    salary_range: str
    growth_outlook: str
    
    def to_dict(self):
        return {
            'name': self.name,
            'category': self.category,
            'description': self.description,
            'required_skills': self.required_skills,
            'personality_traits': self.personality_traits,
            'salary_range': self.salary_range,
            'growth_outlook': self.growth_outlook
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)

def get_default_career_paths():
    """Return default career paths"""
    return [
        CareerPath(
            name="Software Developer",
            category="STEM",
            description="Design, develop, and maintain software applications and systems",
            required_skills=["Programming", "Problem-solving", "Analytical thinking"],
            personality_traits=["Detail-oriented", "Logical", "Creative"],
            salary_range="$70k-$150k+",
            growth_outlook="Excellent (22% growth)"
        ),
        CareerPath(
            name="Data Scientist",
            category="STEM",
            description="Analyze complex data to help organizations make informed decisions",
            required_skills=["Statistics", "Python/R", "Machine Learning", "Data Visualization"],
            personality_traits=["Analytical", "Curious", "Patient"],
            salary_range="$80k-$180k+",
            growth_outlook="Excellent (31% growth)"
        ),
        CareerPath(
            name="UX/UI Designer",
            category="Arts",
            description="Design user interfaces and experiences for digital products",
            required_skills=["Design thinking", "Prototyping", "User research", "Design tools"],
            personality_traits=["Empathetic", "Creative", "Analytical"],
            salary_range="$60k-$130k",
            growth_outlook="Excellent (13% growth)"
        ),
        CareerPath(
            name="Digital Marketing Specialist",
            category="Business",
            description="Develop and execute online marketing campaigns",
            required_skills=["SEO/SEM", "Social media", "Analytics", "Content creation"],
            personality_traits=["Creative", "Analytical", "Adaptable"],
            salary_range="$40k-$85k",
            growth_outlook="Excellent (10% growth)"
        ),
        CareerPath(
            name="Sports Therapist",
            category="Sports",
            description="Help athletes recover from injuries and improve performance",
            required_skills=["Anatomy", "Physical therapy", "Communication", "Problem-solving"],
            personality_traits=["Empathetic", "Patient", "Motivational"],
            salary_range="$50k-$90k",
            growth_outlook="Good (7% growth)"
        )
    ]

def save_career_paths_to_file(career_paths, filename):
    """Save career paths to JSON file"""
    data = [career.to_dict() for career in career_paths]
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def load_career_paths_from_file(filename):
    """Load career paths from JSON file"""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return [CareerPath.from_dict(item) for item in data]
    except FileNotFoundError:
        return get_default_career_paths()