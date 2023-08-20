from langchain import PromptTemplate, HuggingFaceHub, LLMChain
import os
template = """Question: {question}

Answer: """
prompt = PromptTemplate(template=template, input_variables=["question"])

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
llm = HuggingFaceHub(repo_id='google/flan-t5-small')

question = "How to save my money from inflation?"
chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run(question))