import requests
from io import BytesIO
from openai import OpenAI

client = OpenAI()
vectorstoreid = ""
def create_file(client, file_path):
    # Handle local file path
    with open(file_path, "rb") as file_content:
        result = client.files.create(
            file=file_content,
            purpose="assistants"
        )

    return result.id

def prepSQLFileVector():
    # Replace with your own file path or URL
    file_id = create_file(client, "./DeveloperFiles/ProcessSales_SQL_PROCEDURE.json")

    vector_store = client.vector_stores.create( name="knowledge_base" )

    client.vector_stores.files.create(
        vector_store_id=vector_store.id,
        file_id=file_id
    )
    result = client.vector_stores.files.list(
        vector_store_id=vector_store.id
    )


    response = client.responses.create(
        model="gpt-4-turbo",
        input="understand the SQL file detail and be ready to provide data models and also source, target and all other details properly and be ready for questions",
        tools=[{
            "type": "file_search",
            "vector_store_ids": [vector_store.id]
        }]
    )
    return vector_store.id
    
