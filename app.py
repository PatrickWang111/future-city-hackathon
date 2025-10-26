from flask import Flask, request, jsonify
from transit_translation import save_audio, text_to_speech, translate_text

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text')
    language = data.get('language')

    if not text or not language:
        return jsonify({'error': 'Missing text or language parameter'}), 400

    try:
        translated_text = translate_text(text, language)
        return jsonify({'translated_text': translated_text})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    
@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    data = request.json
    text = data.get('text')
    language = data.get('language')
    voice = data.get('voice', 'adam')
    
    try:
        translated = translate_text(text, language)
        audio_data = text_to_speech(translated, voice)
        # Save and return filename
        filename = f"{language}_{voice}.mp3"
        save_audio(audio_data, filename)
        return jsonify({'audio_file': filename, 'translated_text': translated})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)