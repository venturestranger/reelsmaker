from moviepy.editor import VideoFileClip, ImageClip, AudioFileClip, TextClip, CompositeVideoClip, concatenate_videoclips
from config import Config
from moviepy.video.fx.all import crop
import random
import os
import re


# remove all extra characters
def preprocess_text(text: str) -> str:
	text = re.sub(Config.TRANSLATE, '', text)
	return text


# split by punct characters specified in the config file
def split_by_punct(text: str) -> list:
	for character in Config.PUNCT:
		text = text.replace(character, '@#$')
	return list(filter(lambda x: len(x) != 0, text.split('@#$')))


# generate a random name
def get_random_name() -> str:
	alphabet = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
	return ''.join([random.choice(alphabet) for i in range(30)])


# generate subtitles from a given text and audio duration
def generate_subtitles(text: str, duration: float, shift: float) -> list:
	subtitles = []
	prv_len = 0

	for chunk in split_by_punct(text):
		words = chunk.split(' ')
		buffer = ''

		for i in range(len(words)):
			if len(buffer + words[i]) < Config.CHARACTER_LIMIT:
				buffer += words[i] + ' '
			else:
				subtitles.append({'text': buffer.strip(), 'start': prv_len})
				prv_len += duration * len(buffer) / len(text) - shift * len(buffer)
				buffer = words[i] + ' '

		if buffer != '':
			subtitles.append({'text': buffer.strip(), 'start': prv_len})
			prv_len += duration * len(buffer) / len(text) - shift * len(buffer.split())
	
	return subtitles


# generate an audio file from a piece of text
def generate_audio(name: str, text: str, lang: str = 'Русский', driver = None) -> str:
	if lang == 'Русский':
		# os.system(f'./phonify_ru.sh "{name}" "{text}"')
		driver(name, text)
	else:
		os.system(f'./phonify_en.sh "{name}" "{text}"')

	return name


# remove a storage from files
def remove_files(file_type: str = '.wav'):
	try:
		if file_type == '':
			os.system(f'mv {Config.OUTPUT_PATH}{Config.OUTPUT_FILE} {Config.OUTPUT_PATH}.tmp')

		os.system('rm ./storage/*' + file_type)

		if file_type == '':
			os.system(f'mv {Config.OUTPUT_PATH}.tmp {Config.OUTPUT_PATH}{Config.OUTPUT_FILE}')
	except:
		pass


# generate a video file from the collected media (video, imgs, audio)
def generate_video(media: list, audio: list, text: list, shift: float):
	video_clips = []

	for i in range(len(media)):
		if audio[i] != None:
			audio_clip = AudioFileClip(audio[i])

			file_name = Config.OUTPUT_PATH + get_random_name() + '.' + media[i].name.split('.')[-1]

			with open(file_name, 'wb') as f:
				f.write(media[i].read())

			if media[i].name.split('.')[-1] in Config.VIDEO:
				video_clip = VideoFileClip(file_name).subclip(0, audio_clip.duration)
			else:
				video_clip = ImageClip(file_name, duration=audio_clip.duration)

			if video_clip.h / video_clip.w <= 16 / 9:
				video_clip = video_clip.resize(height=Config.AREA[0])
			else:
				video_clip = video_clip.resize(width=Config.AREA[1])

			video_clip = crop(video_clip, height=Config.AREA[0], width=Config.AREA[1], x_center=video_clip.size[0] // 2, y_center=video_clip.size[1] // 2)

			subtitles = []
			subs = generate_subtitles(preprocess_text(text[i]), audio_clip.duration, shift)
			for i in range(len(subs)):
				subtitle = subs[i]

				text_clip = TextClip(subtitle['text'], font=Config.FONT_PATH, fontsize=Config.FONT_SIZE, color='white', bg_color='black')
				text_clip = text_clip.set_start(subtitle['start'])
				if subs[(i + 1) % len(subs)]['start'] != 0:
					text_clip = text_clip.set_end(subs[(i + 1) % len(subs)]['start'])
				text_clip = text_clip.set_position(((Config.AREA[1] - text_clip.w) / 2, (Config.AREA[0] - text_clip.h) * 7/8))
				subtitles.append(text_clip)

			video_clip.audio = audio_clip
			video_clip = CompositeVideoClip([video_clip, *subtitles]).set_duration(audio_clip.duration)
			video_clips.append(video_clip)

	final_clip = concatenate_videoclips(video_clips)
	logo_clip = ImageClip(Config.LOGO_PATH).resize(width=Config.LOGO_WIDTH)

	final_clip = CompositeVideoClip([final_clip, logo_clip.set_position(Config.LOGO_POSITION)]).set_duration(final_clip.duration)
	file_name = f'{Config.OUTPUT_PATH}{Config.OUTPUT_FILE}'
	final_clip.write_videofile(file_name, fps=30, codec='libx264', audio_codec='aac')
