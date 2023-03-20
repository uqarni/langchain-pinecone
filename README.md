# langchain-pinecone
experiment with langchain and pinecone

# how it works
ingest a PDF
langchain breaks it up into documents
openai changes these into embeddings - literally a list of numbers. a giant vector in 1500-dimensional space
pinecone stores these embeddings externally

openai turns a question into an embedding; pinecone will return the embeddings most similar to that query
openai will take those supplied embeddings and return an answer

# to get detectron2 (doesnt work still)
apt-get update && apt-get -y install pybind11-dev
CC=clang CXX=clang++ ARCHFLAGS="-arch x86_64" python -m pip install 'git+https://github.com/facebookresearch/detectron2.git' --user
???


# pinecone
remember, openai embeddings have 1536 dimensions

# inspired by
https://www.youtube.com/watch?v=h0DHDp1FbmQ&ab_channel=DataIndependent


#notes for refactor:
1. Format Tara's docs and upload them all to PineCone
2. Create a QA bot from those
3. Use Just call API to ask questions from the QA bot
4. ensure it's remembering the history
5. store all conversations in archive
