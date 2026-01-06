"""
Application logic
All the details go here, not in main.py
"""
import os
import yaml
import re
from datetime import datetime
from src.gemini.connector import GeminiConnector
from src.prompts.custom_prompts import get_prompt
from src.utils.logger import setup_logger
from src.tts.google_tts import GoogleTTS


def load_config():
    """Load YAML config"""
    with open('config/settings.yaml', 'r') as f:
        return yaml.safe_load(f)


def save_response(prompt: str, response: str) -> str:
    """Save prompt and response to file"""
    output_dir = 'output/scripts'
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_dir, f"response_{timestamp}.txt")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"Generated: {timestamp}\n")
        f.write(f"\n{'='*60}\n\n")
        f.write("PROMPT:\n")
        f.write(prompt)
        f.write(f"\n\n{'='*60}\n\n")
        f.write("RESPONSE:\n")
        f.write(response)
    
    return output_path


def extract_script_from_response(response: str) -> str:
    """
    Extract the SCRIPT content from Gemini's response
    
    Args:
        response: Full response from Gemini
        
    Returns:
        Just the script text (without SCRIPT:, DURÉE, etc.)
    """
    # Remove common labels if present
    text = response.strip()
    
    # Remove "SCRIPT:" prefix if exists
    if text.startswith("SCRIPT:"):
        text = text.replace("SCRIPT:", "", 1).strip()
    
    # Remove metadata lines (DURÉE, MOTS-CLÉS, SOURCE, TYPE, etc.)
    lines = text.split('\n')
    script_lines = []
    
    for line in lines:
        # Skip metadata lines
        if any(keyword in line for keyword in ['DURÉE ESTIMÉE:', 'MOTS-CLÉS:', 'SOURCE D\'INSPIRATION:', 
                                                 'ÉMOTION PRINCIPALE:', 'TYPE DE CONSEIL:', 'DIFFICULTÉ:', 
                                                 'TYPE D\'HUMOUR:', 'INSPIRATION:']):
            break
        script_lines.append(line)
    
    return '\n'.join(script_lines).strip()


def run_gemini_test(theme: str = None, prompt_type: str = "default", voice_preset: str = "reel_female", generate_audio: bool = True):
    """
    Main app logic with dynamic theme injection
    
    Args:
        theme: The theme for the content (e.g., "Confiance en soi", "Productivité")
        prompt_type: Type of prompt template to use ("default", "conseil", "histoire", "jokes")
        voice_preset: Voice preset for TTS ("reel_female", "reel_male", "story", "calm")
        generate_audio: Whether to generate audio file (default: True)
    """
    logger = setup_logger()
    logger.info("🚀 Starting Gemini Content Generator")
    
    # Default theme if none provided
    if not theme:
        theme = "Confiance en soi"
        logger.info(f"ℹ️ No theme provided, using default: {theme}")
    else:
        logger.info(f"🎨 Theme: {theme}")
    
    try:
        # Get API key
        config = load_config()
        api_key = config.get('api_keys', {}).get('gemini')
        
        if not api_key or api_key == "YOUR_GEMINI_API_KEY":
            logger.error("❌ Gemini API key not configured")
            return
        
        # Connect to Gemini
        gemini = GeminiConnector(api_key)
        
        # Get prompt with dynamic theme
        prompt = get_prompt(prompt_type, theme=theme)
        
        logger.info(f"\n{'='*60}")
        logger.info(f"📝 PROMPT (Type: {prompt_type}):")
        logger.info(f"{'='*60}")
        logger.info(prompt)
        logger.info(f"{'='*60}\n")
        
        # Send to Gemini
        response = gemini.send_prompt(prompt)
        
        if not response:
            logger.error("❌ No response")
            return
        
        # Show response
        logger.info(f"\n{'='*60}")
        logger.info("✅ RESPONSE:")
        logger.info(f"{'='*60}")
        logger.info(response)
        logger.info(f"{'='*60}\n")
        
        # Save
        path = save_response(prompt, response)
        logger.info(f"💾 Saved: {path}")
        
        # Generate TTS audio
        if generate_audio:
            logger.info(f"\n{'='*60}")
            logger.info("🎤 GÉNÉRATION AUDIO (TTS avec SSML)")
            logger.info(f"{'='*60}")
            
            try:
                # Extract script from response
                script = extract_script_from_response(response)
                
                # Create audio output directory
                audio_dir = 'output/audio'
                os.makedirs(audio_dir, exist_ok=True)
                
                # Generate audio filename
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                audio_path = os.path.join(audio_dir, f"reel_{timestamp}.mp3")
                
                # Initialize TTS and generate audio
                logger.info(f"🎙️ Voix: {voice_preset}")
                logger.info(f"📝 Script: {len(script)} caractères")
                
                # Get Google Cloud credentials path from config
                google_creds = config.get('google_cloud', {}).get('credentials_path')
                if not google_creds:
                    google_creds = 'config/google-credentials.json'
                
                tts = GoogleTTS(credentials_path=google_creds)
                tts.synthesize_speech(
                    text=script,
                    output_path=audio_path,
                    voice_preset=voice_preset,
                    use_ssml=True  # Active SSML pour les pauses et emphases
                )
                
                logger.info(f"✅ Audio généré: {audio_path}")
                logger.info("🎧 Écoute pour entendre les pauses et emphases SSML!")
                
            except Exception as e:
                logger.error(f"❌ Erreur TTS: {e}")
                logger.warning("⚠️ Script sauvegardé mais audio non généré")
        
        logger.info(f"\n{'='*60}")
        logger.info("✅ Done!")
        logger.info(f"{'='*60}\n")
        
        return response
        
    except Exception as e:
        logger.error(f"❌ Error: {e}")
        import traceback
        logger.error(traceback.format_exc())
