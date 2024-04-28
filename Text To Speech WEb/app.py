from flask import Flask, render_template, request
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_text_to_speech():
    text = request.form['text']
    if text:
        tts = gTTS(text=text, lang='en')
        tts.save('static/output.mp3')
        return render_template('index.html', text=text, converted=True)
    else:
        return render_template('index.html', error=True)

if __name__ == '__main__':
    app.run(debug=True)
