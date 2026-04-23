from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class SummarizerEngine:
    model_name = 'sshleifer/distilbart-cnn-12-6'
    
    try:
        # Load the Dictionary (Tokenizer)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        # Load the Brain (Model)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    except Exception as e:
        print(f"Failed to load the model components: {e}")
        tokenizer = None
        model = None
    # model = 'sshleifer/distilbart-cnn-12-6'
    # try:
    #     summerizer = pipeline(model=f"{model}")
    # except Exception as e:
    #     print(f"Failed to load the model {e}.")
    #     summerizer = None

    # @staticmethod
    # def summerize(text):
    #     if len(text) < 100:
    #         print('Error: Text is too short to summarize.')

    #     summarize_text = SummerizerEngine.summerizer(text, max_length=130, min_length=30, do_sample=False)['summary_text']
    #     compression_ratio = (len(text)-len(summarize_text))/len(text)*100

    #     return text, summarize_text, compression_ratio

    @staticmethod
    def summarize(text):
        if len(text) < 100:
            return "Error: Text is too short to summarize.", "", "0%"

        if SummarizerEngine.model is None:
            return "Model failed to load.", "", "0%"

        # 1. Translate English to Numbers (Tokens)
        # We set truncation=True so it doesn't crash if the article is massively long
        inputs = SummarizerEngine.tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)

        # 2. Generate the Summary (in Numbers)
        summary_ids = SummarizerEngine.model.generate(
            inputs["input_ids"], 
            max_length=130, 
            min_length=30, 
            do_sample=False
        )

        # Translate Numbers back to English
        # skip_special_tokens removes the hidden AI tags like <s> and </s>
        summarize_text = SummarizerEngine.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        compression_ratio = ((len(text) - len(summarize_text)) / len(text)) * 100
        ratio_str = f"Reduced by {compression_ratio:.2f}%"

        return text, summarize_text, ratio_str
