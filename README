# Hotmart RAG App
A RAG-based app to answer questions about Hotmart. Database is fed based on data present on Hotmart blog page (https://hotmart.com/pt-br/blog/como-funciona-hotmart)

## Features
- [x] API to make embeddings from text and vector search
- [x] API for a RAG-based app to answer questions about Hotmart

## Tech Stack
- `Python` as the main programming language
- `uv` for package management
- `ChromaDB` as the open-source vector database
- `Langchain` for data processing, microservices integrations and helper utilities
- `FastAPI` for the APIs
- `Huggingface Transformers` for the multilingual open-source embedding model (Alibaba-NLP/gte-large-en-v1.5)
- `Ollama` for model serving (used Llama 3.2-3B as the inferece model due to hardware limitations and also because of lower latency and costs)
- `Docker and Docker Compose` for containerization and orchestration

## Architecture
The app is composed of 4 main microservices, in which 2 were developed in this project and 2 were used from open-source projects. The two services developed in this project are:
- `hotmart_rag_db`: Service to store the text embeddings in the ChromaDB vector database and make vector searches
- `hotmart_rag_llm`: Service that comprises the RAG-based app to answer questions about Hotmart

The two services used from open-source projects are:
- `chromadb`: Open-source vector database to store and search embeddings
- `ollama`: Open-source model serving platform to serve the Llama 3.2-3B model


## Running the app

### Requirements
 - Docker and Docker Compose installed (https://docs.docker.com/get-docker/ and https://docs.docker.com/compose/install/)
 - Windows, Linux or MacOS
 - Make sure the following ports are available: 8091, 8092, 8093 and 11434

1. Clone the repository and change directory to the repository folder
```bash
git clone https://github.com/felipeoes/hotmart_rag
cd hotmart_rag
```

2. Create a .env file with the same content as the .env.example file
```bash
cp .env.example .env
```

Optional: Change the values of the .env file if you want to use different ports, database credentials, etc.

3. Build images and start containers
```bash
docker-compose up -d
```

Note: The first time you run the app, it will take some time to download the necessary images and build the containers. After that, the app will start and you can access the APIs at the URLs mentioned below. 
Also, make sure you comment the below lines in the `docker-compose.yml` file if you are not using a GPU.
```
deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [ gpu ]
``` 


## API Documentation
The API documentation for the `hotmart_rag_db` service can be accessed at http://localhost:8091/docs and the one for the `hotmart_rag_llm` service can be accessed at http://localhost:8093/docs
Note: If you changed the ports in the .env file, make sure to change the ports in the URLs above accordingly.

Also, you can access the POSTMAN collection with the API requests at the following link: https://elements.getpostman.com/redirect?entityId=39244532-90afed10-7b65-4436-b9b0-5447e1b2894b&entityType=collection or by using the file `HOTMART_RAG.postman_collection` in this repository.

## Considerations and limitations
- The app was developed in a short period of time and having resources constraints in mind. Prompt engineering was used to mitigate hallucinations, keep the model answers within the domain of Hotmart and ensure inappropriate (harmful) content, but it's known that LLama.3.2-3B can struggle with those issues, mainly because of the lack of fine-tuning to the specific domain and also because of the its nature of being a smaller language model.
Some improvements that can be made:
    - Implementing monitoring and observability, as well as a CI/CD pipeline, to keep track of model performance and improve it over time.
    - Fine-tuning both the embeddings and the inference model in order to improve the accuracy of the answers and deal with the specific domain of Hotmart, making sure the answers are factually correct.
    - Implementing a feedback loop based on RLHF to improve the model over time, by collecting feedback from users and using it to retrain the model.
    - Developing a more robust security layer, with rate limiting, authentication and authorization mechanisms, and data encryption.
    - Implemeting guardrails to prevent the model from generating harmful content, by filtering out inappropriate answers and ensuring the model generates safe and respectful content.
    