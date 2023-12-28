from dotenv import load_dotenv
import streamlit as st
from model.geminimodel import get_model
from model.geminimodel import get_llm_model
from result.result import get_result
from loader.loader import load_pdf
from loader.loader import text_split
from embedding.embedding import get_embedding
from database.database import store_data
from database.database import get_retriever
from chain.chain import process_response
## Get the Model 

gmodel = get_llm_model()



##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini  LangChain Application")

input=st.text_input("Input: ",key="input")


submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    ## Load the PDF and Store the embeddings
    ## Pass the response to the result
    doc = load_pdf("data")
    text = text_split(doc)
    #print(text[0].page_content)
    embedding = get_embedding()
    vdb = store_data(text,embedding)
    retriever = get_retriever(vdb,input)
    ##response=get_result(gmodel,input)
    response = process_response(gmodel,retriever,input)
    st.subheader("The Response is")
    st.write(response['result'])
    ##for chunk in response:
    ##    print(st.write(chunk.text))
    ##    print("_"*80)

    vdb.delete_collection()
    vdb.persist()
