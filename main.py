import psycopg2
from psycopg2 import sql
from Dataset_Loader import load_data
from langchain import SQLDatabase, SQLDatabaseChain
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
import os


#load_data()
username = "postgres" 
password = "joelbunyan" 
host = "localhost" 
port = "5432"
mydatabase = "Finance---database"

pg_uri = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{mydatabase}"
db = SQLDatabase.from_uri(pg_uri)

PROMPT = """  
The name of the table is table1.
DO NOT USE DOUBLE QOUTES("") ANYWHERE IN THE QUERY USE SINGLE QOUTES('') AS AN ALTERNATIVE.
Write a syntactically correct sql query to access data and answer the question.
The question: {question}
"""

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
llm = HuggingFaceHub(repo_id='google/flan-t5-xxl')

db_agent = SQLDatabaseChain(llm = llm,
                            database = db)
     

question = input("Ask your question: ")
db_agent.run(PROMPT.format(question=question))
