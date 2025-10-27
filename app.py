from flask import Flask, request, jsonify
from flask_cors import CORS
from transit_translation import save_audio, text_to_speech, translate_text

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'message': 'PolyVoice Transit API',
        'endpoints': {
            '/translate': 'POST - Translate text to different languages',
            '/generate-audio': 'POST - Generate audio from translated text'
        }
    })

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
        filename = f"{language}_{voice}.mp3"
        save_audio(audio_data, filename)
        
        # returns the audio as binary data
        return audio_data, 200, {'Content-Type': 'audio/mpeg'}
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)