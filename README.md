# ai-text-summarization-app

This project is an AI-based **Text Summarization App** built using the **BART model** from **Hugging Face** and **Gradio** for creating an interactive web interface. The app allows users to input any text and receive a concise, AI-generated summary.

## Features
- **Text Summarization**: The app uses the pretrained BART model from Hugging Face to summarize input text.
- **Interactive Interface**: Built with Gradio to provide an easy-to-use web interface for summarizing text in real-time.
- **Token Length Validation**: The app checks if the input text exceeds the token limit for the model and raises an appropriate error.
- **Pretrained Model**: The app uses **Hugging Face's BART model** fine-tuned for summarization tasks.

## Installation

1. **Clone this repository**:

```bash
git clone https://github.com/yourusername/ai-text-summarization-app.git
```

2. **Install the required dependencies**:

```bash
pip install -r requirements.txt
```

`requirements.txt` includes:
- `transformers`
- `gradio`
- `torch`
  
3. **Run the app**:

```bash
python app.py
```
