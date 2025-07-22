from gtts import gTTS
import tempfile
import pygame
import time

def speak(text):
    tts = gTTS(text=text)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tts.save(tmp.name)

        pygame.mixer.init()
        pygame.mixer.music.load(tmp.name)
        pygame.mixer.music.play()

        # 等待播放结束
        while pygame.mixer.music.get_busy():
            time.sleep(0.3)