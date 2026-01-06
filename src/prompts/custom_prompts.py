"""
Custom Prompts for Gemini
Using structured PromptTemplate
"""
from .prompt_model import PromptTemplate


# ========================================
# 🎯 TEMPLATES POUR REELS/TIKTOK
# ========================================

# 1️⃣ TEMPLATE PAR DÉFAUT - Contenu engageant et polyvalent
DEFAULT_TEMPLATE = PromptTemplate(
    role="expert en contenu viral TikTok/Reel",
    
    task="Crée un script COURT (30-40 sec) pour un Reel. Captive en 3 secondes, inspire, engage.",
    
    theme=None,
    
    context="Public: 18-35 ans. Scroll rapide, attention limitée.",
    
    hook_type="Question choc OU Affirmation contre-intuitive OU Statistique surprenante",
    
    structure="""HOOK (10 mots): Phrase choc
CORPS (80 mots): 3 points max, phrases courtes
CONCLUSION (20 mots): Message inspirant""",
    
    style="""Phrases ultra-courtes. Ton ami.  Conversationnel.""",
    
    constraints="120-150 mots MAX. 30-40 secondes.",
    
    examples="""EXEMPLE:
"Pourquoi tu n'arrives jamais à tenir tes résolutions? La science a une réponse. Ton cerveau déteste le changement. C'est biologique. Quand tu fixes un gros objectif, il panique. La solution? Pense micro. Un petit geste par jour. Juste un. Ton cerveau l'accepte sans résistance. Commence petit aujourd'hui. Un pas suffit. Le reste suivra naturellement."
""",
    
    output_format="Écris directement le script complet en texte fluide. Pas de 'SCRIPT:', pas de sections."
)


# 2️⃣ TEMPLATE CONSEIL - Donner des conseils pratiques et actionnables
CONSEIL_TEMPLATE = PromptTemplate(
    role="expert bienveillant en conseils pratiques",
    
    task="Crée un conseil CONCRET (15-20 sec) que les gens peuvent appliquer aujourd'hui.",
    
    theme=None,
    
    context="Public cherchant solutions simples. Format: astuce applicable immédiatement.",
    
    hook_type="Problème courant OU Astuce surprenante",
    
    structure="""HOOK (5 sec): Identifie le problème
CONSEIL (15 sec): 3 étapes simples
ACTION (5 sec): Pourquoi ça marche + encourage""",
    
    style="Instructions claires. Ton encourageant. ",
    
    constraints="80-110 mots MAX. 20-25 secondes. Max 3 étapes.",
    
    examples="""EXEMPLE:
"Tu procrastines tout le temps? Voici la règle des 2 minutes. Quand une tâche te stresse, fais juste les 2 premières minutes. Ouvre le fichier. Lis la première ligne. C'est tout. Ton cerveau va naturellement continuer. La résistance disparaît. Teste demain matin avec ta tâche la plus pénible. ⏰"
""",
    
    output_format="Écris directement le conseil complet en texte fluide. Pas de 'SCRIPT:', pas de sections."
)


# 3️⃣ TEMPLATE HISTOIRE - Raconter une histoire inspirante ou édifiante
HISTOIRE_TEMPLATE = PromptTemplate(
    role="conteur captivant pour réseaux sociaux",
    
    task="Crée une HISTOIRE COURTE (35-40 sec) vraie ou inspirée du réel qui inspire ou émeut.",
    
    theme=None,
    
    context="Public aimant histoires authentiques. Récit court: début-milieu-fin. Source: faits réels.",
    
    hook_type="Début mystérieux OU Révélation surprenante",
    
    structure="""HOOK (5 sec): Capte attention + situe (qui, quand, où)
HISTOIRE (30 sec): Contexte → Défi → Tournant → Résolution
LEÇON (5 sec): Message inspirant""",
    
    style="Présent narratif. Détails sensoriels. Émotions authentiques. ",
    
    constraints="130-160 mots MAX. Histoire vraie ou inspirée. 35-40 secondes.",
    
    examples="""EXEMPLE:
"1962. Un professeur demande à ses élèves de dessiner leur futur. Un garçon dessine des fusées et des étoiles. Les autres se moquent. Trop fou. Impossible. Ce garçon c'était Elon Musk. Aujourd'hui ses fusées touchent l'espace. La leçon? Les rêveurs qu'on trouve fous aujourd'hui sont souvent les visionnaires de demain. Alors garde tes rêves précieusement. 🚀"
""",
    
    output_format="Écris directement l'histoire complète en texte fluide. Pas de 'SCRIPT:', pas de sections."
)


# 4️⃣ TEMPLATE JOKES - Créer des blagues courtes et percutantes
JOKES_TEMPLATE = PromptTemplate(
    role="humoriste créatif spécialisé humour court",
    
    task="Crée une BLAGUE COURTE (20-30 sec) drôle et relatable.",
    
    theme=None,
    
    context="Public jeunes adultes. Humour intelligent, observation, autodérision, absurde.",
    
    hook_type="Setup intrigant OU Question amusante OU Constat absurde",
    
    structure="""SETUP (10 sec): Établis situation
BUILD-UP (10 sec): Détails amusants
PUNCHLINE (10 sec): Chute inattendue""",
    
    style="Humour d'observation. Situations relatable. Timing parfait. ",
    
    constraints="60-100 mots MAX. 20-30 secondes. Bon goût.",
    
    examples="""EXEMPLE:
"Mon cerveau à 3h du matin: Tu te souviens de ce truc gênant que tu as fait en 2012? Parlons-en pendant 4 heures. Mon cerveau à 9h du matin quand je dois travailler: Je crois qu'on devrait dormir encore. 😴"
""",
    
    output_format="Écris directement la blague complète en texte fluide. Pas de 'SCRIPT:', pas de sections."
)


# ========================================
# 🔧 FONCTION DE RÉCUPÉRATION
# ========================================

def get_prompt(prompt_name: str = "default", theme: str = None) -> str:
    """
    Get a prompt by name with dynamic theme injection
    
    Args:
        prompt_name: "default", "conseil", "histoire", "jokes"
        theme: Theme to inject dynamically (e.g., "Confiance en soi")
        
    Returns:
        The complete prompt text ready for Gemini
    """
    templates = {
        "default": DEFAULT_TEMPLATE,
        "conseil": CONSEIL_TEMPLATE,
        "histoire": HISTOIRE_TEMPLATE,
        "jokes": JOKES_TEMPLATE,
    }
    
    template = templates.get(prompt_name, DEFAULT_TEMPLATE)
    return template.build(theme_override=theme)


def list_available_prompts() -> list:
    """Return list of available prompt names"""
    return ["default", "conseil", "histoire", "jokes"]
