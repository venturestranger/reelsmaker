#!/bin/bash

PIPER_PATH="./piper"
PIPER_PRESETS_PATH="./piper_presets"
OUTPUT_PATH="./storage"

echo $2 | $PIPER_PATH/build/piper --espeak-data $PIPER_PATH/install/espeak-ng-data \
--model $PIPER_PRESETS_PATH/en_US-ryan-high.onnx \
--output_file $OUTPUT_PATH/$1.wav
