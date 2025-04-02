from transformers import pipeline, AutoTokenizer
import gradio as gr

tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

MAX_TOKENS = 1024 
    
def summarize_text(text):
    tokens = tokenizer.encode(text, return_tensors='pt')
    token_length = len(tokens[0])
    
    if token_length > MAX_TOKENS:
        return print(f"Input text is too long. The text contains {token_length} tokens, which exceeds the {MAX_TOKENS} token limit.")
    
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

iface = gr.Interface(
    fn=summarize_text,
    inputs="textbox",
    outputs="textbox",
    title="AI Text Summarization",
    description="Enter text and get a summary."
)

iface.launch()