# llm-fltenwall

## Install packages

pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

pip install modelscope==1.20.0
pip install transformers=4.51.0
pip install accelerate=1.6.0
pip install compressed-tensors=0.9.3
pip install flask==3.1.0

## Load Models

python model_download.py

## Running
python app.py
