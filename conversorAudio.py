# Reconhecimento de Voz audio em texto
import speech_recognition as sr

# Antes de rodar precisar instalar essas duas api 🔽🔽

# pip install pyaudio
# pip install SpeechRecognition

rec = sr.Recognizer()

with sr.Microphone(1) as mic:
  rec.adjust_for_ambient_noise(mic)
  print("Pode falar que eu vou gravar")
  audio = rec.listen(mic)
  texto = rec.recognize_google(audio, language="pt-br")
  print(texto)