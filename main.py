import streamlit as st
from utils import preprocess_text
from utils import generate_audio
from utils import get_random_name
from utils import generate_video
from utils import remove_files
from config import Config
import os


# initialization of supplemental drivers for speech synthesis
if st.session_state.get('initialized', False) == False:
	from synth_ru import synth
	st.session_state['ru_synth_driver'] = synth
	st.session_state['initialized'] = True


# media and text fields
media = []
text = []
audio = []
lang = st.radio(
	'Choose reels language / выберите язык для reels',
	['Русский', 'English'],
	index=0
)


# removes all previously generated audio
# remove_files('wav')


# implements video and audio dropdown menu
for i in range(st.session_state.get('piece_count', 1)):
	media.append(st.file_uploader('Drop your media / предоставьте ваше медиа', type=['mp4', 'wmv', 'mov', 'png', 'jpg', 'jpeg', 'heic', 'avi'], key=f'media_{i}'))
	text.append(st.text_area('Input text / введите текст', key=f'text_{i}').strip())

	if text[-1] != None and len(text[-1].strip()) != 0 and not os.path.exists(Config.OUTPUT_PATH + str(hash(text[-1]))[1:] + '.wav'):
		name = generate_audio(str(hash(text[-1]))[1:], preprocess_text(text[-1]), lang, st.session_state['ru_synth_driver'])
		audio.append(Config.OUTPUT_PATH + f'{name}.wav')
		st.audio(Config.OUTPUT_PATH + f'{name}.wav')
	elif os.path.exists(Config.OUTPUT_PATH + str(hash(text[-1]))[1:] + '.wav'):
		name = str(hash(text[-1]))[1:]
		audio.append(Config.OUTPUT_PATH + f'{name}.wav')
		st.audio(Config.OUTPUT_PATH + f'{name}.wav')
	else:
		audio.append(None)


# implements media removal an X button
if media[-1] != None:
	st.session_state['piece_count'] = st.session_state.get('piece_count', 1) + 1
	st.rerun()
elif len(media) > 1 and media[-2] == None:
	st.session_state['piece_count'] = st.session_state.get('piece_count', 1) - 1
	st.rerun()


# triggers clip generation
if st.button('Generate a clip / создать клип'):
	if any([i == None for i in media[:-1]]) or any([i == None for i in audio[:-1]]) or len(media) == 1:
		st.error('Fill in all fields / Заполните все поля')
	else:
		generate_video(media[:-1], audio[:-1], text[:-1])
		for file_type in Config.VIDEO:
			if file_type != 'mp4':
				remove_files(file_type)
		for file_type in Config.IMAGE:
			remove_files(file_type)


try:
	st.video(Config.OUTPUT_PATH + Config.OUTPUT_FILE)
	with open(Config.OUTPUT_PATH + Config.OUTPUT_FILE, 'rb') as f:
		st.download_button('Download / загрузить', f.read(), file_name='generated_video.mp4')
except:
	pass
