import sys
import os
sys.path.append('src')

from config.config import config
from src.career_paths import get_default_career_paths

def test_setup():
    print("Testing Career Guidance System Setup...")
    print("=" * 50)
    
    # Test config
    print(f"Environment: {config.environment}")
    print(f"Debug mode: {config.debug}")
    print(f"OpenAI API Key: {'Set' if config.openai_api_key else 'Not set'}")
    
    # Test career paths
    careers = get_default_career_paths()
    print(f"Loaded {len(careers)} career paths")
    
    # Test imports
    try:
        import openai
        print("✓ OpenAI imported successfully")
    except ImportError:
        print("✗ OpenAI import failed")
    
    try:
        from langchain.llms import OpenAI
        print("✓ LangChain imported successfully")
    except ImportError:
        print("✗ LangChain import failed")
    
    try:
        import faiss
        print("✓ FAISS imported successfully")
    except ImportError:
        print("✗ FAISS import failed")
    
    print("\nSetup test completed!")

if __name__ == "__main__":
    test_setup()