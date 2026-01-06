"""
Main entry point
Usage examples:
    python main.py                                          # Default: "Confiance en soi" + default template + TTS
    python main.py "Productivité"                           # Custom theme
    python main.py "Gestion du stress" conseil              # Custom theme + conseil template
    python main.py "Motivation" default reel_male           # Custom theme + male voice
    python main.py "Histoire inspirante" histoire story     # Histoire template + story voice
    
Available templates: default, conseil, histoire, jokes
Available voices: reel_female, reel_male, story, calm, neutral
"""
import sys
from src.app import run_gemini_test

if __name__ == "__main__":
    # Parse command line arguments
    theme = sys.argv[1] if len(sys.argv) > 1 else None
    prompt_type = sys.argv[2] if len(sys.argv) > 2 else "default"
    voice_preset = sys.argv[3] if len(sys.argv) > 3 else "reel_male"  # Changé en masculine par défaut
    
    # Run with dynamic theme and TTS
    run_gemini_test(
        theme=theme, 
        prompt_type=prompt_type,
        voice_preset=voice_preset,
        generate_audio=True
    )
