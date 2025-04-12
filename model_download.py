# model_download.py
from modelscope import snapshot_download

# model_dir = snapshot_download('LLM-Research/Llama-4-Scout-17B-16E-Instruct', cache_dir='./model', revision='master')


model_dir = snapshot_download('LLM-Research/gemma-3-1b-it', cache_dir='./model', revision='master')
# model_dir = snapshot_download('LLM-Research/Llama-4-Scout-17B-16E-Instruct-FP8', cache_dir='./model', revision='master')
# model_dir = snapshot_download('LLM-Research/Llama-4-Maverick-17B-128E-Instruct-FP8', cache_dir='请修改我！', revision='master')
