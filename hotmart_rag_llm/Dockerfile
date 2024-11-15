FROM python:3.11-slim

# ENV variables
ENV DEBIAN_FRONTEND=noninteractive
ENV RAG_LLM_FASTAPI_PORT=$RAG_LLM_FASTAPI_PORT
ENV RAG_LLM_FASTAPI_HOST=$RAG_LLM_FASTAPI_HOST
ENV LLM_BASE_URL=$LLM_BASE_URL


# ENV Model inference-related
ENV SYSTEM_MESSAGE=$SYSTEM_MESSAGE
ENV TEMPERATURE=$TEMPERATURE
ENV SEED=$SEED
ENV MAX_TOKENS=$MAX_TOKENS

# RAG DB API-related
ENV DB_API_HOST=$DB_API_HOST
ENV DB_API_PORT=$DB_API_PORT

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

# Install uv
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

# Copy project files
COPY . /hotmart_rag_llm

# Set working directory
WORKDIR /hotmart_rag_llm

# Install python libraries
RUN uv sync

# Run project
CMD ["uv", "run", "main.py"]