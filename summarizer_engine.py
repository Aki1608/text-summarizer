from transformers import pipeline
import requests
from bs4 import BeautifulSoup

class SummerizerEngine:
    model = 'facebook/bart-large-cnn'
    try:
        summerizer = pipeline('summerizer', f"{model}")
    except Exception as e:
        print(f"Failed to load the model {model}.")
        summerizer = None

    @staticmethod
    def summerize(text):
        if len(text) < 100:
            print('Error: Text is too short to summarize.')

        summarize_text = SummerizerEngine.summerizer(text, max_length=130, min_length=30, do_sample=False)['summary_text']
        compression_ratio = (len(text)-len(summarize_text))/len(text)*100

        return text, summarize_text, compression_ratio
