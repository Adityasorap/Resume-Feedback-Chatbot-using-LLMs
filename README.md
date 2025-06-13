# Resume-Feedback-Chatbot-using-LLMs
# 📄 Resume Feedback Chatbot using LLMs

This is an AI-powered chatbot that reviews resumes using LLaMA 2 via Ollama. Built with LangChain and Streamlit, it provides real-time feedback on structure, clarity, and impact.

## 🚀 Tech Stack
- Python
- Streamlit
- LangChain
- Ollama
- LLaMA 2
- Prompt Engineering

## 💻 How It Works
- You paste your resume text.
- The app sends the content to LLaMA 2 running locally via Ollama.
- LangChain chains the prompt and gets structured feedback.

## 🔧 Setup Instructions

```bash
# 1. Clone the repo
$ git clone https://github.com/yourusername/resume-feedback-bot.git
$ cd resume-feedback-bot

# 2. Set up environment
$ python -m venv venv
$ source venv/bin/activate  # Windows: venv\Scripts\activate
$ pip install -r requirements.txt

# 3. (Optional) Set .env if customizing Ollama
# OLLAMA_BASE_URL=http://localhost:11434

# 4. Make sure Ollama is running with LLaMA 2
$ ollama run llama2

# 5. Launch the app
$ streamlit run app.py
