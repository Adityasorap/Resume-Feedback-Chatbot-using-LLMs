import os
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

llm = Ollama(model="llama2")

prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
You are an expert resume reviewer. Provide constructive feedback on the following resume:

Resume:
{resume}

Your feedback should focus on:
1. Structure & Formatting
2. Clarity & Readability
3. Skills & Achievements
4. Suggestions for Improvement

Feedback:
"""
)

feedback_chain = LLMChain(llm=llm, prompt=prompt)

def get_resume_feedback(resume_text):
    return feedback_chain.run(resume=resume_text)
