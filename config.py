class Config:
	OUTPUT_PATH = './storage/'
	OUTPUT_FILE = 'ret.mp4'
	IMAGE = ['png', 'jpg', 'jpeg', 'heic']
	VIDEO = ['mp4', 'mov', 'wmv', 'avi']
	AREA = [1280, 720]
	# FONT_PATH = './bebas.ttf'
	FONT_PATH = 'Arial'
	FONT_SIZE = 50
	CHARACTER_LIMIT = 25
	SUBS_SHIFT = 0.02
	TRANSLATE = '[^qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMйцукенгшщзхъфывапролдджэячсмитьбюёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДДЖЭЯЧСМИТЬБЮЁ\,\.\?\:\-\ ]'
	PUNCT = ',.?:-'
