"""
Prompt Template Model
Structured way to create prompts
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class PromptTemplate:
    """
    Structured prompt template optimized for social media content
    """
    role: str                    # Ex: "expert en création de contenu"
    task: str                    # Ex: "Crée un script court..."
    theme: Optional[str] = None  # Ex: "Confiance en soi" - Dynamique
    context: Optional[str] = None  # Ex: "Pour un public jeune (18-35 ans)"
    hook_type: Optional[str] = None  # Ex: "Question provocante", "Statistique choc"
    structure: Optional[str] = None  # Ex: "Hook, Corps, Conclusion"
    style: Optional[str] = None  # Ex: "Phrases courtes, ton bienveillant"
    constraints: Optional[str] = None  # Ex: "Maximum 150 mots"
    examples: Optional[str] = None  # Ex: "Exemple de hook: 'Et si je te disais...'"
    output_format: Optional[str] = None  # Ex: "SCRIPT: ... CONCLUSION: ..."
    text_rules: str = """- ZÉRO markdown (**bold**, *italic*, # titres)
- Ajoute 2-3 emojis stratégiques pour ponctuer l'émotion 😊💡✨
- Phrases courtes et percutantes (max 15 mots/phrase)
- Langage conversationnel et authentique
- TOUT EN FRANÇAIS - 100% NATUREL"""
    
    def build(self, theme_override: Optional[str] = None) -> str:
        """
        Build the complete prompt from template
        
        Args:
            theme_override: Override the default theme (dynamic theme injection)
        
        Returns:
            Complete prompt string
        """
        parts = []
        active_theme = theme_override or self.theme
        
        # === HEADER: ROLE + MISSION ===
        parts.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
        parts.append("🎯 MISSION DE CRÉATION\n")
        parts.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n")
        
        if self.role:
            parts.append(f"🎭 RÔLE: {self.role}\n\n")
        
        if self.task:
            parts.append(f"📋 TÂCHE:\n{self.task}\n\n")
        
        # === CONTEXTE ===
        if active_theme or self.context:
            parts.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
            parts.append("🎨 CONTEXTE\n")
            parts.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n")
            
            if active_theme:
                parts.append(f"💡 THÈME: {active_theme}\n\n")
            
            if self.context:
                parts.append(f"👥 PUBLIC/CONTEXTE:\n{self.context}\n\n")
        
        # === STRUCTURE ===
        if self.structure:
            parts.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
            parts.append("📐 STRUCTURE REQUISE\n")
            parts.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n")
            parts.append(f"{self.structure}\n\n")
        
        # === HOOK TYPE ===
        if self.hook_type:
            parts.append(f"🎣 TYPE DE HOOK: {self.hook_type}\n\n")
        
        # === STYLE ===
        if self.style:
            parts.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
            parts.append("✨ STYLE & TON\n")
            parts.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n")
            parts.append(f"{self.style}\n\n")
        
        # === CONSTRAINTS ===
        if self.constraints:
            parts.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
            parts.append("⚠️ CONTRAINTES STRICTES\n")
            parts.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n")
            parts.append(f"{self.constraints}\n\n")
        
        # === TEXT RULES (ALWAYS) ===
        parts.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
        parts.append("🚨 RÈGLES DE TEXTE OBLIGATOIRES\n")
        parts.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n")
        parts.append(f"{self.text_rules}\n\n")
        
        # === EXAMPLES ===
        if self.examples:
            parts.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
            parts.append("💡 EXEMPLES DE RÉFÉRENCE\n")
            parts.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n")
            parts.append(f"{self.examples}\n\n")
        
        # === OUTPUT FORMAT ===
        if self.output_format:
            parts.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")
            parts.append("📤 FORMAT DE SORTIE\n")
            parts.append("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n")
            parts.append(f"{self.output_format}\n")
        
        return "".join(parts)
    
    def __str__(self) -> str:
        """Return the built prompt"""
        return self.build()
