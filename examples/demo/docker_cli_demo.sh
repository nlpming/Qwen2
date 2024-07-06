#!/bin/sh

#sudo docker run -d --gpus all -v ~/workspace:/home -p 8060:8888 nlpming/qwen:v1.0 \
#  bash -c "while true; do sleep 1000; done"

sudo docker run -d --gpus all -v ~/workspace:/home -p 8060:8888 nlpming/qwen:v1.0 \
  python cli_demo.py -c /home/nlpming/workspace/Qwen2/models/Qwen2-0.5B-Instruct


