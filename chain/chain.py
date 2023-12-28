from langchain.chains import RetrievalQA

def process_response(gmodel,retriever,query):
    # create the chain to answer questions
    qa_chain = RetrievalQA.from_chain_type(gmodel,
                                  retriever=retriever,
                                  return_source_documents=True)
    llm_response = qa_chain(query)
    return llm_response
    