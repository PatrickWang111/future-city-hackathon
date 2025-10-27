# PolyVoice

Professional multi-lingual voice synthesis for transit systems using ElevenLabs and DeepL.

## Features
- Multi-language translation (English, French, Chinese, Spanish, German, Italian, Japanese, Korean)
- Multiple voice options (Adam, Rachel, Alice, Bill)
- Sequential audio playback in multiple languages
- Demo announcements for quick testing
- Real-time progress tracking

## Tech Stack
- **Frontend:** React, Tailwind CSS, HTML
- **Backend:** Flask, Python
- **APIs:** ElevenLabs (TTS), DeepL (Translation)

## Setup

### Backend
```bash
pip install -r requirements.txt
python app.py
```

### Frontend
Hosted on Render using Figma Make AI conversion to React.

## How It Works
1. User selects languages and a voice
2. Enters transit announcement text (or picks a demo)
3. Clicks "Generate Audio"
4. System translates text to each language
5. Generates speech using ElevenLabs
6. Plays audio sequentially for each language

## Demo
https://citron-silver-60211045.figma.site/
