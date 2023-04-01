import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.organization = "org-9gFweLPBiQroCILySsu6cZBQ"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()
