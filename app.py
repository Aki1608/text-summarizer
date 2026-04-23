import gradio as gr
from text_extractor import extract_txt_from_url
from summarizer_engine import SummarizerEngine

def process_user_input(input):
    if input.startswith("http"):
        text = extract_txt_from_url(input)
        original, summarized, comp_ratio = SummarizerEngine.summarize(text[:4000])
        return original, summarized, comp_ratio
    else:
        original, summarized, comp_ratio = SummarizerEngine.summarize(input)
        return original, summarized, comp_ratio


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# AI Document Summarizer")
    
    # The Input
    with gr.Row():
        user_input = gr.Textbox(lines=5, label="Paste URL or Text Here")
    
    # By defining the button right after the input, it renders directly below it!
    with gr.Row():
        submit_btn = gr.Button("Summarize Text", variant="primary")
        
    # The Outputs
    with gr.Row():
        # Left Side
        with gr.Column():
            output_1 = gr.Textbox(label="Original Text", lines=10)
            
        # Right Side
        with gr.Column():
            output_2 = gr.Textbox(label="AI Summary", lines=6)
            output_3 = gr.Label(label="Compression Ratio")

    submit_btn.click(
        fn=process_user_input, 
        inputs=[user_input], 
        outputs=[output_1, output_2, output_3]
    )

if __name__ == "__main__":
    demo.launch()
