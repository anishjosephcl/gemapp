from langchain.vectorstores import Chroma

def store_data(text,embedding):
    persist_directory = 'db'
    vectordb = Chroma.from_documents(documents=text,embedding=embedding,persist_directory=persist_directory)
    # persiste the db to disk
    vectordb.persist()
    vectordb = Chroma(persist_directory=persist_directory,embedding_function=embedding)
    return vectordb

def get_retriever(vectordb,input):
    retriever = vectordb.as_retriever(search_kwargs={"k": 1})
    docs = retriever.get_relevant_documents(input)
    print(docs[0].page_content)
    return retriever
