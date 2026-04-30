import pvporcupine
import pyaudio

class WakeWordDetector:
    def __init__(self, access_key):
        self.porcupine = pvporcupine.create(key=access_key)
        self.audio = pyaudio.PyAudio()

    def start(self):
        with self.audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.porcupine.sample_rate,
            input=True,
            frames_per_buffer=self.porcupine.frame_length,
        ) as stream:
            print("Listening for wake word...")
            while True:
                pcm = stream.read(self.porcupine.frame_length)
                pcm = np.frombuffer(pcm, dtype=np.int16)
                keyword_index = self.porcupine.process(pcm)

                if keyword_index >= 0:
                    print("Wake word detected!")
                    break

    def stop(self):
        self.porcupine.delete()
        self.audio.terminate()

if __name__ == '__main__':
    detector = WakeWordDetector(access_key='your_access_key_here')
    try:
        detector.start()
    except KeyboardInterrupt:
        print("Stopped by user")
    finally:
        detector.stop()