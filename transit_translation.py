from env import DEEPL_API_KEY, ELEVEN_LABS_API_KEY
import requests
import deepl

translator = deepl.Translator(DEEPL_API_KEY)

# ElevenLabs voices
voice_ids = {
    "adam": "pNInz6obpgDQGcFmaJgB",
    "rachel": "21m00Tcm4TlvDq8ikWAM",
    "alice": "Xb7hH8MSUJpSbSDYk0k2",
    "bill": "pqHfZKP75CvOlQylNhV4"
}

# DeepL language codes
language_codes = {
    "English": "EN-US",
    "French": "FR",
    "Chinese (Simplified)": "ZH-HANS",
    "Spanish": "ES",
    "German": "DE",
    "Italian": "IT",
    "Portuguese": "PT-PT",
    "Japanese": "JA",
    "Korean": "KO",
}

# DeepL function
def translate_text(text, language_name):
    if language_name not in language_codes:
        raise ValueError(f"Unsupported language: {language_name}")
    target_code = language_codes[language_name]
    result = translator.translate_text(text, target_lang=target_code)
    return result.text

# ElevenLabs function
def text_to_speech(text, voice_name="adam"):
    # get voice ID from dictionary, with validation
    if voice_name not in voice_ids:
        raise ValueError(f"Unsupported voice: {voice_name}. Available voices: {list(voice_ids.keys())}")
    
    voice_id = voice_ids[voice_name]
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "Accept": "audio/mpeg",
        "xi-api-key": ELEVEN_LABS_API_KEY,
        "Content-Type": "application/json"  
    }

    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,  # how consistent the voice is (0-1), higher is more monitone lower is more expressive
            "similarity_boost": 0.75  # how close to original voice it is (0-1)
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.content  # this is the audio file as bytes
    else:
        raise Exception(f"ElevenLabs API error: {response.status_code} - {response.text}")
    
def save_audio(audio_bytes, filename):
    # audio bytes is the Elevenlabs data

    with open(filename, "wb") as f:  # write binary mode
        f.write(audio_bytes)
    print(f"Audio saved to {filename}")

# combine translation and Text-To-Speech
def translate_and_speak(text, target_language, voice_name="adam", output_file="output.mp3"):
    # translate the text
    translated_text = translate_text(text, target_language)
    print(f"Translated Text ({target_language}): {translated_text}")
    
    # convert translated text to speech
    audio_data = text_to_speech(translated_text, voice_name)
    
    # save the audio data to a file
    save_audio(audio_data, output_file)

if __name__ == "__main__":
    # tests the full pipeline
    text = "Hello, next stop is Market Street"
    translate_and_speak(text, "French", voice_name="rachel", output_file="test_french.mp3")
    translate_and_speak(text, "Chinese (Simplified)", voice_name="adam", output_file="test_chinese.mp3")