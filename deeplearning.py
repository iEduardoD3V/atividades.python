# Reconhecimento de Voz
import speech_recognition as sr

rec = sr.Recognizer()

with sr.Microphone(3) as mic:
  rec.adjust_for_ambient_noise(mic)
  print("Pode falar que eu vou gravar")
  audio = rec.listen(mic)
  texto = rec.recognize_google(audio, language="pt-br")
  print(texto)