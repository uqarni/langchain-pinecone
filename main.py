#from langchain.document_loaders import OnlinePDFLoader
#from langchain.text_splitter import RecursiveCharacterTextSplitter
#from langchain.vectorstores import Pinecone
#from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI 
from langchain.chains.question_answering import load_qa_chain
import pinecone
import openai
import os

#initialize pinecone
pinecone.init(
    api_key = os.environ.get("PINECONE_API_KEY"),
    environment= os.environ.get("PINECONE_API_ENV")
)

openai.api_key = os.environ.get("OPENAI_API_KEY")

# loader = OnlinePDFLoader("https://wolfpaulus.com/wp-content/uploads/2017/05/field-guide-to-data-science.pdf")
# data = loader.load()

# print(f'You have {len(data)} docuemnt(s) in your data')
# print(f'There are {len(data[0].page_content)} characters in your document')

# text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# texts = text_splitter.split_documents(data)

# print(f'Now you have {len(texts)} documents')
# print(texts[4])

# embeddings = OpenAIEmbeddings(openai_api_key = openai.api_key)

index_name = 'langchain1'
query = "What are examples of good data science teams?"

#docsearch = Pinecone.from_texts([t.page_content for t in texts], embeddings, index_name = index_name)


docs = docsearch.similarity_search(query, include_metadata = True)



llm = OpenAI(temperature = 0, openai_api_key = os.environ.get("OPENAI_API_KEY"))
chain = load_qa_chain(llm, chain_type = "stuff")

query = "What is the advise stage of data maturity?"
response = chain.run(input_documents=docs, question=query)
print(response)