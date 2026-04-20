from transformers import pipeline

class SummerizerEngine:
    model = 'facebook/bart-large-cnn'
    try:
        summerizer = pipeline('summerizer', f"{model}")
    except Exception as e:
        print(f"Failed to load the model {model}.")
        summerizer = None

    @staticmethod
    def get_summery(text):
        if len(text) < 100:
            error "Text is too short to summerize."        