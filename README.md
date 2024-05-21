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
