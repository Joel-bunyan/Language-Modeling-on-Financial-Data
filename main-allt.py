import psycopg2
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
import os
from dataprep import preparedata



def access_data():
    
    host = "localhost"
    port = "5432"
    dbname = "Finance--database"
    user = "postgres"
    password = "joelbunyan"

    
    connection = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )

    cursor = connection.cursor()

    select_query = 'SELECT * FROM "table";'
    cursor.execute(select_query)
    records = cursor.fetchall()

    for record in records:
        print(record)



    if connection:
        cursor.close()
        connection.close()
    return records

records = access_data()



os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
llm = HuggingFaceHub(repo_id='google/flan-t5-xxl')

inp_template = """
The following database contains of : Month, Salary and savings of a person. Answer the questions accordingly
Database: {Data}
Question: {input_question}
Answer: """



prompt = PromptTemplate(template=inp_template, 
                        input_variables=["Data","input_question"])

database_str = preparedata(records)

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run(Data=database_str,input_question='Which month is my worst saving?'))