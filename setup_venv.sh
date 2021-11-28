#!/bin/bash
python3 -m venv py3venv
source py3venv/bin/activate
mkdir input output originals
pip install -r requirements.txt
deactivate