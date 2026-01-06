"""
Google Cloud Text-to-Speech Integration
Synthèse vocale de haute qualité pour Reels
"""
from google.cloud import texttospeech
import os
from typing import Optional, Literal
from dataclasses import dataclass


@dataclass
class VoiceConfig:
    """Configuration de la voix"""
    language_code: str = "fr-FR"
    voice_name: str = "fr-FR-Neural2-A"  # Voix féminine dynamique (TOP pour Reels)
    speaking_rate: float = 1.1  # Vitesse (0.25 à 4.0) - 1.1 = légèrement plus rapide
    pitch: float = 0.0  # Tonalité (-20.0 à 20.0)
    volume_gain_db: float = 0.0  # Volume (-96.0 à 16.0)
    
    # Voix disponibles pour Reels/TikTok
    FEMALE_DYNAMIC = "fr-FR-Neural2-A"  # Féminin, jeune, énergique ⭐ RECOMMANDÉ
    MALE_ENERGETIC = "fr-FR-Neural2-B"  # Masculin, dynamique
    FEMALE_WARM = "fr-FR-Neural2-C"     # Féminin, chaleureux
    MALE_DEEP = "fr-FR-Neural2-D"       # Masculin, profond
    FEMALE_SOFT = "fr-FR-Neural2-E"     # Féminin, doux


class GoogleTTS:
    """
    Google Cloud Text-to-Speech client
    
    Prérequis:
    1. Installer: pip install google-cloud-texttospeech
    2. Créer un projet Google Cloud
    3. Activer l'API Text-to-Speech
    4. Créer une clé de service (JSON)
    5. Définir: GOOGLE_APPLICATION_CREDENTIALS dans config/settings.yaml
    """
    
    def __init__(self, credentials_path: Optional[str] = None):
        """
        Initialize Google TTS client
        
        Args:
            credentials_path: Path to Google Cloud credentials JSON file
        """
        # Set credentials if provided
        if credentials_path:
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path
        
        # Initialize client
        self.client = texttospeech.TextToSpeechClient()
        self.voice_config = VoiceConfig()
    
    def set_voice(self, voice_name: str):
        """Change la voix utilisée"""
        self.voice_config.voice_name = voice_name
    
    def set_speaking_rate(self, rate: float):
        """
        Change la vitesse de parole
        
        Args:
            rate: 0.25 (très lent) à 4.0 (très rapide)
                  1.0 = normal
                  1.1-1.2 = idéal pour Reels (dynamique)
        """
        self.voice_config.speaking_rate = max(0.25, min(4.0, rate))
    
    def set_pitch(self, pitch: float):
        """
        Change la tonalité de la voix
        
        Args:
            pitch: -20.0 (grave) à 20.0 (aigu)
                   0.0 = normal
                   2-5 = légèrement plus enjoué pour Reels
        """
        self.voice_config.pitch = max(-20.0, min(20.0, pitch))
    
    def synthesize_speech(
        self, 
        text: str, 
        output_path: str,
        voice_preset: Optional[Literal['reel_female', 'reel_male', 'story', 'calm']] = None,
        use_ssml: bool = True
    ) -> str:
        """
        Synthétise le texte en audio
        
        Args:
            text: Le texte à synthétiser (peut contenir des balises SSML)
            output_path: Chemin de sortie du fichier audio (.mp3)
            voice_preset: Preset de voix prédéfini
                - 'reel_female': Féminin dynamique pour Reels (défaut)
                - 'reel_male': Masculin énergique pour Reels
                - 'story': Voix narrative pour histoires
                - 'calm': Voix calme pour contenu relaxant
            use_ssml: Si True, traite le texte comme du SSML (recommandé)
        
        Returns:
            Le chemin du fichier audio généré
        """
        # Apply preset if specified
        if voice_preset:
            self._apply_preset(voice_preset)
        
        # Clean text for SSML (remove emojis)
        clean_text = self._clean_text_for_ssml(text)
        
        # Prepare synthesis input
        if use_ssml and ('<' in clean_text and '>' in clean_text):
            # Wrap in SSML speak tag if not already present
            if not clean_text.strip().startswith('<speak>'):
                clean_text = f'<speak>{clean_text}</speak>'
            synthesis_input = texttospeech.SynthesisInput(ssml=clean_text)
        else:
            synthesis_input = texttospeech.SynthesisInput(text=clean_text)
        
        # Configure voice
        voice = texttospeech.VoiceSelectionParams(
            language_code=self.voice_config.language_code,
            name=self.voice_config.voice_name
        )
        
        # Configure audio
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=self.voice_config.speaking_rate,
            pitch=self.voice_config.pitch,
            volume_gain_db=self.voice_config.volume_gain_db,
            # High quality for social media
            sample_rate_hertz=24000
        )
        
        # Perform synthesis
        response = self.client.synthesize_speech(
            input=synthesis_input,
            voice=voice,
            audio_config=audio_config
        )
        
        # Save audio file
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'wb') as out:
            out.write(response.audio_content)
        
        return output_path
    
    def _clean_text_for_ssml(self, text: str) -> str:
        """
        Nettoie le texte pour SSML (retire les emojis, etc.)
        """
        import re
        # Remove emojis (they can cause issues with TTS)
        emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags
            u"\U00002702-\U000027B0"
            u"\U000024C2-\U0001F251"
            "]+", flags=re.UNICODE)
        return emoji_pattern.sub('', text)
    
    def _apply_preset(self, preset: str):
        """Applique un preset de voix prédéfini"""
        presets = {
            'reel_female': {
                'voice_name': VoiceConfig.FEMALE_DYNAMIC,
                'speaking_rate': 1.0,  # Vitesse normale (plus compréhensible)
                'pitch': 1.5,  # Légèrement enjoué
                'volume_gain_db': 2.0  # Légèrement plus fort
            },
            'reel_male': {
                'voice_name': VoiceConfig.MALE_ENERGETIC,
                'speaking_rate': 0.95,  # Légèrement plus lent
                'pitch': 0.0,
                'volume_gain_db': 2.0
            },
            'story': {
                'voice_name': VoiceConfig.FEMALE_WARM,
                'speaking_rate': 0.95,  # Un peu plus lent (narrative)
                'pitch': -1.0,  # Légèrement plus grave (sérieux)
                'volume_gain_db': 0.0
            },
            'calm': {
                'voice_name': VoiceConfig.FEMALE_SOFT,
                'speaking_rate': 0.85,  # Plus lent (apaisant)
                'pitch': -2.0,
                'volume_gain_db': -2.0  # Plus doux
            },
            'neutral': {
                'voice_name': VoiceConfig.FEMALE_WARM,
                'speaking_rate': 0.95,  # Vitesse normale
                'pitch': 0.0,
                'volume_gain_db': 0.0
            }
        }
        
        if preset in presets:
            config = presets[preset]
            self.voice_config.voice_name = config['voice_name']
            self.voice_config.speaking_rate = config['speaking_rate']
            self.voice_config.pitch = config['pitch']
            self.voice_config.volume_gain_db = config['volume_gain_db']
