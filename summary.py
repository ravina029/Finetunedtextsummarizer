import streamlit as st
import os
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
load_dotenv()

os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv('HUGGINGFACEHUB_API_TOKEN')
llm = HuggingFaceHub(repo_id="codebasics/finetuned-facebook-bart-samsum",model_kwargs={"temperature":0.1, "min_length":20,"max_length":500})


st.set_page_config(layout='wide')
st.title("Text Summarization")

# Input field for the text
text_input = st.text_area("Enter the text you want to summarize:")

# Prompt Template
summary_template = PromptTemplate(
    input_variables=['text'],
    template="Provide a concise summary of the following text including all the important aaspects of the text: {text}"
)

# Memory for conversation history
summary_memory = ConversationBufferMemory(input_key='text', memory_key='chat_history')

# LLM Chain with Hugging Face Hub
summary_chain = LLMChain(
    llm=llm,
    prompt=summary_template,
    output_key='summary',
    memory=summary_memory,
    verbose=True
)

# Button for summarization
summarize_button = st.button("Summarize")

if summarize_button or text_input:  # Summarize on button click or text input
    data_load_state = st.text('Summarizing...')
    summary = summary_chain.run(text=text_input)
     
    st.success("Summary Generated Successfully...")

    #columns for displaying text and summary
    col1, col2 = st.columns(2)
    with col1:
        st.header("Original Text:")
        st.write(text_input)
    with col2:
        st.header("Summary:")
        st.write(summary)

