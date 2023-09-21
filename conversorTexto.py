from gtts import gTTS

def texto_para_voz(texto, audio):
  tts = gTTS(texto,lang='pt-br')
  
  tts.save(audio)
  
texto = """Seja bem vindo ao mundo de 2044!❤"""

audio = "vozSintetica.mp3"

texto_para_voz(texto, audio)

print(f"Áudio salvo como{audio}")