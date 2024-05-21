# Automated Reels Generation

This program provides an interface for automatic reels generation in multiple languages (currently supports English and Russian). It utilizes `Streamlit` for interface rendering, `MoviePy` for video compilation, and `Piper` for speech synthesis in different languages.

## Installation
To install the required libraries, run:
```bash
$> pip install -r requirements.txt
$> git clone https://github.com/rhasspy/piper
$> cd piper
$> make
```
Download `en_US-ryan-high.onnx`, `en_US-ryan-high.onnx.json`, `ru_RU-dmitri-medium.onnx`, `ru_RU-dmitri-medium.onnx.json` voices from `https://github.com/rhasspy/piper/blob/master/VOICES.md` and place them in `piper_presets` folder.

## Run
To start the program, run:
```bash
$> streamlit run main.py
```

## Interface
The interface includes the following features:

- **Language Selection:** A radio button to choose the desired language.
- **Media Upload Fields:** Fields for uploading media materials (videos or pictures) and specifying text for speech synthesis.

### Steps to Use the Interface:
1. **Choose Media and Text:**
   - Upload your media materials and specify the text for speech synthesis.
   - The interface will then display two additional fields for uploading extra media material (optional).

2. **Remove Redundant Fields:**
   - If you need to remove any redundant fields, start with the last ones and clear all specified data.

3. **Generate the Clip:**
   - Press the `Generate a clip` button to compile the reel. The compilation time may vary based on the amount of data and your computational power.

4. **Download the Clip:**
   - Once the clip is generated, press the `Download` button to save it.

This program streamlines the process of creating multimedia reels with synthesized speech.

---

Эта программа предоставляет интерфейс для автоматического создания барабанов на нескольких языках (в настоящее время поддерживается английский и русский). Он использует `Streamlit` для рендеринга интерфейса, `MoviePy` для компиляции видео и `Piper` для синтеза речи на разных языках.

## Установка
Чтобы установить необходимые библиотеки, запустите:
```bash
$> pip install -r requirements.txt
$> git clone https://github.com/rhasspy/piper
$> cd piper
$> make
```
Загрузите голоса `en_US-ryan-high.onnx`, `en_US-ryan-high.onnx.json`, `ru_RU-dmitri-medium.onnx`, `ru_RU-dmitri-medium.onnx.json` с `https:/ /github.com/rhasspy/piper/blob/master/VOICES.md` и поместите их в папку `piper_presets`.

## Запуск
Чтобы запустить программу, запустите:
```bash
$> streamlit run main.py
```

## Интерфейс
Интерфейс включает в себя следующие функции:

- **Выбор языка:** переключатель для выбора желаемого языка.
- **Поля загрузки мультимедиа:** Поля для загрузки медиаматериалов (видео или изображений) и указания текста для синтеза речи.

### Шаги по использованию интерфейса:
1. **Выбрать медиафайл и текст:**
    - Загрузите свои медиаматериалы и укажите текст для синтеза речи.
    - В интерфейсе отобразятся два дополнительных поля для загрузки дополнительных медиаматериалов (необязательно для заполнения).

2. **Удалить лишние поля:**
    - Если вам нужно удалить лишние поля, начните с последних и очистите все указанные данные.

3. **Создать клип:**
    - Нажмите кнопку `Создать клип`, чтобы скомпилировать ролик. Время компиляции может варьироваться в зависимости от объема данных и вашей вычислительной мощности.

4. **Загрузить клип:**
    - После создания клипа нажмите кнопку `Загрузить`, чтобы сохранить его.
