import OpenAI
import json, os
# from dotenv import load_dot_env

# load_dot_env()
# openai_api_key = os.getenv('openai_api_key')
# print(openai_api_key)

def get_api_key():
  with open(r'..\..\..\..\Python\config.json') as config_file:
    config = json.load(config_file)
  return config['openai_api_key']

client = OpenAI.openai
