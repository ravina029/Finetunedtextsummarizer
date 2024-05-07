# finetuned-facebook-bart-samsum  [codebasics/finetunedN-facebook-bart-samsum](https://huggingface.co/codebasics/finetunedN-facebook-bart-samsum/commit/2e5c2086edc535c995ed6b8666daa0e718a83b82)

1. This model is a fine-tuned version of [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn) on samsum dataset. Which utalizes the text summarization capbilities of the base model. 
2. This model is primarily trained on the samsum dataset, which comprises 16,370 dialogues and their corresponding summaries. The dataset is invaluable for fine-tuning summarization models specifically tailored for dialogue summarization tasks. The model's applicability extends to various scenarios, such as analyzing conversations between customers and support teams in financial entities, e-commerce companies, or any other organization. By leveraging the model's capabilities, organizations can extract concise summaries of these conversations, enabling them to provide more effective solutions to their customers.

4. Given that the base model, facebook/bart-large-cnn, is trained on the CNN news dataset, this fnetuned model demonstrates proficiency in generating high-quality summaries for a wide range of text data.
5. Training was limited to one epoch due to constraints posed by the large dataset and memory limitations. This restriction led to an average training loss of approximately 1.428.
6. Original Model:

                  Rouge-1: 0.0923
                  Rouge-2: 0.0178
                  Rouge-L: 0.0771
                  Rouge-Lsum: 0.0754
   
  Fine-tuned Model:

                  Rouge-1: 0.1491
                  Rouge-2: 0.0619
                  Rouge-L: 0.1152
                  Rouge-Lsum: 0.1152
The fine-tuned model consistently outperforms the original model across all Rouge metrics, demonstrating its improved summarization capabilities after fine-tuning for dialogue summarization task.

6. Further enhancing the model's performance can be achieved by increasing the number of training epochs


# Streamlit application:
I have developed a Streamlit application to enhance usability and provide a user-friendly experience. This application utilizes the finetuned-facebook-bart-samsum model available on the Hugging Face platform to generate summaries of dialogue or simple text. Users can input text, and the application will generate a concise summary, highlighting the essential aspects of the input.


Screenshots of some sample summaries:

![Alt Text](https://github.com/ravina029/TextSummarizer-finetuned-bart-samsum/raw/main/samharry1.png)

![Alt Text](https://github.com/ravina029/TextSummarizer-finetuned-bart-samsum/blob/main/samharry2.png)

![Alt Text](https://github.com/ravina029/TextSummarizer-finetuned-bart-samsum/blob/main/india.png))


# Steps to develop interactive streamlit application using finetuned-facebook-bart-samsum model:

## Requirements

1. Python==3.10 
2. Streamlit==1.33.0
3. LangChain==0.1.15
4. huggingface_hub==0.22.2
5. python-dotenv==1.0.1

# Installation

1. Create a virtual environment (recommended) and activate it.
2. Install the required libraries
3. Create a file named app.py and paste the code in the file summaryfinetuned.py.
4. Create a file named .env in the same directory as summaryfinetuned.py, Add the line HUGGINGFACEHUB_API_TOKEN=YOUR_API_TOKEN
,replace YOUR_API_TOKEN with your Hugging Face Hub API token. (never share your API token)
5. Run the application from your terminal:
   streamlit run app.py
6. A Streamlit web app will open in your browser. Enter text in the "Enter the text you want to summarize:" field and click "Summarize".

7. The application will display the summarized text alongside the original input.

