import os
import requests

def text_to_speech(text, voice='en-US-Wavenet-D'):
    url = 'https://api.piper.ponte.com/v1/text-to-speech'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {os.getenv("PIPER_API_KEY")}'
    }
    data = {
        'text': text,
        'voice': voice,
        'output_format': 'mp3'
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        with open('output.mp3', 'wb') as audio_file:
            audio_file.write(response.content)
        print("Audio saved as output.mp3")
    else:
        print(f"Error: {response.status_code} - {response.text}")
