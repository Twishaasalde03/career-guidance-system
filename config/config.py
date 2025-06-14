import os
import yaml
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.config_file = self.base_dir / "config" / "settings.yaml"
        self.settings = self._load_settings()
        
    def _load_settings(self):
        with open(self.config_file, 'r') as file:
            return yaml.safe_load(file)
    
    @property
    def openai_api_key(self):
        return os.getenv("OPENAI_API_KEY")
    
    @property
    def mistral_api_key(self):
        return os.getenv("MISTRAL_API_KEY")
    
    @property
    def environment(self):
        return os.getenv("ENVIRONMENT", "development")
    
    @property
    def debug(self):
        return os.getenv("DEBUG", "False").lower() == "true"

# Global config instance
config = Config()