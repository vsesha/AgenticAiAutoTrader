"""
import requests
import os
from openai import OpenAI

client = OpenAI()
vectorstoreid = ""

def create_file(client, file_path):
    #Uploads a file to OpenAI and returns the file ID.
    with open(file_path, "rb") as file_content:
        result = client.files.create(
            file=file_content,
            purpose="assistants"
        )
    print(f"Uploaded: {file_path}, File ID: {result.id}")
    return result.id

def prepSalesFile(directory):
    #Processes all PDF files in a folder and returns vector store ID with file IDs.
    file_ids = []
    
    # Get all PDF files in the specified directory
    pdf_files = [f for f in os.listdir(directory) if f.endswith(".pdf")]
    
    if not pdf_files:
        print("No PDF files found in the directory.")
        return None
    
    # Create vector store
    vector_store = client.vector_stores.create(name="knowledge_base")
    print(f"Vector Store ID: {vector_store.id}")
    
    for pdf in pdf_files:
        file_path = os.path.join(directory, pdf)
        file_id = create_file(client, file_path)
        file_ids.append(file_id)
        
        # Attach file to vector store
        client.vector_stores.files.create(
            vector_store_id=vector_store.id,
            file_id=file_id
        )
    
    # List all files in vector store
    result = client.vector_stores.files.list(vector_store_id=vector_store.id)
    print(result)
    
    # Create a response model
    response = client.responses.create(
        model="gpt-4o-mini",
        input="Understand the sales details properly and be ready for questions",
        tools=[{
            "type": "file_search",
            "vector_store_ids": [vector_store.id]
        }]
    )
    
    print(response)
    return {"vector_store_id": vector_store.id, "file_ids": file_ids}

# Example Usage
#directory_path = "./AllSalesFiles/sales"
#result = prepSalesFile(directory_path)
#print(result)

"""
import requests
from io import BytesIO
from openai import OpenAI
from GPT_ModelUser import ai_model_to_use

client = OpenAI()
vectorstoreid = ""
def create_file(client, file_path):
    # Handle local file path
    with open(file_path, "rb") as file_content:
        result = client.files.create(
            file=file_content,
            purpose="assistants"
        )
    #print(file_path)
    #print(result.id)
    return result.id

def prepSalesFile():
    # Replace with your own file path or URL
    file_id = create_file(client, "./AllSalesFiles/Sales/DailySales.pdf")
    
    vector_store = client.vector_stores.create( name="knowledge_base" )

    #print(vector_store.id)

    client.vector_stores.files.create(
        vector_store_id=vector_store.id,
        file_id=file_id
    )
    result = client.vector_stores.files.list(
        vector_store_id=vector_store.id
    )
    #print(result)


    response = client.responses.create(
        model=ai_model_to_use,
        input="understand the sales details properly and be ready for questions",
        tools=[{
            "type": "file_search",
            "vector_store_ids": [vector_store.id]
        }]
    )
    #print(response)
    return vector_store.id
    
