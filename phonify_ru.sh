#!/bin/bash

PIPER_PATH="./piper/piper"
OUTPUT_PATH="./storage"

echo $2 | $PIPER_PATH/build/piper --espeak-data $PIPER_PATH/install/espeak-ng-data \
--model $PIPER_PATH/build/ru_RU-denis-medium.onnx \
--output_file $OUTPUT_PATH/$1.wav