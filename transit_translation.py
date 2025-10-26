from env import DEEPL_API_KEY, ELEVEN_LABS_API_KEY
import requests
import deepl

translator = deepl.Translator(DEEPL_API_KEY)

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

def translate_text(text, language_name):
    if language_name not in language_codes:
        raise ValueError(f"Unsupported language: {language_name}")
    target_code = language_codes[language_name]
    result = translator.translate_text(text, target_lang=target_code)
    return result.text

text = "Hello, next stop is Market Street"
print("French:", translate_text(text, "French"))
print("Chinese:", translate_text(text, "Chinese (Simplified)"))
print("Spanish:", translate_text(text, "Spanish"))
print("Japanese:", translate_text(text, "Japanese"))