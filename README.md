# LLM Text Summarization Project

This project involves building a web application which can generate concise and quality summaries of the input diaglogue text without losing the context of the input. This application can be used by different buisnesses to find out the summaries of the text recieved from a conversation between company representatives and the user, or conversation between the chatbot and the user, or other type of conversations. These summaries can be helpful to find out the insights from long conversations and can save time from hovering over to find the issues to address. 

Screenshots of some sample summaries:

![Alt Text](https://github.com/ravina029/TextSummarizer-finetuned-bart-samsum/raw/main/samharry1.png)

![Alt Text](https://github.com/ravina029/TextSummarizer-finetuned-bart-samsum/blob/main/samharry2.png)

![Alt Text](https://github.com/ravina029/TextSummarizer-finetuned-bart-samsum/blob/main/india.png)



# Project Structure:

1. Data ingestion
2. model fine tuning 
3. deploying it on Huggingface
4. loading the fintuned model on local machine using Huggingface API
5. Creating the streamlit web app to generate concise summaries for better user experience.

# Data Ingestion: 
Samsum dataset comprises 16,370 dialogues and their corresponding summaries.
Data can be downloaded fro kaggle https://www.kaggle.com/datasets/nileshmalode1/samsum-dataset-text-summarization
or from Huggingface site or using tne command "samsum=load_dataset('samsum')" using load_datset function.


# Model Finetuning 

1. first we loaded a base LLM [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn) from hugging face. this model is a text summarization model trained on cnn dataset containing news articles and their summaries.


2. Above base model is fine tuned on samsum dataset to get: finetuned-facebook-bart-samsum  [codebasics/finetunedN-facebook-bart-samsum](https://huggingface.co/codebasics/finetunedN-facebook-bart-samsum/commit/2e5c2086edc535c995ed6b8666daa0e718a83b82). Which utalizes the text summarization capbilities of the base model to create concise summaries of the dialogue based data. 
2. Samsum dataset is invaluable for fine-tuning summarization models specifically tailored for dialogue summarization tasks. The model's applicability extends to various scenarios, such as analyzing conversations between customers and support teams in financial entities, e-commerce companies, or any other organization. By leveraging the model's capabilities, organizations can extract concise summaries of these conversations, enabling them to provide more effective solutions to their customers.

4. Given that the base model, facebook/bart-large-cnn, is trained on the CNN news dataset, this fnetuned model demonstrates proficiency in generating high-quality summaries for a wide range of text data.
5. Training was limited to one epoch due to constraints posed by the large dataset and memory limitations. This restriction led to an average training loss of approximately 1.428.

6. Performance metrices of base model and fintuned model
   Base Model:

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

6. Further the model's performance can be enhanced by increasing the number of training epochs.

7. The finetuned model is downloaded on the local machine using Huggiface API.


# Streamlit application:
I have developed a user-friendly streamlit application for easy usability and better experience. This application utilizes the finetuned-facebook-bart-samsum model available on the Hugging Face platform to generate summaries of dialogue or simple text. Users can input text, and the application will generate a concise summary, highlighting the essential aspects of the input.




# Steps to run the streamlit application:


clone the repository: https://github.com/ravina029/TextSummarizer-finetuned-bart-samsum/tree/main


1. Create a virtual environment (recommended) and activate it.

2. Install the required depencies.

3. Create a file named app.py and paste the code in the file summaryfinetuned.py.

4. Create a file named .env in the same directory as summaryfinetuned.py, 
   Add the line HUGGINGFACEHUB_API_TOKEN=YOUR_API_TOKEN
   ,replace YOUR_API_TOKEN with your Hugging Face Hub API token. (never share your API token)

5. Run the application from your terminal:
   streamlit run app.py

6. A Streamlit web app will open in your browser. Enter text in "Enter the text you want to summarize:" field and click "Summarize".

7. The application will display the summarized text alongside the original input.



# Points of improvement: 
Quality of summry can be improved by thraining the model for more than 1 epoch.