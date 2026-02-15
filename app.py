import os
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Coloque sua chave da LamaTok aqui ou nas configurações do Render
API_KEY = os.environ.get('LAMATOK_KEY', 'SUA_CHAVE_AQUI')

@app.route('/', methods=['GET', 'POST'])
def index():
    video_data = None
    if request.method == 'POST':
        url_input = request.form.get('url')
        api_url = f"https://api.lamatok.com/v1/media/video/download/by/url?url={url_input}"
        headers = {'access_key': API_KEY}
        
        try:
            response = requests.get(api_url, headers=headers).json()
            if 'video_url' in response:
                video_data = response['video_url']
        except:
            video_data = "erro"

    return render_template('index.html', video=video_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
