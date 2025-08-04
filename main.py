# First Cell: Setting Up Google Drive
# This project was originally done on Google Colab, so the files for each student were uploaded to Google Drive. 
from google.colab import drive
drive.mount('/content/Drive/')

#Second Cell: Installing Necessary Libraries
#Dotenv is only needed if you encrypt your API key for safety as a .env file. Otherwise, it is not needed for this program. 
!pip install python-dotenv
!pip install chromadb

#Third Cell: Imports
#Splitting my cells up is a personal preference, but I find a great deal of pleasure in being able to pick and choose specific blocks of code to run. 
from dotenv import dotenv_values
import glob
import matplotlib.pyplot as plt
import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb.utils.embedding_functions as embedding_functions #chromadb provides you with the option to get many embedding functions, so we're importing one here.

api_key = dotenv_values(".env")['OpenAI_APIkey']

#Fourth Cell: Step 1 - Data: 
chroma_client = chromadb.Client()
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key = api_key,
    model_name = "text-embedding-3-small"
)
collection = chroma_client.create_collection(name = "Student_Profiles",embedding_function = openai_ef)
import chromadb.utils.embedding_functions as embedding_functions
Brian_Light = "RAG-Project-Database-Files/Brian_Light.md"
Ava_Hatestring = "RAG-Project-Database-Files/Ava_Hatestring.md"
Arya_Arupathy = "RAG-Project-Database-Files/Arya_Arupathy.md"
collection.add(documents=[open(Brian_Light).read(),open(Ava_Hatestring).read(),open(Arya_Arupathy).read()],ids=["students1","students2","students3"])

#Fifth Cell: Step 1- Data Continued
#This was just me adding more data after the fact, to test and make sure that it was possible. 
Demetrius_Obole = "RAG-Project-Database-Files/Demetrius_Obole.md"
collection.add(documents=[open(Demetrius_Obole).read()],ids=["students4"])
print(open(Demetrius_Obole).read())

#Sixth Cell: Step 2 - Querying and Retrieval
query = "Tell me all about Shelrond Looper AND Timothey Shallotme. Would they be friends?"
relevant_info = []
for i in database:
  if i in query:
    relevant_info.append(database[i])
client = OpenAI(api_key=api_key)
completions = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "system", "content": f"You're an expert. Give brief, accurate answers. "},{"role":"user", "content":f"{query} Here is data that may be useful: {relevant_info}"}])
print(completions.choices[0].message.content)
