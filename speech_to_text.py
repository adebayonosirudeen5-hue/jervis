import whisper

class SpeechToText:
    def __init__(self, model_size='small'):
        self.model = whisper.load_model(model_size)

    def transcribe(self, audio_file):
        result = self.model.transcribe(audio_file)
        return result['text']

# Example usage:
# stt = SpeechToText()
# text = stt.transcribe('path_to_audio.wav')
# print(text)