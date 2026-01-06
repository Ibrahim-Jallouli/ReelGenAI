# 🎬 AI Reel Generator

> **⚠️ POC (Proof of Concept)** - This project is an experiment to test AI-assisted development. The goal was to build a functional project while writing as little code as possible, mainly through AI prompts.

## 💡 The Idea

Create an automatic content generator for **Reels/TikTok**:
- You provide a topic (e.g., "Self-confidence")
- AI generates a script optimized for social media
- The script is converted to audio (voice-over)
- You get an MP3 file ready to use on your video

## 🔧 APIs Used

| API | Role | Cost |
|-----|------|------|
| **Google Gemini** | Script generation with optimized prompts | Free (generous quota) |
| **Google Cloud TTS** | Neural2 speech synthesis (natural voices) | Free (1M characters/month) |

## 🔄 Execution Pipeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Terminal: python main.py "Productivity" conseil reel_female               │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  1️⃣ ARGUMENT PARSING                                                        │
│     • theme = "Productivity"                                                │
│     • template = "conseil"                                                  │
│     • voice = "reel_female"                                                 │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  2️⃣ PROMPT GENERATION                                                       │
│     • Template selection (conseil, histoire, jokes, default)               │
│     • Theme injection into the prompt                                      │
│     • Structured prompt construction for Gemini                            │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  3️⃣ GOOGLE GEMINI API CALL                                                  │
│     • Send prompt to Gemini API                                            │
│     • Receive generated script (20-40 sec of content)                      │
│     • Save to output/scripts/response_*.txt                                │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  4️⃣ SPEECH SYNTHESIS (Google Cloud TTS)                                     │
│     • Script cleanup (remove metadata, emojis)                             │
│     • Text → audio conversion with Neural2 voice                           │
│     • Export MP3 to output/audio/reel_*.mp3                                │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  📦 FINAL OUTPUT                                                            │
│     • output/scripts/response.txt  (text script)                           │
│     • output/audio/reel.mp3        (audio voice-over)                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

## 🚀 Usage

```bash
# Basic
python main.py "Self-confidence"

# With specific template
python main.py "Productivity" conseil

# With custom voice
python main.py "Inspiring story" histoire story
```

### Available Templates
- `default` - Viral content (strong hooks)
- `conseil` - Practical tips
- `histoire` - Emotional storytelling
- `jokes` - Observational humor

### Available Voices
- `reel_male` / `reel_female` - Energetic
- `story` - Narrative
- `calm` - Soothing

## ⚙️ Configuration

1. Copy `config/settings.yaml.example` → `config/settings.yaml`
2. Add your Gemini key: [Google AI Studio](https://makersuite.google.com/app/apikey)
3. Configure Google Cloud TTS: [Console](https://console.cloud.google.com/) → Enable Text-to-Speech API → Create service account JSON key

## 📂 Structure

```
project/
├── main.py                 # CLI entry point
├── src/
│   ├── app.py              # Main pipeline
│   ├── gemini/             # Gemini API client
│   ├── prompts/            # Prompt templates
│   ├── tts/                # Speech synthesis
│   └── utils/              # Logger
├── config/                 # Configuration (API keys)
└── output/                 # Generated scripts and audio
```

## 🚧 Future Improvements

This POC can be extended to create **complete Reels**:

1. **Image Collection** - Use Pixabay/Pexels API to fetch images based on script keywords
2. **Subtitle Generation** - Sync text with audio
3. **Video Assembly** - Combine images + audio + subtitles with MoviePy/FFmpeg
4. **Final Export** - Reel ready to publish on Instagram/TikTok

```
Script → Images (Pixabay) → Audio (TTS) → Subtitles → Final Video
```

## 📄 License

MIT License

---

**🧪 AI Experiment** - Project built primarily through AI prompts to explore AI-assisted development possibilities.

<img width="1209" height="482" alt="Screenshot 2026-01-06 174519" src="https://github.com/user-attachments/assets/311bf966-441b-4c11-b354-8380f9135ded" />
