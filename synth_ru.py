from TeraTTS import TTS
from ruaccent import RUAccent
from config import Config


accentizer = RUAccent()
accentizer.load(omograph_model_size='turbo', use_dictionary=True)
tts = TTS("TeraTTS/natasha-g2p-vits", add_time_to_end=1, tokenizer_load_dict=True)


def synth(filename, text):
	text = accentizer.process_all(text)
	audio = tts(text, lenght_scale=0.9) 
	tts.save_wav(audio, Config.OUTPUT_PATH + f'{filename}.wav')
