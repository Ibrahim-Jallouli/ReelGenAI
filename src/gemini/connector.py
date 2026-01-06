"""
Gemini Connection Module
Handles all communication with Gemini API
"""
import logging
from typing import Optional
import google.generativeai as genai


class GeminiConnector:
    """
    Simple connector for Gemini API
    Clean and modular
    """
    
    def __init__(self, api_key: str, model: str = "gemini-2.0-flash-exp"):
        """
        Initialize Gemini connector
        
        Args:
            api_key: Google Gemini API key
            model: Model name
        """
        self.api_key = api_key
        self.model_name = model
        self.logger = logging.getLogger('GeminiConnector')
        
        # Configure and create model
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model)
        
        self.logger.info(f"✅ Gemini connected ({model})")
    
    def send_prompt(self, prompt: str) -> Optional[str]:
        """
        Send a prompt to Gemini and get response
        
        Args:
            prompt: The text prompt to send
            
        Returns:
            Raw text response from Gemini or None if failed
        """
        try:
            self.logger.info("📤 Sending prompt to Gemini...")
            
            # Call Gemini API
            response = self.model.generate_content(prompt)
            
            if not response or not response.text:
                self.logger.error("❌ Empty response from Gemini")
                return None
            
            self.logger.info("✅ Response received from Gemini")
            return response.text
            
        except Exception as e:
            self.logger.error(f"❌ Gemini API error: {e}")
            return None
    
    def is_connected(self) -> bool:
        """Check if connection is active"""
        return self.model is not None
