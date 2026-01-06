# 🎯 Guide Rapide - 4 Templates Disponibles

## 📋 Utilisation

```bash
python main.py "Ton thème" [template]
```

---

## 🎨 Les 4 Templates

### 1️⃣ **DEFAULT** (Par défaut) - Contenu Viral
**Quand l'utiliser** : Contenu engageant et polyvalent

```bash
python main.py "Confiance en soi"
python main.py "Gestion du stress" default
```

**Style** : 
- Hook captivant
- Message impactant
- Appel à l'action

**Exemple de sortie** :
```
Pourquoi tu doutes tout le temps de toi? Ton cerveau te ment...
```

---

### 2️⃣ **CONSEIL** - Astuces Pratiques
**Quand l'utiliser** : Donner des conseils actionnables

```bash
python main.py "Productivité" conseil
python main.py "Sommeil" conseil
python main.py "Organisation" conseil
```

**Style** :
- Problème → Solution
- Étapes claires
- Facile à appliquer

**Exemple de sortie** :
```
Tu perds du temps le matin? Voici la règle des 3 P. 
Prépare ta tenue. Place tes clés au même endroit. Prévois ton sac...
```

**Thèmes recommandés** :
- Productivité, Organisation, Routine
- Sommeil, Alimentation, Sport
- Communication, Relations
- Finances personnelles

---

### 3️⃣ **HISTOIRE** - Récits Inspirants
**Quand l'utiliser** : Raconter une histoire vraie qui inspire

```bash
python main.py "Persévérance" histoire
python main.py "Réussite malgré l'échec" histoire
python main.py "Courage" histoire
```

**Style** :
- Récit captivant
- Basé sur faits réels
- Leçon inspirante

**Exemple de sortie** :
```
1954. Rosa Parks est assise dans le bus. Un homme lui ordonne de se lever.
Elle refuse. Ce simple "non" va changer l'histoire...
```

**Thèmes recommandés** :
- Persévérance, Courage, Résilience
- Innovation, Créativité
- Justice, Égalité
- Transformation personnelle

**Sources d'inspiration** :
- Personnalités historiques (Einstein, Rosa Parks, Steve Jobs)
- Sportifs (Jordan, Serena Williams)
- Entrepreneurs (Musk, Oprah)
- Scientifiques, artistes, militants

---

### 4️⃣ **JOKES** - Humour Court
**Quand l'utiliser** : Faire rire avec de l'humour relatable

```bash
python main.py "Vie quotidienne" jokes
python main.py "Travail" jokes
python main.py "Réseaux sociaux" jokes
```

**Style** :
- Setup + Punchline
- Humour d'observation
- Relatable et léger

**Exemple de sortie** :
```
Mon cerveau à 3h du matin: Tu te souviens de ce truc gênant en 2012?
Parlons-en pendant 4 heures.
Mon cerveau à 9h quand je dois bosser: On devrait dormir encore. 😴
```

**Thèmes recommandés** :
- Vie quotidienne, Routine
- Travail, Réunions
- Réseaux sociaux, Technologie
- Adulte vs Enfant
- Attentes vs Réalité

**Types d'humour** :
- Observation (vie de tous les jours)
- Autodérision (se moquer de soi)
- Absurde (situations illogiques)
- Contraste (attente vs réalité)

---

## 🎯 Exemples Complets

### Productivité
```bash
# Conseil pratique
python main.py "Productivité" conseil
→ Astuce concrète pour être plus productif

# Histoire inspirante
python main.py "Productivité" histoire
→ Histoire d'Elon Musk, Bill Gates, etc.

# Humour
python main.py "Productivité" jokes
→ Blague sur la procrastination
```

### Confiance en soi
```bash
# Contenu viral
python main.py "Confiance en soi" default
→ Message motivant et impactant

# Conseil
python main.py "Confiance en soi" conseil
→ Exercice pour développer sa confiance

# Histoire
python main.py "Confiance en soi" histoire
→ Récit de quelqu'un qui a surmonté ses doutes
```

### Relations
```bash
# Conseil
python main.py "Communication de couple" conseil
→ Technique de communication

# Histoire
python main.py "Relations toxiques" histoire
→ Histoire de quelqu'un qui s'en est sorti

# Humour
python main.py "Relations amoureuses" jokes
→ Blague sur les relations modernes
```

---

## 📊 Quel Template Choisir ?

| Objectif | Template | Exemple |
|----------|----------|---------|
| **Informer/Aider** | `conseil` | "Voici comment mieux dormir" |
| **Inspirer/Émouvoir** | `histoire` | "Elle a tout perdu puis..." |
| **Divertir/Détendre** | `jokes` | "Mon cerveau à 3h du mat..." |
| **Engager/Impacter** | `default` | "Pourquoi tu doutes toujours?" |

---

## 🎨 Mix & Match

Tu peux varier les templates sur le même thème :

**Thème : Procrastination**
```bash
# Lundi - Conseil
python main.py "Procrastination" conseil

# Mercredi - Blague
python main.py "Procrastination" jokes

# Vendredi - Histoire
python main.py "Procrastination" histoire
```

→ **3 contenus différents, même thème !**

---

## ✨ Astuces Pro

### Pour CONSEIL
- Utilise des verbes d'action : "Fais", "Essaye", "Teste"
- Limite à 3-4 étapes max
- Thèmes : Productivité, Santé, Organisation

### Pour HISTOIRE
- Choisis des personnages connus (Einstein, Jobs, Rosa Parks)
- Ou des faits historiques marquants
- Thèmes : Persévérance, Courage, Innovation

### Pour JOKES
- Préfère l'humour d'observation (quotidien)
- Évite l'humour sensible
- Thèmes : Vie moderne, Travail, Réseaux sociaux

### Pour DEFAULT
- Utilise pour tous les sujets émotionnels
- Parfait pour les messages motivants
- Thèmes : Développement perso, Psychologie

---

## 🚀 Workflow Recommandé

### Semaine Type
- **Lundi** : Conseil (démarrer la semaine avec du pratique)
- **Mercredi** : Humour (détendre en milieu de semaine)
- **Vendredi** : Histoire (inspirer pour le week-end)
- **Dimanche** : Default (réflexion pour la semaine)

---

## 📝 Résumé Ultra-Rapide

```bash
# CONSEIL = "Comment faire X"
python main.py "Ton sujet" conseil

# HISTOIRE = "L'histoire de..."
python main.py "Ton sujet" histoire

# JOKES = "C'est drôle parce que c'est vrai"
python main.py "Ton sujet" jokes

# DEFAULT = "Message impactant"
python main.py "Ton sujet" default
```

**C'est tout ! 4 templates, possibilités infinies.** 🎉
